import unittest
from setting import driver
from setting import CloudSetUp
from data import TestData
from locators import Locator
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains




class CommonFunc(CloudSetUp) :

    def resources_testing(self) :

        resources_list = driver.find_elements_by_xpath(Locator.resources_list)

        print('number of resources present are : {}' .format(len(resources_list)))

        # node_active = driver.find_element_by_css_selector(Locator.node_active)
        # node_deactive = driver.find_element_by_css_selector(Locator.node_deactive)

        for resource in resources_list:

            print(resource)

            if resource == driver.find_element_by_xpath(Locator.video):

                if resource == driver.find_element_by_xpath(Locator.video_deactive):
                    resource.click()
                    print('video node is active')

                else:
                    print('video node is active')

                score = resource.text
                print('Score before attempting node is : {}'.format(score))

                resource.click()

                resource_list = WebDriverWait(driver, 200).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.transition-medium.resource-container.resource-container-slide-out')))

            elif resource == driver.find_element_by_xpath(Locator.practice):

                if resource == driver.find_element_by_xpath(Locator.practice_deactive):
                    resource.click()
                    print('Practice node is active')

                else:
                    print('Practice node is active')

                practice_level_list = driver.find_elements_by_xpath(
                    Locator.practice_level_list)

                for level in practice_level_list:

                    highest_score_before_practice = driver.find_element_by_css_selector(
                        Locator.highest_score).text
                    latest_score_before_practice = driver.find_element_by_css_selector(
                        Locator.highest_score).text

                    print("highest_score_before_practice : {}".format(
                        highest_score_before_practice))
                    print("latest_score_before_practice : {}".format(
                        latest_score_before_practice))

                    start_button = driver.find_element_by_css_selector(
                        Locator.start_button)
                    start_button.click()



    def questions_testing(self) :
        pass

  
  
  
