

#### 전체 컨셉은 표준 입출력

print("python"," JAVA")     # 일반적으로 python  JAVA   으로 출력됨

print("python","JAVa","C++", sep=" vs ")        #sep안에 각 인자들사이에 들어갈 문자열 넣을수 있음

print("python","JAVa","C++", end="?")        #sep안에 각 인자들사이에 들어갈 문자열 넣을수 있음
print("무엇이 더 재미있을까여???")          # python JAVa C++?무엇이 더 재미있을까여??? 와 같이 출력됨 ?는 한줄로 이어서 출력되게함


#
scores = {"수학": 0,"영어":50,"코딩":100}

for subject, score in scores.items():
    print(subject, score)
# 아래와 같이 나오지만  뒷 점수를 열을 맞추고 싶다면.  
# 수학 0
# 영어 50
# 코딩 100
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=" : ")     #ljust()   인자만큼 왼쪽부터 정렬, rjust() 인자만큼 오른쪽 정열
    
    
    
# 은행 대기 번호를 001, 002 , 003 순으로 만들고싶다면?
# 아래와 같이 노가다로 만들수도 있지만....
for num in range(1,111):
    # print(num)
    if(num<10):
        print("00"+str(num).rjust(1))
    elif(num>=10 and num<100):
        print("0"+str(num).rjust(2))
    else:
        print(num)
        
#위의 7줄짜리 코드가 아래와 같이 두줄로 처리됨.
for number in range(1,110):
    print("대기번호 :" +str(number).zfill(3))           # zfill(3): 3자리숫자지만 numer의 숫자 이외는 0으로 채운다.
    
    
    

#### 표준 입력 = input
# input으로 받은 값은 숫자건 문자건 스트링으로 받아진다.***
answer= input("아무 값이나 입력하세요: ")       
print(" 입력하신 값은 ", answer, "입니다")