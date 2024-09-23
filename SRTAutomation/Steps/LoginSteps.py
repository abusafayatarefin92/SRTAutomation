import time
from Pages.login_page import LoginPage

class LoginSteps:

    def login_steps(self, driver_function):
        login_page = LoginPage(driver_function)
        login_page.open_page_and_give_credentials('https://srt.scibd.info/',
                                                  'TASM@gmail.com',
                                                  '12345')
        time.sleep(1)
        login_page.click_login_button()
        time.sleep(5)
