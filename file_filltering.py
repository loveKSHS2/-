import os

image_path = os.getcwd() + "/images" #이미지 경로
list_path = "./delete_img_lst.txt" #검색어 리스트가 저장된 파일 위치

def delete_error_img(path):
    list = open(list_path, 'r')
    delete_img_list = list.read().split(", ")
    list.close()

    for name in delete_img_list:
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            os.remove(full_path)
            print("delete ", full_path)

if __name__ == "__main__":
   delete_error_img(image_path)