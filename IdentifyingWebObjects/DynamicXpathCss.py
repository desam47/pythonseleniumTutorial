'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
driver= webdriver.Firefox()
driver.get("https://paytm.com/")

driver.find_element_by_xpath("//input[contains(@id,'mobile')]").send_keys("96766")

driver.find_element_by_css_selector("[id*='amou']").send_keys("400") 