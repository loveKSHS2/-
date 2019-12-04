import os
import pandas as pd

img_path = os.getcwd() + "/image" #이미지 경로
code_path = os.getcwd() + "/material/K-stat.csv" #지역코드

#비교할 이미지들의 목록을 얻는 함수
def get_cmpr_img_lst():
    code = pd.read_csv(code_path, header=None, encoding="euc_kr")

    search_lst = [] #비교할 이미지들의 목록이 담길 리스트

    print("검색하려는 장소범위를 '[행정구역] [시/군/구]' 형태로 입력해주세요.")
    print("검색범위가 전국이면 '전국'만, 특정 행정구역의 전체 시/군/구라면 '[행정구역] 전체'로 입력헤주세요.")
    range = input(">>> ")

    if(range == "전국"):
         space_keyword = '00_000_'

    else: #특정 행정구역인 경우
        detail_space = range.split(" ")
        f_row = code[code[0] == detail_space[0]].index[0]
        fst_cNum = str(code.loc[f_row][1])

        if(detail_space[1] == '전체'): #특정 행정구역의 전체인 경우
            snd_cNum = '000'
        else:
            s_row = code[code[0] == (detail_space[0] + " " + detail_space[1])].index[0]
            snd_cNum = str(code.loc[s_row][1])
        space_keyword = fst_cNum + "_" + snd_cNum + "_"

    #범위가 전국인 경우
    if(space_keyword == '00_000_'):
        for (path, dirs, files) in os.walk(img_path):
            search_lst = files
        return search_lst

    #특정 범위로 지정된 경우
    for (path, dirs, files) in os.walk(img_path):
        for f in files:
            if( f[:7] == space_keyword):
                search_lst.append(f)
    return search_lst

if __name__ == "__main__":
    img_lst = get_cmpr_img_lst()
    print(img_lst)
