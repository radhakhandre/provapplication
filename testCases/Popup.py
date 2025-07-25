import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Popup():
    def demo_windows(self):
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver137\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://10.10.30.47:8089/mul-spr-800/login.html#!/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='details-button']").click()
        self.driver.find_element(By.XPATH, "//a[@id='proceed-link']").click()
        username_input = self.driver.find_element(By.XPATH,
                                                  "//input[@id='username']")  # Replace with actual ID if different
        password_input = self.driver.find_element(By.ID, "password")  # Replace with actual ID if different
        username_input.send_keys("Superuser-1")
        password_input.send_keys("Superuser-1")

        login_button = self.driver.find_element(By.XPATH, "//input[@id='login']")  # Replace with actual ID if different
        login_button.click()
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://10.10.30.47:8089/mul-spr-800/login.html#!/")
        # self.driver = setup
        # self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        # time.sleep(25)
        # self.driver=webdriver.Chrome()
        # self.lp = LoginPage(self.driver)
        # self.lp.setLoginPrev()
        # self.lp.setLoginPrevTwo()
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # self.lp.clickLogout()
        self.driver.find_element(By.ID, "imgplus").click()


        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        # self.lp.clickLogoutone();
        self.driver.find_element(By.ID, "logout").click()
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@id='ok_btn']").click()
        time.sleep(4)

                # wait = WebDriverWait(self.driver, 10)
                # ok_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//a[.='Yes']")))
                # ok_btn.click()

logoutpopup = Popup()
logoutpopup.demo_windows()
