import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()



    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********test_homePageTitle********")

        #self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lppre = LoginPage(self.driver)
        #time.sleep(400)

        self.lppre.setLoginPrev()
        self.lppre.setLoginPrevTwo()

        #wait = WebDriverWait(driver, 50)
        act_title=self.driver.title
        #self.driver.close()
        if act_title=="TOMIA Provisioning Tool":
            assert True
            self.driver.close()
            self.logger.info("********test_homePageTitle TC Pass********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********test_homePageTitle TC Failed********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
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
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            #self.driver.close()
            if act_title == "TOMIA Provisioning Tool":
                assert True
                self.driver.close()
                self.logger.info("********Login TC Pass********")
            else:
                #self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.driver.close()
                self.logger.error("********Login TC Fail********")
                assert False




