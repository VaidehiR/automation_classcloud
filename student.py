from setting import driver
from setting import CloudSetUp
from data import TestData
from locators import Locator
from common_func import CommonFunc
import unittest
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


class Student(CommonFunc):

    @unittest.skip('select_school')
    def test_01_select_school(self):
        # Find and Select demoschool from school list

        school_list = driver.find_elements_by_xpath(Locator.school_list)
        while(school_list):

            school_list = driver.find_elements_by_xpath(Locator.school_list)
            for school in school_list:

                if (school.text == 'Demo School, Zaya'):

                    school.click()
                    sleep(5)
                    break

            try:

                next_button = driver.find_element_by_xpath(Locator.next_button)
                next_button.click()

            except:
                print('Next button not present')
                break

    def test_02_login(self):
        # select student  and login
        sleep(3)

        student = driver.find_element_by_xpath(Locator.student)
        student.click()

        username = CommonFunc().wait_presence(5 , By.XPATH, Locator.username)
        username.send_keys(TestData.student_username)

        password = driver.find_element_by_xpath(Locator.password)
        password.send_keys(TestData.student_password)

        login = driver.find_element_by_id(Locator.login)
        login.click()

    def test_03_landing_page(self):

        try:

            # learn = WebDriverWait(driver , 10).until(EC.visibility_of_element_located((By.XPATH , Locator.learn)))
            learn = CommonFunc().wait_visibility(10, By.XPATH , Locator.learn)

        except NoSuchElementException:

            print('Learn not present')

        try:

            quiz = driver.find_element_by_xpath(Locator.quiz)

        except NoSuchElementException:

            print('quiz not present')

        try:

            logout = driver.find_element_by_xpath(Locator.logout)

        except NoSuchElementException:

            print('logout not present')

        learn.click()

        confirmation_modal = CommonFunc().wait_visibility(5,By.CSS_SELECTOR, Locator.confirmation_modal)
        
        yes = driver.find_element_by_css_selector(Locator.yes_button)

        if (confirmation_modal.is_displayed()):
            sleep(3)
            yes.click()

        else:
            print('No confirmation modal')           

        try:

            welcome_pop_up = driver.find_elements_by_xpath(Locator.welcome_pop_up)
            welcome_next_button = driver.find_elements_by_css_selector(Locator.welcome_next_button)

            for pop_up, next_button  in zip(welcome_pop_up, welcome_next_button) :                

                    next_button.click()
                    
             
        except ElementNotVisibleException as e :

            print('No Welcome pop up')

    def test_04_learn_home_page(self):

        sleep(5)
        right_header_score = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locator.right_header_score)))

        print('Initial score of user is : {}'.format(right_header_score.text))

        course_list = driver.find_elements_by_xpath(Locator.course_list)

        while(course_list):

            course_list = driver.find_elements_by_xpath(Locator.course_list)

            for course in course_list:
                print(course.text)

                if (TestData.course_name_contain in course.text):

                    course.click()
                    break

            try:

                next_button = driver.find_element_by_xpath(Locator.next_button)
                next_button.click()

            except NoSuchElementException as e:
                print(e)

                break

    def test_05_lesson_selection(self):
        # select lesson
        
        CommonFunc().select_lesson()     

        CommonFunc().resources_testing()


if __name__ == "__main__":
    unittest.main()
