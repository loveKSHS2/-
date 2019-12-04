import os

# 라인별로 되어 있는 장소목록을 검색을 위한 '/'로 구분하는 형태로 변경
list_t = os.getcwd() + "/material/space_list.txt"  # real list
list_s = os.getcwd() + "/material/space_list_for_crawling.txt" # list for search

# real list를 읽어와서 '/'로 구분하는 문자열로 변경
f = open(list_t, 'r')
str = ""
while True:
    msg = f.readline()[:-1]
    if not msg: break
    if (msg != "-"):
        str += msg + "/"
f.close()

#검색을 위한 리스트에 쓰기
f = open(list_s, 'w')
f.write(str)
f.close()
