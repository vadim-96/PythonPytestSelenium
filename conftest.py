from typing import Generator

import pytest
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


@pytest.fixture(scope="session")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture(scope="session")
def webdriver(config: TestConfig) -> Generator[WebDriver, None, None]:
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

    yield driver

    driver.quit()
