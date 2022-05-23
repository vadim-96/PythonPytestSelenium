import pytest
from assertpy import assert_that
from selenium.webdriver.remote.webdriver import WebDriver

from common_steps import AuthenticationSteps
from DTO import BillModel
from page_object.pages import BillsPage


class BillsTests:
    @pytest.mark.skip(reason="There is no validation on the form yet")
    def test_validate_BIK_field_on_creating_bill_form(self, webdriver: WebDriver) -> None:
        authentication_steps = AuthenticationSteps(webdriver)
        bills_page = BillsPage(webdriver)
        bill = BillModel("demo", "10.00", "Безнал", "bank", "123456789", "12345", "123")

        authentication_steps.log_in_to_site_as_test_user()
        bills_page.open().create_bill(bill)
