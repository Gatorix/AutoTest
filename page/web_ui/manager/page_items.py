from selenium.common import ElementNotVisibleException

from base.base_case import BaseTestCase
from base.manager.base_items import BaseItems


class ItemsPage(BaseTestCase, BaseItems):
    def switch_tab_item(self, tab):
        self.click(self.tab_item(tab))

    def click_normal_button(self, button_name, dropdown_button=None):
        self.click(self.inventory_buttons(button_name))
        self.wait(0.5)
        if '导出' in button_name:
            self.wait(3)
        if dropdown_button:
            self.click(self.dropdown_buttons(dropdown_button))

    def click_dropdown_button(self, button_name, dropdown_button):
        self.click_normal_button(button_name)
        self.wait(0.5)
        self.click(self.inventory_dropdown_buttons(dropdown_button))
        self.wait(0.5)

    def input_head_details(self, placeholder, text):
        self.type(self.receiving_items_input_box(placeholder), text)
        self.wait(0.5)

    def click_company_list(self, company_name):
        self.click(self.company_list(company_name))
        self.wait(0.5)

    def input_item_details(self, item):
        self.click(self.receiving_items_table_input())
        self.wait(0.5)
        self.click(self.receiving_items_select(item))

    def submit_items(self):
        self.click(self.receive_or_return_items_submit_button())
        self.wait(0.5)

    def close_items(self):
        self.click(self.receive_or_return_items_close_button())

    def check_items(self, company_name):
        self.click(self.inventory_table_checkbox(company_name))

    def close_ads(self):
        try:
            if self.is_element_visible(self.ads()):
                self.click(self.ads())
            else:
                pass
        except ElementNotVisibleException:
            pass

    def select_person(self, person):
        self.type(self.trans_inputs('请选择接收人'), person)
        self.wait(0.5)
        self.click(self.trans_list(person))

    def click_table_button(self, button_name):
        self.click(self.table_buttons(button_name))

    def click_receiving_table_button(self, company_name):
        self.click(self.receiving_table_button(company_name))

    def click_table_buttons(self, button_name):
        self.click(self.table_buttons(button_name))

    def click_check_all(self):
        self.click(self.check_all())

    def click_trans_conform(self):
        self.click(self.trans_conform())

    def click_trans_submit(self):
        self.click(self.trans_submit())

    def search_company(self, placeholder, company):
        self.type(self.input_box(placeholder), company)
        self.wait(0.5)
        self.click(self.search_button())
        self.wait(1)

    def click_download_template(self):
        self.click(self.download_items_template())
        self.wait(3)

    def click_transfer_record_button(self, company):
        self.click(self.transfer_record_button(company))
        self.wait(1)

    def click_transfer_record_list_button(self, button):
        # self.execute_script('arguments[0].click();',self.transfer_record_list_button(button)[0])
        self.click(self.transfer_record_list_button(button))
        self.wait(1)

    def click_transfer_record_conform_delete(self):
        self.click(self.transfer_record_conform_delete())

    def upload_file(self, filepath):
        self.wait(1)
        self.choose_file(self.upload_file_input(), filepath)
        self.wait(1)
        self.click(self.upload_file_buttons('确定'))

    def modify_memo_or_location(self, area, text=None):
        if text:
            self.type(self.area_textarea(area), text)
        self.click(self.area_buttons(area, '确定'))
        self.click(self.conform_alert())

    def click_button_in_line_by_company(self, company):
        self.click(self.button_in_line_by_company(company))

    def is_company_name_in_line_visible(self, company):
        return self.is_element_visible(self.company_name_in_line(company))
