from openpyxl import load_workbook
from openpyxl.chart import BarChart, LineChart, Reference  #챠트사용시에는 임포트해줘야함.

# 전체 컨셉은 챠트

wb= load_workbook("sample4.xlsx")
ws =wb.active
bar_value= Reference(ws,min_row=1, max_row=11, min_col=2, max_col=3)            
#min_row=1로 설정하고 제목부분(영어,수학)이부분을 13,19번째라인의   titles_from_data=TRUE로 인자를 넣어주면 차트에서의 계열이 제목으로 알아서 들어감.
#b2~C11까지 영역 설정함.

#barchart부분
bar_chart= BarChart()   #차트의 정류를 변수에 지정(Bar, Line, Pie 등등)
bar_chart.add_data(bar_value, titles_from_data=True)   #차트 데이터 추가
ws.add_chart(bar_chart,"E1")    #챠트를 넣을 위치 지정해줌  E1에 넣어줌.


#linechart부분      barchart와 모든 부분 동일 변수이름만 드리게지정했음.
line_chart=LineChart()
line_chart.add_data(bar_value,titles_from_data= True)
ws.add_chart(line_chart,"N1")

line_chart.title="성적표"
line_chart.style=20         #그래프 색깔 설정
line_chart.y_axis.title= "점수"
line_chart.x_axis.title= "학생"


wb.save("sample4_chart.xlsx")
