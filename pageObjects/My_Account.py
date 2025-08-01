from selenium.webdriver.common.by import By


class MyAccount:
    link_Logout_Xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_Logout_Xpath).click()