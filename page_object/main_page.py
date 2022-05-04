from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .page_object import PageObject


class MainPage(PageObject):
    def __init__(self, webdriver: WebDriver) -> None:
        super().__init__(webdriver)

    @property
    def company_name(self) -> str:
        label = self._webdriver.find_element(By.XPATH, "//span[@class='companyNameLabel']")
        return label.text
