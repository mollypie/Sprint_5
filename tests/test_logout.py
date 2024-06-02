from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from helpers import Helpers
from locators import *
from url_adresses import login_page


class TestLogout:

    def test_logout_from_account_open_login_page(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        driver.find_element(By.XPATH, ACCOUNT_BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_BUTTON)))

        assert 'login' in driver.current_url
