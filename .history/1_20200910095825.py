from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("http://192.168.0.249:18080/common")
driver.find_element_by_id("username").send_keys('15839900966')
driver.find_element_by_id("password").send_keys('qq.123')
driver.find_element_by_id("login").click()
driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="search"]').send_keys('410104199409091621')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/img').click()