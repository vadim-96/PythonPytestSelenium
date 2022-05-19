from assertpy import assert_that
from selenium.webdriver.remote.webdriver import WebDriver

from config import TestConfig
from page_object.pages import LoginPage, MainPage


class AuthenticationTests:
    def test_user_should_be_logged_in_to_site(self, webdriver: WebDriver, config: TestConfig) -> None:
        main_page = MainPage(webdriver)

        self.log_in_to_site(webdriver, config.login, config.password)

        assert_that(main_page.profile_title).is_equal_to(config.login)

    def log_in_to_site(self, webdriver: WebDriver, login: str, password: str) -> None:
        login_page = LoginPage(webdriver)

        login_page.open().login_as(login, password)
