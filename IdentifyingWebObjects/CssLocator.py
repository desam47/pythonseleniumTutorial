'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://facebook.com")
driver.maximize_window()



#using css Locator

driver.find_element_by_css_selector("input[value='Log In']").click()