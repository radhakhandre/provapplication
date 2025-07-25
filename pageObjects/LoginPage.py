from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_id = "password"
    button_login_xpath = "//input[@id='login']"
    link_one_xpath = "//button[@id='details-button']"
    link_two_xpath = "//a[@id='proceed-link']"
    button_logout_id="imgplus"
    button_logout_one_id = "logout"
    button_logout_two_xpath = "//a[@id='ok_btn']"

    def __init__(self, driver):
        self.driver = driver

    def setLoginPrev(self):
        # wait = WebDriverWait(self.driver, 80)
        # self.driver.wait.until(EC.element_to_be_clickable((By.ID, "link_one_xpath"))).click
        self.driver.find_element(By.XPATH, self.link_one_xpath).click()

    def setLoginPrevTwo(self):
        self.driver.find_element(By.XPATH, self.link_two_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.ID,self.button_logout_id).click()

    def clickLogoutone(self):
        self.driver.find_element(By.ID,self.button_logout_one_id).click()

    def clickLogouttwo(self):
        self.driver.find_element(By.XPATH, self.button_logout_two_xpath).click()
