
import webbrowser
from attr import attrs
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

options = webdriver.ChromeOptions()         #시스템 오류를 위해 삽입한구문
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #시스템 오류를 위해 삽입한구문
browser = webdriver.Chrome(options=options)  #시스템 오류를 위해 삽입한구문
#위의 3줄은 로그 숨기기 

browser.maximize_window()


url="https://play.google.com/store/movies"
browser.get(url)

    
    
#### 현 사이트에서는 필요 없지만, 로딩되는 시간관련되서 스크롤내리기
# browser.execute_script("window.scrollTo(0,1080)")   #모니터 해상도가 1920 * 1080이므로 y축최대가 1080이므로 1080만큼 아래로 스크롤

## 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(2)



## 화면 가장 아래로 스크롤 내리는 반복문 작성.
first_height= browser.execute_script('return document.body.scrollHeight') # 현재 문서 높이를 가져와서 저장.
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 처음 스크롤을 가장 아래로 내리는 작업.
    time.sleep(2)
    current_height=browser.execute_script('return document.body.scrollHeight')  # 현재 문서 높이를 가져와서 저장.
    if current_height == first_height:      #내린 높이와 현제 높이가 같으면 더이상 내릴 필요가 없으니까  높이가 같다는 소리니 브레이크걸고.
        break
    first_height= current_height        #현제 위치 = 처음위치로 값을 넣어줌.
print("스크롤이 모두 완려됐습니다.")

