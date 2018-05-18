from setting import driver
from setting import CloudSetUp
import unittest
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locator

class Student(CloudSetUp):
    def testlogin(self):

        next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class= 'next land-page-btn']")))

        # school_list = WebDriverWait(driver, 10.).until(EC.presence_of_all_elements_located((By.XPATH ,Locator.school_list)))
        school_list = WebDriverWait(driver, 10.).until(EC.presence_of_element_located((By.XPATH ,Locator.school_list)))
        pdb.set_trace()
        # driver.find_element_by_xpath("//button[@class= 'next land-page-btn']")
        while(school_list.is_displayed()):
            list = driver.find_elements_by_xpath(
                '/html/body/div[3]/div/div/div[1]/div[2]/ul/li')

            for school in list:
                pdb.set_trace()

                print(school.text)

                if (school.text == 'Demo School, Zaya'):

                    school.click()
                    pdb.set_trace()
                
                    break

                
            next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//button[@class= 'next land-page-btn']")))
            next_button.click()

        student = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[3]/div/div/div[2]/div[1]/div")))
        student.click()

        # driver.find_elements_by_css_selector('/html/body/div[3]/div/div/div[1]/div[2]/ul/li[1]/a').click()

if __name__ == "__main__" :
    unittest.main()