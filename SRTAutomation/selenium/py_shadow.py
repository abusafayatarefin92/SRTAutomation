from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from pyshadow.main import Shadow

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
shadow = Shadow(driver)

driver.maximize_window()
driver.get("https://srt.scibd.info/")
driver.implicitly_wait(time_to_wait= 2)

#Email
shadow_host = shadow.find_element(By.CSS_SELECTOR, '[name="Input.Email"]')
time.sleep(2)
shadow_root = shadow_host.shadow_root
time.sleep(2)
shadow_root.find_element(By.CSS_SELECTOR, '[id="control"]').send_keys('TASM@gmail.com')

time.sleep(5)

driver.close()
driver.quit()