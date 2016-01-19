'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://google.com")

search=driver.find_element_by_class_name("gsfi")

#Rightclicking

ActionChains(driver).move_to_element(search).context_click(search).perform() 