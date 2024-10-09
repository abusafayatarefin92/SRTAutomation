from pydoc import describe

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
driver.implicitly_wait(time_to_wait= 20)

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

# #Open the Section 1: Program Overview
# open_program_overview_shadow_host = driver.find_element(By.XPATH,'(//fluent-accordion-item[@class="rounded"])[1]')
# open_program_overview_shadow_root = driver.execute_script('return arguments[0].shadowRoot',open_program_overview_shadow_host)
# open_program_overview_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()
# time.sleep(3)
#
# #Edit 1.1. Program Overview
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
# program_overview_save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
# program_overview_save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_overview_save_as_draft_shadow_host)
# program_overview_save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
# time.sleep(2)
#
# program_overview_yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
# program_overview_yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_overview_yes_shadow_host)
# program_overview_yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()
# time.sleep(3)
#
# #Edit 1.3 Changes in Program Context
# driver.find_element(By.XPATH, '(//fluent-button[@title=\'Edit\'])[4]').click()
# time.sleep(1)
#
# context_details_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="ContextDetails"])[1]')
# context_details_shadow_root = driver.execute_script('return arguments[0].shadowRoot', context_details_shadow_host)
# context_details_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
# time.sleep(1)
#
# program_context_save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
# program_context_save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_context_save_as_draft_shadow_host)
# program_context_save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
# time.sleep(2)
#
# program_context_yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
# program_context_yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_context_yes_shadow_host)
# program_context_yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()
# time.sleep(3)
#
# #Close the Section 1: Program Overview
# close_program_overview_shadow_host = driver.find_element(By.XPATH,'(//fluent-accordion-item[@class="rounded expanded"])[1]')
# close_program_overview_shadow_root = driver.execute_script('return arguments[0].shadowRoot',close_program_overview_shadow_host)
# close_program_overview_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()
# time.sleep(3)

#Open the Section 2: Program Approach
open_program_approach_shadow_host = driver.find_element(By.XPATH,'(//fluent-accordion-item[@class="rounded"])[2]')
open_program_approach_shadow_root = driver.execute_script('return arguments[0].shadowRoot',open_program_approach_shadow_host)
open_program_approach_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()
time.sleep(3)

#Edit 2.1 Program Implementation Strategy
driver.find_element(By.XPATH, '(//fluent-button[@title=\'Edit\'])[5]').click()
time.sleep(3)

outcome_details_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="OutcomeDetails"])[1]')
outcome_details_shadow_root = driver.execute_script('return arguments[0].shadowRoot',outcome_details_shadow_host)
outcome_details_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(2)

program_implementation_strategy_save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
program_implementation_strategy_save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_implementation_strategy_save_as_draft_shadow_host)
program_implementation_strategy_save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
time.sleep(2)

program_implementation_strategy_yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
program_implementation_strategy_yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', program_implementation_strategy_yes_shadow_host)
program_implementation_strategy_yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()
time.sleep(3)

#Add Pernership Strategy
driver.find_element(By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, "(//fluent-select[@class=\"valid w-full collapsible outline required\"])[1]").click()
time.sleep(2)

driver.find_element(By.XPATH, '(//fluent-option[@value="2"])[1]').click()
time.sleep(1)

share_name_of_partner_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@class="valid outline required"])[1]')
share_name_of_partner_shadow_root = driver.execute_script('return arguments[0].shadowRoot', share_name_of_partner_shadow_host)
share_name_of_partner_shadow_root.find_element(By.CSS_SELECTOR, 'input.control').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(2)

partner_contribution_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="PartnerContribution"])[1]')
partner_contribution_shadow_root = driver.execute_script('return arguments[0].shadowRoot', partner_contribution_shadow_host)
partner_contribution_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(2)

sci_role_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="SCIRole"])[1]')
sci_role_shadow_root = driver.execute_script('return arguments[0].shadowRoot', sci_role_shadow_host)
sci_role_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(2)

partnership_strategy_save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
partnership_strategy_save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', partnership_strategy_save_as_draft_shadow_host)
partnership_strategy_save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
time.sleep(2)

partnership_strategy_yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
partnership_strategy_yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', partnership_strategy_yes_shadow_host)
partnership_strategy_yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()

#Add 2.3 Risk Mitigation Strategy
# # Scroll to the Element: Sometimes, scrolling to the element can help.
# element = driver.find_element(By.ID, "your_element_id")
# driver.execute_script("arguments.scrollIntoView(true);", element)
# element.click()

risk_mitigation_strategy_element = driver.find_element(By.XPATH, '(//fluent-button[@type=\'button\'][normalize-space()=\'Add New\'])[2]')
driver.execute_script("arguments.scrollIntoView(true);", risk_mitigation_strategy_element)
risk_mitigation_strategy_element.click()
time.sleep(3)

identified_risk_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-field[@name="IdentifiedRisk"])[1]')
identified_risk_shadow_root = driver.execute_script('return arguments[0].shadowRoot', identified_risk_shadow_host)
identified_risk_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(1)

description_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="Description"])[1]')#(//fluent-text-area[@id='f32590e76'])[1]
description_shadow_root = driver.execute_script('return arguments[0].shadowRoot', description_shadow_host)
description_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(1)

activities_shadow_host = driver.find_element(By.XPATH, '(//fluent-text-area[@name="Activities"])[1]')#(//fluent-text-area[@id='f23bebf68'])[1]
activities_shadow_root = driver.execute_script('return arguments[0].shadowRoot', activities_shadow_host)
activities_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('Lorem ipsum odor amet, consectetuer adipiscing elit.')
time.sleep(1)

risk_mitigation_strategy_save_as_draft_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[normalize-space()=\'Save as Draft\'])[1]')
risk_mitigation_strategy_save_as_draft_shadow_root = driver.execute_script('return arguments[0].shadowRoot', risk_mitigation_strategy_save_as_draft_shadow_host)
risk_mitigation_strategy_save_as_draft_shadow_root.find_element(By.CSS_SELECTOR, '[part="control"]').click()
time.sleep(2)

risk_mitigation_strategy_yes_shadow_host = driver.find_element(By.XPATH, '(//fluent-button[@title=\'Yes\'])[1]')
risk_mitigation_strategy_yes_shadow_root = driver.execute_script('return arguments[0].shadowRoot', risk_mitigation_strategy_yes_shadow_host)
risk_mitigation_strategy_yes_shadow_root.find_element(By.CSS_SELECTOR, '[class="control"]').click()

#Close the Section 2: Program Approach
close_program_approach_shadow_host = driver.find_element(By.XPATH,'(//fluent-accordion-item[@class="rounded expanded"])[1]')
close_program_approach_shadow_root = driver.execute_script('return arguments[0].shadowRoot',close_program_approach_shadow_host)
close_program_approach_shadow_root.find_element(By.CSS_SELECTOR, '[class="button"]').click()

time.sleep(10)
driver.close()
driver.quit()
