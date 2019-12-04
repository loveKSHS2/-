import os
from PIL import Image

def prt_gps(img_lst):
    for f in img_lst:
        try:  # GPS정보를 가지고 있지 않다면 에러발생
            exif_gps_dict = Image.open(f)._getexif()[34853] #exif["GPS"]
            img_GPS = convert_dms_to_degree(exif_gps_dict)
            print("{}>>>  {}".format(f, img_GPS))
        except:
            print("occur error")

#DMS형태의 GPS값을 Degree형태로 출력
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

    latitude = str(lat_d + lat_m / 60 + lat_s / 3600) + latRef
    lontitude = str(lng_d + lng_m / 60 + lng_s / 3600) + lngRef
    gps = latitude + ", " + lontitude
    return gps

if __name__ == "__main__":
    #리스트에 '경로/파일명.확장자'식으로 저장되어 있어야 함
    #임의의 리스트
    image_list = [os.path.join(os.getcwd(), 'image/10_100_02_0002.jpg'),
                  os.path.join(os.getcwd(), 'image/10_100_02_0011.jpg'),
                  os.path.join(os.getcwd(), 'image/41_414_01_0010.jpg')]
    prt_gps(image_list)
