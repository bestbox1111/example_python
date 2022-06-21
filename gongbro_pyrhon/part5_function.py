


## 함수에 관해서 ###


#함수 정의 def + 함수이름 +(인자) + :
# 즉 def park(a):


# def park_1():
#     print("hellow")
# park_1()

# def park_2(x):
#     print("hellow",str(x))
# park_2(4)

#위의 park_2에서 함수를 프린트 하는 변수에 저장하여 그걸 프린트 하면 none이 출력됨.

#위의 park_2를 조금 변형해서

# def park_3(a):
#     y= a+10
#     return y
# park_3(11)      #함수만 호출
# print(park_3(11))   #호출한 함수값을  프린트로 확인.




#### local (지역 변수와)  global (전역변수)  ###



# 함수 정의 
# 함수내의 y변수 확인필욧.
# def add(x):
#     y= x+10
#     print("함수내의 y의 합의 갑은",y,"입니다.")
#     return y   
# # 함수밖에서 y를 10으로 넣어줌.
# y=10
# add(19)     #함수불러오면. 두개의y는 다른 값으로 출력됨. a반 철수와 b반 철수와 비슷한 의미라고 보면됨.
# print("함수밖의 y의 값은 ",y, "입니다.")


#위의 예로 동일한 y값으로 작업하고 싶다면.
# def add2(x):
#     global y
#     y= x+10
#     print("add2 함수내의 y의 합의 갑은",y,"입니다.")
#     return y   
# add2(20)
# print("add2 전역함수의 y의 값은" ,y,"입니다.")


#함수의 input
# def add3(x):
#     print(x+10)
#     return x+10
# add3()  #원래 대로 라면 함수에 x인자 하나 들어가야 하는데 노인자로 함수호출하니 오류가뜨지만.

# def add3(x=5):  #이러식으로 인자에 기본값을 줘버리면 호출시 값을 안줘도 됨.
#     print(x+10)
#     return x+10
# add3()  