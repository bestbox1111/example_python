from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

options = webdriver.ChromeOptions()         #시스템 오류를 위해 삽입한구문
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #시스템 오류를 위해 삽입한구문
browser = webdriver.Chrome(options=options) 

browser.maximize_window()


url ="https://flight.naver.com/"
browser.get(url)

#출발지 선택을 위해.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()          #예전 버전으로 쓰이지 않는다네...
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()         #신버전 이렇게 쓰라네..



#출발지 선택을 위핸 국내 해외 구분을 위한 선택.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()#
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()         #신버전 이렇게 쓰라네..


#국내구분을 했으면 항공장을 선택을 위해.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[14]/span/i[1]").click()
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[14]/span/i[1]").click()         #신버전 이렇게 쓰라네..

#### 출발 세팅은 끝...


# 이제 도착 선택.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()         #신버전 이렇게 쓰라네..

#출발지 선택을 위핸 국내 해외 구분을 위한 선택.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()#
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()         #신버전 이렇게 쓰라네..


#항공장 선택 국내 제주로 가정.
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()         #신버전 이렇게 쓰라네..


time.sleep(1)
#가는 날 선택 링크의 텍스트로.
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()# go_day=browser.find_element_by_link_text('가는 날')
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()         #신버전 이렇게 쓰라네..


# 가는 날 선택 후 뜨는 날짜 캘린더를  xpath로 클릭
# 가는 날짜 선택
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click()#
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click()         #신버전 이렇게 쓰라네..

#오는 날짜 선택
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button/b").click()# 
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button/b").click()         #신버전 이렇게 쓰라네..



#성인 및 인원 클릭 부분
time.sleep(1)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[3]/button[1]").click()# 
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[3]/button[1]").click()         #신버전 이렇게 쓰라네..

time.sleep(1)

#인원 추가 및 감소 부분
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[3]/div/div/div[1]/div[1]/button[2]").click()# 
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[3]/div/div/div[1]/div[1]/button[2]").click()         #신버전 이렇게 쓰라네..
time.sleep(1)

# 등급 클릭 
# browser.find_element_by_link_text("프리미엄 일반석").click()  #d안되는 이유 모름..
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[3]/div/div/div[2]/button[2]").click()# 
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[3]/div/div/div[2]/button[2]").click()         #신버전 이렇게 쓰라네..

time.sleep(1)



###항공권 검색 누리기
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/button").send_keys(Keys.ENTER)        #신버전 이렇게 쓰라네..
browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").send_keys(Keys.ENTER)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()





# 예약세팅은 끝나고, 실제 항공편 리스트가 나옴.(1번째것 일단 출력해봄.)


