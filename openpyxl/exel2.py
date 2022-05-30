from openpyxl import Workbook


wb= Workbook()  #새로운 워크북 생성

#전체 컨셉은 시트생성및 이름 변경 등

ws= wb.create_sheet()   # 기존 시트 옆에다가 새로운 시트를 생성
ws.title="박준형의 예제연습2"   #sheet이름 변경

ws.sheet_properties.tabColor ="ff66ff"  #sheet의 탭샐깔을 변경

ws1 = wb.create_sheet("박준형의 예제연습3") #sheet를 새로 생성하면서 시트이름을 동시에넣음 7라인이 생략된버전
ws2 = wb.create_sheet("박준형의 예제연습--시트중간에 넣기",2)  # 기존 시트옆에다가 생성하는거 말고 원하는 시트옆에 넣을때 인덱스를 인자로 넣어줌.


new_ws = wb["박준형의 예제연습3"]   #딕션 형태로 sheet에 접근--시트 생성의방법

# print(wb.sheetnames)    # 현제 활성화 되어 있는 시트 이름들 확인가능.

new_ws["A1"]="park"     #new_ws ==> 박준형의 예제연습3의 시트의 A1에 park을 넣어주고
target= wb.copy_worksheet(new_ws)   #new_ws의 시트를 타켓에 넣어주고
target.title="Copied sheet"     # 그타켓의 시트 타이틀을 coped sheet라고 해줌.



wb.save("sample.xlsx")
