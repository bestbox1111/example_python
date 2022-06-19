
# string
# 변수 지정하고 값을 넣으면 a=9 처엄 값만 들어가지만..
# a= "park" 과 같이 스트링을 저장하면 인덱스처리가됨.


# a ="park"
# print(a)

# print(a.capitalize())   #첫글자만 대문자
# print(a.find("p"))      #해당 문자가 존재하는 인댁스반환
# print(a.find("e"))      # 해당 문자 없으면 -1반환


# b="parkjun3"
# # print(b.index("b"))     # 해당 문자 없으면 에러반환해줌.
# print(b.isalpha())      #  문자만 으로 되어있냐??? 트루 및 펄스 반환.

# c="park 3"
# print(c.isalnum())  #문자와 숫자가 들어갔느냐?? 펄스로나옴..이유는 스페이스가 존재해서
# c2="park3"
# print(c2.isalnum())     #스페이스 제거하면 문자와 숫자로 인식.


# d="9"
# print(d.isdecimal())    #0부터~~ 숫자만 들어갔는지 물어보는거임..
# d2="9.999"
# print(d2.isdecimal())  # 소수점 값은 펄스로 리턴해줌.


# e="Python"
# print(e.islower())  #소문자로돼어있냐??? P가 대문자니 펄스임
# print(e.isupper())  #대문자로 돼어있냐???
# print(e.replace("P","A"))       #P를 A로 바꿔줌.
# print(e.split("t"))  # 해당 문자를 기준으로 나누어줌.






##print , format ###

from h11 import Data


s= "python {}"
print(s.format(4))


s2= "python {0} {1}"        
print(s2.format("4","version"))     #python 4 version


s2= "python {1} {0}"        
print(s2.format("4","version"))   #python version 4         순서바꿔서 출력도가능.



#format을 쓰는게 유용한 이유

data=1234.5678
print("data=",str(data))
print("data={}".format(data))

print('data={:.2f}'.format(data))  #소수점 2번째까지만.
print('data={:.0f}'.format(data))  #소수점 0번째까지만.
print('data={:4.0f}'.format(data))  #4째자리 수까지만.
print('data={:6.0f}'.format(data))  #공백포함 6자리 숫자만듬.

# :6 자리수  .0소수점자리  f 숫자타입

