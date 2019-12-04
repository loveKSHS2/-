import os
import piexif

image_path = os.getcwd() + "/image" #이미지 경로

def remove_exif_dict():
    for d in os.listdir(image_path):
        if(d == "except"): #exif 정보를 삭제하지 않을 폴더
            continue
        sub_dir_path = os.path.join(image_path, d)

        print(" processing ---", sub_dir_path)
        exif_dict = {}
        exif_dict["0th"] = {}
        exif_dict["Exif"] = {}
        exif_dict["GPS"] = {}

        for (path, dirs, files) in os.walk(sub_dir_path):
            for f in files:
                file_path = os.path.join(sub_dir_path, f)
                try: #GPS정보를 가지고 있을 떄
                    exif_bytes = piexif.dump(exif_dict)
                    piexif.insert(exif_bytes, file_path)

                except: #이미지가 GPS값을 가지고 있지 않을 때
                    pass
    return True


if __name__ == "__main__":
    print(" *** remove exif dict in {} ***".format(image_path))
    res = remove_exif_dict()
    if(res): print("\n *** success all process ***")
