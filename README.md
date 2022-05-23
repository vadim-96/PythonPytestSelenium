# About
Demo test project using Python, Pytest and Selenium.

# How to run
* Install Python 3.8
* Install dependencies from `pyproject.toml` file
    * or use Poetry: `poetry install`
* Create `.env` file in the root directory. Example of file:
    * ```
      BROWSER=Chrome
      IMPLICIT_WAIT=10
      ROOT_URL=https://example.com
      LOGIN=test@example.com
      PASSWORD=example123
      ```
* Run `pytest` command
