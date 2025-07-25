import self
from selenium.webdriver.common.by import By
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


class SearchRegion:
    table_Rows_xpath = "//table[@id='previewTable']//tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def setonRegion(self):
        self.driver.find_element(By.XPATH, self.submenu_xpath).click()

    def getNoRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))


# region_page = SearchRegion(driver)
# row_count = region_page.getNoRows()
SearchRegion.getNoRows(self.driver)
region = SearchRegion(driver)
row_count = region.getNoRows()