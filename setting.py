import unittest
from selenium import webdriver
from data import TestData
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    executable_path='/home/alqama/workspace/driver_automation/chromedriver')


class CloudSetUp (unittest.TestCase):
    @classmethod
    def setUpClass(self):

        driver.maximize_window()
        # driver.implicitly_wait(2)
        driver.get(TestData.url)


    @classmethod
    def tearDownClass(self):

        driver.quit()
