

# 글 쓰기 및 저장하기
# with open("hardstudy.txt","w", encoding="utf8") as hardstudy_file:
#     hardstudy_file.write("파이썬을 공부합시다.")


#불러오기
with open("hardstudy.txt","r", encoding="utf8") as hardstudy_file:
    print(hardstudy_file.read())