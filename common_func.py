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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
from fractions import Fraction


class CommonFunc(CloudSetUp) :
    def element_xpath(self,locator):
        return driver.find_element_by_xpath(locator)

    def element_css(self, locator) :
        return driver.find_element_by_css_selector(locator)

    def wait_presence(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.presence_of_element_located((locator , locator_value)))

    def wait_visibility(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.visibility_of_element_located((locator , locator_value)))

    def wait_presence_all(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.presence_of_all_elements_located((locator , locator_value)))

    def wait_visibility_all(self, sec , locator, locator_value) :

        return WebDriverWait(driver , sec).until(EC.visibility_of_all_elements_located((locator , locator_value)))


    def select_course(self) :

        course_list = self.wait_presence_all(5, By.XPATH, Locator.course_list)

        while(course_list):

            course_list = driver.find_elements_by_xpath(Locator.course_list)                       

            for course in course_list:
            
                if (TestData.course_name_contain in course.text):
                    course.click()
                    break
            try:

                next_button = driver.find_element_by_xpath(Locator.next_button)
                next_button.click()

            except NoSuchElementException as e:
                print(e)


    def select_lesson(self) :

        lesson_list = self.wait_presence_all(10, By.CSS_SELECTOR , Locator.lesson_list)
        start_list = self.wait_presence_all(5, By.CSS_SELECTOR , Locator.start_lesson)


        for lesson in lesson_list :
            print(lesson)
               
            if(TestData.lesson_name_contain in lesson.text) :

                lesson.click()

                for start in start_list :
                    if start.is_displayed() :
                        start.click()
                        break
                break
            
            else :
                print('lesson not found')


    def resource_exist(self, locator) :
        
        try :
            return driver.find_element_by_xpath(locator)
            
        except :
            return False

    def element_exist(self, sec , locator, locator_value) :
        
        try :
            self.wait_presence(sec , locator, locator_value)
            return True

        except :
            return False

    def lesson_intro_popUp(self) :        

        lesson_intro_pop_up = self.wait_presence(5,By.XPATH , Locator.lesson_intro_pop_up)
        take_ride_button = self.wait_presence(5,By.CSS_SELECTOR, Locator.take_ride_button)
        

        if (lesson_intro_pop_up.is_displayed()) :

            take_ride_button.click()
            skip = self.wait_presence(2, By.XPATH, Locator.skip)
            skip.click()

        else :

            print('lesson intro not present')

    def resource_presence(self) :

        self.lesson_intro_popUp()

        try :

            resources_list = self.wait_visibility_all(10 , By.XPATH, Locator.resources_list)
            print('number of resources present are : {}' .format(len(resources_list)))
            return resources_list

        except :
            print('no resource present')


    def resources_testing(self) :  

        self.resource_presence()
        
        right_header_score = self.wait_visibility(5, By.XPATH, Locator.right_header_score)   
        resources_list = self.wait_visibility_all(10 , By.XPATH, Locator.resources_list)        

        for resource in resources_list:            

            if resource == self.resource_exist(Locator.video) :                                
                
                try :

                    resource == driver.find_element_by_xpath(Locator.video_deactive)
                    resource.click()
                    print('video node is active')

                except:
                    print('video node is active')
                    
                score = resource.text
                print('Score before attempting video node is : {}'.format(score))
                resource == driver.find_element_by_xpath(Locator.video)
                resource.click()

                resources_list = self.wait_visibility_all(200, By.XPATH, Locator.resources_list)
                if score == '50' :
                    new_score = int(right_header_score.text) + 0
                    self.assertEqual(int(right_header_score.text) , new_score)
                
                else :
                    new_score = int(right_header_score.text) + 50
                    self.assertEqual(int(right_header_score.text) , new_score)

            elif resource == self.resource_exist(Locator.practice):
                
                try :
                    resource == driver.find_element_by_xpath(Locator.practice_deactive)
                    resource.click()
                    print('Practice node is active now')
                    print('check resource.click has clicked on resource')

                except:

                    print('Practice node is active')

                score = resource.text
                right_header_score = right_header_score.text
                print('Score before attempting practice node is : {}'.format(score)) 

                resource = WebDriverWait(driver , 5).until(EC.element_to_be_clickable((By.XPATH, Locator.practice)))
                sleep(2)
                resource.click()          
                print('check resource.click has clicked on resource')

                practice_level_list = self.wait_visibility_all(10, By.XPATH, Locator.practice_level_list)     

                for level in practice_level_list:

                    highest_score_before_practice = driver.find_element_by_css_selector(Locator.highest_score).text
                    recent_score_before_practice = driver.find_element_by_css_selector(Locator.recent_score).text
                    right_header_score = self.wait_visibility(5, By.XPATH, Locator.right_header_score)
                    total_score = right_header_score.text

                    start_button = self.wait_visibility(5, By.CSS_SELECTOR, Locator.start_button)
                    start_button.click()

                    self.questions_testing()

                    highest_score_after_practice = driver.find_element_by_css_selector(Locator.highest_score).text
                    recent_score_after_practice = driver.find_element_by_css_selector(Locator.recent_score).text 
                    recent_score = Fraction(recent_score_after_practice).numerator

                    new_score = int(total_score) + recent_score
                    right_header_score = self.wait_visibility(5, By.XPATH, Locator.right_header_score) 
                    self.assertEqual(int(right_header_score.text) , new_score)


            elif resource == self.resource_exist(Locator.node) :
                
                print('pdf present')

                # import PyPDF2 
                # pdf_file = open('8_7W91OQ.pdf', 'rb') 
                # read_pdf = PyPDF2.PdfFileReader(pdf_file) 
                # number_of_pages = read_pdf.getNumPages() 
                # page = read_pdf.getPage(0) 
                # page_content = page.extractText() 
                # print (page_content.encode('utf-8'))  

            elif resource == self.resource_exist(Locator.game) : 

                try :

                    resource == driver.find_element_by_xpath(Locator.game_deactive)
                    resource.click()
                    print('game node is active')

                except:
                    print('game node is active')
                    
                score = resource.text
                print('Score before attempting game node is : {}'.format(score))
                resource == driver.find_element_by_xpath(Locator.game)
                resource.click()

                score = resource.text
                print('Score before attempting game node is : {}'.format(score))
                resource == driver.find_element_by_xpath(Locator.game)
                resource.click()

                game_close = driver.find_element_by_css_selector(Locator.game_close)
                game_close.click()

                if score == '50' :
                    new_score = int(right_header_score.text) + 0
                    self.assertEqual(int(right_header_score.text) , new_score)
                
                else :
                    new_score = int(right_header_score.text) + 50
                    self.assertEqual(int(right_header_score.text) , new_score)



              
    def check_submit_enability_and_click(self) :
        try :
            
            submit = WebDriverWait(driver , 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locator.submit)))
            submit.click()
            go_next_question = driver.find_element_by_css_selector(Locator.go_next_question) 
            go_next_question.click()

        except :
            print('submit button is not enabled')

    def questions_testing(self) :      

        submit = self.wait_presence(10,By.CSS_SELECTOR, Locator.submit)
        go_prev_question = driver.find_element_by_css_selector(Locator.go_prev_question)
        go_next_question = driver.find_element_by_css_selector(Locator.go_next_question) 
        intro = self.wait_presence(5 , By.CSS_SELECTOR ,Locator.intro)

        # practice_level_page = driver.find_element_by_css_selector(Locator.practice_level_page)
        # practice_level_page = False
     
        while(self.element_exist(5, By.CSS_SELECTOR, Locator.go_next_question)) :


            if  driver.find_elements_by_css_selector(Locator.SCQ) :
                
                SCQ_options_list = self.wait_presence_all(5, By.CSS_SELECTOR, Locator.SCQ_options_list)
                print("number of scq options are : {}".format(len(SCQ_options_list)))
                SCQ_option = self.wait_presence(5 , By.CSS_SELECTOR, Locator.SCQ_option.format(random.randint(1 , len(SCQ_options_list))))

                SCQ_option.click()
                submit = self.wait_presence(10,By.CSS_SELECTOR, Locator.submit)
                act = ActionChains(driver)
                act.move_to_element(submit).perform()
                self.check_submit_enability_and_click()
            

            elif driver.find_elements_by_css_selector(Locator.DR): 

                input_field = driver.find_element_by_name(Locator.input_field)
                input_field.send_keys("text")
                self.check_submit_enability_and_click()
                
            elif driver.find_elements_by_css_selector(Locator.PUZ):

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

                intro.click()

                submit = driver.find_element_by_css_selector(Locator.submit)
                submit.click()
                go_next_question.click()

            elif driver.find_elements_by_css_selector(Locator.MTF) :

                intro.click()
                go_next_question.click()















  
  
  
