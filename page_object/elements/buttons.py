from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Buttons:
    __webdriver: WebDriver

    def __init__(self, webdriver: WebDriver) -> None:
        self.__webdriver = webdriver

    @property
    def add_button(self) -> WebElement:
        add_button = self.__webdriver.find_element(By.XPATH, "//button[contains(@class, 'addButton')]")
        return add_button

    @property
    def save_button(self) -> WebElement:
        save_button = self.__webdriver.find_element(By.XPATH, "//button[contains(@class, 'saveButton')]")
        return save_button
