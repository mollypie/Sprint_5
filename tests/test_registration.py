import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data import *
from locators import *
from url_adresses import *


class TestRegistration:

    def test_registration_correct_name_email_and_password_successful_registration(self, driver):
        driver.get(registration_page)

        driver.find_element(By.XPATH, REGISTRATION_NAME).send_keys(reg_name)
        driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(reg_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(reg_password)

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_BUTTON)))

        assert 'login' in driver.current_url

    def test_registration_invalid_password_error_text(self, driver):
        driver.get(registration_page)

        driver.find_element(By.XPATH, REGISTRATION_NAME).send_keys(reg_name)
        driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(reg_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(reg_invalid_password)

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,
                                                                                          PASSWORD_TEXT_ERROR)))

        assert driver.find_element(By.CLASS_NAME, PASSWORD_TEXT_ERROR).text == 'Некорректный пароль'
