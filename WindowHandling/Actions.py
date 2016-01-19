'''
Created on Jan 14, 2016

@author: Dipesh
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.spicejet.com/")

ab=driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/a")
ActionChains(driver).move_to_element(ab).perform()
driver.implicitly_wait(6)

bc=driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/a")
ActionChains(driver).move_to_element(bc).perform()
driver.implicitly_wait(4)

ca=driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/a")
ActionChains(driver).move_to_element(ca).perform()
driver.implicitly_wait(4)

abc=driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[1]/a")
ActionChains(driver).move_to_element(abc).click(abc).perform() 