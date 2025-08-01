import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Registering custom command-line option safely
def pytest_addoption(parser):
    parser.addoption("--my_browser", action="store", default="chrome", help="Browser name: chrome, firefox, edge")

# Accessing the browser option
@pytest.fixture()
def browser(request):
    return request.config.getoption("--my_browser")


# WebDriver initialization based on browser
@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

# ########################### HTML Report ##################################################

# This hook for deleting the unnecessary info from html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# This hook will add environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'OpenCart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Ravi Ranjan'

# This will specify the folder location and save report with time stamp.
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+'\\reports\\'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"