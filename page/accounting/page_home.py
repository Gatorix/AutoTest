from base.accounting.base_home import AccountingHomeBase

from base.base_case import BaseTestCase


class AccountingHomePage(AccountingHomeBase, BaseTestCase):
    def switch_to_home_frame(self):
        self.switch_to_frame(self.home_frame())

    def click_home_report_link(self, report):
        self.click(self.home_report_link(report))

    def click_home_blue_buttons(self, button):
        self.click(self.home_blue_buttons(button))
        self.wait(2)

    def get_text_from_home_report_cal_result(self, report):
        return self.get_text(self.home_report_cal_result(report))

    def click_home_measure_div_month_adj_buttons(self, measure_title, adj_button):
        self.click(self.home_measure_div_month_adj_buttons(measure_title, adj_button))
        self.wait(0.5)

    def get_text_from_home_measure_div_month_span(self, measure_title):
        return self.get_text(self.home_measure_div_month_span(measure_title))

    def get_loading_span_attribute(self, measure_title):
        return self.get_attribute(self.home_measure_div_loading_span(measure_title), 'class')

    def click_home_measure_div_buttons(self, button):
        self.click(self.home_measure_div_buttons(button))

    def get_text_from_home_financial_indices_list_item(self, span):
        return self.get_text(self.home_financial_indices_list_item(span))

    def click_home_financial_indices_add_new_item(self):
        self.click(self.home_financial_indices_add_new_item())

    def type_to_home_financial_indices_input_by_label(self, label, text):
        self.type(self.home_financial_indices_input_by_label(label), text)

    def click_home_financial_indices_add_button(self):
        self.click(self.home_financial_indices_add_button())

    def click_home_financial_indices_table_buttons(self, name, button):
        self.click(self.home_financial_indices_table_buttons(name, button))

    def get_title_text(self, company_name):
        return self.get_text(self.home_title(company_name))

    def click_accounting_menu(self, level_one, level_two=None):
        self.wait_for_ready_state_complete()
        self.click(self.menu(level_one))
        if level_two:
            self.click(self.menu(level_two))
        self.wait(0.3)

    def click_accounting_data_menu(self, level_one, level_two=None):
        self.wait_for_ready_state_complete()
        self.click(self.menu(level_one))
        if level_two:
            self.click(self.data_menu(level_two))
        self.wait(0.3)

    def close_top_tabs(self, tab_name):
        self.click(self.top_tabs(tab_name))

    def click_switch_button(self):
        self.click(self.acct_switch_button())
        self.wait(1)

    def type_to_search_input(self, company):
        self.type(self.search_input(), company)
        self.wait(1)

    def click_search_button(self):
        self.click(self.search_button())
        self.wait(2)

    def click_company_line(self, company: str):
        self.wait_for_element_clickable(self.company_line(company))
        self.click(self.company_line(company))
        self.wait(1)

    def get_text_from_my_company_span(self):
        return self.get_text(self.my_company_span())

    def is_company_span_visible(self):
        return self.is_element_visible(self.my_company_span())

    def switch_acct(self, company):
        self.click_switch_button()
        self.type_to_search_input(company)
        self.click_search_button()
        self.click_company_line(company)
        self.wait_for_ready_state_complete()
