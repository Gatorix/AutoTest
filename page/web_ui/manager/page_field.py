from base.manager.base_field import FieldBase
from base.base_case import BaseTestCase


class FieldPage(FieldBase, BaseTestCase):
    def click_home_button(self, button_name):
        self.click(self.field_home_button(button_name))
        self.wait(3)

    def input_task_type(self, text):
        self.type(self.task_type_input(), text)

    def click_new_task_button(self):
        self.click(self.new_task_type_button())

    def click_task_operate_button(self, side, operate, index, text=''):
        if operate == 'input':
            self.send_keys(self.task_type_operate(side, operate, index), text)
        else:
            self.click(self.task_type_operate(side, operate, index))
        self.wait(0.5)

    def click_checkbox_in_table(self, task_name):
        self.click(self.checkbox_in_table_by_task_name(task_name))
        self.wait(0.5)

    def search_task_by_task_detail(self, task_detail):
        self.type(self.search_input(), task_detail)
        self.wait(0.5)
        self.click(self.search_button())
        self.wait(0.5)

    def new_task_customer(self, customer_name):
        self.type(self.new_task_input('客户'), customer_name)
        self.wait(1)
        self.click(self.new_task_select_customer(customer_name))

    def new_task_type(self, task_type):
        self.click(self.new_task_input('任务类型'))
        self.click(self.new_task_select_task_type(task_type))

    def new_task_input_details(self, details):
        self.type(self.new_task_input_task_detail(), details)

    def new_task_click_button(self, button_name):
        self.click(self.new_task_buttons(button_name))
        self.wait(0.5)

    def distribution_task_click_buttons(self, button_name):
        self.click(self.distribution_task_buttons(button_name))

    def distribution_task_select_org_and_employee(self, org, employee):
        self.click(self.distribution_task_input('部门'))
        self.click(self.distribution_task_select_org(org))
        self.click(self.distribution_task_input('职员'))
        self.click(self.distribution_task_select_employee(employee))

    def cancel_task_input(self, text):
        self.type(self.cancel_task_textarea(), text)

    def cancel_task_click_button(self, button_name):
        self.click(self.cancel_task_buttons(button_name))

    def close_task_input(self, text):
        self.type(self.close_task_textarea(), text)

    def close_task_click_button(self, button_name):
        self.click(self.close_task_buttons(button_name))

    def finish_task_input(self, text):
        self.type(self.finish_task_textarea(), text)

    def finish_task_click_button(self, button_name):
        self.click(self.finish_task_buttons(button_name))

    def click_filed_head_filter(self, label, span):
        self.click(self.filed_head_filter(label, span))
