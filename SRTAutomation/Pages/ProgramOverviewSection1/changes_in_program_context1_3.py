from selenium.webdriver.common.by import By
import time

class AddChangesInProgramContext1_3:

    def __init__(self, driver):
        self.driver = driver
        self.edit_button = (By.XPATH, '(//fluent-button[@title=\'Edit\'])[4]')
        self.changes_in_program_context_shadow_host = (By.XPATH, '(//fluent-text-area[@name="ContextDetails"])[1]')
        self.changes_in_program_context_shadow_root = (By.CSS_SELECTOR, '[class="control"]')
        self.save_as_draft_shadow_host = (By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
        self.save_as_draft_shadow_root = (By.CSS_SELECTOR, '[class="control"]')
        self.yes_shadow_host = (By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
        self.yes_shadow_root = (By.CSS_SELECTOR, '[class="control"]')

    def click_edit_button(self):
        self.driver.find_element(*self.edit_button).click()
        time.sleep(3)


    def insert_changes_in_program_context(self, changes_in_program_context):
        changes_in_program_context_shadow_host = self.driver.find_element(*self.changes_in_program_context_shadow_host)
        changes_in_program_context_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', changes_in_program_context_shadow_host)
        changes_in_program_context_shadow_root.find_element(*self.changes_in_program_context_shadow_root).send_keys(changes_in_program_context)
        time.sleep(1)

    def click_save_button(self):
        save_as_draft_shadow_host = self.driver.find_element(*self.save_as_draft_shadow_host)
        save_as_draft_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', save_as_draft_shadow_host)
        save_as_draft_shadow_root.find_element(*self.save_as_draft_shadow_root).click()
        time.sleep(3)

        yes_shadow_host = self.driver.find_element(*self.yes_shadow_host)
        yes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', yes_shadow_host)
        yes_shadow_root.find_element(*self.yes_shadow_root).click()
        time.sleep(2)
