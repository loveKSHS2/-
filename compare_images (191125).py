import os
import pandas as pd
from PIL import Image

img_path = os.getcwd() + "/images" #이미지가 저장되어 있는 경로
print(os.getcwd())
code_path = "./material/K-stat.csv" #지역코드가 저장된 파일
print(code_path)
code = pd.read_csv(code_path, header=None, encoding="euc_kr")

#지역코드를 바탕으로 비교해야할 이미지들의 파일명이 담긴 리스트를 반환
def get_cmpr_img_lst():
    cmpr_img_lst = []

    print("검색하려는 장소범위를 '[행정구역] [시/군/구]' 형태로 입력해주세요.")
    print("검색범위가 전국이면 '전국'만, 특정 행정구역의 전체 시/군/구라면 '[행정구역] 전체'로 입력헤주세요.")
    range = input(">>> ")

    space_key = get_space_key(range)

    # 범위가 전국인 경우
    if (space_key == '00_000_'):
        for (path, dirs, files) in os.walk(img_path):
            return files

    # 특정 범위로 지정된 경우
    for (path, dirs, files) in os.walk(img_path):
        for f in files:
            if (f[:7] == space_key):
                cmpr_img_lst.append(os.path.join(img_path, f))
    return cmpr_img_lst

#사용자가 입력한 장소범위로 비교할 이미지들을 지정하는 지역코드를 반환
def get_space_key(range):
    range = range.split(" ")
    if (range[0] == "전국"):
        return '00_000_'

    f_row = code[code[0] == range[0]].index[0]
    fst_cNum = str(code.loc[f_row][1])

    if (range[1] == "전체"):
        return fst_cNum + "_000_"

    s_row = code[code[0] == (range[0] + " " + range[1])].index[0]
    snd_cNum = str(code.loc[s_row][1])
    return fst_cNum + "_" + snd_cNum + "_"

#현재 코드에서는 임시로 비교할 이미지 리스트를 그대로 반환함
#반드시 수정하길 바람!!
#유사도가 가장 높은 이미지 10개의 파일명과 유사도 값을 반환
def smlt_cmpr(cmpr_img_lst):
    for f in cmpr_img_lst:
        pass
        # f가 비교할 대상 이미지
        # 여기에 f랑 사용자로부터 받은 이미지와의 유사도 분석하는 알고리즘

    key = [] #top10 ratio
    value = [] #top10 value
    #return key, value #--- 원래 반환해야 하는 값
    return cmpr_img_lst, value

#top10 img list의 GPS값을 리스트로 반환
def get_gps_lst(top10_img_lst):
    gps_lst = []
    for f in top10_img_lst:
        full_path = os.path.join(img_path, f)
        try:  # GPS정보를 가지고 있지 않다면 에러발생
            exif_gps_dict = Image.open(full_path)._getexif()[34853]
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

    latitude = str(lat_d + lat_m / 60 + lat_s / 3600) + latRef
    lontitude = str(lng_d + lng_m / 60 + lng_s / 3600) + lngRef
    gps = latitude + ", " + lontitude
    return gps

if __name__ == "__main__":
    cmpr_img_lst = get_cmpr_img_lst() #비교해야할 이미지 목록
    top10_img, top10_smlt = smlt_cmpr(cmpr_img_lst) #유사도 가장 높은 이미지 10개의 경로와 유사도 값
    print(top10_img)
    print(top10_smlt)
    top10_gps = get_gps_lst(top10_img)  #top10에 대한 GPS값이 담긴 리스트
    print(top10_gps)

