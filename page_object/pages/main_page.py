from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .page_object import PageObject


class MainPage(PageObject):
    def __init__(self, webdriver: WebDriver) -> None:
        super().__init__(webdriver)

    @property
    def profile_title(self) -> str:
        span = self._webdriver.find_element(By.XPATH, "//span[@class='profileTitle']")
        return span.text
