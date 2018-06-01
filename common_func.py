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
from selenium.webdriver.common.keys import Keys
import random





class CommonFunc(CloudSetUp) :

    def resources_testing(self) :

        lesson_intro_pop_up = WebDriverWait(driver , 2).until(EC.presence_of_element_located((By.XPATH , Locator.lesson_intro_pop_up)))
        take_ride_button = driver.find_element_by_css_selector(Locator.take_ride_button)
        skip = driver.find_elements_by_xpath(Locator.skip)

        lesson_intro_pop_up = driver.find_element_by_xpath(Locator.lesson_intro_pop_up)

        if (lesson_intro_pop_up.is_displayed()) :

            take_ride_button.click()
            skip.click()

        else :

            print('lesson intro not present')

        resources_list = driver.find_elements_by_xpath(Locator.resources_list)


        print('number of resources present are : {}' .format(len(resources_list)))

        # node_active = driver.find_element_by_css_selector(Locator.node_active)
        # node_deactive = driver.find_element_by_css_selector(Locator.node_deactive)

        for resource in resources_list:
            

            print(resource)
            

            if resource == driver.find_element_by_xpath(Locator.video):
                
                try :

                    resource == driver.find_element_by_xpath(Locator.video_deactive)
                    resource.click()
                    print('video node is active')

                except:
                    print('video node is active')
                    
                score = resource.text
                print('Score before attempting video node is : {}'.format(score))

                resource.click()

                resources_list = WebDriverWait(driver, 200).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.transition-medium.resource-container.resource-container-slide-out')))
                

            elif resource == driver.find_element_by_xpath(Locator.practice):

                try :
                    resource == driver.find_element_by_xpath(Locator.practice_deactive)
                    resource.click()
                    print('Practice node is active')

                except:

                    print('Practice node is active')

                score = resource.text
                print('Score before attempting practice node is : {}'.format(score))

                resource.click()
                
                practice_level_list = driver.find_elements_by_xpath(Locator.practice_level_list)


                for level in practice_level_list:

                    highest_score_before_practice = driver.find_element_by_css_selector(
                        Locator.highest_score).text
                    latest_score_before_practice = driver.find_element_by_css_selector(
                        Locator.highest_score).text

                    print("highest_score_before_practice : {}".format(
                        highest_score_before_practice))
                    print("latest_score_before_practice : {}".format(
                        latest_score_before_practice))

                    start_button = driver.find_element_by_css_selector(Locator.start_button)
                    start_button.click()
                    self.questions_testing()



    def select_lesson(self) :

        lesson_list = driver.find_elements_by_css_selector(Locator.lesson_list)
        start_list = driver.find_elements_by_css_selector(Locator.start_lesson)          

        for lesson in lesson_list :
               
            if(TestData.lesson_name_contain in lesson.text) :

                lesson.click()

                for start in start_list :
                    if start.is_displayed() :
                        start.click()
                        break
                break
            
            else :
                print('lesson not found')

    def questions_testing(self) :

        submit = driver.find_element_by_css_selector(Locator.submit)
        go_prev_question = driver.find_element_by_css_selector(Locator.go_prev_question)
        go_next_question = driver.find_element_by_css_selector(Locator.go_next_question) 
        intro = driver.find_element_by_css_selector(Locator.intro)      

        pdb.set_trace()

        while (go_next_question) :

            # SCQ = driver.find_elements_by_css_selector(Locator.SCQ)
            SCQ = WebDriverWait(driver , 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR , Locator.SCQ)))
            DR = driver.find_elements_by_css_selector(Locator.DR)
            # DR = WebDriverWait(driver , 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR , Locator.DR)))
            PUZ = driver.find_elements_by_css_selector(Locator.PUZ)
            # PUZ = WebDriverWait(driver , 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR , Locator.PUZ)))
            pdb.set_trace()

            if SCQ :
                
                SCQ_options_list = driver.find_elements_by_css_selector(Locator.SCQ_options_list)
                SCQ_option = driver.find_element_by_css_selector(Locator.SCQ_option.format(random.randint(1 , len(SCQ_options_list))))

                SCQ_option.click()
                submit.click()
                go_next_question.click()

            elif DR : 

                input_field = driver.find_element_by_name(Locator.input_field)
                input_field.send_keys("text")

                submit.click()
                go_next_question.click()

            elif PUZ :

                stick_list = driver.find_element_by_css_selector(Locator.stick_list)
                container = driver.find_element_by_css_selector(Locator.container)
                

                intro.click()

                action_chains = ActionChains(driver)

                for stick in stick_list :
                    action_chains.drag_and_drop(stick , container).perform()

                submit.click()













  
  
  
