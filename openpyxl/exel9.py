from openpyxl import load_workbook

# 전체 컨셉은 이동...

wb= load_workbook("sample4.xlsx")
ws =wb.active

#현제 파일 에는 번호, 영어,수학으로 되있지만
#번호, (국어), 영어, 수학으로 변화하려하는 목적

ws.move_range("B1:C11", rows=0, cols=1)     #이동을 원하는 부분을 설정하고 , 이후에 row와 col으로 원하는 이동 설정
ws["B1"].value ="국어"  #B1셀에 국어입력됨.

wb.save("sample4_moveto.xlsx")