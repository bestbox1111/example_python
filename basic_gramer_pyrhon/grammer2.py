

#####전체 컨셉 문자열 포맷

age= 20

#방법1
print("나는 %d 살입니다." %20)  #와 같은 문법 숫자
# print("나는 %d 살입니다" %age) # 와 같이 바꿀수 있음.
print("나는 %s 을 좋아해여" %"파이썬")  #문자형
print("apple은 %c 로 시작해여" %"a")    

#방법2
print("나는 %s 과 %s 과목을 좋아해여" %("파이썬","자바"))   #넣어주는 인자가 하나이상일때.

#방법3
print("나는 {} 과 {}과목을 좋아해여".format("파이썬","자바"))   #위와 같이 넣어주는 인자가 2개일때 다른 방법사용
print("나는 {0} 과 {1}과목을 좋아해여".format("파이썬","자바"))   #위와 같이 넣어주는 인자가 2개일때 인자의 순서대로.
print("나는 {1} 과 {0}과목을 좋아해여".format("파이썬","자바"))   #위와 같이 넣어주는 인자가 2개일때 인자의 순서대로.

#방법4
print("나는 {main} 과 {sub}과목을 좋아해여".format(main="파이썬",sub="자바"))   #위와 동일한 방법이지만 포맷안에서 변수선언해서 인자에 바로 적용때려넣음


#방법5
age =20
color ="red"
print(f"나는 { age}살 이며, {color}색을 좋아해요")  # f 로 시작한후 {}안에 변수 적용시킴


#탈출문자
print("백문이 불여일견 \n백견이 불여일타")    #\n 은 줄바꿈
print("저는 \"나도 코딩\" 입니다.")          #\"으로 이중 따옴표 적용시킬수 있음.
print("저는 \\나도 코딩\\ 입니다.")          # 출력하면   저는 \나도 코딩\ 입니다. 이렇게 나옴.


#\r 커서를 맨 앞으로 이동
print("red apple\r pine")

#\b 한글자를 삭제
print("redd\bapple")

#\t 텝  탬만큼 4자리 비워주기
print("red\tapple")



