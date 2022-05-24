from openpyxl import Workbook
import datetime

#전체 컨셉은 수식

wb= Workbook()
ws =wb.active

ws["A1"]= datetime.datetime.today()     #오늘 날짜 정보
ws["A2"]= "=SUM(1, 2, 3)"     #1+2+3 =6이 출력
ws["A3"]="=AVERAGE(1,2,3)"  # 6의 평균인 2가 출력

ws["A4"] =10    #A4에 10을 넣어줌.
ws["A5"] =20    #A4에 20을 넣어줌.
ws["A6"]="=SUM(A4:A5)"  # 6의 평균인 2가 출력

wb.save("sample_formul.xlsx")



