# SRTAutomation
It is an automation project of SRT (Strategic Reporting Tool) using Selenium &amp; python

How to locate a web element inside shadow dom of fluent ui by using selenium & python:
# Locate the shadow host element
email_shadow_host = driver.find_element(By.CSS_SELECTOR,'[name="Input.Email"]')

# Access the shadow root
email_shadow_root = driver.execute_script('return arguments[0].shadowRoot', email_shadow_host)

# Locate the element inside the shadow DOM and Perform actions on the element
email_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com') # Example action
