""""동네에 항상 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하여 적절한 예외처리 구문을 넣으시오

조건1 : 1보다 적거나 숫자가 아닌 입력값이 들어올때는,valueError로처리
        출력 메세지 "잘못된 값을 입력했습니다.
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 솟진시 사용자 저의 에러 soldsoutError를 발생시키고 프로그램 정료
        출력 메시지 : 재고가 소진되어 더 이상 주문을 받지 않습니다.
"""

#문제 기본제공 코드
# from tokenize import Number


# chicken =10
# waiting =1
# while(True):
        
#     print("남은 치킨 : {}". format(chicken))
#     order=int(input("치킨을 몇 마리 주문하시겠습니까???"))
    
#     if order > chicken:
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 : {}]   {} 마리 치킨이 주문되었습니다.".format(waiting,order))
#         waiting+=1
#         chicken-=order




from tokenize import Number

class SoudOutError(Exception):
    pass


chicken =10
waiting =1




while(True):
    try:    
        print("남은 치킨 : {}". format(chicken))
        order=int(input("치킨을 몇 마리 주문하시겠습니까???"))
        
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 : {}]   {} 마리 치킨이 주문되었습니다.".format(waiting,order))
            waiting+=1
            chicken-=order
            if chicken == 0:
                raise SoudOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoudOutError:
        print("재료가 소진되어 주문을 더이상 받지 않습니다..")
        break
