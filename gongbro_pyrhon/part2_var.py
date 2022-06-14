
# 변수(35:00 ~ 58:00)

a=1  # 값을 저장하기 위한 공간.
print(a)


a=1
b=4     

a=b     #또다른 변수에 변수의 값을 저장가능.
print(a)
 
 
c=1+2j
c.conjugate 


name ="park"
print(name.capitalize())        #첫글자 대문자
print(name.count("p"))  #포함되는 글자 갯수


name2="dongsoo"
name2.split("g")
print(name2.split("g"))
name2_split=name2.split("g")    #g로 나눠진 애를 쪼갠리스트를 변수에 저장.

# print(type(name2.split("g")))    #list로 나옴.
print(name2_split[0])   
print(name2_split[1])


s="ab\\cdef"    #심벌로 인식되는 부분으로 \ 외에 \\으로 해줘야함.
print(s)

#input 함수를 통해 받게 되면 무조건 스트링으로 받게된다.인트로 받고싶으면 받으면서 형변환하거나 나중에 변환해야함.



# 변수동시 저장 가능

a,b = 20,40;
print(a,b)  #a=20, b=40


a,b =b,a    #미친 기능임... a,b를 b,a로 대입.
print(a,b)      #a=40, b=20