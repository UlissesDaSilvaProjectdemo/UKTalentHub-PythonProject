import pytest
import time
from mobile.Appiumframework.Base.DriverClass import Driver

@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')