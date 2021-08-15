from pytest import mark


# parameters coupled to test case
@mark.parametrize('parameters', ['hello world'])
def check_passing(parameters):
    assert parameters == 'hello world'


# parameters coupled to test case
@mark.xfail(reason='if parameter is a list, it runs once for each element (parameter)')
@mark.parametrize('parameters', ['hello', 'world'])
def check_passing_list(parameters):
    assert parameters == 'hello'


@mark.with_params
def check_fixture_params_web_eldetape(browser):
    browser.get('https://www.eldestapeweb.com/')
    assert True
