import os
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub

img_path = os.getcwd() + "/images" #이미지가 저장되어 있는 경로
#print(os.getcwd())

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


def results(target_img_path,cmp_img_list):
    input_img_paths = []

    # grab the paths to the input images in our dataset
    import os

    photo_all = []
    # grab the paths to the input images in our dataset
    print("[INFO] quantifying image...")
    path = "./images/"
    #file_list = os.listdir(path)
    for i in range(len(cmp_img_list)):
        photo_path = path + cmp_img_list[i]
        # print(path2)
        photo_all.append(photo_path)
        #file_list2 = os.listdir(path2)  # 카테고리 폴더안 사진들
        #for j in range(len(file_list2)):
        #    photo_path = path2 + "/" + file_list2[j]
        #    photo_all.append(photo_path)
            # print(photo_path)


    import time
    import tensorflow as tf
    from IPython.display import Image, display

    tf.logging.set_verbosity(tf.logging.ERROR)

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

    for similarity, input_img_path in zip(similarities[1:], photo_all):
        #print(input_img_path)
        display(Image(input_img_path))
        #print("- similarity: %.2f" % similarity)

    top = dict(zip(similarities[1:], photo_all))
    # max(similarities)
    # print(top.items()[:10])
    #key = list(reversed(sorted(list(top.keys()))))
    #value = list(reversed(sorted(list(top.values()))))
    diction = sorted(top.items(), reverse=True)

    arr_key = []
    arr_value = []
    for key, value in diction:
        arr_key.append(key)
        arr_value.append(value)
    result=unique_value(arr_value[:30])
    return result[:3]


k_stat = {'서울':10, '강원':20, '대전':30, '충남':31, '세종':33, '충북':36,
   '인천':40, '경기':41, '광주':50, '전남':51, '전북':56, '부산':60,
   '경남':62, '울산':68, '제주':69, '대구':70, '경북':71}

#지역코드를 바탕으로 비교해야할 이미지들의 파일명이 담긴 리스트를 반환
def get_cmpr_img_lst(area):
    cmpr_img_lst = []

    if(area == '전국'):
        for (path, dirs, files) in os.walk(img_path):
            return files

    # 특정 범위로 지정된 경우
    stat_key = k_stat[area]
    for (path, dirs, files) in os.walk(img_path):
        for f in files:
            if(f[:2] == str(stat_key)):
                cmpr_img_lst.append(f)
    return cmpr_img_lst


#top10 img list의 GPS값을 리스트로 반환
def get_gps_lst(top10_img_lst):
    gps_lst = []
    for f in top10_img_lst:
        try:  # GPS정보를 가지고 있지 않다면 에러발생
            exif_gps_dict = Image.open(f)._getexif()[34853]
            img_GPS = convert_dms_to_degree(exif_gps_dict)
            gps_lst.append(img_GPS)
        except:
            gps_lst.append("error")
    return gps_lst

#도분초 형식으로 된 GPS정보를 도(degree)형태로 변환하여 반환
def convert_dms_to_degree(gps_dict):
    latRef = gps_dict[1]
    lat_tuple = gps_dict[2]  # ((d, 1), (m, 1), (int(s*100), 100))
    lngRef = gps_dict[3]
    lng_tuple = gps_dict[4]

    lat_d = lat_tuple[0][0]
    lat_m = lat_tuple[1][0]
    lat_s = lat_tuple[2][0] / 100

    lng_d = lng_tuple[0][0]
    lng_m = lng_tuple[1][0]
    lng_s = lng_tuple[2][0] / 100

    #latitude = str(lat_d + lat_m / 60 + lat_s / 3600) + latRef
    #lontitude = str(lng_d + lng_m / 60 + lng_s / 3600) + lngRef
    latitude = str(lat_d + lat_m / 60 + lat_s / 3600)
    lontitude = str(lng_d + lng_m / 60 + lng_s / 3600)

    #gps = latitude + ", " + lontitude
    return latitude, lontitude


def unique_value(value):

    diction = dict()

    list2 = list(reversed(value))

    for i in range(len(list2)):
        temp = list2[i][9:10]
        diction[list2[i][9:19]] = list2[i]

    #print(diction)
    print_paths = []
    for key in diction.keys():
        print_paths.append(diction[key])

    return print_paths

if __name__ == "__main__":
    region = ["전국", "서울", "경기", "강원", "강원", "대전", "인천", "광주", "충북", "충남", "전북", "전남", "경북", "경남", "부산", "대구", "울산",
              "제주"]
    file = get_cmpr_img_lst(region[5]) #콤보박스에서 들어온 행정구역 str
    
    value = results("./images/10_138_02_0053.jpg",file)


    gps = get_gps_lst(value)  #top10에 대한 GPS값이 담긴 리스트
    print(gps)          #top gps위치
