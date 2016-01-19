'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver
chromedriverpath= "C:\webbrowser selenium\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("http://google.com")

driver.save_screenshot("D:\home.png")
co=driver.get_cookies()
print(len(co))

driver.delete_all_cookies()
co1=driver.get_cookies()
print(len(co1)) 