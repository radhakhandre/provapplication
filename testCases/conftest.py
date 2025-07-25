from _pytest.config import Config
from selenium import webdriver
# from pytest_html import Config
import pytest
import os

os.makedirs("Reports", exist_ok=True)


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#######Pytest Html report ############
def pytest_configure(config):
    if hasattr(config,'_metadata'):
        config._metadata['Project Name'] = 'Prov application'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Radha'


# it is hook for delete/Modify Environment info to html Report
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
