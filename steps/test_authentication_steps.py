from assertpy import assert_that
from pytest_bdd import given, scenarios
from selenium.webdriver.remote.webdriver import WebDriver

from config import TestConfig
from page_object import LoginPage, MainPage

scenarios('../features/')


@given('I logged in to the site as a test user')
def I_logged_in_to_site_as_test_user(webdriver: WebDriver):
    config = TestConfig()
    login_page = LoginPage(webdriver)

    login_page.open().login_as(config.login, config.password)

    main_page = MainPage(webdriver)

    assert_that(main_page.company_name).is_equal_to('Test')
