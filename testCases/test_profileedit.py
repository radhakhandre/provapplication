import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.ProfilePage import ProfilePageqa
# from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random


class Test_Profile_01:
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
    def test_profileedit(self, setup):
        self.mesg="Operation completed successfully"
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

        self.ProfilePageqa = ProfilePageqa(self.driver)
        self.ProfilePageqa.clickOnIPN()
        time.sleep(20)
        self.ProfilePageqa.clickOnConfig()
        time.sleep(10)
        self.ProfilePageqa.clickOnProfilemenu()
        time.sleep(10)
        self.ProfilePageqa.textOnProfile("EGYPT")
        time.sleep(10)
        self.ProfilePageqa.drpOnProfile("-- All Statuses --")
        time.sleep(10)
        self.ProfilePageqa.btnOnProfile()
        time.sleep(10)
        self.ProfilePageqa.preOnProfile()
        time.sleep(10)
        self.ProfilePageqa.btneditOnProfile()
        time.sleep(10)
        self.ProfilePageqa.checkOnProfile()
        time.sleep(10)
        self.ProfilePageqa.btnOnProfileSave()
        time.sleep(10)

        # self.msg = self.driver.find_element(By.XPATH, "//span[.='Operation completed successfully']").text
        # print(self.msg)

        if 'Operation completed successfully' == self.mesg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_test_profileedit_scr.png")
            assert True == False

        time.sleep(10)
        self.ProfilePageqa.clickOnProfile()
        time.sleep(10)

        self.driver.close()
