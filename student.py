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

        username = CommonFunc().wait_presence(5, By.XPATH, Locator.username)
        username.send_keys(TestData.student_username)

        password = driver.find_element_by_xpath(Locator.password)
        password.send_keys(TestData.student_password)

        login = driver.find_element_by_id(Locator.login)
        login.click()

        current_url = driver.current_url

        self.assertEqual(TestData.expected_url , current_url)


    def test_03_landing_page(self):

        try:
            learn = CommonFunc().wait_visibility(10, By.XPATH, Locator.learn)

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


    def test_04_confirmation_popup_in_Learn(self) :        

        confirmation_modal = CommonFunc().wait_visibility(
            5, By.CSS_SELECTOR, Locator.confirmation_modal)
        confirmation_modal_title = driver.find_element_by_css_selector(Locator.confirmation_modal_title)          

        if (confirmation_modal.is_displayed()):

            try:

                self.assertIn(confirmation_modal_title.text.upper(), TestData.student_username.upper())
                yes = driver.find_element_by_css_selector(Locator.yes_button)
                sleep(1)
                yes.click()

            except:

                no = driver.find_element_by_css_selector(Locator.no_button)
                no.click()
                sleep(1)
                self.assertEqual(TestData.expected_url , driver.current_url)
                print('Login not confirmed')

        else:
            print('No confirmation modal')


    def test_05_welcome_popup(self) :

        try:
            welcome_pop_up = driver.find_elements_by_xpath(
                Locator.welcome_pop_up)
            welcome_next_button = driver.find_elements_by_css_selector(
                Locator.welcome_next_button)

            for pop_up, next_button in zip(welcome_pop_up, welcome_next_button):

                next_button.click()

        except ElementNotVisibleException as e:

            print('No Welcome pop up')


    def test_06_check_initial_score_home_page(self):

        right_header_score = CommonFunc().wait_visibility(
            5, By.XPATH, Locator.right_header_score)        

        if right_header_score.text >= '100' :
            initial_score = right_header_score.text

        else :
            print('initial score is wrong')

    def test_07_check_profile_page_navigation(self):

        profile = driver.find_element_by_css_selector(Locator.profile)
        profile.click()

        self.assertEqual(Locator.profile_navigation_url, driver.current_url)

        try :

            recent_activity_list = driver.find_element_by_css_selector(Locator.recent_activity_list)

        except :

            print('No recent activity')

        profile_page_back = driver.find_element_by_id(Locator.profile_page_back)
        profile_page_back.click()

    def test_08_check_badge_sidebar_navigation(self) :

        badge = driver.find_element_by_id(Locator.badge)
        badge.click()

        try:
            badge_sidebar = driver.find_element_by_css_selector(Locator.badge_sidebar)
            badge_sidebar.is_displayed()

        except :

            print('badge sidebar is not active')

        badge.click()



    # def test_07_(self):

    #     CommonFunc().select_course()

    #     CommonFunc().select_lesson()

    #     CommonFunc().resources_testing()


if __name__ == "__main__":
    unittest.main()
