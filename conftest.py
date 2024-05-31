import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

import data
from url_adresses import *
from locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(login_page)

    yield driver

    driver.quit()


@pytest.fixture
def user(driver):
    driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(data.email)
    driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(data.password)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    return driver
