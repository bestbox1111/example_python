

# 함수 설명 해주는 방법     """엔터"""
# def add(x):
#     """_summary_

#     Args:
#         x (_type_): gragrargagar
#     Returns:
#         _type_: _description_
#     """
#     c=x+10
#     return c
# add(10)
# print(add(10))


#annotaion
# def fn(num):
#     out=num+10
#     return out
# print(fn.__annotations__)

# def fn(num:int):
#     out=num+10
#     return out
# print(fn.__annotations__)
#{'num': <class 'int'>} 이런식으로 인풋의 파라미터가 인트어야 한다는 주석.

#리턴값의 타입을 주석달고 싶으면 -> 형식으로 인풋값옆에 표시.
# def fn(num:int)->int:
#     out=num+10
#     return out
# print(fn.__annotations__)       
#{'num': <class 'int'>, 'return': <class 'int'>} 위와 같은 형식으로 나옴.


#lamda  사용.
# def add(a):
#     c=a+1
#     return c
#위의 add 함수와

#아래의 lamda를 사용한 add 함수는 동일하지만 더욱 간결.
# add= lambda x: x+1
# print(add(4))

# #lamda 함수를 매개변수까지 넣어서 변수에 지정하여 사용가능함.
# y= (lambda x: x+1)(10)  # 변수=(lamda 구문)(매개변수)
# print(y)


# def add10(x):
#     return x+10     #함수를 하나 만듬.

# high= (lambda x: x+add10(x))(10)    #만든 함수를 다른 람다함수의 매개 변수로 넣을수 있음.
# print(high)


import numpy as np 

#map의 예시1

a= np.array([1,2,3,4,5])
c=a*2
print(c)
#[ 2  4  6  8 10] 으로 출력됨.

b=[1,2,3,4,5]
c2=2*b
print(c2)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]으로 출력됨.

# 위와 같이 각 인덱스값에 해당 값이 계신되길 원할때 map()을 사용.

def add(x):
    return x+10

d=list(map(add,a))  #list를 안감싸주면.. <map object at 0x000002674AAC34C0> 객체 주소형식으로 반환.
# [11, 12, 13, 14, 15] 이런식으로 각 인덱스값이 하나씩 계산됨.


#map의 예시2
vip='euler'
print(vip.upper())      #하나의 변수로 적용할때 upper 함수는 사용가능함

vip_l=["park","jun","hyung"]
# print(vip_l.upper())        #리스트에는 upper함수 적용안됨.오류로 인해 주석처리
# 이럴때 map
vip_list=list(map(lambda x: x.upper(), vip_l))      #vip_l이 리스트지만 마지막 맵핑할떄 list로 형변환 덧쒸워져야 하는듯.
print(vip_list) #['PARK', 'JUN', 'HYUNG'] 으로 각 인덱스안애 애덜이 적용받음.


#위의 각 인덱스안에 있는 애덜의 글자 길이를 알고 싶다면 원래는 각 인덱스 별로    len을 때려야 하는데.
print(len(vip_l[0]))
print(len(vip_l[1]))
print(len(vip_l[2]))



vip_len=list(map(lambda x: len(x), vip_l))
print(vip_len)  #[4, 3, 5] 다음과 같이 람다도 한꺼 번에 묶어서 계산