import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Steps.LoginSteps import LoginSteps
from Steps.NewPlanSteps import NewPlanSteps

@pytest.fixture()
def driver_function():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)

    yield driver

    driver.close()
    driver.quit()

def test_SRT(driver_function):
    #Login
    login_steps = LoginSteps()
    login_steps.login_steps(driver_function)

    #Add new plan
    add_new_plan = NewPlanSteps()
    add_new_plan.plan_steps(driver_function)
    add_new_plan.program_overview(driver_function)
    add_new_plan.program_implementation_strategy(driver_function)
    time.sleep(10)
