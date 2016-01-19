'''
Created on Jan 14, 2016

@author: Dipesh
'''
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.tizag.com/javascriptT/javascriptalert.php")

driver.find_element_by_xpath("//div[@class='display']/form/input").click()

print(driver.switch_to_alert().text)

driver.switch_to_alert().accept()

#driver.switch_to_alert().dismiss()

#driver.switch_to_alert().send_keys("adafds") 