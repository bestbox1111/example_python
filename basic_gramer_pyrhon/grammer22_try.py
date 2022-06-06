


#### 전체 컨셉 = 예외처리


#계산기 만들는 예제시에
# 1번째 기본 문자열 입력 에러용
# try:
#     print("나누기 전용계산기 입니다.")
#     num1 =int(input("첫번째 숫자는 ?"))
#     num2 =int(input("두번째 숫자는 ?"))       #숫자가 아닌 문자를 넣었을경우 ValueError: invalid literal for int() with base  '삼' 
#     num3= num1/num2
#     print(" {} / {} ={}".format(num1,num2,int(num3)))
# except ValueError:
#     print("에러가 발생하였습니다.")
#10라인 이후, 11라인 이후 오류 발생후 12, 13라인 실행 안되고 14라인으로 넘어옴

# 2번째 기본 0으로 나누는 예제에러
# try:
#     print("나누기 전용계산기 입니다.")
#     num1 =int(input("첫번째 숫자는 ?"))
#     num2 =int(input("두번째 숫자는 ?"))         # 문자가 아닌 숫자를 나눌수 없는 0이들어갈때
#     num3= num1/num2
#     print(" {} / {} ={}".format(num1,num2,int(num3)))
# except ValueError:
#     print("에러가 발생하였습니다.")
# except ZeroDivisionError as  zeroerr:
#     print(zeroerr)
    

# 3번째 에러 out of index err
try:
    print("나누기 전용계산기 입니다.")
    nums=[]
    nums.append(int(input("첫번째 숫자는 ?")))
    nums.append(int(input("두번째 숫자는 ?")))
    # nums.append(int(nums[0]/ nums[1]))            #배열 즉 리스트 사용시 가장 많은 오류로 인덱스 범위의 사용범위를 넘어서사용하려 할때 나오는애레

    print(" {} / {} ={}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러가 발생하였습니다.")
except ZeroDivisionError as  zeroerr:
    print(zeroerr)
except IndexError as  inerr:
    print(inerr)