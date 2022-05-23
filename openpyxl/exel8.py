from openpyxl import load_workbook

# 전체 컨셉은 삭제...

wb= load_workbook("sample4.xlsx")
ws =wb.active

#sample3 파일중 7번째줄 6번친구가 전학을 가서 삭재되어야 할때.
ws.delete_rows(7)
#sample3 파일중 7번째줄 6번부터 3줄 삭제할때
ws.delete_rows(7,3)



#sample3 파일중 1번쨰 컬럼 삭제.
ws.delete_cols(1)
#sample3 파일중 1번쨰 컬럼부터. 2줄 삭제할때
ws.delete_rows(1,2)



wb.save("sample4_delete_row.xlsx")