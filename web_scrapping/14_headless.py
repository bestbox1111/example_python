
### headless는 웹 브라우져의 실질적인 동작없이 메모리의 부담을 줄이는 백그라운드에서 실행되는 동작.


import webbrowser
from attr import attrs
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()         #시스템 오류를 위해 삽입한구문
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #시스템 오류를 위해 삽입한구문

browser = webdriver.Chrome(options=options)

url="https://play.google.com/store/movies"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36","Accept-Language":"ko-KR,ko"}
res= requests.get(url, headers=headers)
res.raise_for_status()




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
browser.get_screenshot_as_file("google_movie_jjang.jpg")            ###웹브라우져에서는 뜨지 않지만 백라운드에서 도는 스크린 샷을 저장하는데...난 안뜸니다....


soup= BeautifulSoup(res.text, "lxml")

movies= soup.find_all("div", attrs={"class":["VfPpkd-EScbFb-JIbuQc", "MxsXJd"]})


# with open("movies.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"hP61id"}).get_text()
     
    # title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)