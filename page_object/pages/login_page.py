from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Self

from .page_object import PageObject


class LoginPage(PageObject):
    def __init__(self, webdriver: WebDriver) -> None:
        super().__init__(webdriver)
        self._url = "/auth"

    def login_as(self, login: str, password: str) -> Self:
        login_field = self._webdriver.find_element(By.XPATH, "//input[@name='email']")
        password_field = self._webdriver.find_element(By.XPATH, "//input[@name='password']")
        login_button = self._webdriver.find_element(By.XPATH, "//button[contains(@class, 'loginButton')]")

        login_field.send_keys(login)
        password_field.send_keys(password)
        login_button.click()

        return self
