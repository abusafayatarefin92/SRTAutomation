from selenium.webdriver.common.by import By
import time

class AddRiskMitigationStrategy2_3:

    def __init__(self, driver):
        self.driver = driver
        self.add_new_button = (By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[2]')
        self.identified_risk_shadow_host = (By.XPATH, '(//fluent-text-field[@name="IdentifiedRisk"])[1]')
        self.identified_risk_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.description_shadow_host = (By.XPATH, '(//fluent-text-area[@name="Description"])[1]')
        self.description_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.activities_shadow_host = (By.XPATH, '(//fluent-text-area[@name="Activities"])[1]')
        self.activities_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.risk_mitigation_strategy_save_as_draft_shadow_host = (By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
        self.risk_mitigation_strategy_save_as_draft_shadow_root = (By.CSS_SELECTOR, '[part="control"]')
        self.risk_mitigation_strategy_yes_shadow_host = (By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
        self.risk_mitigation_strategy_yes_shadow_root = (By.CSS_SELECTOR, '[class="control"]')
        self.close_program_approach_shadow_host = (By.XPATH, '(//fluent-accordion-item[@class="rounded expanded"])[2]')#(//fluent-accordion-item[@id='f37f8cfff'])[1]
        self.close_program_approach_shadow_root = (By.CSS_SELECTOR, '[class="button"]')

    def click_add_new_button(self):
        self.driver.find_element(*self.add_new_button).click()
        time.sleep(2)

    def insert_all_text_fields(self, identified_risk, description, activities):
        identified_risk_shadow_host = self.driver.find_element(*self.identified_risk_shadow_host)
        identified_risk_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', identified_risk_shadow_host)
        identified_risk_shadow_root.find_element(*self.identified_risk_shadow_root).send_keys(identified_risk)
        time.sleep(1)

        description_shadow_host = self.driver.find_element(*self.description_shadow_host)
        description_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', description_shadow_host)
        description_shadow_root.find_element(*self.description_shadow_root).send_keys(description)
        time.sleep(1)

        activities_shadow_host = self.driver.find_element(*self.activities_shadow_host)
        activities_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', activities_shadow_host)
        activities_shadow_root.find_element(*self.activities_shadow_root).send_keys(activities)
        time.sleep(1)

    def save_as_draft(self):
        risk_mitigation_strategy_save_as_draft_shadow_host = self.driver.find_element(*self.risk_mitigation_strategy_save_as_draft_shadow_host)
        risk_mitigation_strategy_save_as_draft_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', risk_mitigation_strategy_save_as_draft_shadow_host)
        risk_mitigation_strategy_save_as_draft_shadow_root.find_element(*self.risk_mitigation_strategy_save_as_draft_shadow_root).click()
        time.sleep(2)

        risk_mitigation_strategy_yes_shadow_host = self.driver.find_element(*self.risk_mitigation_strategy_yes_shadow_host)
        risk_mitigation_strategy_yes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', risk_mitigation_strategy_yes_shadow_host)
        risk_mitigation_strategy_yes_shadow_root.find_element(*self.risk_mitigation_strategy_yes_shadow_root).click()
        time.sleep(3)

    def close_section_program_approach(self):
        close_program_approach_shadow_host = self.driver.find_element(*self.close_program_approach_shadow_host)
        close_program_approach_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', close_program_approach_shadow_host)
        close_program_approach_shadow_root.find_element(*self.close_program_approach_shadow_root).click()
        time.sleep(1)