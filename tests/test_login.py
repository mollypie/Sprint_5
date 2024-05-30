from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from url_adresses import *


class TestLogin:

    @staticmethod
    def login(driver):
        email = 'anyaserikova9123@yandex.ru'
        password = '125l!s87'

        driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    def test_login_from_main_page_successful_login(self):
        driver = webdriver.Chrome()
        driver.get(main_page)

        driver.find_element(By.XPATH, MAIN_REDIRECT_TO_LOGIN).click()

        self.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

        driver.quit()

    def test_login_from_account_page_successful_login(self):
        driver = webdriver.Chrome()
        driver.get(main_page)

        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()

        self.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

        driver.quit()

    def test_login_from_registration_page_successful_login(self):
        driver = webdriver.Chrome()
        driver.get(registration_page)

        driver.find_element(By.XPATH, LINK_REDIRECT_TO_LOGIN).click()

        self.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

        driver.quit()

    def test_login_from_forgot_password_page_successful_login(self):
        driver = webdriver.Chrome()
        driver.get(forgot_password_page)

        driver.find_element(By.XPATH, LINK_REDIRECT_TO_LOGIN).click()

        self.login(driver)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

        driver.quit()
