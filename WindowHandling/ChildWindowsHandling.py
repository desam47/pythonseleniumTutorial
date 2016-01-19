'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://accounts.google.com/signup")
driver.find_element_by_xpath(".//*[@id='wrapper']/div[2]/div/div[1]/p/a").click()
print("Before Switching")
parent=driver.current_window_handle
print(driver.title)
driver.switch_to_window(driver.window_handles[-1])
child=driver.current_window_handle
print("After Switching")
print(driver.title)
#workon child browser
driver.switch_to_window(parent)
print("Switching Back")
print(driver.title)