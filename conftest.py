from typing import Generator

import pytest
from playwright.sync_api import (Browser, BrowserContext, BrowserType, Page,
                                 Playwright, sync_playwright)

from config import TestConfig


@pytest.fixture(scope="session")
def config() -> Generator[TestConfig, None, None]:
    yield TestConfig()


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, browser_name: str) -> Generator[BrowserType, None, None]:
    config = TestConfig()
    browser_type: BrowserType

    if config.browser == "chromium":
        browser_type = playwright.chromium
    elif config.browser == "firefox":
        browser_type = playwright.firefox
    else:
        raise ValueError(f'Unsupported browser: {config.browser}')

    yield browser_type


@pytest.fixture(scope="session")
def browser(browser_type: BrowserType) -> Generator[Browser, None, None]:
    browser = browser_type.launch(
        **{
            "executable_path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "headless": False,
        }
    )

    yield browser

    browser.close()


@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    config = TestConfig()
    context = browser.new_context(
        **{
            "ignore_https_errors": True,
            "base_url": config.root_url,
        }
    )

    yield context

    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()

    yield page

    page.close()
