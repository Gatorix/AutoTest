from base.manager.base_system import DepartmentAndStaffBase, SystemBinBase
from base.base_case import BaseTestCase


class DepartmentAndStaffPage(DepartmentAndStaffBase, BaseTestCase):
    def click_department_and_staff_normal_button(self, button_name):
        self.click(self.department_and_staff_normal_button(button_name))
        self.wait(1)

    def type_new_stuff_input(self, label, text):
        self.type(self.new_staff_input_boxes(label), text)

    def click_new_stuff_buttons(self, button):
        self.click(self.new_staff_buttons(button))

    def click_new_stuff_alert(self):
        self.click(self.new_staff_alert())

    def search_staff(self, staff):
        self.type(self.search_staff_input_box(), staff)
        self.wait(1)
        self.click(self.search_staff_button())
        self.wait(1)

    def click_list_checkbox(self, staff):
        self.click(self.list_checkbox(staff))
        self.wait(0.5)

    def click_conform_delete_buttons(self, button):
        self.click(self.conform_delete_buttons(button))


class SystemBinPage(SystemBinBase, BaseTestCase):
    def type_to_system_bin_inputs_by_label(self, label, text):
        self.type(self.system_bin_inputs_by_label(label), text)

    def click_system_bin_buttons(self, button):
        self.click(self.system_bin_buttons(button))

    def click_system_bin_check_all_span(self):
        self.click(self.system_bin_check_all_span())

    def click_system_bin_conform_delete(self, button):
        self.click(self.system_bin_conform_delete(button))

    def type_to_system_bin_conform_again_input(self):
        self.type(self.system_bin_conform_again_input(), '我已清楚了解将产生的后果')

    def click_system_bin_conform_again_button(self):
        self.click(self.system_bin_conform_again_button())

    def click_system_bin_button_in_line_by_company(self, company, button):
        self.click(self.system_bin_button_in_line_by_company(company, button))

    def click_system_bin_conform_recover_buttons(self, button='确 定'):
        self.click(self.system_bin_conform_recover_buttons(button))
