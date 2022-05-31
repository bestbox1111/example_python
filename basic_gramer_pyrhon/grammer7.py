

# 전체 컨셉 = if

# wheather= input('오늘날씨는 어떄요 ???ㄴ')

# if wheather == "비":
#     print("우산을 챙기세여")
# elif wheather =="미세먼지":
#     print("마스크를 챙기세여")    
# else:
#     print("그냥 잘 보내세요")
    
    

# temp= int(input("기온이 어떄요???"))

# if 30<= temp:
#     print("너무 더워요 나가지 마세요")
# elif 10<= temp and temp <30:
#     print("괜찮은 날씨네요")
# elif 0<=temp and temp<10:
#     print("외투를 챙기세여")
# else:
#     print("나가지 마세요")



# #전체 컨셉 = for
# # 씁R for문도 햇갈리네...
# for wait in [0,1,2,3,4,5,6]:            #for문에 리스트형식으로 넣어줌
#     print("대기번호 {}".format(wait))
# print()
# print()
# for wait2 in range(5):          #range함수로 0부터5까지를 넣어줌
#     print("대기번호 {}".format(wait2))
# print()
# print()
# for wait2 in range(1,5):          #range함수로 첫번째 시작점 두번째 끝나기바로전
#     print("대기번호 {}".format(wait2))


#위와 동일 한 예제임.
# bugs=["아이언","토르","그루트"]
# for star in bugs:
#     print("{}님 커피가 준비되었습니다.".format(star))






#####전체 컨셉 = while

customer ="토르"
index=5
call=1
while index>=1:
    print("{}님 커피가 준비되었습니다 {}번 호출했습니다.".format(customer,call))
    index-=1
    call+=1
    if index==0:
        print("커피는 없습니다.")
        

#아래는 무한루프...조건이 무조건 참이라...분기의 여지가없음..
# customer ="그르트"
# index=1
# while True:
#     print("{}님 커피가 준비되었습니다 {}번 호출했습니다.".format(customer,index))
#     index+=1




##### 전체 컨셉 = continue와  break

absent =[2,5]   #결석한애덜
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue                #2,5빼고는 계속 출력
    elif student in no_book:
        break                   #7번이 걸리는 순간 끝남.
    print("{}야 책을 읽어봐".format(student))





##### 전체 컨셉 = 한줄 for

# 점수 평가를 한후 문제 오류로 인해 모두 정답인정해 주기로 한경우
# score=[90,20,30,40,89]
# print(score)
# score_modify=[i+10 for i in score]
# print(score_modify)



#학생이름을 길이로 변환
students2=["iron man","Thor","I am groot"]
students2=[len(i) for i in students2]
print(students2)


#학생이름을  대문자로 변환
students3=["iron man","Thor","I am groot"]
students3=[i.upper() for i in students3]

print(students3)