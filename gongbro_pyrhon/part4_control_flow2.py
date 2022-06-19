

#if 구문

# x = input("알맞은 숫자를 넣어라.")
# # print(x.isdigit())          #isdigt()함수는 정수냐 아니냐를 블린으로 확인가능함.
# while x.isdigit() != True:
#     x = input("알맞은 숫자를 넣어라.")
#     if x.isdigit():
#         y= int(x)+1
#         print(y)
#     else:
#         print("정수를 입력해주세요")


#elif 구문

# x = int(input("몇살이냐??."))
# if x>= 20:
#     print("운전할수 있구나")
# elif x>15 and x<20:
#     print("조금만 더 기다려라.")
# else:
#     print("어린것들1")



#while구문의 효율성
#몇 년 후에 발란스가 20000원이 넘어가는지 알고싶을때..

# balance = 10000
# interest = 0.05
# yr=0
# while balance < 20000:
#     balance+= balance*interest
#     yr+=1
#     print("year {}",yr)
#     print("balance의 금액은 {:6.3f}".format(balance))   #소수점 처리할때 {}안의 방법
#     print()



#for 와 if의 break continue를 사용

# balance = 10000
# interest = 0.05
# yr=0
# for i in range(10000, 21000):
#     balance+= balance*interest
#     yr+=1
    
#     if balance> 20000:
#         break
    
#     print("year: ",yr)
#     print("balance의 금액은 {:6.3f}".format(balance))   #소수점 처리할때 {}안의 방법
#     print()



#pass
# for x in range(5):
#     pass    #그냥 무시해줘 다음을 진행해줘..


# try catch 예외처리..

# age= int(input("나이가 어떻게 되시나여??"))
# print('age :{}'.format(age))

# while True:
#     try: 
#         age= int(input("나이가 어떻게 되시나여??"))
#         break
#     except ValueError:
#         print("정수를 입력해주세요")
     
     

# 아이디 및 패스워드 시도 

DB= {'a1':'aaaa', "b1":'vvvv',"c1": 'xxxx'}

pw_attemps= 3

while pw_attemps>0:
    user_id= input('id :')
    user_pw= (input('pw :'))
    if user_id in DB.keys() and user_pw in DB.values():
        print("로그인 성공 축화합니다.")
        
    else:
        pw_attemps-=1
        print("로그인 실패입니다.")
        print("{} 남았습니다.".format(pw_attemps))
    break
    