from openpyxl import load_workbook  #파일불러오기

#전체 컨셉은 파일 불러오기

wb= load_workbook("sample3.xlsx")   #sample3.xlsx 파일에서 wb불러옴
ws= wb.active   # 활성화된 sheet


# cell 데이터 불러오기 셀갯수를 알때
for x in range(1,11):
    for y in range(1,11):
        print(ws.cell(row=x, column=y).value, end=" ")
    print()


# cell 데이터 불러오기  셀갯수를 모를때
for x in range(1, ws.max_row +1):
    for y in range(1, ws.max_column +1):
        print(ws.cell(row=x, column=y).value, end=" ")
    print()