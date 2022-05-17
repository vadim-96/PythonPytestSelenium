from typing import Union

from playwright.sync_api import Page

from .page_object import PageObject


class MainPage(PageObject):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def company_name(self) -> Union[str, None]:
        label = self._page.locator("//span[@class='companyNameLabel']")
        return label.text_content()
