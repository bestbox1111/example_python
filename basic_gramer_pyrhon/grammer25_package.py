



#### 전체 컨셉 = package
# 페키지를 위해 travel 폴더에 패키지파일들 몇개 만들어 논거 임포트하는 부분은 아래에

# import travel.thailand  #트레블.타일랜드 임포트     (모듈이나 패키지까지만 )     클래스나 함수느 임포는 암ㅍㅎ트 안됨.
# trip_ro = travel.thailand.ThailandPackage() # 변수에 타일랜드 패키지클래스의 객체를 만듬
# trip_ro.detail()    #함수실행시킴


# from travel import vietnam  #프럼을 사용한 임포트
# trip2_to = vietnam.VietnamPackage().detail()


from travel import*     

trip_to = vietnam.VietnamPackage()      #위와 같이 임포트를 해도 사용이 안되는데 그이유는 패키지  __init__  에서 설정안해서그럼.
trip_to.detail()

trip_to2=thailand.ThailandPackage().detail()