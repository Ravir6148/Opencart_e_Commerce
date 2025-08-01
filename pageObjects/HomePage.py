from selenium.webdriver.common.by import By

class HomePage:
    link_MyAccount_Xpath = "//a[@title='My Account']"
    link_Register_Xpath = "//a[normalize-space()='Register']"
    link_Login_Xpath = "//a[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount_Xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.link_Register_Xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.link_Login_Xpath).click()
