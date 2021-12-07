"""Home work - practice with XPATH"""
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestHomeWorkTestXpath:
    """TC1 - After click to text "Complex app for testing - QA" redirected to main page """

    def test_test_case1(self):
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

    """Check text "Remember Writing?" is display in main page """

    def test_test_case2(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc2 = driver.find_element(by=By.XPATH, value=".//h1")
        checked_text_tc2.is_displayed()

    """Check text on "Sign up for OurApp"""

    def test_test_case3(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc3 = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        checked_text_tc3.is_displayed()

    """Check text "Are you sick of short..." is display on the page"""

    def test_test_case4(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Found the text
        checked_text_tc4 = driver.find_element(by=By.XPATH, value=".//p[@class='lead text-muted']")
        checked_text_tc4.is_displayed()

    """Check after clicking on the text "Our App" redirected is happened"""

    def test_test_case5(self):
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
