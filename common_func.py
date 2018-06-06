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

    def wait_presence(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.presence_of_element_located((locator , locator_value)))

    def wait_visibility(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.visibility_of_element_located((locator , locator_value)))

    def wait_presence_all(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.presence_of_all_elements_located((locator , locator_value)))

    def wait_visibility_all(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.visibility_of_all_elements_located((locator , locator_value)))


    def resources_testing(self) :        

        lesson_intro_pop_up = self.wait_presence(2,By.XPATH , Locator.lesson_intro_pop_up)
        take_ride_button = self.wait_presence(2,By.CSS_SELECTOR, Locator.take_ride_button)
        

        if (lesson_intro_pop_up.is_displayed()) :

            take_ride_button.click()
            skip = self.wait_presence(2, By.XPATH, Locator.skip)
            skip.click()

        else :

            print('lesson intro not present')

        resources_list = self.wait_visibility_all(5 , By.XPATH, Locator.resources_list)


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

                resources_list = self.wait_visibility_all(200, By.XPATH, Locator.resources_list)
                

            elif resource == driver.find_element_by_xpath(Locator.practice):
                
                try :
                    resource == driver.find_element_by_xpath(Locator.practice_deactive)
                    resource.click()
                    print('Practice node is active now')

                except:

                    print('Practice node is active')

                score = resource.text
                print('Score before attempting practice node is : {}'.format(score)) 

                sleep(2) 

                act = ActionChains(driver)
                act.move_to_element(resource).double_click().perform()                    

                
                print('check resource.click has clicked on resource')

                self.practice_level_score()             

                

    def practice_level_score(self) :

        practice_level_list = self.wait_visibility_all(10, By.XPATH, Locator.practice_level_list)                


        for level in practice_level_list:

            highest_score_before_practice = driver.find_element_by_css_selector(
                Locator.highest_score).text
            latest_score_before_practice = driver.find_element_by_css_selector(
                Locator.highest_score).text

            print("highest_score_before_practice : {}".format(
                highest_score_before_practice))
            print("latest_score_before_practice : {}".format(
                latest_score_before_practice))

            start_button = self.wait_visibility(5, By.CSS_SELECTOR, Locator.start_button)
            start_button.click()
            self.questions_testing()


    def select_lesson(self) :
  

        lesson_list = self.wait_presence_all(5, By.CSS_SELECTOR , Locator.lesson_list)
        start_list = self.wait_presence_all(5, By.CSS_SELECTOR , Locator.start_lesson)


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
        

        submit = self.wait_presence(10,By.CSS_SELECTOR, Locator.submit)
        go_prev_question = driver.find_element_by_css_selector(Locator.go_prev_question)
        go_next_question = driver.find_element_by_css_selector(Locator.go_next_question) 
        intro = driver.find_element_by_css_selector(Locator.intro)    


        # practice_level_page = driver.find_element_by_css_selector(Locator.practice_level_page)
        # practice_level_page = False
     
        while(go_next_question.is_displayed()) :            

            if  driver.find_elements_by_css_selector(Locator.SCQ) :
                
                SCQ_options_list = self.wait_presence_all(5, By.CSS_SELECTOR, Locator.SCQ_options_list)
                print("number of scq options are : {}".format(len(SCQ_options_list)))
                SCQ_option = self.wait_presence(5 , By.CSS_SELECTOR, Locator.SCQ_option.format(random.randint(1 , len(SCQ_options_list))))

                SCQ_option.click()
                submit = self.wait_presence(10,By.CSS_SELECTOR, Locator.submit)
                act = ActionChains(driver)
                act.move_to_element(submit).perform()
                submit.click()
                sleep(2)
                go_next_question.click()

            elif driver.find_elements_by_css_selector(Locator.DR): 

                input_field = driver.find_element_by_name(Locator.input_field)
                input_field.send_keys("text")
                submit = self.wait_presence(5 , By.CSS_SELECTOR, Locator.submit)
                submit.click()
                go_next_question.click()

            elif driver.find_elements_by_css_selector(Locator.PUZ):

                intro = self.wait_presence(5 , By.CSS_SELECTOR ,Locator.intro)
                intro.click()

                stick_list = driver.find_elements_by_css_selector(Locator.stick)

                stick = driver.find_element_by_css_selector(Locator.stick)

                for stick in range(0 ,len(stick_list)) :

                    
                    stick = driver.find_element_by_css_selector(Locator.stick)                    
                    container = driver.find_element_by_css_selector(Locator.container)
                    
                    action_chains = ActionChains(driver)
                    action_chains.drag_and_drop(stick , container).perform()

                    stick = driver.find_element_by_css_selector(Locator.stick)
                    

                submit = driver.find_element_by_css_selector(Locator.submit)
                submit.click()
                go_next_question.click()

            elif driver.find_elements_by_css_selector(Locator.SST) :

                intro = self.wait_presence(5 , By.CSS_SELECTOR ,Locator.intro)
                intro.click()

                submit = driver.find_element_by_css_selector(Locator.submit)
                submit.click()
                go_next_question.click()

        pdb.set_trace()
        self.practice_level_score()













  
  
  
