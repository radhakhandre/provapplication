import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.RicountryPage import RicountryPageqa
from pageObjects.ProfilePage import ProfilePageqa
# from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random


class Test_Ricountry_01:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # def __init__(self):
    #     self.driver = setup
    #     self.lp = LoginPage(self.driver)
    #     self.addprofile = ProfilePage(self.driver)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_countryedit(self, setup):
        self.mesg = "Operation completed successfully"
        self.logger.info("**********profile edit************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # self.lppre = LoginPage(self.driver)
        # self.lppre.setLoginPrev()
        # self.lppre.setLoginPrevTwo()

        self.lp = LoginPage(self.driver)
        self.lp.setLoginPrev()
        self.lp.setLoginPrevTwo()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(20)
        self.logger.info("************Login Successfull*************")

        self.RicountryPageqa = RicountryPageqa(self.driver)
        self.RicountryPageqa.clickOnRicountry()
        time.sleep(5)
        self.RicountryPageqa.clickOnAlbctryedit()
        time.sleep(5)
        self.RicountryPageqa.clickOnedit()
        time.sleep(10)
        self.RicountryPageqa.clickTextCountrycode()
        time.sleep(10)
        self.RicountryPageqa.clickTextCountrycodesend()
        time.sleep(10)
        self.RicountryPageqa.clickSaveButton()
        time.sleep(10)
        self.RicountryPageqa.clickOkButton()