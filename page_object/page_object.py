from urllib.parse import urljoin

from playwright.sync_api import Page
from typing_extensions import Self


class PageObject:
    __page: Page
    __url: str

    def __init__(self, page: Page) -> None:
        self.__page = page

    def open(self, url_params: str = '') -> Self:
        full_url = urljoin(self.__url, url_params) if url_params else self.__url

        self.__page.goto(full_url)

        return self

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def _url(self, relative_url: str) -> None:
        if not relative_url or relative_url is None:
            raise ValueError('Relative URL cannot be empty')

        self.__url = relative_url

    @property
    def _page(self) -> Page:
        return self.__page
