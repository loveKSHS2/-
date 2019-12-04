import os
import pandas as pd

###참고 : https://118k.tistory.com/303

image_path = os.getcwd() + "/image" #이미지 경로
code_path = os.getcwd() + "/material/K-stat.csv" #지역코드 파일

area_dict = {}

#본 코드에서는 모든 이미지가 장소명으로 된 디렉터리에 들어가 있다고 가정
def rename(dir_path):
    code = pd.read_csv(code_path, header=None, encoding="euc_kr")

    #모든 디렉터리의 이름은 ---"행정구역" "시군구 "?"이하 장소명"---으로 되어 있다고 가정
    dirnames = os.listdir(dir_path)
    for d in dirnames:
        names = d.split(' ')

        #area_dict에 활용될 키값
        area_key = names[0] #행정구역
        if( len(names) >= 2): #시군구를 나타내는 문자열이 있는 경우 행정구역+시군구
            area_key = area_key + " " + names[1]

        if( area_dict.get(area_key) == None): #사전에 해당되는 value가 없다면 value를 1로 하여 추가
            area_dict[area_key] = 1
        else:
            area_dict[area_key] = area_dict[area_key] + 1 #있는 경우 value값을 1 증가
        d_index = area_dict[area_key] #동일한 "행정구역_시군구"인 디렉터리를 구분하는 번호

        #행정구역 번호
        f_row = code[code[0] == names[0]].index[0]
        fst_cNum = str(code.loc[f_row][1])

        #시군구 번호 : 시군구를 나타내는 문자열이 없을 때에만 000으로 설정
        if( len(names) >= 2):
            s_row = code[code[0] == area_key].index[0]
            snd_cNum = str(code.loc[s_row][1])
        else: snd_cNum = '000'

        new_name_base = fst_cNum + "_" + snd_cNum + "_" + str(d_index).zfill(2) #행정구역+시군구+디렉터리 번호

        sub_dir_path = os.path.join(image_path, d) #이미지 경로 내의 하위 디렉터리 명 == 장소명으로 된 디렉터리
        print("====={}=====".format(sub_dir_path))

        i_index = 1 #이미지 인덱스
        for (path, dirs, files) in os.walk(sub_dir_path):
            for f in files: #디렉터리 내의 모든 파일에 대해
                new_name = new_name_base + "_" + str(i_index).zfill(4) + "." + f.split('.')[-1] #실제로 변경할 파일명: 행정구역+시군구+디렉터리+이미지 번호.확장자
                ori_path = os.path.join(sub_dir_path, f) #원래 경로+파일명
                new_path = os.path.join(sub_dir_path, new_name) #새로운 경로+파일명
                os.rename(ori_path, new_path) #기존의 이름을 새 이름으로 변경
                #print("{} -> {}".format(f, new_name)) #변경 확인을 위한 안내문
                i_index = i_index + 1

if __name__ == "__main__":
    rename(image_path)