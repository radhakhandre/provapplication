import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************Test_002_DDT_login*****************")
        self.logger.info("********Login TC started********")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # time.sleep(25)
        # self.driver=webdriver.Chrome()
        self.lp = LoginPage(self.driver)
        self.lp.setLoginPrev()
        self.lp.setLoginPrevTwo()
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        lst_status = []  # empty list variable

        for r in range(3, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            print(self.user)
            self.passw = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.passw)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "TOMIA Provisioning Tool"
            # self.driver.close()
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed")
                    time.sleep(5)
                    # self.driver.close()
                    # self.lp.clickLogout()
                    # self.lp.clickLogoutone();
                    # parent_window_handle = self.driver.current_window_handle
                    # all_window_handles = self.driver.window_handles
                    # for handle in all_window_handles:
                    #     if handle != parent_window_handle:
                    #         new_window_handle = handle
                    #         break
                    # self.driver.switch_to.window(new_window_handle)

                    # self.lp.clickLogouttwo();
                    # self.driver.switch_to.window(parent_window_handle)
                    lst_status.append("Pass")
                    # self.driver.close()
                elif self.exp == "Fail":
                    self.logger.info("***Failed*****")
                    # self.driver.close()
                    # self.lp.clickLogout();
                    # self.lp.clickLogoutone();
                    # self.lp.clickLogouttwo;
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info('***failed***')
                    # self.lp.clickLogout()
                    # self.lp.button_logout_one_id
                    # self.lp.button_logout_two_id
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("****passed*****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test failed******")
            self.driver.close()
            assert False
        self.logger.info("********End of DDT test****************")
