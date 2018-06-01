import unittest
from selenium import webdriver
from data import TestData


driver = webdriver.Chrome(executable_path = '/home/alqama/workspace/driver_automation/chromedriver')


class CloudSetUp (unittest.TestCase) :
    @classmethod
    def setUpClass(self) :
        
        driver.maximize_window()
        # driver.implicitly_wait(5)
        driver.get(TestData.url)

    @classmethod
    def tearDownClass(self) :
        
        driver.quit()