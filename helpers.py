from selenium.webdriver.common.by import By

from data import *
from locators import *


class Helpers:

    @staticmethod
    def login(driver):
        driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(login_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(login_password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
