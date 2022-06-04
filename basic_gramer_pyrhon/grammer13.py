


#### 전체 컨셉 = 파일 입 출력


# score_file = open("score.txt", "w", encoding="utf8")        # w는 쓰기 전용 utf8 = 한글 깨지는거 방지위함.
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()



#기존 파일에 add 시키면서 파일 불러오기.
# score_file = open("score.txt", "a", encoding="utf8")        # w는 읽기 전용 utf8 = 한글 깨지는거 방지위함.
# score_file.write("영어 : 90")
# score_file.write("\n과학 : 38")     #자동 줄바꿈이 안되어서 \n으로 잘부꿈 해줘야함.
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")        # r는 읽기 전용 utf8 = 한글 깨지는거 방지위함.
# print(score_file.read())    #해당 파일을 다 읽어오기
# score_file.close()


#한줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")        # r는 읽기 전용 utf8 = 한글 깨지는거 방지위함.
# print(score_file.readline(), end=" ")    #해당 파일을 한줄씩 읽어오기
# print(score_file.readline(),end=" ")    #해당 파일을 한줄씩 읽어오기
# print(score_file.readline(), end=" ")    #해당 파일을 한줄씩 읽어오기
# print(score_file.readline(), end=" ")    #해당 파일을 한줄씩 읽어오기
# score_file.close()


#전체 데이터나 반복의 횟수를 모를때 조건으로 반복설정
# score_file = open("score.txt", "r", encoding="utf8")        # r는 읽기 전용 utf8 = 한글 깨지는거 방지위함.
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line , end= " ")

# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")        # r는 읽기 전용 utf8 = 한글 깨지는거 방지위함.
# lines = score_file.readlines()      #list형태로 저장.

# for line in lines:
#     print(line, end= " ")
    
# score_file.close()