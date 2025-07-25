import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.ProfilePage import ProfilePageqa
# from pageObjects.LoginPage import LoginPage
from pageObjects.SearchRegioonPage import SearchRegion
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random


class Test_searchRegionByname_01:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # def __init__(self):
    #     self.driver = setup
    #     self.lp = LoginPage(self.driver)
    #     self.addprofile = ProfilePage(self.driver)

    @pytest.mark.regression
    def test_searchRegionByname(self, setup):
        self.logger.info("**********region edit************")
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

        self.RegionPageqa = SearchRegion(self.driver)
        self.RegionPageqa.setonRegion()
        status = self.RegionPageqa.searchRegionByName("Europe")
        print(status)
        assert False==status
        self.logger.info("*************TC serach Region name finished*******************")

        #self.RegionPageqa.setonEdit()
