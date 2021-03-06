from typing import Generator

import allure
import pytest
from pluggy._result import _Result
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config import TestConfig


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> Generator[None, _Result, pytest.TestReport]:
    outcome: _Result = yield
    rep: pytest.TestReport = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)

    return rep


@pytest.fixture(scope="session")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture()
def webdriver(request: pytest.FixtureRequest, config: TestConfig) -> Generator[WebDriver, None, None]:
    driver = setup_webdriver(config)

    yield driver

    try:
        if request.node.rep_call.failed:
            test_name = request.node.name
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name=test_name, attachment_type=allure.attachment_type.PNG)
    finally:
        driver.quit()


def setup_webdriver(config: TestConfig) -> WebDriver:
    driver: WebDriver

    if config.browser == "Chrome":
        chrome_driver = ChromeDriverManager().install()
        chrome_options = ChromeOptions()
        chrome_options.accept_insecure_certs = True
        driver = Chrome(service=ChromeService(chrome_driver), options=chrome_options)
    elif config.browser == "Firefox":
        firefox_driver = GeckoDriverManager().install()
        firefox_options = FirefoxOptions()
        firefox_options.accept_insecure_certs = True
        driver = Firefox(service=FirefoxService(firefox_driver), options=firefox_options)
    else:
        raise ValueError(f"Unknown browser: {config.browser}")

    driver.implicitly_wait(config.implicit_wait)
    driver.maximize_window()

    return driver
