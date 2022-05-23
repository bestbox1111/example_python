from openpyxl import load_workbook

# 전체 컨셉은 삽입...

wb= load_workbook("sample3.xlsx")
ws =wb.active

# ws.insert_rows(8)   #sample3파일 8번쨰줄에 삽입줄이 하나 생기는것 ======>좌에서우로  row로
# ws.insert_rows(9,3) #위와 같은 방식이지만 9번쨰 줄부터 3줄을 삽입한다는 의미.

ws.insert_cols(2)  #sample3파일 2번 줄에 삽입 ======>우에서 아래로 comumn

ws.insert_cols(2,3)  #위와 같은 방식이지만 2번쨰 줄부터 3줄을 삽입한다는 의미.

wb.save("sample3_insert_rows.xlsx")



