# 출석 10
# 퀴즈1 10
# 퀴즈2 10
# 중간고사 20
# 기말고사 30
# 프로젝트 20

# 총합 100


# 마지막 수업을 모두 마치고 이번학기 학생들의 최종 성적을 
# 학생은 10명으로 하며, 점수는 각각 알아서
# 검토하는 과정에서 퀴즈2 문제에 오류를 발견하여 모두 만점 처리를 
# 하기로 했습니다
# 현제 까지 작성된 최종 성적 데이터를 기준으로 아래와 같이 수정하시오.

# 1. 퀴즈2 점수를 10으로 수정
# 2. H열에 총점(sum 이용) , I열에 성적 정보 추가
# -총점 90 이상 A, 80이상 B, 70이상 C 나머지 D
# 3. 출석이 5미만인 학생은 총점 상관없이 F

# *최종 파일명은 score.xlsx


from openpyxl import Workbook
from random import *    #랜덤값 넣기 위해 임포트
  

wb= Workbook()  #새워크북 생성(새 시트 생성)
ws =wb.active  # 현제 활성화된 sheet 가져옴.

ws.title ="박준형의 엑셀연습"




ws.append(("학번", "출석","퀴즈1","퀴즈2","중간","기말","프로젝트"))   #한줄씩 값을 넣을때.
 
scores = [
(1,10,8,5,14,26,12),
(2,7,3,7,15,24,18),
(3,9,5,8,8,12,4),
(4,7,8,7,17,21,18),
(5,7,8,7,16,25,15),
(6,3,5,8,8,17,0),
(7,4,9,10,16,27,18),
(8,6,6,6,15,19,17),
(9,10,10,9,19,30,19),
(10,9,8,8,20,25,20)
]


for s in scores:
    ws.append(s)


#1. 퀴즈2 점수를 모두 10으로 수정

for idx , cell in enumerate(ws["D"]):
    if idx == 0:
        continue
    cell.value = 10
    
#2. H열에 총점(sum)이용 , I 열에 설적 정보 추가
    
ws["H1"]="총점"
ws["I1"]="성적"



#컬럼        a b c d e f g h i
#컬럼 숫자로 1 2 3 4 5 6 7 8 9
for idx, score in enumerate(scores, start=2):  
    sum_val = sum(score[1:])-score[3]+10         # 스타트2는 score에 7개의 인덱스가 있는데 1번째는 학번이라2부터
    ws.cell(row=idx, column=8).value ="=SUM(B{}:G{})".format(idx,idx)
    
#3 성적 정보 A,B,C,D 나누는 부분

    grade = None

    if sum_val >=90:
        grade= "A"
    elif sum_val>=80:
        grade= "B"
    elif sum_val>=70:
        grade= "C"
    else:
        grade="D"
    
    
    
    #4 출석이 5미만인 학생은 무조건 성적 F
    if score[1] < 5:
        grade="F"

    ws.cell(row=idx, column=9).value=grade          #쓰박 파이선은 줄 틀리면 답안나오네....

wb.save("score.xlsx")