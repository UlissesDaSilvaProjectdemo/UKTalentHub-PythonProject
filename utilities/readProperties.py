import configparser
import self
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def trello_password():
        trello_password = config.get('common info', 'trello_password')
        return trello_password

    @staticmethod
    def supportUrl():
        supportUrl = config.get('common info', 'supportUrl')
        return supportUrl

    @staticmethod
    def sychronizepage():
        sychronizepage = config.get('common info', 'sychronizepage')
        return sychronizepage





     