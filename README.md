# SRTAutomation
It is an automation project of SRT (Strategic Reporting Tool) using Selenium &amp; python

How to locate a web element inside shadow dom of fluent ui by using selenium & python:
# Locate the shadow host element
email_shadow_host = driver.find_element(By.CSS_SELECTOR,'[name="Input.Email"]')

# Access the shadow root
email_shadow_root = driver.execute_script('return arguments[0].shadowRoot', email_shadow_host)

# Locate the element inside the shadow DOM and Perform actions on the element
email_shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com') # Example action

CSS selectors can also be used to target specific elements based on their attributes, classes, or hierarchy.
# Find the specific <div> element by its class
specific_div = driver.find_element(By.CSS_SELECTOR, "div.specific-class")

# Find the specific <div> element by its ID
specific_div = driver.find_element(By.CSS_SELECTOR, "div#specific-id")

# Find the specific <div> element by its position within a parent
specific_div = driver.find_element(By.CSS_SELECTOR, "div.parent-class > div:nth-child(2)")

The “element not interactable” exception in Selenium Python can be frustrating, but there are several strategies to troubleshoot and resolve this issue. Here are some common causes and solutions:

Common Causes
Element is Hidden: The element is present in the DOM but not visible.
Element is Covered: Another element is overlaying the target element.
Timing Issues: The element is not yet fully loaded or rendered.
Element is Disabled: The element is present but not enabled for interaction.
Element is Outside the Viewport: The element is not within the visible area of the browser window.

element = driver.find_element(By.ID, "element_id")
driver.execute_script("arguments[0].click();", element)

Use ActionChains to Move to the Element
ActionChains can be used to move to the element before interacting with it.
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "element_id")
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
