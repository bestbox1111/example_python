from openpyxl import Workbook


wb= Workbook()  #새워크북 생성(새 시트 생성)
ws =wb.active  # 현제 활성화된 sheet 가져옴.

ws.title ="박준형의 엑셀연습"   #sheet의 이름을 변경
wb.save("sample.xlsx")  #파일이름을 정하고 저장해줌.


# wb= Workbook()
# ws= wb.create_sheet()
# wb.save("sample2.xlsx")