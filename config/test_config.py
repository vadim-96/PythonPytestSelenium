import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class TestConfig(object):
    __test__ = False

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TestConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        load_dotenv(".env", verbose=True)

    @property
    def browser(self) -> str:
        browser_env = os.getenv("BROWSER")
        if not browser_env or browser_env is None:
            raise EnvironmentError("BROWSER env is not defined")

        return browser_env

    @property
    def implicit_wait(self) -> int:
        implicit_wait_env = os.getenv("IMPLICIT_WAIT")
        if not implicit_wait_env or implicit_wait_env is None:
            raise EnvironmentError("IMPLICIT_WAIT env is not defined")

        return int(implicit_wait_env)

    @property
    def root_url(self) -> str:
        root_url_env = os.getenv("ROOT_URL")
        if not root_url_env or root_url_env is None:
            raise EnvironmentError("ROOT_URL env is not defined")

        return root_url_env

    @property
    def login(self) -> str:
        login_env = os.getenv("LOGIN")
        if not login_env or login_env is None:
            raise EnvironmentError("LOGIN env is not defined")

        return login_env

    @property
    def password(self) -> str:
        password_env = os.getenv("PASSWORD")
        if not password_env or password_env is None:
            raise EnvironmentError("PASSWORD env is not defined")

        return password_env
