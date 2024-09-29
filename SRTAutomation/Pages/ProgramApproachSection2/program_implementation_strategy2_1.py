from selenium.webdriver.common.by import By
import time

class AddProgramImplementationStrategy2_1:

    def __init__(self, driver):
        self.driver = driver
        self.program_approach_section_open_shadow_host = (By.XPATH, '(//fluent-accordion-item[@class="rounded"])[2]')
        self.program_approach_section_open_shadow_root = (By.CSS_SELECTOR, '[part="button"]')
        self.edit_button = (By.XPATH, '(//fluent-button[@title=\'Edit\'])[5]')
        self.program_implementation_strategy_shadow_host = (By.XPATH, '(//fluent-text-area[@class="valid outline resize-vertical required"])[1]')
        self.program_implementation_strategy_shadow_root = (By.CSS_SELECTOR, '[class="control"]')
        self.save_as_draft_shadow_host = (By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
        self.save_as_draft_shadow_root = (By.CSS_SELECTOR, '[class="control"]')
        self.yes_shadow_host = (By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
        self.yes_shadow_root = (By.CSS_SELECTOR, '[class="control"]')

    def open_program_approach_section(self):
        program_approach_section_open_shadow_host = self.driver.find_element(*self.program_approach_section_open_shadow_host)
        program_approach_section_open_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_approach_section_open_shadow_host)
        program_approach_section_open_shadow_root.find_element(*self.program_approach_section_open_shadow_root).click()
        time.sleep(3)

    def click_edit_button(self):
        self.driver.find_element(*self.edit_button).click()
        time.sleep(3)

    def insert_program_implementation_strategy(self, program_implementation_strategy):
        program_implementation_strategy_shadow_host = self.driver.find_element(*self.program_implementation_strategy_shadow_host)
        program_implementation_strategy_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', program_implementation_strategy_shadow_host)
        program_implementation_strategy_shadow_root.find_element(*self.program_implementation_strategy_shadow_root).send_keys(program_implementation_strategy)
        time.sleep(3)

    def click_save_button(self):
        save_as_draft_shadow_host = self.driver.find_element(*self.save_as_draft_shadow_host)
        save_as_draft_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', save_as_draft_shadow_host)
        save_as_draft_shadow_root.find_element(*self.save_as_draft_shadow_root).click()
        time.sleep(2)

        yes_shadow_host = self.driver.find_element(*self.yes_shadow_host)
        yes_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', yes_shadow_host)
        yes_shadow_root.find_element(*self.yes_shadow_root).click()
        time.sleep(2)
