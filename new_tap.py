from selenium import webdriver
import time


# 시스템에 부탁된 장치가 작동하지 않습니다라는 오류가 뜨면 다음아래와같이
# 2줄을 입력후 3번째 줄처럼 옵션값을 넣어주면된다.
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


# driver =webdriver.Chrome()
driver.get('https://naver.com')
time.sleep(2)




# 드라이버창옆에 스크립트로 작성한 새로운 창(네이버)를 새로 뛰움
driver.execute_script('window.open("https://daum.net");')  
time.sleep(2)

# driver.execute_script('window.open("https://daum.net");')  
# time.sleep(2)


# 쓰바라쉬.... switch_to_window가 예전함수라.... 사용법이 달라졌는데...쓰발...
# 죄다 예전 정보라 3시간동안 뻘짓거리 했네...

#

#swithch_to.window로 함수 바뀜... 

# 

# 창2개뛰운것중에 배열순으로0번이 메인   1로 포커스바꾼후
# 드라이버 클로즈하니 당연히 네이버가 메인
driver.switch_to.window(driver.window_handles[1])
driver.close()



time.sleep(2)

driver.close()

