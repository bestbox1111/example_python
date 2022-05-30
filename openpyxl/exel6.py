from openpyxl import load_workbook  #엑셀파일 불러오기.

wb= load_workbook("sample4.xlsx")
ws = wb.active

#전체 컨셉은 셀의 조건설정 및 수정

# 영어 점수가 80인 학생들에 대해 출력했지만
for row in ws.iter_rows(min_row=2):
    if int(row[1].value)>80:
        print(row[0].value,"번 학생은 80점 이상힙니다.")
        
        

#해당 영어란이 컴퓨터란이어야 하는데 오류가 발생했을시 수정
for row in ws.iter_rows(max_row=1):
    for cell in row:
        if cell.value =="영어":
            cell.value="컴퓨터"


wb.save("sample4_modified.xlsx")    #수정한 파일을 다른이름으로 다시저장.