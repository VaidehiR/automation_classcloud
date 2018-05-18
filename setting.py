import unittest
from selenium import webdriver


driver = webdriver.Chrome(executable_path = '/home/alqama/workspace/driver_automation/chromedriver')

class CloudSetUp (unittest.TestCase) :

    def setUp(self) :
        driver.maximize_window()
        driver.get('http://home.zaya.in/#/')

    def tearDown(self) :
        driver.quit()