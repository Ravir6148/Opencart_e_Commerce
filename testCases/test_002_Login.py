import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import readProperties
from utilities.customLogger import LogGen
from utilities.randomString import random_string_generator


class Test_002_Login:
    Url = readProperties.ReadConfig.getURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*** Test_002_Login Started ***")
        self.driver = setup
        self.driver.get(self.Url)
        self.logger.info("*** Application Launched ***")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.logger.info("*** Landed on Login Page ***")
        self.lp = LoginPage(self.driver)
        # self.email = random_string_generator() + "@gmail.com"
        self.lp.entEmail("ravhhhhu123@gmail.com")
        self.lp.entPassword("123654789")
        self.lp.clickLoginButton()
        self.status = self.lp.validationMsg()
        if self.status:
            assert True
            self.logger.info("*** Test_002_Login Pased ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_login.png")
            self.logger.info("*** Test_002_Login Failed ***")
            self.driver.close()
            assert False

