'''
Created on Jan 14, 2016

@author: Dipesh
'''

from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.ebay.com/")

# no of links present in Website ebay home page

totallinks=driver.find_elements_by_tag_name("a")
print(len(totallinks))
footer=driver.find_element_by_xpath(".//*[@id='glbfooter']")
linksfooter=footer.find_elements_by_tag_name("a")
print(len(linksfooter))
for ob in linksfooter :
    print(ob.text)