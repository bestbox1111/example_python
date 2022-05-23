from openpyxl import load_workbook
from openpyxl.styles import Font, Border, Side, PatternFill, Alignment      #폰트 꾸미기할때


# 전체 컨셉은 셀 꾸미기 셀의 [높이와 너비]

wb= load_workbook("sample4.xlsx")
ws =wb.active


# 번호 ,영어, 수학
a1= ws["A1"]    #번호셀을 a1으로 저장
b1= ws["B1"]    #영어셀을 b1으로 저장
c1= ws["C1"]    #수학셀을 c1으로 저장.


ws.column_dimensions["A"].width = 5    #A열의 너비를 10으로 설정
ws.row_dimensions[1].height = 35    #A열의 높이를 35으로 설정

a1.font= Font(color="FF0000", bold=True)    #폰트 색상을 빨갱이로, 글자굵기는 굵게로
b1.font= Font(color="CC33FF", name="Arial", strike=True)    #폰트 색상은 분홍, 글꼴은 아미알, 스트라이크는 취소선임.글자에 짝대기
c1.font= Font(color="0000FF",size=10, underline="single")   #폰트 색상은 블루, 사이즈는 30, 언더라인은 글자밑에 한줄치기

#테두리 적용

# thin = Border(left=Side(style="thin"),right=Side(style="thin"),top=Side(style="thin"),bottom=Side(style="thin"))
# a1.border=thin
# b1.border=thin
# c1.border=thin

#셀에 조건 걸어서 확인 하는법
#90점 넘는 셀에 대해서 초록색으로 적용

for row in ws.rows:     #ws.rows에 있는 정보를 row에 대입
    for cell in row:        #row에 있는 정보를 cell에 대입  --->전체 셀
        cell.alignment = Alignment(horizontal="center",vertical="center")    #글자를 중앙정렬 시키는 부분


        if cell.column == 1:     #1번째 컬럼에는 넘버,영어,수학의 타이틀이 있으니까  
            continue            #컨티뉴로 넘기고
        
        
        # cell.value가 인트이면서 90점 이상이면 
        if isinstance(cell.value, int) and cell.value > 80: 
            cell.fill = PatternFill(fgColor="00FF00",fill_type="solid")
            cell.font=  Font(color="FF0000")

#틀고정하기 엑셀데이터가 많아질시 스크롤하면 제목이랑 타이틀 같은게 안나올때
ws.freeze_panes = "B2"


wb.save("sample4_style.xlsx")