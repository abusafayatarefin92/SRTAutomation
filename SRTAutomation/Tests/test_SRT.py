import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Steps.LoginSteps import LoginSteps
from Steps.AddNewPlanSteps import AddNewPlanSteps

@pytest.fixture()
def driver_function():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.close()
    driver.quit()

def test_SRT(driver_function):
    #Login
    login_steps = LoginSteps()
    login_steps.login_steps(driver_function)

    #Add new plan
    add_new_plan = AddNewPlanSteps()
    add_new_plan.add_new_plan_steps(driver_function)

