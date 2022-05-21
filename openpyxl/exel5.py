from openpyxl import Workbook
from openpyxl.utils.cell import coordinate_from_string      #셀의 정보를 알고 싶을때 (좌표정보)
from random import *    #랜덤값 넣기 위해 임포트

wb= Workbook()  #새로운 워크북 생성
ws= wb.active



ws.append(["번호","영어","수학"])   #한줄씩 값을 넣을때.
for i in range(1,11):      
    ws.append([i,randint(0,100),randint(0,100)])

english =ws["B"]    #영어 컬럼만 가지고 오기위해서

for cell in english:    #영어 컬럼의 값을 반복문을 통해 가지고오기
    print(cell.value)

col_range= ws["B:C"]    #영어와 수학의 컬럼의 값만 가지고 오기
for cols in col_range:      #B:C의 셀 cols에 저장
    for cell in cols:       #cols에 값을 cell에 저장함.
        print(cell.value)   
  


row_range= ws[1]    #row가지고 오기1번째 줄만
for cell in row_range:      #1번째줄을 cell 에넣기
    print(cell.value)   


row_ranges= ws[1:5]    # 여러줄의 row가지고 오기 1 부터5까지
for rows in row_ranges:      #row_ranges의 셀을 rows에 넣고
    for cell in rows:       #rows의 값을 cell에 저장함.
        print(cell.value, end=" ")   
    print()


#로우의 마지막줄까지 넣고 싶을때
row_ranges2= ws[1:ws.max_row]    # 2번째 줄부터 마지막 줄까지
for rows in row_ranges2:     
    for cell in rows:      
        print(cell.value, end=" ")   
        print(cell.coordinate, end=" ")     #셀의 정보를 알고 싶을때   A2 B2 C2 이런식으로나옴
        xy = coordinate_from_string(cell.coordinate)    #'(A', 2) ('B', 2) ('C', 2) 이런식으로확인
        # xy[0]=A   이라는걸 확인
        # xy[1]=1   이라는걸 확인
        print(xy,end=" ")
    print()




print(tuple(ws.rows))   #(<Cell 'Sheet'.A1>, <Cell 'Sheet'.B1>, <Cell 'Sheet'.C1>)
print(tuple(ws.columns))  #(<Cell 'Sheet'.A1>, <Cell 'Sheet'.A2>, <Cell 'Sheet'.A3>, <Cell 'Sheet'.A4>, <Cell 'Sheet'.A5>, <Cell 'Sheet'.A6>, <Cell 'Sheet'.A7>, <Cell 'Sheet'.A8>, <Cell 
# 'Sheet'.A9>, <Cell 'Sheet'.A10>

print()
print()
print()
print()


#시트에 원하는 셀에 있는 값만 찾아 보고싶을대
for rows in tuple(ws.rows):         
    print(rows[1].value)    #rows에 1번째 있는 값만 확인 하고싶을때



for rows in ws.iter_rows():
    print(rows[2].value)    #전체 rows에 2번째 있는 값만 확인 하고싶을때




for columns in ws.iter_cols():
    print(columns[0].value)    #전체 column 에 0번째 있는 값만 확인 하고싶을때



for rows in ws.iter_rows(min_row=2, max_row=5):
    print(rows[2].value)    #전체 rows[2]에 있는 2번째부터 5번째 값만 확인 하고싶을때





for row in ws.iter_rows(min_row=2, max_row=11, min_col=2, max_col=3):
    print(row[0].value, row[1].value)   #전체 row 2번째부터 11번째 값 column은 2번쨰부터 3번째 확인 하고싶을때
wb.save("sample4.xlsx") 