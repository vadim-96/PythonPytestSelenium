import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from environment_variables import EnvironmentVariables


@pytest.fixture()
def browser(config):
    driver = None

    if config.browser == 'Chrome':
        chrome_driver = ChromeDriverManager().install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs

        driver = webdriver.Chrome(service=Service(chrome_driver), options=chrome_options)
    elif config.browser == 'Firefox':
        firefox_driver = GeckoDriverManager().install()
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.accept_insecure_certs

        driver = webdriver.Firefox(service=Service(firefox_driver), options=firefox_options)
    else:
        raise ValueError(f'Unknown browser: {config.browser}')

    yield driver

    driver.quit()


@pytest.fixture()
def config():
    envs = EnvironmentVariables()
    return envs
