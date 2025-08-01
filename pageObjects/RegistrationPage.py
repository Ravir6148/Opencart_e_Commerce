from selenium.webdriver.common.by import By

class RegistrationPage:
    inputBox_FirstName_Xpath = "//input[@id='input-firstname']"
    inputBox_LastName_Xpath = "//input[@id='input-lastname']"
    inputBox_Email_Xpath = "//input[@id='input-email']"
    inputBox_Telephone_Xpath = "//input[@id='input-telephone']"
    inputBox_Password_Xpath = "//input[@id='input-password']"
    inputBox_ConfirmPassword_Xpath = "//input[@id='input-confirm']"
    checkBox_PrivacyPolicy_Xpath = "//input[@name='agree']"
    button_Continue_Xpath = "//input[@value='Continue']"
    text_message_Xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.inputBox_FirstName_Xpath).send_keys(fname)
    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.inputBox_LastName_Xpath).send_keys(lname)
    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.inputBox_Email_Xpath).send_keys(email)
    def setTelephone(self, tnumber):
        self.driver.find_element(By.XPATH, self.inputBox_Telephone_Xpath).send_keys(tnumber)
    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.inputBox_Password_Xpath).send_keys(password)
    def setConfirmPassword(self, confirmPassword):
        self.driver.find_element(By.XPATH, self.inputBox_ConfirmPassword_Xpath).send_keys(confirmPassword)
    def checkPolicy(self):
        self.driver.find_element(By.XPATH, self.checkBox_PrivacyPolicy_Xpath).click()
    def saveButton(self):
        self.driver.find_element(By.XPATH, self.button_Continue_Xpath).click()
    def getConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_message_Xpath).text
        except:
            None