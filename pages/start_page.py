from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base import BasePage


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def login(self, username_value, password_value):
        """Login using provided password and username"""

        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username_value)
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields are filled with invalid value")
        # Find Sign In button
        button = self.wait_until_find_element(by=By.XPATH, value=self.constants.SIGN_IN_BUTTON_XPATH)
        # Click button
        button.click()
        self.log.debug("Clicked on 'Sign In' button")

    def verify_incorrect_login(self):
        """Verify error message on invalid login"""
        # Find error message
        message = self.wait_until_find_element(by=By.XPATH, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        # Verify message
        assert message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT_XPATH

    def register_user(self, username_value, email_value, password_value):
        """register user using provided data"""
        # Fill username
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_USERNAME_XPATH, value=username_value)
        # Fill email
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=email_value)
        # Fill password
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields were filled")
        sleep(1)

        # Click on Sign Up button
        self.wait_until_find_element(by=By.XPATH, value=self.constants.SIGN_UP_BUTTON_XPATH).click()
        self.log.debug("User was registered")
