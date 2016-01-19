'''
Created on Jan 12, 2016

@author: Dipesh
'''

from selenium import webdriver
chromedriverpath="C:\webbrowser selenium\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("http://facebook.com")
print(driver.title)

#Closing Chrome Browser
driver.close()
print("Closed Chrome")

#Closing all WINDOWS
driver.quit()
print("All window closed")