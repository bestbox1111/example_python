'''당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.'''


# -X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :


# 1 주차 부터 50 주차가지의 보고서 파일을 만드는 프로그램을 만드시오.



# week = open("x주차.txt", "w", encoding="utf8") # w는 쓰기 전용 utf8 = 한글 깨지는거 방지위함.

# for i in range(1,51):
#     week = open("{}주차.txt".format(i), "w", encoding="utf8") # w는 쓰기 전용 utf8 = 한글 깨지는거 방지위함.

#     print("- {} 주차 주간보고 -".format(i), file=week)
#     print("부서 :", file=week)
#     print("이름 : ", file=week)
#     print("업무요약 : ", file=week)

# week.close()



for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("{}주차 주간보고".format(i))
        report_file.write("\n부서", )
        report_file.write("\n이름")
        report_file.write("\n업무요약")

report_file.close()