from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

edge_driver.maximize_window()
edge_driver.get("https://srt.scibd.info/")
edge_driver.implicitly_wait(time_to_wait= 2)

#Email
email_shadow_host = edge_driver.find_element(By.CSS_SELECTOR,
                                                   '[name="Input.Email"]')
time.sleep(2)
email_shadow_root = edge_driver.execute_script('return arguments[0].shadowRoot',
                                               email_shadow_host)
time.sleep(2)
email_shadow_root.find_element(By.CSS_SELECTOR,
                         '[id="control"]').send_keys('TASM@gmail.com')
time.sleep(2)

#Password
password_shadow_host = edge_driver.find_element(By.CSS_SELECTOR,
                                                   '[name="Input.Password"]')
time.sleep(2)
password_shadow_root = edge_driver.execute_script('return arguments[0].shadowRoot',
                                               password_shadow_host)
time.sleep(2)
password_shadow_root.find_element(By.CSS_SELECTOR,
                         '[id="control"]').send_keys('12345')
time.sleep(2)

#Log in
login_shadow_host = edge_driver.find_element(By.XPATH,
                                                   '(//fluent-button[@type=\'submit\'])[1]')
time.sleep(2)
login_shadow_root = edge_driver.execute_script('return arguments[0].shadowRoot',
                                               login_shadow_host)
time.sleep(2)
login_shadow_root.find_element(By.CSS_SELECTOR,
                         '[class="control"]').click()
time.sleep(5)

edge_driver.close()
edge_driver.quit()
