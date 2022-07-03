
# map 과 filer 과 reduce 관련.

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



## filter 관련


#flilter 예시1
find_filter= list(filter(lambda x: 'u' in x, vip_l))    #람다식으로 vip_l을 x라고 넣고 그 x에 p 라는 문자열들어간게 있으면 출력해라.
print(find_filter)      #['park']으로 출력됨.


#filte r예시2
x=[1,2,3,4,5]

filter_val= list(filter(lambda x: x%2==0, x))   #람다식의 x에 조건을 넣을수도 있음 이 경우는 x의 나머지가==0일 경우임.
print(filter_val)   #[2, 4]로 출력됨.



#### reduce

from functools import reduce    #reduce 사용하기 위한 임포트

#reduce 예시 1
num_l=[10,20,30]    #리스트일단 만듬.

def add(x,y):       #함수 매개변수 두개 더하는걸로 일단 만듬.
    return x+y      # 리턴 각 매개변수더하는걸로 일단 만듬.

redece_p= reduce(add,num_l)     
# 변수지정후 reduce(함수, 데이터변수) 함수의 x+y 즉10+20먼저 계산후 20+30이 후 계산됨.
print(redece_p)

lambda_p=reduce(lambda a,b: a+b, num_l) #위와 동일한 결과지만 람다식을 이용하여 계산.
print(lambda_p)


#reduce 예시 2

str_l=["p","y","t","h","o","n"]
reduce_l=reduce(add,str_l)
print(reduce_l)     #python 출력    문자열에도 적용됨.

lambda_l=reduce(lambda a,b: a+b, str_l)
print(lambda_l)   #python 출력    문자열에도 적용됨.    위와 동일.


for sum_l in str_l:     #for문을 이용했을때는 다음과같다.
    print(sum_l,end="")