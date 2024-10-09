from selenium.webdriver.common.by import By
import time

class AddPartnershipStrategy2_2:

    def __init__(self, driver):
        self.driver = driver
        self.add_new_button = (By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[1]')
        self.identify_the_partnership_category_field = (By.XPATH, "(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]")
        self.identify_the_partnership_category_option = (By.XPATH, '(//fluent-option[@value="2"])[1]')
        self.share_name_of_partner_shadow_host = (By.XPATH, '(//fluent-text-field[@class="valid outline required"])[1]')
        self.share_name_of_partner_shadow_root = (By.CSS_SELECTOR, 'input.control')
        self.partner_contribution_shadow_host = (By.XPATH, '(//fluent-text-area[@name="PartnerContribution"])[1]')
        self.partner_contribution_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.sci_role_shadow_host = (By.XPATH, '(//fluent-text-area[@name="SCIRole"])[1]')
        self.sci_role_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.partnership_strategy_save_as_draft_shadow_host = (By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
        self.partnership_strategy_save_as_draft_shadow_root = (By.CSS_SELECTOR, '[part="control"]')
        self.partnership_strategy_yes_shadow_host = (By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
        self.partnership_strategy_yes_shadow_root = (By.CSS_SELECTOR, '[class="control"]')

    def click_add_new_button(self):
        self.driver.find_element(*self.add_new_button).click()
        time.sleep(2)

    def select_identify_the_partnership_category(self):
        self.driver.find_element(*self.identify_the_partnership_category_field).click()
        time.sleep(2)
        self.driver.find_element(*self.identify_the_partnership_category_option).click()
        time.sleep(1)

    def insert_all_text_field(self, share_name_of_partner, partner_contribution, sci_role):
        share_name_of_partner_shadow_host = self.driver.find_element(*self.share_name_of_partner_shadow_host)
        share_name_of_partner_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', share_name_of_partner_shadow_host)
        share_name_of_partner_shadow_root.find_element(*self.share_name_of_partner_shadow_root).send_keys(share_name_of_partner)
        time.sleep(2)

        partner_contribution_shadow_host = self.driver.find_element(*self.partner_contribution_shadow_host)
        partner_contribution_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', partner_contribution_shadow_host)
        partner_contribution_shadow_root.find_element(*self.partner_contribution_shadow_root).send_keys(partner_contribution)
        time.sleep(2)

        sci_role_shadow_host = self.driver.find_element(*self.sci_role_shadow_host)
        sci_role_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', sci_role_shadow_host)
        sci_role_shadow_root.find_element(*self.sci_role_shadow_root).send_keys(sci_role)
        time.sleep(2)


    def save_as_draft(self):
        partnership_strategy_save_as_draft_shadow_host = self.driver.find_element(*self.partnership_strategy_save_as_draft_shadow_host)
        partnership_strategy_save_as_draft_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', partnership_strategy_save_as_draft_shadow_host)
        partnership_strategy_save_as_draft_shadow_root.find_element(*self.partnership_strategy_save_as_draft_shadow_root).click()
        time.sleep(2)

        partnership_strategy_yes_shadow_host = self.driver.find_element(*self.partnership_strategy_yes_shadow_host)
        partnership_strategy_yes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', partnership_strategy_yes_shadow_host)
        partnership_strategy_yes_shadow_root.find_element(*self.partnership_strategy_yes_shadow_root).click()
        time.sleep(3)
