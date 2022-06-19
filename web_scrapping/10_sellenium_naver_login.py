
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

options = webdriver.ChromeOptions()         #시스템 오류를 위해 삽입한구문
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #시스템 오류를 위해 삽입한구문
browser = webdriver.Chrome(options=options)  #시스템 오류를 위해 삽입한구문




# 1 네이버 로그인
browser.get('https://naver.com')
browser.maximize_window()   #창의 크기 맥시멈
action = ActionChains(browser)  #키다운 할때 필요한 부분을 액션으로 저장함.


# 2 네이버 로그인 버튼 찾기 및 클릭.
browser.find_element_by_class_name("link_login").click()
time.sleep(random.uniform(1,3)) 
# 3네이버 아이디 및 패스워드 창
time.sleep(3)
browser.find_element_by_id("id").send_keys("bestbox1111")

# action.send_keys(Keys.TAB).perform()
time.sleep(3)
browser.find_element_by_id("pw").send_keys("k9910k057")
time.sleep(3)


# 4 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()


