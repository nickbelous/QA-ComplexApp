import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, by, locator, value):
        """Fill field using provided variables """
        username = self.wait_until_find_element(by=by, value=locator)
        # username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def verify_element_is_displayed(self, by, locator):
        """Verify text on the page by xpath locator"""
        verify_text = self.wait_until_find_element(by=by, value=locator)
        assert verify_text.is_displayed()

    def verify_redirect_is_successfully(self, by, locator):
        """Verify redirect after clicking to link"""
        verify_redirect = self.wait_until_find_element(by=by, value=locator)
        verify_redirect.click()
        verify_redirect = self.wait_until_find_element(by=by, value=locator)
        assert verify_redirect.is_displayed()

    def wait_until_find_element(self, by, value):
        """Wait when element is unable"""
        return self.wait.until(EC.presence_of_element_located(locator=(by, value)))
