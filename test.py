import tensorflow as tf

import tensorflow_hub as hub
import os


CHANNELS = 3  # number of image channels (
def build_graph(hub_module_url, target_image_path):
    # Step 1) Prepare pre-trained model for extracting image features.
    module = hub.Module(hub_module_url)
    height, width = hub.get_expected_image_size(module)

    # Copied a method of https://github.com/GoogleCloudPlatform/cloudml-samples/blob/bf0680726/flowers/trainer/model.py#L181
    # and fixed for all type images (not only jpeg)
    def decode_and_resize(image_str_tensor):
        """Decodes jpeg string, resizes it and returns a uint8 tensor."""
        image = tf.image.decode_image(image_str_tensor, channels=CHANNELS)
        # Note resize expects a batch_size, but tf_map supresses that index,
        # thus we have to expand then squeeze.  Resize returns float32 in the
        # range [0, uint8_max]
        image = tf.expand_dims(image, 0)
        image = tf.image.resize_bilinear(
            image, [height, width], align_corners=False)
        image = tf.squeeze(image, squeeze_dims=[0])
        image = tf.cast(image, dtype=tf.uint8)
        return image

    def to_img_feature(images):
        """Extract the feature of image vectors"""
        outputs = module(dict(images=images), signature="image_feature_vector", as_dict=True)
        return outputs['default']

    # Step 2) Extract image features of the target image.
    target_image_bytes = tf.gfile.GFile(target_image_path, 'rb').read()
    target_image = tf.constant(target_image_bytes, dtype=tf.string)
    target_image = decode_and_resize(target_image)
    target_image = tf.image.convert_image_dtype(target_image, dtype=tf.float32)
    target_image = tf.expand_dims(target_image, 0)
    target_image = to_img_feature(target_image)

    # Step 3) Extract image features of input images.
    input_byte = tf.placeholder(tf.string, shape=[None])
    input_image = tf.map_fn(decode_and_resize, input_byte, back_prop=False, dtype=tf.uint8)
    input_image = tf.image.convert_image_dtype(input_image, dtype=tf.float32)
    input_image = to_img_feature(input_image)

    # Step 4) Compare cosine_similarities of the target image and the input images.
    dot = tf.tensordot(target_image, tf.transpose(input_image), 1)
    similarity = dot / (tf.norm(target_image, axis=1) * tf.norm(input_image, axis=1))
    similarity = tf.reshape(similarity, [-1])

    return input_byte, similarity


target_image_url = "./target_img.jpg" #@param {type:"string"}
input_image1_url = "./3.jpg" #@param {type:"string"}
input_image2_url = "./4.jpg" #@param {type:"string"}
input_image3_url = "./5.jpg" #@param {type:"string"}
input_image4_url = "./2.jpg" #@param {type:"string"}



input_image_urls = [input_image1_url, input_image2_url, input_image3_url, input_image4_url]
def results(target_img_path):
    input_img_paths = []

    # grab the paths to the input images in our dataset
    import os

    photo_all = []
    # grab the paths to the input images in our dataset
    print("[INFO] quantifying image...")
    path = "./images"
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        photo_path = path + file_list[i]
        # print(path2)
        photo_all.append(photo_path)
        #file_list2 = os.listdir(path2)  # 카테고리 폴더안 사진들
        #for j in range(len(file_list2)):
        #    photo_path = path2 + "/" + file_list2[j]
        #    photo_all.append(photo_path)
            # print(photo_path)

    # print(photo_all)
    # print(len(photo_all))

    import time
    import tensorflow as tf
    from IPython.display import Image, display

    tf.compat.v1.logging.set_verbosity(tf.logging.ERROR)

    # Load bytes of image files
    image_bytes = [tf.gfile.GFile(name, 'rb').read()
                   for name in [target_img_path] + photo_all]

    hub_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/1"  # @param {type:"string"}

    with tf.Graph().as_default():
        input_byte, similarity_op = build_graph(hub_module_url, target_img_path)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            t0 = time.time()  # for time check

            # Inference similarities
            similarities = sess.run(similarity_op, feed_dict={input_byte: image_bytes})

            print("%d images inference time: %.2f s" % (len(similarities), time.time() - t0))

    # Display results
    # print("# Target image")
    #display(Image(target_img_path))

    # 1print("- similarity: %.2f" % similarities[0])

    def make_path(path, file_list):
        paths = []
        for i in range(len(file_list)):
            temp = path + file_list[i]
            paths.append(temp)

        return paths

    # print("# Input images")
    # print(similarities[1:])
    for similarity, input_img_path in zip(similarities[1:], photo_all):
        #print(input_img_path)
        display(Image(input_img_path))
        #print("- similarity: %.2f" % similarity)

    top = dict(zip(similarities[1:], photo_all))
    # max(similarities)
    # print(top.items()[:10])
    key = list(reversed(sorted(list(top.keys()))))
    value = list(reversed(sorted(list(top.values()))))

    return (key[:5], value[:5])


print(results(target_image_url))