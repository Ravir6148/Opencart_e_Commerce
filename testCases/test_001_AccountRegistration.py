import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.customLogger import LogGen
from utilities.randomString import random_string_generator
from utilities.readProperties import ReadConfig


class Test_001_AccountRegistration:
    baseURL = ReadConfig.getURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_accResTesting(self, setup):
        self.logger.info("*** Test_001_AccountRegistration Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Application Launched ***")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("*** Landed on Registration Page ***")
        self.rg = RegistrationPage(self.driver)
        self.rg.setFirstName("Ravi Ranjan")
        self.rg.setLastName("Sharma")
        self.email = random_string_generator() + "@gmail.com"
        self.rg.setEmail(self.email)
        self.rg.setTelephone("9855632170")
        self.rg.setPassword("hyjhkjiykk635521!@11")
        self.rg.setConfirmPassword("hyjhkjiykk635521!@11")
        self.rg.checkPolicy()
        self.rg.saveButton()
        self.confmsg = self.rg.getConfirmation()
        if self.confmsg == "Your Account Has Been Created!":
            assert True
            self.logger.info("*** Test_001_AccountRegistration Passed ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_accResTesting.png")
            self.logger.error("*** Test_001_AccountRegistration Failed ***")
            self.driver.close()
            assert False