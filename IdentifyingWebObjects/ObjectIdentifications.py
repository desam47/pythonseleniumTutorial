'''
Created on Jan 13, 2016

@author: Dipesh
'''

from selenium import webdriver
driver= webdriver.Firefox()
driver.get("http://facebook.com")

#Identify element by name and enter data
driver.find_element_by_name("firstname").send_keys("Dipesh")

#Identify element by id and enter data
driver.find_element_by_id("u_0_3").send_keys("Chand")

#Identify element by id and click button
driver.find_element_by_name("websubmit").click()

#Identify link text and click link text
driver.find_element_by_link_text("Forgot your password?").click()

#Closing Firefox Browser
driver.close()
print("Closed Firefox")

#Closing all WINDOWS
driver.quit()
print("All window closed")