from selenium.webdriver.common.by import By
import time

class AddPlan:

    def __init__(self, driver):
        self.driver = driver
        self.add_new_button = (By.XPATH, '(//fluent-anchor[@class=\'accent\'])[1]')
        self.period_field = (By.XPATH, '(//fluent-select[@id=\'Period\'])[1]')
        self.period_value_option = (By.XPATH, '(//fluent-option[@value="2022-2024"])[1]')



    def click_add_new_button(self):
        self.driver.find_element(*self.add_new_button).click()
        time.sleep(5)

    def select_period(self):
        #Click on period drop-down
        self.driver.find_element(*self.period_field).click()
        time.sleep(2)

        #Select value
        self.driver.find_element(*self.period_value_option).click()
        time.sleep(2)
