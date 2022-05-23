from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing_extensions import Self

from DTO import BillModel

from ..elements import Buttons
from .page_object import PageObject


class BillsPage(PageObject):
    def __init__(self, webdriver: WebDriver) -> None:
        super().__init__(webdriver)
        self._url = "/bills"

    def create_bill(self, bill: BillModel) -> Self:
        buttons = Buttons(self._webdriver)

        buttons.add_button.click()

        self.__enter_bill_name(bill.name)
        self.__enter_balance(bill.balance)
        self.__select_category(bill.category)
        self.__enter_bank_fields(bill.bank_name, bill.BIK, bill.invoice_number)
        self.__select_to(bill.to)

        buttons.save_button.click()

        return self

    def __enter_bill_name(self, name: str) -> None:
        input_name = self._webdriver.find_element(By.XPATH, "//input[@name='title']")
        input_name.send_keys(name)

    def __enter_balance(self, balance: str) -> None:
        input_balance = self._webdriver.find_element(By.XPATH, "//input[@name='balance']")
        input_balance.send_keys(balance)

    def __select_category(self, category: str) -> None:
        select_category = self._webdriver.find_element(
            By.XPATH, "//div[@class='selectText' and text()='Выберите категорию']"
        )
        select_category.click()

        option = self._webdriver.find_element(By.XPATH, f"//div[contains(@class, 'itemText') and text()='{category}']")
        option.click()

    def __enter_bank_fields(self, bank_name: str, BIK: str, invoice_number: str) -> None:
        input_bank_name = self._webdriver.find_element(By.XPATH, "//input[@name='titleBank']")
        input_BIK = self._webdriver.find_element(By.XPATH, "//input[@name='bikBank']")
        input_invoice = self._webdriver.find_element(By.XPATH, "//input[@name='invoiceNumber']")

        input_bank_name.send_keys(bank_name)
        input_BIK.send_keys(BIK)
        input_invoice.send_keys(invoice_number)

    def __select_to(self, to: str) -> None:
        select_to = self._webdriver.find_element(
            By.XPATH, "//div[@class='selectText' and text()='Выберите направление']"
        )
        select_to.click()

        option = self._webdriver.find_element(By.XPATH, f"//div[contains(@class, 'itemText') and text()='{to}']")
        option.click()
