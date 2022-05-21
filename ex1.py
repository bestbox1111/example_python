from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 웹드라이버로 열고 요소찾아서 자동 검색하는 예제..
# 구글은 검색요소관련 장애가 많아서 네이버로 국내포탈로 에제진행햐야할듯.


driver =webdriver.Chrome()
url='https://www.naver.com'
driver.get(url)

time.sleep(1)


driver.find_element_by_css_selector('#query').send_keys("파이썬")
time.sleep(1)
driver.find_element_by_css_selector('#query').send_keys(Keys.ENTER)

