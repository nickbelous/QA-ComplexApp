"""Stores tests related to start page"""
import random
from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

import constants.start_page
from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage(BaseTest):

    @pytest.fixture(scope="function")
    def driver(self):
        """Create and return driver, close after test"""
        # Create driver
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    def test_try_login_with_empty_field(self, driver, start_page):
        """
        - Go to main page
        - Found username & password value
        - Do not add any data to field
        - Press Sign In button
        - Verify error message

        """

        start_page.login("", "")
        sleep(3)
        self.log.info("Error message to expected")

    def test_invalid_login(self, start_page):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Click on Sign In button
        - Verify error message
        """
        # Fill field with invalid data
        start_page.login("Namee12", "Pwd8687")
        # Verify error message
        start_page.verify_incorrect_login()
        self.log.info("Error message to expected")

    def test_redirect_after_click_complex_app(self, driver, start_page):
        """TC1 - After click to text "Complex app for testing - QA" redirected to main page """

        # Found the link
        start_page.verify_redirect_is_successfully(by=By.XPATH, locator=constants.start_page.StartPageConstants.LINK_COMPLEX_APP_FOR_TESTING_XPATH)
        # Check link on the page
        assert start_page.verify_redirect_is_successfully
        self.log.info("Redirect after click to text 'Complex app for testing - QA' successfully ")

    def test_check_text_on_main_page(self, driver, start_page):
        """TC2 - Check text "Remember Writing?" is display in main page """

        # Found the text
        start_page.verify_element_is_displayed(by=By.XPATH, locator=constants.start_page.StartPageConstants.TEXT_REMEMBER_WRITING_MAIN_PAGE_XPATH)
        assert start_page.verify_element_is_displayed
        self.log.info("The text Remember Writing?' is display on the page")

    def test_check_text_sign_up_button(self, driver, start_page):
        """TC3 - Check text on "Sign up for OurApp button"""

        # Found the text
        start_page.verify_element_is_displayed(by=By.XPATH, locator=constants.start_page.StartPageConstants.TEXT_ON_SUBMIT_BUTTON_XPATH)
        assert start_page.verify_element_is_displayed
        self.log.info("The text on Sign up button  is 'Sign up for OurApp'")

    def test_check_text_under_slogan(self, driver, start_page):
        """TC4 - Check text "Are you sick of short..." is display on the page"""

        # Found the text
        start_page.verify_element_is_displayed(by=By.XPATH, locator=constants.start_page.StartPageConstants.TEXT_ARE_YOU_SICK_OF_SHORT_XPATH)
        assert start_page.verify_element_is_displayed
        self.log.info("The text 'Are you sick of short...' is display on the page")

    def test_redirect_after_click_to_our_app_link(self, driver, start_page):
        """TC5 - Check after clicking on the text "Our App" redirected is happened"""

        # Found the link
        start_page.verify_redirect_is_successfully(by=By.XPATH, locator=constants.start_page.StartPageConstants.LINK_OUR_APP_XPATH)
        # Check link on the page
        assert start_page.verify_redirect_is_successfully
        self.log.info("After click to 'Our App' redirect successfully")
