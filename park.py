from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

# pip install selenium 해야 사용가능/

driver = webdriver.Chrome()
url='http://www.daum.net'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
time.sleep(1)

driver.find_element_by_css_selector('.link_daumid').click()

time.sleep(2)

action.send_keys('with-jun-000').perform()
driver.find_element_by_css_selector('#inputPwd').click()
time.sleep(1)

action.send_keys('k99100057k').perform()
driver.find_element_by_css_selector('.btn_comm').click()
time.sleep(2)

driver.find_element_by_css_selector('.link_basis').click()
time.sleep(2)
driver.find_element_by_css_selector('.btn_comm.btn_my').click()
time.sleep(2)

action.send_keys('안녕하세요').perform()
driver.find_element_by_css_selector('.yoga_wrapper').click()
action.send_keys('예비용테스트입니다.').perform()

driver.find_element_by_css_selector('.btn_toolbar.btn_write').click()

time.sleep(1)
driver.find_element_by_css_selector('.btn_g.btn_ok').click()
