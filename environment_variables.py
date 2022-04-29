from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass
class EnvironmentVariables:
    browser: str
    implicit_wait: int
    root_url: str
    login: str
    password: str

    def __init__(self):
        load_dotenv()

        browser_env = os.getenv('BROWSER')
        implicit_wait_env = os.getenv('IMPLICIT_WAIT')
        root_url_env = os.getenv('ROOT_URL')
        login_env = os.getenv('LOGIN')
        password_env = os.getenv('PASSWORD')

        if browser_env is None \
                or implicit_wait_env is None \
                or root_url_env is None \
                or login_env is None \
                or password_env is None:
            raise EnvironmentError('One of the envs are not defined. Please create .env file correctly')

        self.browser = browser_env
        self.implicit_wait = int(implicit_wait_env)
        self.root_url = root_url_env
        self.login = login_env
        self.password = password_env
