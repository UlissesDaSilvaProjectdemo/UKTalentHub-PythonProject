import allure
import pytest



def test_method2A():
    allureLogs('TEST Logs')
    allureLogs('TEST Logs')
    allureLogs('TEST Logs')

    print("This is method A")


def test_method2B():
    print("This is method B")


@pytest.mark.skip
def test_method2C():
    allureLogs('TEST Logs')
    print("This is method C")


def test_method2D():
    allureLogs('TEST Logs')
    print("This is method D")
    assert False

def allureLogs(text):
    with allure.step(text):
        pass


