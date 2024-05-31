from selenium.webdriver.common.by import By

import data
from locators import *


class Helpers:

    @staticmethod
    def login(driver):
        driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(data.email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(data.password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
