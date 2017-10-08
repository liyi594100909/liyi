# coding=utf-8

from selenium import webdriver
import time
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')



driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://www.baidu.com")

for i in range (1,4):
	driver.find_element_by_link_text(u"地图").click()

	print(driver.title)
	driver.back()

driver.quit()