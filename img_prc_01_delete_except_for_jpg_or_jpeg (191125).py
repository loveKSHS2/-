import os

###참고1-이미지 확장자 확인 : https://www.trossjo.kr:444/wordpress/index.php/2019/04/05/imagegps-python/
###참고2-하위 디렉터리 검색 : https://wikidocs.net/39

image_path = os.getcwd() + "/image" #이미지 경로

def delete_except_for_jpg_or_jpeg(path):
	names = os.listdir(path) #경로 내의 모든 파일과 디렉터리 이름을 가져옴
	for name in names:
		full_path = os.path.join(path, name)
		if os.path.isdir(full_path): #해당 이름의 경로가 디렉터리 가리키면 재귀
			delete_except_for_jpg_or_jpeg(full_path)
		else: #파일을 가리키면 jpg와 jpeg가 아닌 파일을 삭제
			extension = full_path.split('.')[-1]
			if ((extension != 'jpg') & (extension != 'JPG') & (extension != 'jpeg') & (extension != 'JEPG')):
				os.remove(full_path)
				#print('Delete', full_path) #삭제한 파일 경로 출력

if __name__ == "__main__":
	delete_except_for_jpg_or_jpeg(image_path)
