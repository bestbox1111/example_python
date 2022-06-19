


## 모듈 몇개 ###

# import math     #임포트 해야함.

# a=math.pi
# print(a)
# print(math.floor(a))    #소수점 버리기 3
# print(math.ceil(a))    #올림 4
# print(math.isinf(a))    #해당 숫자가 무한대니??
# print(math.isnan(a))    #숫자가 아닌게 들어왔니??


import os       #os 임포트 시스템의 일부분

a=os.getcwd()       #현제 디렉토리확인
print(a)
os.chdir("C:\\Users\\park\\Desktop\\Rounding")      #디렉토리 이동 할떄
print(os.getcwd())  #이동한 현제 디렉토리 확인





# #파일 만들기 
# f=open("file1.txt","w",encoding='utf8')
# print(type(f))
# print(f.closed)     #f파일이 닫혀있냐??? 쓸려고 w해놨으니 당연히 false임..

# f.write("나는 절라 공부중입니다..")     #f 파일에 쓰기 로 데이터넣어줌.
# f.close()
# print(f.closed)     # 바로 위에서 f.close를 했으니 ..트루가됨

## 일반 open 은 파일 closed를 해줘야 해서 번거로움..

# with open("file2.txt","w", encoding="utf8") as f2:
#     f2.write('역시 절라 공부중입니다...하하\n')
#     f2.write('역시 절라절라 공부중입니다...하하\n')
#     f2.write('역시 절라절라절라 공부중입니다...하하\n')

# print(f2.closed)        #닫아주지 않아도 알아서 트루해줌.


#파일 불러오기
# fid =open("file2.txt","r",encoding="utf8")
# a=fid.read()
# print(a)
# print(fid.closed)       #파일을 불러왔으니 당연히 열려져있으니 false니까


# b= fid.readline()       #한줄씩 불러오기...
# print(b)
# b= fid.readline()
# print(b)
# b= fid.readline()
# print(b)

# fid.close() # 확실히 파일 닫아줌.



import json

data=["abfga","gargrag","gargargargargar.."]
print(data)
print(type(data))


#joson으로 저장하기...
f= open("file3.txt","w",encoding="utf8")
a=json.dump(data, f)
f.close


#json으로 불러오기
f=open("file3.txt", "r", encoding="utf8")
x= json.load(f)
f.closed
print(x)



