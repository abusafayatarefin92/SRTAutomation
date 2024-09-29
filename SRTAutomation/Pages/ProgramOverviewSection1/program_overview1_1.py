from selenium.webdriver.common.by import By
import time

class AddProgramOverView1_1:

    def __init__(self, driver):
        self.driver = driver
        self.program_overview_shadow_host = (By.XPATH, '(//fluent-accordion-item[@class="rounded"])[1]')
        self.program_overview_open = (By.CSS_SELECTOR, '[class="button"]')
        self.program_overview_edit_button = (By.XPATH, '(//fluent-button[@title=\'Edit\'])[1]')
        self.program_themes_shadow_host = (By.XPATH, '(//fluent-text-field[@class="outline"])[1]') #(//fluent-text-field[@id='f3554d8b8'])[1]
        self.program_themes_shadow_root = (By.CSS_SELECTOR, '[id="control"]') #By.CSS_SELECTOR, "div.specific-class"
        self.program_themes_options = (By.XPATH, '(//div[@role="listbox"])[1]')
        self.Common_approches_shadow_host = (By.XPATH, '(//fluent-text-field[@class="outline"])[2]')
        self.Common_approches_shadow_root = (By.CSS_SELECTOR, '[id="control"]') #'[part="control"]'
        self.Common_approches_options = (By.XPATH, '(//div[@role="listbox"])[1]')
        self.group_child_engage_shadow_host = (By.XPATH, '(//fluent-text-field[@name="GroupChildEngage"])[1]')
        self.group_child_engage_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.girls_shadow_host = (By.XPATH, '(//fluent-number-field[@name="ReachGirls"])[1]')
        self.girls_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.boys_shadow_host = (By.XPATH, '(//fluent-number-field[@name="ReachBoys"])[1]')
        self.boys_shadow_root = (By.CSS_SELECTOR, '[id="control"]')
        self.save_as_draft_shadow_host = (By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
        self.save_as_draft_shadow_root = (By.CSS_SELECTOR, '[part="control"]')
        self.yes_shadow_host = (By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
        self.yes_shadow_root = (By.CSS_SELECTOR, '[class="control"]')

    def open_program_overview_section(self):
        program_overview_shadow_host = self.driver.find_element(*self.program_overview_shadow_host)
        program_overview_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_overview_shadow_host)
        program_overview_shadow_root.find_element(*self.program_overview_open).click()
        time.sleep(3)

    #Program Overview Form
    def click_program_overview_edit_button(self):
        self.driver.find_element(*self.program_overview_edit_button).click()
        time.sleep(3)

    def select_all_multiple_option_value(self):
        program_themes_shadow_host = self.driver.find_element(*self.program_themes_shadow_host)
        program_themes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_themes_shadow_host)
        program_themes_shadow_root.find_element(*self.program_themes_shadow_root).click()
        time.sleep(1)

        self.driver.find_element(*self.program_themes_options).click()
        time.sleep(1)

        Common_approches_shadow_host = self.driver.find_element(*self.Common_approches_shadow_host)
        Common_approches_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', Common_approches_shadow_host)
        Common_approches_shadow_root.find_element(*self.Common_approches_shadow_root).click()
        time.sleep(1)

        self.driver.find_element(*self.Common_approches_options).click()
        time.sleep(1)


    def insert_all_text_fields(self,
                               group_child_engage,
                               girls,
                               boys):
        group_child_engage_shadow_host = self.driver.find_element(*self.group_child_engage_shadow_host)
        group_child_engage_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', group_child_engage_shadow_host)
        group_child_engage_shadow_root.find_element(*self.group_child_engage_shadow_root).send_keys(group_child_engage)
        time.sleep(1)

        girls_shadow_host = self.driver.find_element(*self.girls_shadow_host)
        girls_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', girls_shadow_host)
        girls_shadow_root.find_element(*self.girls_shadow_root).send_keys(girls)
        time.sleep(1)

        boys_shadow_host = self.driver.find_element(*self.boys_shadow_host)
        boys_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', boys_shadow_host)
        boys_shadow_root.find_element(*self.boys_shadow_root).send_keys(boys)
        time.sleep(1)

    def click_save_button(self):
        save_as_draft_shadow_host = self.driver.find_element(*self.save_as_draft_shadow_host)
        save_as_draft_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', save_as_draft_shadow_host)
        save_as_draft_shadow_root.find_element(*self.save_as_draft_shadow_root).click()
        time.sleep(2)

        yes_shadow_host = self.driver.find_element(*self.yes_shadow_host)
        yes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', yes_shadow_host)
        yes_shadow_root.find_element(*self.yes_shadow_root).click()
        time.sleep(2)