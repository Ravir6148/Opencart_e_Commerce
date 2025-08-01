import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getURL():
        URL = config.get('commonInfo', "baseurl")
        return URL
    @staticmethod
    def getEmail():
        email = config.get('commonInfo', "email")
        return email
    @staticmethod
    def getPassword():
        password = config.get('commonInfo', "password")
        return password