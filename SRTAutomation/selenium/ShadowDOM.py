from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# driver.find_element(By.XPATH, '(//*[name()=\'svg\'][@role=\'button\'])[1]').click()
# time.sleep(1)

program_themes_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@aria-label="Program Themes"])[1]')
program_themes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_themes_shadow_host)
program_themes_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').click()
time.sleep(1)

# program_themes_option1_shadow_host = driver.find_element(By.XPATH, '(//fluent-option[@role="option"])[1]')
# program_themes_option1_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_themes_option1_shadow_host)
# program_themes_option1_shadow_root_element = program_themes_option1_shadow_root.find_element(By.CSS_SELECTOR, 'span.content')
# driver.execute_script("arguments[0].click();", program_themes_option1_shadow_root_element)

program_themes_option_element = driver.find_element(By.XPATH, '(//fluent-option[@role="option"])[1]')
driver.execute_script("arguments[0].click();", program_themes_option_element)
time.sleep(1)


# Wait for the element to be visible and enabled
# element = WebDriverWait(driver, 10).until(
#     # EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="content"]'))
#     EC.element_to_be_clickable((By.XPATH, '//span[@class="content"]'))
# )
# element.click()
# time.sleep(1)

# program_themes_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@aria-label="Program Themes"])[1]')
# program_themes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_themes_shadow_host)
# program_themes_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').click()
# time.sleep(1)
#
# program_themes_option2_shadow_host = driver.find_element(By.XPATH, '(//fluent-option[@role="option"])[2]')
# program_themes_option2_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_themes_option2_shadow_host)
# program_themes_option2_shadow_root.find_element(By.CSS_SELECTOR, '[class="content"]').click()
# time.sleep(1)


time.sleep(5)
driver.close()
driver.quit()
