import os
from google_images_download import google_images_download
import ssl
import datetime as dt
import sys


###참고 : https://data-make.tistory.com/172

# 실행결과를 txt 파일로 저장하기 위한 변수
log_filename = "log_data(" + dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H-%M-%S") + ").txt"
log_path = os.getcwd() + "/log/" + log_filename

list_path = os.getcwd() + "/material/space_list.txt" #검색어 리스트가 저장된 파일 위치


ssl._create_default_https_context = ssl._create_unverified_context

#keyword로 크롤링한 사진을 dir에 저장
def imageCrawling(keyword, dir):
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords": keyword,       # 검색 키워드
                 "limit": 100,              # 크롤링 이미지 수
                 "print_urls": True,        # 이미지 url을 출력
                 "no_directory": True,      #
                 'output_directory': dir}   # 크롤링 이미지를 저장할 폴더
    paths = response.download(arguments)
    print(paths)

#장소 리스트를 리스트 형태로 가져옴
def get_keywords_list():
    list = open(list_path, 'r')
    keywords_list = list.readline().split("/")
    list.close()

    return keywords_list


if __name__ == "__main__":
    keywords = get_keywords_list()

    sys.stdout = open(log_path, 'w') #log_data 작성을 위한 표준출력장치 시작

    for keyword in keywords:
        imageCrawling(keyword, os.getcwd() + "/image/" + keyword) #(현재 py파일이 저장된 디렉토리)/image/(검색어명)

    sys.stdout.close()
