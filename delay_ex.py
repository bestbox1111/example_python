from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 10~13줄은 시스템 어쩌구 오류메시지 지우기위해.

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()
url='https://www.naver.com/'
driver.get(url)

# 대기 방법 time.sleep, implicitly, webDriverWait(이건 임포트 해야함) 위에서 234줄
# 각 방법의 차이

# time.sleep(10)===> 무조건 10초를 기다림.

time.sleep(10)

# driver.implicitly_wait(10) ====> 10초안에 로드되면 넘어가고나 로드안되도 10초는 무조건 기다림.
driver.implicitly_wait(10)

driver.find_element_by_css_selector('._NM_THEME_CATE.tab.id_finance').click()

# 3번째 방법은 해당요소가 뜰때까지만 10초를 기다림===> 어떤 요소를 기준점으로 잡아서 시간대기할떄 사용

button = webDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".thumb_bd")))
button.click()