
##### 전체 컨셉 = 펑션 = 함수

#함수 만드는 방법이 좀 다름....다른언어랑.ㅆR....
def open_account():
    print("새로운 계좌가 개설되었습니다.")
open_account()


##### 전체 컨셉 = 전달값과 반환값
def deposit(balance, money):    #입금 하는 함수
    print("{}원 입금이 완료되었습니다. 잔액은 {} 원입니다.".format(money, balance+money))
    return balance+money        


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 출금액은 {}원이며, 잔액은 {} 원입니다.".format(money, balance-money))
        return balance-money
    else:
        print("출금이 불가합니다. 잔액은 {} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission =100
    return commission, balance- money-commission




balance=0
balance= deposit(balance,1000)        #deposot 함수를 balace에저장하는데  print구문 실행후 return값으로 balance와 money의 합이 리턴됨
# balance= withdraw(balance,1000)        #deposot 함수를 balace에저장하는데  print구문 실행후 return값으로 balance와 money의 합이 리턴됨
commission, balance= withdraw_night(balance,500)  
print("수수료는 {}원이며, 잔액은 {}원입니다.".format(commission,balance))
# print(balance)


