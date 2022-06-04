'''표준 페중을 구하는 프로그램을 작성하시오'''

'''표준 체중: 각 개인의 키에 적당한 체중'''

'''(성별에 따른 공식)
남자: 키*키*22
여자: 키*키*21
'''

#조건1 : 표준 체중은 별도의 함수 내에서 계산
    #함수명 std_weight
    #전달값: height, gender
#조건2 :  표준 체중은 소수점 둘째 자리까지 표시

# 키 175 남자의 표준 체중은 67.38kg 입니다.

#아래 방식은 내방식...
# def std_weight(height, gender):
#     if gender == "남자":
#         stand =height * height*22/10000
#         stand=round(stand,2)
#         print("키 {}cm {}의 표준 체중은 {}kg 입니다".format(height,gender,stand))
#         return stand
#     elif gender=="여자":
#         stand =height * height*21/10000
#         stand=round(stand,2)
#         print("키 {}cm {}의 표준 체중은 {}kg 입니다".format(height,gender,stand))
#         return stand
#     else:
#         print("성별을 정확히 입력하시오")
# std_weight(175,"남자")
        

#아래 방식은 강사방식.
def std(height, gender):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21
    
height =175
gender="남자"
weight = std(height/100, gender)

print("키 {}cm {}의 표준 체중은 {}kg 입니다".format(height,gender,round(weight,2)))
