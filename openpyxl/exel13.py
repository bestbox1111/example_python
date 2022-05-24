from openpyxl import load_workbook


#전체 컨셉은 수식(데이터 전용)

wb=load_workbook("sample_formul.xlsx")
ws= wb.active


# 수식을 그대로 가져옴.
for row in ws.values:
    for cell in row:
        print(cell)

''' # 위의 for문 돌리면 아래와 같이 뜸
2022-05-24 19:34:08.107000
=SUM(1, 2, 3)
=AVERAGE(1,2,3)
10
20
=SUM(A4:A5)
'''


# 수식이 아닌 실제 데이터 그대로 가져옴.

wb=load_workbook("sample_formul.xlsx", data_only=True)      #data-only=True 를 추가할시에.~
ws= wb.active


for row in ws.values:
    for cell in row:
        print(cell)