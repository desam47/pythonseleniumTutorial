'''
Created on Jan 12, 2016

@author: Dipesh
'''

from selenium import webdriver
iepath="C:\webbrowser selenium\IEDriverServer.exe"
driver=webdriver.Ie(iepath)
driver.get("http://facebook.com")
print(driver.title)