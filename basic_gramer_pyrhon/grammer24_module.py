

#### 전체 컨셉 = 모듈
# 극장에서 영화 가격모듈

# import c_module         #만든 모듈 임포트
# c_module.price(4)       #c_module에서 만듬 함수 실행
# c_module.price_morning(4)       #c_module에서 만듬 함수 실행
# c_module.price_soldier(4)       #c_module에서 만듬 함수 실행



# import c_module as cm         #만든 모듈 임포트 한애를 as를 쓰면 이름을 내 스타일대로 바꿀수있음(별명)
# cm.price(4)       #c_module에서 만듬 함수 실행
# cm.price_morning(4)       #c_module에서 만듬 함수 실행
# cm.price_soldier(4)       #c_module에서 만듬 함수 실행


# from c_module import *  # 위에들은 파일 내용만 가져온다면 애는 그냥 파일 통체로 가져와서 함수만 사용해도됨.
# price(4)
# price_morning(4)
# price_soldier(4)


# from c_module import price, price_morning# 위에들은 파일 내용만 가져온다면 애는 그냥 파일 통체로 가져와서 함수만 사용해도됨.
# price(4)        
# price_morning(4)
# price_soldier(4)    #위에서 임포트한 함수만 사용가능함