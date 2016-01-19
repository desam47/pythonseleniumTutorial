'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
driver=webdriver.Firefox()

driver.get("http://jqueryui.com/tooltip/")

fra=driver.find_element_by_class_name("demo-frame")

driver.switch_to_frame(fra)

driver.find_element_by_xpath(".//*[@id='age']").send_keys("43253")

driver.switch_to_default_content()

driver.find_element_by_xpath("//*[@id='sidebar']/aside[1]/ul/li[1]/a").click() 