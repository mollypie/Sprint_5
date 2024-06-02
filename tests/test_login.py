from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import Helpers
from conftest import driver
from locators import *
from url_adresses import *


class TestLogin:

    def test_login_from_main_page_successful_login(self, driver):
        driver.get(main_page)

        driver.find_element(By.XPATH, MAIN_REDIRECT_TO_LOGIN).click()

        Helpers.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

    def test_login_from_account_page_successful_login(self, driver):
        driver.get(main_page)

        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()

        Helpers.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

    def test_login_from_registration_page_successful_login(self, driver):
        driver.get(registration_page)

        driver.find_element(By.XPATH, LINK_REDIRECT_TO_LOGIN).click()

        Helpers.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

    def test_login_from_forgot_password_page_successful_login(self, driver):
        driver.get(forgot_password_page)

        driver.find_element(By.XPATH, LINK_REDIRECT_TO_LOGIN).click()

        Helpers.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'
