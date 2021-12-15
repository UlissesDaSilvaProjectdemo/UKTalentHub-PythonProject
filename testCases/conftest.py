import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching chrome browser.........")

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching firefox browser.........")

    elif browser == 'IEBrowser':

        driver = webdriver.Ie(IEDriverManager().install())
        print("Launching IEBrowser browser.........")

    return driver






def pytest_addoption(parser):    # This will get the value from CLI /hooks
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {}  # API metadata
    config._metadata['Project Name'] = 'UKTalentHub'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ulisses Da Silva'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


