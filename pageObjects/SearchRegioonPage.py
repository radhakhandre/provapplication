from selenium.webdriver.common.by import By


class SearchRegion:
    table_xpath = "//table[@id='previewTable']"
    table_Rows_xpath = "//table[@id='previewTable']//tbody/tr"
    table_column_xpath = "//table[@id='previewTable']//tbody/tr//td"
    submenu_xpath = "//a[@id='Regions']"
    region_edit = "//a[@id='Edit...']"

    def __init__(self, driver):
        self.driver = driver

    def setonRegion(self):
        self.driver.find_element(By.XPATH, self.submenu_xpath).click()

    def setonEdit(self):
        self.driver.find_elements(By.XPATH, self.region_edit)

    def getNoRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))

    def getNoColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Columns_xpath))

    def searchRegionByName(self, name):

        flag = False
        for r in range(1, self.getNoRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            regionname = table.find_element(By.XPATH, ("//table[@id='previewTable']/tbody/tr[" + str(r) + "]/td[2]"))
            rname = regionname.text
            print(rname)
            if rname == name:
                flag = True
                break
        return flag
