import os
import requests
from PIL import Image
import piexif

###참고1-구글맵 API : https://djangoworld.tistory.com/4
###참고2-exif_dict 추가 : https://medium.com/@literallywords/replacing-exif-data-with-python-ac7b5c5b6b0
###참고3-exif 접근 : https://www.sylvaindurand.org/gps-data-from-photos-with-python/
###참고4-piexif 변수(971줄부터) : https://openuserjs.org/libs/ProxyFiend/Piexifjs/source

image_path = os.getcwd() + "/image" #이미지 경로
key = input("구글맵 API 키를 입력하세요: ")

#본 코드에서는 모든 이미지가 장소명으로 된 디렉터리에 들어가 있다고 가정
def add_exif_dict():
    for d in os.listdir(image_path):
        if(d == "except"): #exif 정보를 삭제하지 않을 폴더
            continue
        sub_dir_path = os.path.join(image_path, d) #하위 디렉터리

        # exif_dict 생성
        exif_dict = {}
        exif_dict["0th"] = {}
        exif_dict["Exif"] = {}
        exif_dict["GPS"] = {}

        # 구글 API를 이용해서 받아온 위도&경도 값으로 dict 초기화
        location = d #디렉토리명 == 주소검색에 쓰일 검색어명
        URL = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&sensor=false&language=ko&address={}' \
            .format(key, location)
        response = requests.get(URL)
        gps_data = response.json()

        lat = gps_data['results'][0]['geometry']['location']['lat']  # 위도(latitude) : N or S
        lng = gps_data['results'][0]['geometry']['location']['lng']  # 경도(longitude) : E or W

        exif_dict["GPS"][1], exif_dict["GPS"][2], exif_dict["GPS"][3], exif_dict["GPS"][4] = convert_dd_to_dms(lat, lng)

        #GPS정보를 가지고 있지 않은 사진에 한해서만 GPS값 저장
        for (path, dirs, files) in os.walk(sub_dir_path):
            for f in files:
                file_path = os.path.join(sub_dir_path, f)
                try : #GPS정보를 가지고 있지 않다면 에러발생
                    exif_info = Image.open(file_path)._getexif()[34853][2] #latitude: 임의로 위도값이 있는지 확인
                    print("{}>> {}".format(sub_dir_path, f))

                except: #이미지가 GPS값을 가지고 있지 않을 때
                    print(f)
                    exif_bytes = piexif.dump(exif_dict)
                    try :
                        piexif.insert(exif_bytes, file_path)
                    except :
                        pass
                    pass
    return True

#Degree형태의 GPS정보를 DMS 형태로 변환
def convert_dd_to_dms(latitude, longitude):
    #latitude
    lat_d = (int(latitude))
    lat_m = (int((latitude - lat_d) * 60))
    lat_s = (((latitude - lat_d) * 60 - lat_m) * 60)
    latRef = 'N'

    if (latitude < 0):
        lat_d = -lat_d
        lat_m = -lat_m
        lat_s = -lat_s
        latRef = 'S'

    #longitude
    lng_d = (int(longitude))
    lng_m = (int((longitude - lng_d) * 60))
    lng_s = (((longitude - lng_d) * 60 - lng_m) * 60)
    lngRef = 'E'

    if (longitude < 0):
        lat_d = -lng_d
        lat_m = -lng_m
        lat_s = -lng_s
        lngRef = 'W'

    lat_dict = ((lat_d, 1), (lat_m, 1), (int(lat_s * 100), 100))
    lng_dict = ((lng_d, 1), (lng_m, 1), (int(lng_s * 100), 100))

    return latRef, lat_dict, lngRef, lng_dict

if __name__ == "__main__":
    print(" *** add exif dict in {} ***".format(image_path))
    res = add_exif_dict()
    if(res): print("\n *** success all process ***")