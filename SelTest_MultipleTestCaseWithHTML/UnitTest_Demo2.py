'''
Created on Jan 15, 2016

@author: Dipesh
'''

import unittest
from selenium import webdriver
 
class SearchTest1(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("http://enterprise-demo.user.magentotrial.com")
 
    def test_1(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Phones")
        self.search_field.submit()
        self.button = self.driver.find_element_by_xpath(".//*[@id='search_mini_form']/div[1]/button")
        self.button.click()
        self.products = self.driver.find_elements_by_css_selector("h2.product-name")
        self.assertEqual(len(self.products), 3)
        print(len(self.products))
 
    def test_2(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Pant")
        self.search_field.submit()
        self.button = self.driver.find_element_by_xpath(".//*[@id='search_mini_form']/div[1]/button")
        self.button.click()
        self.products = self.driver.find_elements_by_css_selector("h2.product-name")
        self.assertEqual(len(self.products), 4)
        print(len(self.products))
 
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
 
if __name__ == "__main__":
    unittest.main(verbosity=2)