from assertpy import assert_that
from selenium.webdriver.remote.webdriver import WebDriver

from common_steps import AuthenticationSteps
from config import TestConfig
from page_object.pages import MainPage


class AuthenticationTests:
    def test_user_should_be_logged_in_to_site(self, webdriver: WebDriver, config: TestConfig) -> None:
        authentication_steps = AuthenticationSteps(webdriver)
        main_page = MainPage(webdriver)

        authentication_steps.log_in_to_site_as_test_user()

        assert_that(main_page.profile_title).is_equal_to(config.login)
