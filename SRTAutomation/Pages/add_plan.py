from selenium.webdriver.common.by import By
import time

class AddPlan:

    def __init__(self, driver):
        self.driver = driver
        self.add_new_button = (By.XPATH, '(//fluent-anchor[@class=\'accent\'])[1]')
        self.period_field = (By.XPATH, '(//fluent-select[@id=\'Period\'])[1]')
        self.period_value_option = (By.XPATH, '(//fluent-option[@value="2022-2024"])[1]')
        self.program_overview_shadow_host = (By.XPATH, '(//fluent-accordion-item[@class="rounded"])[1]')
        self.program_overview_open = (By.CSS_SELECTOR, '[class="button"]')
        self.program_overview_edit_button = (By.XPATH, '(//fluent-button[@title=\'Edit\'])[1]')
        self.program_themes_shadow_host = (By.XPATH, '(//fluent-text-field[@class="outline"])[1]')
        self.program_themes_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.options = (By.XPATH, '(//div[@role="listbox"])[1]')
        self.Common_approches_shadow_host = (By.XPATH, '(//fluent-text-field[@class="outline"])[2]')
        self.Common_approches_shadow_root = (By.CSS_SELECTOR, '[id="control"]')


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

    def open_program_overview_section(self):
        program_overview_shadow_host = self.driver.find_element(*self.program_overview_shadow_host)
        program_overview_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_overview_shadow_host)
        program_overview_shadow_root.find_element(*self.program_overview_open).click()
        time.sleep(3)

    def click_program_overview_edit_button(self):
        self.driver.find_element(*self.program_overview_edit_button).click()
        time.sleep(3)

    def select_program_themes(self):
        program_themes_shadow_host = self.driver.find_element(*self.program_overview_shadow_host)
        program_themes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_themes_shadow_host)
        program_themes_shadow_root.find_element(*self.program_themes_shadow_root).click()
        time.sleep(1)

        self.driver.find_element(*self.options).click()
        time.sleep(1)

    def select_common_approches(self):
        Common_approches_shadow_host = self.driver.find_element(*self.Common_approches_shadow_host)
        Common_approches_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', Common_approches_shadow_host)
        Common_approches_shadow_root.find_element(*self.Common_approches_shadow_root).click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, '(//div[@role="listbox"])[1]').click()
        time.sleep(1)

