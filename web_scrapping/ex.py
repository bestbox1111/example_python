from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()         #시스템 오류를 위해 삽입한구문
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #시스템 오류를 위해 삽입한구문
browser = webdriver.Chrome(options=options) 

browser.maximize_window()


url ="https://flight.naver.com/"
browser.get(url)


# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()

browser.find_element(By.XPATH, value="//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()


