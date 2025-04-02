from selenium.common import ElementNotVisibleException

from base.manager.base_customer import CustomerBase, LostManageBase
from base.base_case import BaseTestCase


class CustomerPage(CustomerBase, BaseTestCase):
    def click_table_buttons(self, company_name, button_name):
        self.click(self.customer_table_button(company_name, button_name))
        self.wait(0.5)

    def click_normal_button(self, button_name):
        self.click(self.customer_buttons(button_name))

    def click_customer_normal_button(self, button_name):
        self.click(self.customer_buttons(button_name))

    def click_dropdown_buttons(self, button_name, drop_down):
        self.click_normal_button(button_name)
        self.wait(0.5)
        self.click(self.customer_dropdown_buttons(drop_down))
        self.wait(1)

    def click_customer_dropdown_buttons(self, button_name, drop_down):
        self.click_customer_normal_button(button_name)
        self.wait(0.5)
        self.click(self.customer_dropdown_buttons(drop_down))
        self.wait(1)

    def search_customer(self, company_name):
        self.type(self.customer_middle_input('客户名称'), company_name)
        self.wait(1)
        self.click(self.customer_middle_search_button())
        self.wait(1)

    def click_customer_table_checkbox(self, company_name):
        self.click(self.customer_table_checkbox(company_name))
        self.wait(1)

    def click_customer_list_select_all_span(self):
        self.click(self.customer_list_select_all_span())

    def get_text_from_customer_list_total_line(self):
        return self.get_text(self.customer_list_total_line())

    def customer_switch_show_num(self, text):
        self.click(self.customer_list_show_num_input())
        self.click(self.customer_list_show_num_popper(text))
        self.wait(3)

    def close_ads(self):
        try:
            if self.is_element_visible(self.customer_ads()):
                self.click(self.customer_ads())
            else:
                pass
        except ElementNotVisibleException:
            pass
        finally:
            self.wait(0.5)

    def input_new_customer_name(self, name):
        self.type(self.new_customer_input(), name)

    def select_new_customer_type(self, customer_type):
        self.click(self.new_customer_type())
        self.wait(0.5)
        self.click(self.new_customer_type_selector(customer_type))

    def click_new_customer_more_info_button(self):
        self.click(self.new_customer_more_info_button())

    def type_to_new_customer_more_info_inputs_by_label(self, label, text):
        self.type(self.new_customer_more_info_inputs_by_label(label), text)

    def input_contract_details(self, start_period, end_period):
        self.click_new_customer_more_info_button()
        if all([self.is_element_visible(self.new_customer_more_info_inputs_by_label('合同开始日期')),
                self.is_element_visible(self.new_customer_more_info_inputs_by_label('合同结束日期'))]):
            self.type_to_new_customer_more_info_inputs_by_label('合同开始日期', f'{start_period}\n')
            self.type_to_new_customer_more_info_inputs_by_label('合同结束日期', f'{end_period}\n')

    def input_tax_info(self, tax_list, properties='一般纳税人'):
        self.click(self.new_customer_more_info_button())
        self.select_tax_properties(properties)
        for i, _ in enumerate(tax_list):
            self.click(self.new_customer_more_info_tax_add_line_button())
            self.click(self.new_customer_more_info_tax_type_table(i + 1))
            self.click(self.new_customer_more_info_popper_span(_))

    def select_tax_properties(self, properties):
        self.click(self.new_customer_more_info_tax_properties())
        self.click(self.new_customer_more_info_popper_span(properties))

    def click_delete_followup_record(self, record):
        self.click(self.delete_followup_record(record))
        self.wait(1)

    def is_customer_exist(self):
        return self.is_element_visible(self.customer_exist())

    def click_conform_delete_followup_record(self):
        self.click(self.conform_delete_followup_record())

    def click_new_customer_button(self, button_name):
        self.click(self.new_customer_buttons(button_name))
        self.wait(1)

    def click_delete_customer_button(self, button_name):
        self.wait(1)
        self.click(self.delete_customer_buttons(button_name))

    def click_mark_conform(self):
        self.click(self.mark_conform())

    def input_follow_up(self, text):
        self.type(self.follow_up_detail(), text)

    def click_follow_up_button(self, button):
        self.click(self.followup_detail_buttons(button))

    def click_close_followup(self):
        self.click(self.close_followup())

    def click_grant_permission_buttons(self, button):
        self.click(self.grant_permission_buttons(button))

    def click_close_grant_permission(self):
        self.click(self.close_grant_permission())

    def click_tax_box_buttons(self, button):
        self.click(self.tax_box_buttons(button))

    def click_customer_manager_buttons(self, button):
        self.click(self.customer_manager_buttons(button))

    def click_close_customer_manager(self):
        self.click(self.close_customer_manager())

    def click_customer_area_label_button(self, area_label, button_name):
        self.click(self.customer_area_label_buttons(area_label, button_name))

    def click_customer_area_label_input_date(self, area_label, placeholder, date):
        self.execute_script("arguments[0].removeAttribute('readonly');",
                            self.find_visible_elements(self.customer_area_label_inputs(area_label, placeholder))[0])
        self.type(self.customer_area_label_inputs(area_label, placeholder), date)
        # self.execute_script('arguments[0].click();',self.find_visible_elements(self.customer_date_table(date))[0])
        # self.click(self.customer_date_table(date))

    def click_customer_area_label_input_reason(self, area_label, placeholder, reason1, reason2):
        self.click(self.customer_area_label_inputs(area_label, placeholder))
        self.click(self.customer_dropdown_list_1_item(reason1))
        self.wait(0.5)
        self.click(self.customer_area_label_inputs(area_label, placeholder, 2))
        self.click(self.customer_dropdown_list_1_item(reason2))
        self.wait(0.5)

    def type_customer_area_label_textarea(self, area_label, text):
        self.type(self.customer_area_label_textarea(area_label), text)

    def click_re_dispatch_customer_manager_alert_buttons(self, button):
        self.click(self.re_dispatch_customer_manager_alert_buttons(button))

    def click_add_dispatch_button_by_name(self, name):
        self.click(self.add_dispatch_button_by_name(name))

    def click_merge_customer_area_buttons(self, button):
        self.click(self.merge_customer_area_buttons(button))

    def merge_customer(self, customer):
        self.click(self.merge_customer_area_input())
        self.click(self.merge_customer_area_dropdown(customer))

    def type_to_modify_customer_inputs_by_label(self, label, text):
        self.type(self.modify_customer_inputs_by_label(label), text)

    def click_customer_in_line(self, customer):
        self.click(self.customer_in_line(customer))

    def click_modify_customer_conform_button(self):
        self.click(self.modify_customer_conform_button())


class LostManagePage(BaseTestCase, LostManageBase):
    def lost_manage_search_company(self, company):
        self.type(self.company_search_inputs(), company)
        self.click(self.search_button())

    def click_lost_manage_buttons(self, button):
        self.click(self.lost_manage_normal_buttons(button))

    def click_checkbox_in_line_by_company_name(self, company):
        self.click(self.checkbox_in_line_by_company_name(company))

    def click_buttons_in_line_by_company_name(self, company, button):
        self.click(self.buttons_in_line_by_company_name(company, button))

    def click_conform_lost_area_buttons(self, area, button):
        self.click(self.area_buttons(area, button))
