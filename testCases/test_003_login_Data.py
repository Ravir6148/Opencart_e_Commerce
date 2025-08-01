import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import readProperties, customLogger
from utilities.readExcel import read_excel_data


class Test_Login_DDT:
    baseURL = readProperties.ReadConfig.getURL()
    logger = customLogger.LogGen.loggen()
    login_test_data = read_excel_data()

    @pytest.mark.parametrize("username,password,expected_result", login_test_data)
    def test_login_ddt(self, username, password, expected_result, setup):
        self.logger.info("*** Test_003_Login Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("*** Application Launched ***")

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()
        self.logger.info("*** Landed on Login Page ***")

        self.lp = LoginPage(self.driver)
        self.lp.entEmail(username)
        self.lp.entPassword(password)
        self.lp.clickLoginButton()

        actual_result = "Valid" if self.lp.validationMsg() else "Invalid"

        if actual_result == expected_result:
            assert True
            self.logger.info(f"*** Test_003_Login Passed for {username} ***")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\test_login_ddt_failed.png")
            self.logger.error(f"*** Test_003_Login Failed for {username} ***")
            assert False

        self.driver.close()



