from selenium.webdriver.common.by import By
import time

class AddPartnershipStrategy2_2:

    def __init__(self, driver):
        self.driver = driver
        self.add_new_button = (By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[1]')
        self.identify_the_partnership_category_shadow_host = (By.XPATH, '(//fluent-select[@class="valid w-full collapsible outline required below"])[1]')
        self.identify_the_partnership_category_shadow_root = (By.CSS_SELECTOR, '[]')

    def click_add_new_button(self):
        self.driver.find_element(*self.add_new_button).click()
        time.sleep(2)

    def select_identify_the_partnership_category(self, identify_the_partnership_category):
        identify_the_partnership_category_shadow_host = self.driver.find_element(*self.identify_the_partnership_category_shadow_host)
        identify_the_partnership_category_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot',identify_the_partnership_category_shadow_host)
        identify_the_partnership_category_shadow_root.find_element(*self.identify_the_partnership_category_shadow_root).click()
        time.sleep(3)
