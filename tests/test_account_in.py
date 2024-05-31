from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


class TestAccountIn:

    def test_account_in_from_main_page_open_account(self, user):
        user.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        assert 'account/profile' in user.current_url
