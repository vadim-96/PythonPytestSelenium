from pytest_bdd import parsers, scenarios, given


scenarios('../features/remove_sales.feature')


@given(parsers.parse('I logged in to the site as a test user'))
def I_logged_in_as_test_user(browser, config):
    browser.get(config.root_url)
    assert config.root_url == ''
