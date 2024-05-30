import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from url_adresses import *
from locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(login_page)

    email = 'anyaserikova9123@yandex.ru'
    password = '125l!s87'

    driver.find_element(By.XPATH, REGISTRATION_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, REGISTRATION_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    return driver
