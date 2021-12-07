"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    #     def test_start_page(self):
    #         """Sample test"""
    #         # Create driver
    #         driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
    #         # Open start page
    #         driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #         # Find and clean Username field
    #         username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
    #         username.clear()
    #         # Find and clean Password field
    #         password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
    #         password.clear()
    #         # Find Sign In button
    #         button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
    #         # Click button
    #         button.click()
    #         # Find error message
    #         sleep(1)
    #         message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
    #         # Verify message
    #         assert message.text == "Error"
    #
    #     def random_num(self):
    #         """Generate random number"""
    #         return str(random.choice(range(11111, 99999)))
    #
    #         # Создатьтест(поглядыва наимеющийся) который проверяет ошибку при логине с инвалидным
    #         # паролем и логином.(Проверка таже, добавляется только заполнение полей)
    #
    #     def test_invalid_login(self):
    #         """
    #         -Create driver
    #         -Open start page
    #         -Find username field
    #         -Put value
    #         -Click on Sign In button
    #         -Verify error message
    #         """
    #         # Create driver
    #         driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
    #         # Open start page
    #         driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #         # Find and clean Username field
    #         username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
    #         username.clear()
    #         username.send_keys(f"userName{self.random_num()}")
    #         sleep(3)
    #         # Find and clean Password field
    #         password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
    #         password.clear()
    #         password.send_keys(f"Pwn{self.random_num()}")
    #         sleep(3)
    #         # Find Sign In button
    #         button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
    #         # Click button
    #         button.click()
    #         # Find error message
    #         sleep(1)
    #         message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
    #         # Verify message
    #         assert message.text == "Error"

    def test_valid_login(self):
        """
        -Create driver
        -Open start page
        -Add valid data to Username input
        -Add valid data to Email input
        -Add valid data to Password input
        -Click Sign up for OurApp button
        -Check Sigh Out button
        -Click Sigh Out button
        -Check text for main page
        """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Add data to Username input
        username_registration = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_registration.send_keys(f"User{self.random_num_registration()}")
        # Add data to Email input
        email_registration = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email_registration.send_keys(f"nic.belous+{self.random_num_registration()}@gmail.com")
        # Add data to Password input
        password_registration = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_registration.send_keys(f"password{self.random_num_registration()}")
        sleep(2)
        # Click Sigh up button
        button_from_registration = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button_from_registration.click()
        sleep(2)
        # Check Sigh Out button
        button_sigh_out = driver.find_element(by=By.XPATH, value=".//button[@class='btn btn-sm btn-secondary']")
        # Click Sigh Out button
        button_sigh_out.click()
        sleep(2)
        # Check text "Remember Writing?"
        text_from_main_page = driver.find_element(by=By.XPATH, value=".//h1[@class='display-3']")
        text_from_main_page.is_displayed()
        sleep(5)

    def random_num_registration(self):
        """Generate random number"""
        return str(random.choice(range(111111111111, 999999999999)))

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
        """Check text "Remember Writing?" is display in main page """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc2 = driver.find_element(by=By.XPATH, value=".//h1")
        checked_text_tc2.is_displayed()

    def test_check_text_signin_button(self):
        """Check text on "Sign up for OurApp"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc3 = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        checked_text_tc3.is_displayed()

    def test_check_text_under_slogan(self):
        """Check text "Are you sick of short..." is display on the page"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc4 = driver.find_element(by=By.XPATH, value=".//p[@class='lead text-muted']")
        checked_text_tc4.is_displayed()

    def test_redirect_after_click_to_ourapp_link(self):
        """Check after clicking on the text "Our App" redirected is happened"""
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
