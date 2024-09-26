import time
from time import sleep

from Pages.add_plan import AddPlan

class AddNewPlanSteps:
    def add_new_plan_steps(self, driver_function):
        add_new_plan = AddPlan(driver_function)
        add_new_plan.click_add_new_button()
        time.sleep(1)
        add_new_plan.select_period()
        time.sleep(1)
        add_new_plan.open_program_overview_section()
        time.sleep(1)
        add_new_plan.click_program_overview_edit_button()
        time.sleep(1)
        add_new_plan.select_program_themes()
        time.sleep(1)
