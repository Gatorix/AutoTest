from base.manager.base_collection import CollectionAuditBase, CollectionFollowUpBase
from base.base_case import BaseTestCase


class CollectionPage(CollectionAuditBase, CollectionFollowUpBase, BaseTestCase):
    def search_company(self, company_name):
        self.type(self.follow_up_input('企业名称'), company_name)
        self.click(self.follow_up_search_button())

    def click_table_button(self, company_name, operation):
        self.click(self.follow_up_table_line_buttons(company_name, operation))

    def select_collect_type(self, item):
        self.click(self.collection_details_input('收款方式'))
        self.click(self.collection_details_input_dropdown_items(item))

    def type_to_collection_inputs(self, label, text):
        self.type(self.collection_details_input(label), text)

    def get_text_from_collection_list_next_period_item_by_company(self, company, index=1):
        return self.get_text(self.collection_list_next_period_item_by_company(company, index))

    def select_service_month(self, month):
        self.click(self.collection_details_month_select(month))

    def select_multiple_month(self, mon_list):
        for _ in mon_list:
            self.click(self.collection_details_month_select(_))
            self.wait(0.5)

    def get_service_year(self):
        return self.get_text(self.service_year())

    def click_service_year_selector(self, direction):
        self.click(self.service_year_selector(direction))

    def locate_specific_year(self, year):
        if self.get_service_year() == year:
            pass
        elif int(self.get_service_year()) < int(year):
            for _ in range(int(year) - int(self.get_service_year())):
                self.click_service_year_selector('>')
                self.wait(0.5)
        else:
            for _ in range(int(self.get_service_year()) - int(year)):
                self.click_service_year_selector('<')
                self.wait(0.5)

    def click_collection_renew_contract_area_buttons(self, button):
        self.click(self.collection_renew_contract_area_buttons(button))

    def click_collection_details_button(self, button_name):
        self.click(self.collection_details_buttons(button_name))

    def click_collection_details_bottom_button(self, button_name):
        self.click(self.collection_details_bottom_buttons(button_name))

    def input_collection_details(self, label, text):
        self.type(self.collection_details_input(label), text)

    def is_tips_show_up(self):
        return self.is_element_visible(self.collection_details_tips())

    def ignore_tips(self):
        self.wait(1)
        if self.is_tips_show_up():
            self.click(self.collection_details_tips())
            self.wait(1)

    def click_audit_table_button(self, operation):
        self.click(self.audit_collection_operations(operation))
        self.wait(1)

    def click_conform_cancel(self):
        self.click(self.audit_collection_conform_cancel('确定'))

    def click_collection_audit_button(self, button_name):
        self.click(self.collection_audit_buttons(button_name))
        if '导出' in button_name:
            self.wait(3)

    def collection_select_audit_company(self, company_name):
        self.click(self.collection_audit_table_checkbox(company_name))

    def input_overrule_text(self, text):
        self.type(self.audit_overrule_reason(), text)

    def click_overrule_button(self, button_name):
        self.click(self.audit_overrule_buttons(button_name))

    def click_conform_delete(self):
        self.click(self.audit_collection_conform_delete('确定'))

    def click_conform_collect(self, button_name):
        self.click(self.audit_conform_collection_button(button_name))

    def click_normal_button(self, button):
        self.click(self.follow_up_buttons(button))
        if button == '导出':
            self.wait(3)

    def select_collection_class(self, item, biz_type, line):
        self.click(self.select_collection_class_in_table(line))
        self.click(self.select_collection_class_in_table_items(item, biz_type))

    def click_add_line_button(self):
        self.click(self.add_line_button())

    def click_delete_line_button(self, line):
        self.click(self.delete_line_button(line))

    def click_collection_class(self, line):
        self.click(self.select_collection_class_in_table(line))
        self.wait(0.5)

    def type_to_collection_amount_input_in_table(self, item, cell, amount):
        self.type(self.amount_input_in_table(item, cell), amount)

    def type_to_collection_discount_input_in_table(self, item, cell, discount):
        self.type(self.amount_input_in_table(item, cell), discount)

    def click_del_button_in_table(self, line):
        self.click(self.del_button_in_table(line))

    def click_switch_biz_type_on_top(self, biz_name):
        self.click(self.switch_biz_type_on_top(biz_name))

    def select_year(self, year):
        self.click(self.select_year_in_table())
        self.click(self.year_selector(year))

    def type_to_amount_input_in_table_bookkeeping(self, amount):
        self.type(self.amount_input_in_table_bookkeeping('2'), amount)

    def type_to_discount_input_in_table_bookkeeping(self, discount):
        self.type(self.amount_input_in_table_bookkeeping('3'), discount)

    def click_add_collection_class_button(self):
        self.move_mouse_to_element(self.collection_class_select_div())
        if self.is_element_visible(self.collection_class_popup_scroll_bar()):
            bar_loc = self.get_element_location(self.collection_class_popup_scroll_bar())
            self.drag_and_drop_with_offset(self.collection_class_popup_scroll_bar(),
                                           bar_loc.get('x'),
                                           bar_loc.get('y') + 20)
        self.click(self.add_collection_class_button())

    def type_to_add_collection_class_input(self, text):
        self.type(self.add_collection_class_inputs('收费项目名称'), text)

    def select_collection_class_belong_to(self, biz_type):
        self.click(self.add_collection_class_inputs('服务类型归属'))
        self.click(self.add_collection_class_belong_to(biz_type))

    def click_add_collection_class_buttons(self, button):
        self.click(self.add_collection_class_buttons(button))

    def click_collection_class_operate_button(self, item_title, button):
        self.click(self.collection_class_operate_button(item_title, button))

    def click_conform_delete_collection_class_buttons(self, button):
        self.click(self.conform_delete_collection_class_buttons(button))

    def click_collection_filters(self, label, item):
        self.click(self.collection_filters(label, item))
        self.wait(1)

    def click_collection_checkboxes_by_company(self, company):
        self.click(self.collection_checkboxes_by_company(company))

    def is_company_visible(self, company):
        return self.is_element_visible(self.collection_checkboxes_by_company(company))

    def get_list_year(self):
        return self.get_text(self.collection_switch_year())

    def click_collection_switch_year(self, direction):
        self.click(self.collection_switch_year(direction))

    def switch_to_year(self, year):
        if self.get_list_year() == year:
            pass
        elif int(self.get_list_year()) < int(year):
            for _ in range(int(year) - int(self.get_list_year())):
                self.click_collection_switch_year('3')
                self.wait(0.5)
        else:
            for _ in range(int(self.get_list_year()) - int(year)):
                self.click_collection_switch_year('1')
                self.wait(0.5)

    def is_collection_status_in_table_by_company_visible(self, company, mon, status):
        self.wait(1)
        return self.is_element_visible(self.collection_status_in_table_by_company(company, mon, status))

    def click_audit_conform_delete_buttons(self, button):
        return self.click(self.audit_conform_delete_buttons(button))

    def audit_search_by_company(self, company):
        self.type(self.audit_customer_input(), company)
        self.click(self.audit_buttons('查询'))
