from assertpy import assert_that
from playwright.sync_api import Page

from config import TestConfig
from page_object import LoginPage, MainPage


def test_logged_in_to_site_as_test_user(page: Page):
    config = TestConfig()
    login_page = LoginPage(page)

    login_page.open().login_as(config.login, config.password)

    main_page = MainPage(page)
    assert_that(main_page.company_name).is_equal_to('Test')
