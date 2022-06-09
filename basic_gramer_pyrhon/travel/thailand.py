

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원 ")
     
    
    
    
    #### 모듈을 직접 실행 ... 모듈이 정상 작동되는지 확인 하기 위해
if __name__== "__main__":
    print("타일랜드 모듈을 직접 실행")
    
    trip_tp = ThailandPackage()
    trip_tp.detail()
else:
    print("타일랜드 모듈을 외부에서 호출")