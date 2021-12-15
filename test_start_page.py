"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_start_page(self):
        """Sample test"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find adn clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(3)
        # Find adn clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(3)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        # Click button
        button.click()
        # Find error message
        sleep(1)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"

    def random_num(self):
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

        # Создать тест (поглядывая на имеющийся) который проверяет ошибку при логине с инвалидным паролем и логином
        # (Проверка та же, добавляется только значение полей)

    def test_invalid_login(self):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Click on Sign In button
        - Verify error message
        """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find adn clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(f"userName{self.random_num()}")
        sleep(3)
        # Find adn clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(f"PWD{self.random_num()}")
        sleep(3)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        # Click button
        button.click()
        # Find error message
        sleep(1)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"

    def test_redirect_after_click_complex_app(self):
        """TC1 - After click to text "Complex app for testing - QA" redirected to main page """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc1 = driver.find_element(by=By.XPATH, value=".//H4")
        # Click on the link
        checked_text_tc1.click()
        sleep(2)
        # Check link on the page
        checked_text_tc1 = driver.find_element(by=By.XPATH, value=".//H4")
        checked_text_tc1.is_displayed()

    def test_check_text_on_main_page(self):
        """TC2 - Check text "Remember Writing?" is display in main page """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc2 = driver.find_element(by=By.XPATH, value=".//h1")
        checked_text_tc2.is_displayed()

    def test_check_text_signin_button(self):
        """TC3 - Check text on "Sign up for OurApp"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc3 = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        checked_text_tc3.is_displayed()

    def test_check_text_under_slogan(self):
        """TC4 - Check text "Are you sick of short..." is display on the page"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc4 = driver.find_element(by=By.XPATH, value=".//p[@class='lead text-muted']")
        checked_text_tc4.is_displayed()

    def test_redirect_after_click_to_ourapp_link(self):
        """TC5 - Check after clicking on the text "Our App" redirected is happened"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc5 = driver.find_element(by=By.XPATH, value=".//a[@class='text-muted']")
        # Click on the link
        checked_text_tc5.click()
        sleep(2)
        # Check link on the page
        checked_text_tc5 = driver.find_element(by=By.XPATH, value=".//a[@class='text-muted']")
        checked_text_tc5.is_displayed()
