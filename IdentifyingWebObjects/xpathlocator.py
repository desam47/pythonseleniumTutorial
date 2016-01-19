'''
Created on Jan 13, 2016

@author: Dipesh
'''

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://facebook.com")
driver.maximize_window()

#using customized xpath
driver.find_element_by_xpath("//input[@id='email']").send_keys("Customized xpath")

#Identify element by xpath and clicking Button
driver.find_element_by_xpath(".//*[@id='loginbutton']").click()
