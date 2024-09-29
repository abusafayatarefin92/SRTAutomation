import time
from Pages.add_plan import AddPlan
from Pages.ProgramOverviewSection1.program_overview1_1 import AddProgramOverView1_1
from Pages.ProgramOverviewSection1.changes_in_program_context1_3 import AddChangesInProgramContext1_3
from Pages.ProgramApproachSection2.program_implementation_strategy2_1 import AddProgramImplementationStrategy2_1
from Pages.ProgramApproachSection2.partnership_strategy2_2 import AddPartnershipStrategy2_2

class NewPlanSteps:
    def plan_steps(self, driver_function):
        add_new_plan = AddPlan(driver_function)
        add_new_plan.click_add_new_button()
        time.sleep(1)
        add_new_plan.select_period()
        time.sleep(1)

    def program_overview(self, driver_function):
        add_new_program_overview = AddProgramOverView1_1(driver_function)
        add_new_program_overview.open_program_overview_section()
        add_new_program_overview.click_program_overview_edit_button()
        time.sleep(1)
        add_new_program_overview.select_all_multiple_option_value()
        time.sleep(1)
        add_new_program_overview.insert_all_text_fields('Maecenas sed neque vel ex pharetra efficitur vel ac lacus.',
                                                        '10',
                                                        '11')
        time.sleep(1)
        add_new_program_overview.click_save_button()
        time.sleep(1)

        add_new_changes_in_program_context = AddChangesInProgramContext1_3(driver_function)
        add_new_changes_in_program_context.click_edit_button()
        time.sleep(1)
        add_new_changes_in_program_context.insert_changes_in_program_context('test')
        time.sleep(1)
        add_new_changes_in_program_context.click_save_button()
        time.sleep(1)

    def program_implementation_strategy(self, driver_function):
        add_program_implementation_strategy = AddProgramImplementationStrategy2_1(driver_function)
        add_program_implementation_strategy.open_program_approach_section()
        time.sleep(1)
        # add_program_implementation_strategy.click_edit_button()
        # time.sleep(1)
        # add_program_implementation_strategy.insert_program_implementation_strategy('Test')
        # time.sleep(1)
        # add_program_implementation_strategy.click_save_button()
        # time.sleep(1)

        add_paernership_strategy = AddPartnershipStrategy2_2(driver_function)
        add_paernership_strategy.click_add_new_button()
        time.sleep(1)
