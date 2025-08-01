from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    inputBox_Email_CSS = '#input-email'
    inputBox_Password_CSS = '#input-password'
    button_Login_Xpath = "//input[@value='Login']"
    text_validationMsg_Xpath = '//h2[normalize-space()="My Account"]'

    def __init__(self, driver):
        self.driver = driver

    def entEmail(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.inputBox_Email_CSS).send_keys(email)
    def entPassword(self, pswd):
        self.driver.find_element(By.CSS_SELECTOR, self.inputBox_Password_CSS).send_keys(pswd)
    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_Login_Xpath).click()
    def validationMsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element =  wait.until(EC.presence_of_element_located((By.XPATH, self.text_validationMsg_Xpath)))
            return element.is_displayed()
        except:
            return False