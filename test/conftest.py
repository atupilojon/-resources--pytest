from pytest import fixture
from selenium import webdriver
from config import Config

# adding CLI args
def pytest_addoption(parser):
    parser.addoption('--data', action='store', default='None')


# making args availables for test and fixtures
@fixture(scope='session')
def data(request):
    some_data = request.config.getoption('--data')
    return Config(some_data).data


# @fixture(scope='function')
@fixture(scope='session')
def firefox_browser():
    browser = webdriver.Firefox(
        executable_path=r'static\\geckodriver.exe'
    )
    yield browser
