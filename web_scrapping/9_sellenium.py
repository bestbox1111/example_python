
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

browser.get('https://naver.com')
browser.maximize_window()
action = ActionChains(browser)
# elem = browser.find_element_by_class_name("link_login")       #클래스 이름이 link_login이라는 클래스만 가져올때

# time.sleep(1)
# elem.click()
# time.sleep(1)
# browser.back()      # 뒤로 가기..
# browser.forward()   # 앞으로가기
# browser.refresh()   # 새로고침
# browser.close()   #현제 창만 닫는거
# broswer.quit()    #모든 탭을 닫는거

time.sleep(0.5)
elem2 = browser.find_element_by_id("query").click()
time.sleep(1)
action.send_keys('다음').perform()
action.send_keys(Keys.ENTER).perform()

# elem3 = browser.find_elements_by_tag_name("a")  #태크가 a인 모든 애덜을 끌고옴



# for i in elem3:
#     print(i.get_attribute("href"))      #위에서 a 태그인애를 저장한 elem3으로 저장한 애들중 href로 속성을 가져옴.
