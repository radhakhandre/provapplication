import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class ProfilePageqa:
    clickOnIPN_xpath = "//a[@id='IPN']"
    clickOnConfig_xpath = "//div[@id='Configuration']"
    clickOnProfilemenu_xpath = "//a[@id='Profiles']"
    textOnProfile_xpath = "//input[@id='countryName']"
    drpOnProfile_xpath = "//select[@id='profileStatus']"
    btnOnProfile_id = "COMMON_GUI_BUTTON_FIND"
    preOnProfile_id = "EGYPT_DEFAULT"
    btneditOnProfile_xpath = "(//button[@id='editBtnId_EGYPT'])[1]"
    checkOnProfile_id = "distributionProfile.trafficLimitFlag"
    btnOnProfileSave_id = "saveBtnlId"
    clickOnProfile_id = "tabCloseBtnId_1"

    def __init__(self, driver):
        self.driver = driver

    def clickOnIPN(self):
        self.driver.find_element(By.XPATH, self.clickOnIPN_xpath).click()

    def clickOnConfig(self):
        self.driver.find_element(By.XPATH, self.clickOnConfig_xpath).click()

    def clickOnProfilemenu(self):
        self.driver.find_element(By.XPATH, self.clickOnProfilemenu_xpath).click()

    def textOnProfile(self, countryname):
        self.driver.find_element(By.XPATH, self.textOnProfile_xpath).send_keys(countryname)

    def drpOnProfile(self, value):
        drpvalue = Select(self.driver.find_element(By.XPATH, self.drpOnProfile_xpath))
        drpvalue.select_by_visible_text(value)

    def btnOnProfile(self):
        self.driver.find_element(By.ID, self.btnOnProfile_id).click()

    def preOnProfile(self):
        self.driver.find_element(By.ID, self.preOnProfile_id).click()

    def btneditOnProfile(self):
        self.driver.find_element(By.XPATH, self.btneditOnProfile_xpath).click()

    def checkOnProfile(self):
        self.driver.find_element(By.ID, self.checkOnProfile_id).click()

    def btnOnProfileSave(self):
        self.driver.find_element(By.ID, self.btnOnProfileSave_id).click()

    def clickOnProfile(self):
        self.driver.find_element(By.ID, self.clickOnProfile_id).click()

    def printmessage(self):
        #self.driver = driver
        msg = self.driver.find_element(By.XPATH, "//span[.='Operation completed successfully']").text
        #self.mesg = "Operation completed successfully"  # define the attribute here
        print(self.mesg)



    # def validationmessage(self):
    #     def __init__(self, driver):
    #         self.driver = driver
    #     self.msg = self.driver.find_element(By.XPATH, "//span[.='Operation completed successfully']").text

