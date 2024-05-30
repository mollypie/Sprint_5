from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from conftest import driver


class TestAccountIn:

    def test_account_in_from_main_page_open_account(self, driver):
        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        assert 'account/profile' in driver.current_url

        driver.quit()
