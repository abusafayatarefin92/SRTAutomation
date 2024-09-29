from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_shadow_host = (By.CSS_SELECTOR, '[name="Input.Email"]')
        self.email_textbox = (By.CSS_SELECTOR, '[id="control"]')
        self.password_shadow_host = (By.CSS_SELECTOR, '[name="Input.Password"]')
        self.password_textbox = (By.CSS_SELECTOR, '[id="control"]')
        self.login_shadow_host = (By.XPATH, '(//fluent-button[@type=\'submit\'])[1]')
        self.login_button = (By.CSS_SELECTOR, '[class="control"]')

    def open_page_and_give_credentials(self,
                                       url,
                                       email,
                                       password):
        #Open the page
        self.driver.get(url)
        time.sleep(1)

        #Enter email
        email_shadow_host = self.driver.find_element(*self.email_shadow_host)
        time.sleep(1)
        email_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', email_shadow_host)
        time.sleep(1)
        email_shadow_root.find_element(*self.email_textbox).send_keys(email)
        time.sleep(1)

        #Enter password
        password_shadow_host = self.driver.find_element(*self.password_shadow_host)
        time.sleep(1)
        password_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', password_shadow_host)
        time.sleep(1)
        password_shadow_root.find_element(*self.password_textbox).send_keys(password)
        time.sleep(1)

    def click_login_button(self):
        login_shadow_host = self.driver.find_element(*self.login_shadow_host)
        time.sleep(1)
        login_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', login_shadow_host)
        time.sleep(1)
        login_shadow_root.find_element(*self.login_button).click()
        time.sleep(1)