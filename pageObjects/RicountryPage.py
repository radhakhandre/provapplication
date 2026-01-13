import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class RicountryPageqa:
    clickOnCountry_id = "Countries"
    clickOnEditButton_id = "Edit..."
    clickOnAlbctryedit_xpath = "//td[.='ALBANIA']"
    textfieldCntryCode_id = "countryCode"
    clickOnSave_id = "Save & Close"
    clickOnOkpop_id= "ok_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickOnRicountry(self):
        self.driver.find_element(By.ID, self.clickOnCountry_id).click()

    def clickOnAlbctryedit(self):
        self.driver.find_element(By.XPATH, self.clickOnAlbctryedit_xpath).click()

    def clickOnedit(self):
        self.driver.find_element(By.ID, self.clickOnEditButton_id).click()

    def clickTextCountrycode(self):
        move = self.driver.find_element(By.ID, self.textfieldCntryCode_id).clear()
        self.driver.switch_to.frame(move)

    def clickTextCountrycodesend(self):
        self.driver.find_element(By.ID, self.textfieldCntryCode_id).send_keys(355888)

    def clickSaveButton(self):
        self.driver.find_element(By.ID, self.clickOnSave_id).click()

    def clickOkButton(self):
        self.driver.find_element(By.ID, self.clickOnOkpop_id).click()
