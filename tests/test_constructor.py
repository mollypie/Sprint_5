from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from helpers import Helpers
from locators import *
from url_adresses import login_page


class TestBurgerConstructor:

    def test_burger_constructor_section_sauces_scroll_to_sauces(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_SAUCES + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

    def test_burger_constructor_section_buns_scroll_to_buns(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()
        driver.find_element(By.XPATH, MAIN_SECTION_BUNS).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_BUNS + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

    def test_burger_constructor_section_toppings_scroll_to_toppings(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_TOPPINGS).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_TOPPINGS + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))
