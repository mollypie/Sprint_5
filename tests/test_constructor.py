from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from conftest import driver


class TestBurgerConstructor:

    def test_burger_constructor_section_sauces_scroll_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_SAUCES + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

        driver.quit()

    def test_burger_constructor_section_buns_scroll_to_buns(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()
        driver.find_element(By.XPATH, MAIN_SECTION_BUNS).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_BUNS + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

        driver.quit()

    def test_burger_constructor_section_toppings_scroll_to_toppings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        driver.find_element(By.XPATH, MAIN_SECTION_TOPPINGS).click()

        assert (driver.find_element(By.XPATH, MAIN_SECTION_TOPPINGS + '/parent::div')
                == driver.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

        driver.quit()
