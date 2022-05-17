from playwright.sync_api import Page
from typing_extensions import Self

from .page_object import PageObject


class LoginPage(PageObject):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._url = '/auth'

    def login_as(self, login: str, password: str) -> Self:
        login_field = self._page.locator("//input[@name='email']")
        password_field = self._page.locator("//input[@name='password']")
        login_button = self._page.locator("//button[contains(@class, 'loginButton')]")

        login_field.type(login)
        password_field.type(password)
        login_button.click()

        return self
