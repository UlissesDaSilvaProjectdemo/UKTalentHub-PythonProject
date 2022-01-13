import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        #driver = webdriver.Chrome(executable_path=r"C:\Users\Ulisses.Dasilva\UKTalentHub-PythonProject\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching chrome browser.........")

    elif browser == 'firefox':
        #driver = webdriver.Firefox(executable_path="C:\\Users\\Ulisses.Dasilva\\driver\\geckodriver.exe")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driverLocation='C:\\Users\\Ulisses.Dasilva\\driver\\geckodriver.exe'
        os.environ["webdriver.Firefox"] = driverLocation
        driver = webdriver.Firefox(driverLocation)

        driver.maximize_window()
        print("Launching firefox browser.........")

    elif browser == 'Ie':
        driver = webdriver.Ie(IEDriverManager().install())
        print("Launching Ie browser.........")

    elif browser == 'Edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")

    elif browser == 'Opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print("Launching Opera browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
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
