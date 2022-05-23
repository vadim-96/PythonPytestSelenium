from selenium.webdriver.remote.webdriver import WebDriver

from config import TestConfig
from page_object.pages import LoginPage


class AuthenticationSteps:
    __webdriver: WebDriver

    def __init__(self, webdriver: WebDriver) -> None:
        self.__webdriver = webdriver

    def log_in_to_site_as_test_user(self) -> None:
        config = TestConfig()

        self.log_in_to_site(config.login, config.password)

    def log_in_to_site(self, login: str, password: str) -> None:
        login_page = LoginPage(self.__webdriver)

        login_page.open().login_as(login, password)
