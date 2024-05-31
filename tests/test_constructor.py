from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


class TestBurgerConstructor:

    def test_burger_constructor_section_sauces_scroll_to_sauces(self, user):
        WebDriverWait(user, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        user.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()

        assert (user.find_element(By.XPATH, MAIN_SECTION_SAUCES + '/parent::div')
                == user.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

    def test_burger_constructor_section_buns_scroll_to_buns(self, user):
        WebDriverWait(user, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        user.find_element(By.XPATH, MAIN_SECTION_SAUCES).click()
        user.find_element(By.XPATH, MAIN_SECTION_BUNS).click()

        assert (user.find_element(By.XPATH, MAIN_SECTION_BUNS + '/parent::div')
                == user.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))

    def test_burger_constructor_section_toppings_scroll_to_toppings(self, user):
        WebDriverWait(user, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))
        user.find_element(By.XPATH, MAIN_SECTION_TOPPINGS).click()

        assert (user.find_element(By.XPATH, MAIN_SECTION_TOPPINGS + '/parent::div')
                == user.find_element(By.XPATH, MAIN_SELECTED_ELEMENT))
