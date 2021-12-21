import logging
from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)

    def fill_field(self, by, locator, value):
        """Fill field using provided variables """
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def verify_element_is_displayed(self, by, locator):
        """Verify text on the page by xpath locator"""
        verify_text = self.driver.find_element(by=by, value=locator)
        assert verify_text.is_displayed()

    def verify_redirect_is_successfully(self, by, locator, ):
        """Verify redirect after clicking to link"""
        verify_redirect = self.driver.find_element(by=by, value=locator)
        verify_redirect.click()
        sleep(2)
        verify_redirect = self.driver.find_element(by=by, value=locator)
        assert verify_redirect.is_displayed()
