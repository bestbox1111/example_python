from openpyxl import Workbook
from random import *    #랜덤값 넣기 위해 임포트

wb= Workbook()  #새로운 워크북 생성
ws= wb.active
ws.title="parksheet"

ws["A1"]=1
ws["A2"]=2
ws["A3"]=3

ws["b1"]=4
ws["b2"]=5
ws["b3"]=6

# ws.cell(row=1, colum=1) 과 ws["A1"] 과 같은 방식임.

print(ws["A1"]) #ws["A1"]의 객체정보를 출력 <Cell 'parksheet'.A1>

print(ws["A1"].value) #ws["A1"]의 값을 출력
print(ws.cell(row=1,column=1).value) #ws["A1"]의 값을 출력

# 위의 2가지 20,21라인 결과는 똑같음


# ws.cell(row=1,column=10,value=10) 와
# ws["j1"] = 10 과 같은 표현임






# 반복문을 이용해서 랜덤 숫자 채우기


for x in range(1,11):
    for y in range(1,11):
        ws.cell(row=x, column=y, value=randint(0,100))
    # A B C ====> 순서로 값이 들어감.(컬럼순)

wb.save("sample3.xlsx")


# 34분까지 완료
