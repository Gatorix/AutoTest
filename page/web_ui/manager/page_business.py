from base.manager.base_business import BusinessServiceBase, BusinessReportBase

from base.base_case import BaseTestCase


class BusinessServicePage(BusinessServiceBase, BaseTestCase):
    def business_service_search_company(self, company_name):
        """
        输入“客户名称”-点击搜索按钮
        """
        self.type(self.service_input('客户名称'), company_name)
        self.wait(0.5)
        self.click(self.business_service_search_button())
        self.wait(1)

    def click_business_service_normal_button(self, button_name, dropdown_button=None):
        self.click(self.service_management_normal_button(button_name))
        self.wait(0.5)
        if dropdown_button:
            self.click(self.service_management_dropdown_button(dropdown_button))

    def click_conform_stop_service(self):
        if self.is_element_visible(self.conform_stop_service()):
            self.click(self.conform_stop_service())

    def check_checkbox_in_line_by_company(self, company):
        if isinstance(company, list):
            for _ in company:
                self.click(self.checkbox_in_line_by_company(_))
        else:
            self.click(self.checkbox_in_line_by_company(company))

    def click_conform_tips_on_top_buttons(self, button):
        self.click(self.conform_tips_on_top_buttons(button))

    def click_buttons_in_line_by_company(self, company, status):
        self.click(self.buttons_in_line_by_company(company, status))

    def collect_files(self, button, labels: list = None, text=None):
        if isinstance(labels, list):
            for _ in labels:
                self.click(self.collect_file_tooltip_labels(_))
        if text:
            self.type(self.collection_file_tooltip_textarea(), text)
        self.click(self.collect_file_tooltip_buttons(button))

    def new_customer(self, name, cus_type=None):
        self.type(self.new_customer_input(), name)
        if cus_type:
            self.click(self.new_customer_type())
            self.wait(0.5)
            self.click(self.new_customer_type_selector(cus_type))
        self.click(self.new_customer_buttons('确定'))

    def is_customer_exist_tip_visible(self):
        return self.is_element_visible(self.customer_exist())

    def click_stop_service_buttons(self, button):
        self.click(self.stop_service_buttons(button))

    def click_conform_recover_service_buttons(self, button):
        self.click(self.conform_recover_service_buttons(button))


class BusinessReportPage(BusinessReportBase, BaseTestCase):
    def business_report_search_company(self, company_name):
        """
        输入“客户名称”-点击搜索按钮
        """
        self.type(self.service_input('客户名称'), company_name)
        self.wait(0.5)
        self.click(self.business_report_search_button())
        self.wait(1)

    def click_normal_button(self, button):
        self.click(self.service_management_normal_button(button))

    def click_stop_service_buttons(self, button):
        self.click(self.stop_service_buttons(button))

    def is_filter_item_selected(self, label, item):
        return 'item-selected' in self.get_attribute(self.filter_by_label(label, item), 'class')

    def select_if_unselected_filter_item(self, label, item):
        if not self.is_filter_item_selected(label, item):
            self.click(self.filter_by_label(label, item))

    def unselect_if_selected_filter_item(self, label, item):
        if self.is_filter_item_selected(label, item):
            self.click(self.filter_by_label(label, item))

    def business_report_check_checkbox_in_line_by_company(self, company):
        if isinstance(company, list):
            for _ in company:
                self.click(self.report_checkbox_in_line_by_company(_))
        else:
            self.click(self.report_checkbox_in_line_by_company(company))

    def report_click_buttons_in_line_by_company(self, company, button):
        self.click(self.report_buttons_in_line_by_company(company, button))
        self.wait(1)

    def click_conform_already_report_button(self):
        self.click(self.conform_already_report_button())

    def click_conform_report_buttons(self, button):
        self.click(self.conform_report_buttons(button))

    def click_report_type_radio(self, report_type):
        self.click(self.report_type_radio(report_type))

    def click_report_setting_buttons(self, button):
        self.click(self.report_setting_buttons(button))
        self.wait(1)
    def get_report_type_div_text(self, company):
        return self.get_text(self.report_type_div(company))
