from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.maximize_window()
driver.get("https://srt.scibd.info/")
driver.implicitly_wait(time_to_wait= 2)

#Email
email_shadow_host = driver.find_element(By.CSS_SELECTOR,'[name="Input.Email"]')
time.sleep(2)
email_shadow_root = driver.execute_script('return arguments[0].shadowRoot',
                                          email_shadow_host)
time.sleep(2)
email_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com')
time.sleep(2)

#Password
password_shadow_host = driver.find_element(By.CSS_SELECTOR,
                                                   '[name="Input.Password"]')
time.sleep(2)
password_shadow_root = driver.execute_script('return arguments[0].shadowRoot',
                                             password_shadow_host)
time.sleep(2)
password_shadow_root.find_element(By.CSS_SELECTOR,
                         '[id="control"]').send_keys('12345')
time.sleep(2)

#Log in
login_shadow_host = driver.find_element(By.XPATH,
                                                   '(//fluent-button[@type=\'submit\'])[1]')
time.sleep(2)
login_shadow_root = driver.execute_script('return arguments[0].shadowRoot',
                                          login_shadow_host)
time.sleep(2)
login_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()
time.sleep(5)

#Add new button
driver.find_element(By.XPATH, '(//fluent-anchor[@class=\'accent\'])[1]').click()
time.sleep(5)

#Select Period
driver.find_element(By.XPATH, '(//fluent-select[@id=\'Period\'])[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//fluent-option[@value="2022-2024"])[1]').click()
time.sleep(3)

#Open the Section 1: Program Overview
program_overview_shadow_host = driver.find_element(By.XPATH,
                                                   '(//fluent-accordion-item[@class="rounded"])[1]')
time.sleep(2)
program_overview_shadow_root = driver.execute_script('return arguments[0].shadowRoot',
                                          program_overview_shadow_host)
time.sleep(2)
program_overview_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()
time.sleep(3)

driver.find_element(By.XPATH, '(//fluent-button[@title=\'Edit\'])[1]').click()
time.sleep(3)

driver.find_element(By.XPATH, '(//*[name()=\'svg\'][@role=\'button\'])[1]').click()
time.sleep(1)

driver.find_element(By.XPATH, '(//fluent-option[@role="option"])[1]').click()
time.sleep(1)

program_theme_shadow_host = driver.find_element(By.XPATH,
                                                   '(//fluent-text-field[@class="outline"])[1]')
time.sleep(2)
program_theme_shadow_root = driver.execute_script('return arguments[0].shadowRoot',
                                          program_theme_shadow_host)
time.sleep(2)
program_theme_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()
time.sleep(3)

driver.find_element(By.XPATH, '(//fluent-option[@role="option"])[2]').click()
time.sleep(2)

driver.close()
driver.quit()
