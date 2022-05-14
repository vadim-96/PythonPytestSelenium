from urllib.parse import urljoin

from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Self

from config import TestConfig


class PageObject:
    __webdriver: WebDriver
    __url: str

    def __init__(self, webdriver: WebDriver) -> None:
        self.__webdriver = webdriver

    def open(self, url_params: str = '') -> Self:
        full_url = urljoin(self.__url, url_params) if url_params else self.__url

        self.__webdriver.get(full_url)

        return self

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def _url(self, relative_url: str) -> None:
        if not relative_url or relative_url is None:
            raise ValueError('Relative URL cannot be empty')

        config = TestConfig()
        self.__url = urljoin(config.root_url, relative_url) if relative_url else config.root_url

    @property
    def _webdriver(self) -> WebDriver:
        return self.__webdriver
