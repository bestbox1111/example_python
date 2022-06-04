

#### 전체 컨셉은 전역변수와 지역변수
#아래와 같은 코드는 gun= gun-sol부분에서 local---어쩌구머시기 오류가남.
gun =10

def check(sol):
    gun = gun -sol
    print("[함수내] 남은총: {}".format(gun))

print("전체 총: {}".format(gun))
# check(3)  #함수 오류로 인해 주석 처리해놓음.
print("남은 총: {}".format(gun))


# 위 오류의 이유는 gun이라는 변수가 check내에서 사용하는데 선언이 안되어있기 때문이라
# 해당 변수를 함수내외에서 동일하게 쓰기 위해 global 이라고 선언후 사용해야함.
# 하지만 전역변수를 함수내외에서 사용하는건 좋은 방법이 아님.
gun =10

def check(sol):
    global gun
    gun = gun -sol
    print("[함수내] 남은총: {}".format(gun))

print("전체 총: {}".format(gun))
check(3)
print("남은 총: {}".format(gun))


# 위의 2가지 방법보다는 함수내에서 해당 변수를 처리하여 리턴값으로 받아서 원하는 계산처리 방식이 최적임.
# 위2번째와 동일 한 결과임
gun =10

def check_modify(gun, sol):
    gun = gun -sol
    print("[함수내] 남은총: {}".format(gun))
    return gun

print("전체 총: {}".format(gun))
gun=check_modify(gun,2)
print("남은 총: {}".format(gun))
