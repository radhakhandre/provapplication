import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class ProfilePageqa:
    clickOnIPN_xpath = "//a[@id='IPN']"
    clickOnConfig_xpath = "//div[@id='Configuration']"
    clickOnProfilemenu_xpath = "//a[@id='Profiles']"
    countryMousehover_id = "countryNameCellId_EGYPT"
    textOnProfile_xpath = "//input[@id='countryName']"
    drpOnProfile_xpath = "//select[@id='profileStatus']"
    btnOnProfile_id = "COMMON_GUI_BUTTON_FIND"
    preOnProfile_id = "EGYPT_DEFAULT"
    btneditOnProfile_xpath = "(//button[@id='editBtnId_EGYPT'])[1]"
    checkOnProfile_id = "distributionProfile.trafficLimitFlag"
    btnOnProfileSave_id = "saveBtnlId"
    clickOnProfile_id = "tabCloseBtnId_1"
    clickOnRedirectionPatt_id = "redirectionPatternTabId"
    selectOnLTECountrySetting_id = "ird_lte_rejection_typeId_0"
    verifyCheckboxChecked_id = "ird_5g_barred_0"
    percentageField_id = "ird_allocated_percentage_0"
    percentageFieldone_id = "ird_allocated_percentage_1"
    errorMessage_id = "errorMessageId_0"
    doubleClick_xpath = "(//span[@id='countryNameCellId_EGYPT'])[2]"
    tabClose_id = "tabCloseBtnId_1"
    scrollToElement_id = "Service Setup"

    def __init__(self, driver):
        self.driver = driver

    # def clickOnVerticalscroll(self):
    #     self.driver.execute_script("window.scrollBy(0,3000)", "")
    #     value = self.driver.execute_script("return window.pageYOffset;")
    #     print("No of pixels moved", value)
    #def scrollToElement(self):
        # serviceSetup = self.driver.find_element(By.ID, self.scrollToElement_id)
        # self.driver.execute_script("arguments[0].scrollIntoView();", serviceSetup)
        # value = self.driver.execute_script("return window.pageYOffset;")
        # print("No of pixels moved", value)
    def scrollToEnd(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("No of pixels moved", value)

    def scrollTobackup(self):
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("No of pixels moved", value)

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

    def doubleClickcountry(self):
        countrydoubleclick = self.driver.find_element(By.XPATH, self.doubleClick_xpath)
        doubleclick = ActionChains(self.driver)
        doubleclick.double_click(countrydoubleclick).perform()

    def tabClose(self):
        self.driver.find_element(By.ID, self.tabClose_id).click()

    def preOnProfile(self):
        self.driver.find_element(By.ID, self.preOnProfile_id).click()

    def mousehoverCountryname(self):
        countryhover = self.driver.find_element(By.ID, self.countryMousehover_id)
        act = ActionChains(self.driver)
        act.move_to_element(countryhover).click().perform()

    def btneditOnProfile(self):
        self.driver.find_element(By.XPATH, self.btneditOnProfile_xpath).click()

    def checkBoxFivegchecked(self):
        checkbox = self.driver.find_element(By.ID, self.verifyCheckboxChecked_id)
        # status = checkbox.is_selected()
        # print("Checked status:", status)
        if checkbox.is_selected():
            print("check box is already selected")
        else:
            print("check box is NOT selected")

    def percentageCheck(self):
        self.driver.find_element(By.ID, self.percentageField_id).send_keys(60)

    def percentageCheckOne(self):
        self.driver.find_element(By.ID, self.percentageFieldone_id).send_keys(80)

    def checkOnProfile(self):
        self.driver.find_element(By.ID, self.checkOnProfile_id).click()

    def btnOnProfileSave(self):
        self.driver.find_element(By.ID, self.btnOnProfileSave_id).click()

    def validationMessPercen(self):
        actual_text = self.driver.find_element(By.ID, self.errorMessage_id).text
        expected_text = "The sum of all Allocation % does not equal 100%. Change the percentages so that the total " \
                        "equals 100%."
        if actual_text == expected_text:
            print("text matched")
        else:
            print("text not macthed")

    def clickOnProfile(self):
        self.driver.find_element(By.ID, self.clickOnProfile_id).click()

    def clickOnRedirectionpatt(self):
        self.driver.find_element(By.ID, self.clickOnRedirectionPatt_id).click()

    def drpOnProfileRedir(self, value):
        drpvalueredir = Select(self.driver.find_element(By.ID, self.selectOnLTECountrySetting_id))
        drpvalueredir.select_by_visible_text(value)

    # def clickOnUseCountrysettings(self):
    #     self.driver.find_element(By.ID, self.selectOnLTECountrySetting_id).click()
    #     items = self.driver.find_elements(By.ID, "selectOnLTECountrySetting_id")
    #     for item in items:
    #         if item.text == "Diameter Unable To Comply":
    #             item.click()
    #             break

    def printmessage(self):
        # self.driver = driver
        msg = self.driver.find_element(By.XPATH, "//span[.='Operation completed successfully']").text
        # self.mesg = "Operation completed successfully"  # define the attribute here
        print(self.mesg)

    # def validationmessage(self):
    #     def __init__(self, driver):
    #         self.driver = driver
    #     self.msg = self.driver.find_element(By.XPATH, "//span[.='Operation completed successfully']").text
