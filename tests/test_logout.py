from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


class TestLogout:

    def test_logout_from_account_open_login_page(self, user):
        user.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        user.find_element(By.XPATH, ACCOUNT_BUTTON_EXIT).click()
        WebDriverWait(user, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_BUTTON)))

        assert 'login' in user.current_url
