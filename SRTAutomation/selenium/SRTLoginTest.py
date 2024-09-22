from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

edge_driver.maximize_window()
edge_driver.get("https://srt.scibd.info/")
edge_driver.implicitly_wait(time_to_wait= 2)

def expand_shadow_element(edge_driver, element):
    shadow_root = edge_driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

host_element = edge_driver.find_element(By.CSS_SELECTOR,
                                                   '[name="Input.Email"]')
time.sleep(2)
shadow_element1 = expand_shadow_element(edge_driver, host_element)
time.sleep(2)
shadow_element1.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com')
# shadow_element1.find_element(By.CSS_SELECTOR, '[class="fluent-input-label"]').text
# edge_driver.find_element(By.XPATH, '')
# inner_element = shadow_element1.find_element(By.CSS_SELECTOR, '[name="Input.Email"]')
# time.sleep(2)
# shadow_element2 = expand_shadow_element(edge_driver, inner_element)
# time.sleep(2)
# shadow_element2.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com')
# shadow_root1 = edge_driver.execute_script('return arguments[0].shadowRoot',
#                                                credentials_shadow_host)
# time.sleep(2)
# email_shadow_root.find_element(By.CSS_SELECTOR, '[name="Input.Email"]').send_keys('TASM@gmail.com')
# find_email_element.click()
# email_shadow_root.find_element(By.CSS_SELECTOR,
#                                '[id="control"]').send_keys('TASM@gmail.com')
time.sleep(3)

edge_driver.close()
edge_driver.quit()
