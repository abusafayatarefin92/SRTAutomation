from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Install driver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()

#Open the app
driver.get("https://srt.scibd.info/")
driver.implicitly_wait(time_to_wait= 2)

#Email
email_shadow_host = driver.find_element(By.CSS_SELECTOR,'[name="Input.Email"]')
time.sleep(2)
email_shadow_root = driver.execute_script('return arguments[0].shadowRoot',email_shadow_host)
time.sleep(2)
email_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com')
time.sleep(2)

#Password
password_shadow_host = driver.find_element(By.CSS_SELECTOR,'[name="Input.Password"]')
time.sleep(2)
password_shadow_root = driver.execute_script('return arguments[0].shadowRoot',password_shadow_host)
time.sleep(2)
password_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('12345')
time.sleep(2)

#Log in
login_shadow_host = driver.find_element(By.XPATH,'(//fluent-button[@type=\'submit\'])[1]')
time.sleep(2)
login_shadow_root = driver.execute_script('return arguments[0].shadowRoot',login_shadow_host)
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
program_overview_shadow_host = driver.find_element(By.XPATH,'(//fluent-accordion-item[@class="rounded"])[2]')
time.sleep(2)
program_overview_shadow_root = driver.execute_script('return arguments[0].shadowRoot',program_overview_shadow_host)
time.sleep(2)
program_overview_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()
time.sleep(3)

#Edit Program Overview
# driver.find_element(By.XPATH, '(//fluent-button[@title=\'Edit\'])[2]').click()
# time.sleep(3)
#
# program_themes_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@class="outline"])[1]')
# program_themes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_themes_shadow_host)
# program_themes_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').click()
# time.sleep(1)
#
# driver.find_element(By.XPATH, '(//div[@role="listbox"])[1]').click()
# time.sleep(1)
#
# Common_approches_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@class="outline"])[2]')
# Common_approches_shadow_root = driver.execute_script('return arguments[0].shadowRoot', Common_approches_shadow_host)
# Common_approches_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').click()
# time.sleep(1)
#
# driver.find_element(By.XPATH, '(//div[@role="listbox"])[1]').click()
# time.sleep(1)
#
# group_child_engage_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@name="GroupChildEngage"])[1]')
# group_child_engage_shadow_root = driver.execute_script('return arguments[0].shadowRoot', group_child_engage_shadow_host)
# group_child_engage_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Maecenas sed neque vel ex pharetra efficitur vel ac lacus.')
# time.sleep(1)
#
# girls_shadow_host = driver.find_element(By.XPATH, '(//fluent-number-field[@name="ReachGirls"])[1]')
# girls_shadow_root = driver.execute_script('return arguments[0].shadowRoot', girls_shadow_host)
# girls_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('10')
# time.sleep(1)
#
# boys_shadow_host = driver.find_element(By.XPATH, '(//fluent-number-field[@name="ReachBoys"])[1]')
# boys_shadow_root = driver.execute_script('return arguments[0].shadowRoot', boys_shadow_host)
# boys_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('11')
# time.sleep(1)
#
# save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
# save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', save_as_draft_shadow_host)
# save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
# time.sleep(2)
#
# yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
# yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', yes_shadow_host)
# yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()

# #Edit 1.3 Changes in Program Context
# driver.find_element(By.XPATH, '(//fluent-button[@title=\'Edit\'])[4]').click()

#Add Pernership Strategy
driver.find_element(By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[1]').click()
time.sleep(2)

# # Locate the drop-down element
# dropdown = driver.find_element(By.XPATH, "(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]")
#
# # Create a Select object
# select = Select(dropdown)
#
# # Select an option by visible text
# select.select_by_visible_text("Strategic (i.e. alliances, government and civil society networks)")

# driver.find_element(By.XPATH, "(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]").click()
# time.sleep(2)

# identify_partnership_category_shadow_host = driver.find_element(By.XPATH, "(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]")
# identify_partnership_category_shadow_root = driver.execute_script('return arguments[0].shadowRoot', identify_partnership_category_shadow_host)
# identify_partnership_category_shadow_root.find_element(By.CSS_SELECTOR, 'div.control').click()

# driver.find_element(By.XPATH, '(//div[@role="listbox"])[1]').click()

identify_partnership_category_shadow_host = driver.find_element(By.XPATH, '(//fluent-select[@role="combobox"])[1]')
identify_partnership_category_shadow_root = driver.execute_script('return arguments[0].shadowRoot', identify_partnership_category_shadow_host)
# identify_partnership_category_shadow_root.find_element(By.CSS_SELECTOR, 'div.listbox')

element = identify_partnership_category_shadow_root.find_element(By.CSS_SELECTOR, 'div.listbox')
driver.execute_script("arguments.click();", element)


# # Wait for the fluent-select element to be present
# fluent_select = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]'))
# )
#
# # Find all fluent-option elements and select the desired one
# options = fluent_select.find_elements(By.TAG_NAME, 'fluent-option')
# for option in options:
#     if option.text == 'Strategic (i.e. alliances, government and civil society networks)':
#         option.click()
#         break

# # Wait for the fluent-select element to be clickable and click it
# fluent_select = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]')) #fluent-dialog, fluent-select
# )
# fluent_select.click()

# # Find the desired option (e.g., by text or value)
# # Options might be in a child element like a list (e.g., fluent-option)
# desired_option = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "(//fluent-option[@value=\"1\"])[1]"))
# )
#
# # Click the desired option
# desired_option.click()

# driver.find_element(By.CSS_SELECTOR, 'div.listbox').click()

share_name_of_partner_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@class="valid outline required"])[1]')
share_name_of_partner_shadow_root = driver.execute_script('return arguments[0].shadowRoot', share_name_of_partner_shadow_host)
share_name_of_partner_shadow_root.find_element(By.CSS_SELECTOR, 'input.control').send_keys('test')

time.sleep(10)
driver.close()
driver.quit()
