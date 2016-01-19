'''
Created on Jan 12, 2016

@author: Dipesh
'''

print ("Hi Selenium")

#open Firefox Browser and navigate to google homepage
from selenium import webdriver

# invoking firefox Browser
driver= webdriver.Firefox()

#Hit the url
driver.get("http://google.com")

#print current url in console
print(driver.current_url)

#print title of current url
print(driver.title)

#navigate to gmail
driver.get("http://gmail.com")
print(driver.title)
print("Navigating to Gmail Homepage")

#navigate back to google
driver.back()
print(driver.title)
print("Came back to google Homepage")

#navigate forward to gmail
driver.forward()
print(driver.title)
print("Go forward to gmail Homepage")

#refresh the browser
driver.refresh()
print("Refresh")

#maximixe the browser
driver.maximize_window()
print("Window maximize")

#Closing Firefox Browser
driver.close()
print("Closed Firefox")

#Closing all WINDOWS
driver.quit()
print("All window closed")