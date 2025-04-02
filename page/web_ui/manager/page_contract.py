from base.manager.base_contract import ContractBase, ContractInvoiceBase, ContractChangeRecordBase, ContractExpireBase
from base.base_case import BaseTestCase


class ContractPage(ContractBase, BaseTestCase):
    def click_new_contract(self):
        """
        点击新增合同按钮
        @return:
        """
        self.click(self.normal_contract_button('新增合同'))

    def click_contract_num(self, contract_id):
        """
        点击合同编码
        @param contract_id:
        @return:
        """
        self.click(self.contract_id_in_table(contract_id))

    def search_contract(self, contract_num):
        """
        按合同编码搜索
        @param contract_num: 合同编码
        @return:
        """
        self.type(self.contract_input('合同编号'), contract_num)
        self.wait(1)
        self.click(self.search_button('合同编号'))

    def input_contract_detail(self, label, text):
        """
        新增合同页面，输入文本
        @param label: 标签名称
        @param text: 输入的文本
        @return:
        """
        self.type(self.add_contract_input(label), text)

    def click_save_button(self):
        """
        点击保存按钮
        @return:
        """
        self.click(self.add_contract_save_button())
        self.wait(0.5)

    def check_service_type(self, service_type):
        """
        勾选服务类型
        @param service_type: 服务类型名称
        @return:
        """
        self.click(self.service_type(service_type))

    def input_bookkeeping_detail(self, label, text):
        """
        代账服务输入框中输入内容
        @param label: 输入框标签
        @param text: 输入的文本
        @return:
        """
        self.type(self.bookkeeping_agency_input(label), text)

    def click_spacial_dropdown_button(self, line=1):
        """
        点击特殊的下拉菜单

        @return:
        """
        self.click(self.spacial_dropdown_button(line))
        self.wait(0.5)

    def click_spacial_dropdown_drop_button(self, business_type='工商注册'):
        """
        点击特殊的下拉菜单下面的二级按钮
        @return:
        """
        self.click(self.spacial_dropdown_drop_button(business_type))

    def type_to_contract_business_service_table_amount_input_by_line(self, line, text):
        self.type(self.contract_business_service_table_amount_input_by_line(line), text)

    def type_to_add_contract_table_service_date_input(self, placeholder, text, line=1):
        self.type(self.add_contract_table_service_date_input(placeholder, line), f'{text}\n')

    def input_start_and_end_date_to_table_line(self, start_date, end_date):
        if all([self.is_element_visible(self.add_contract_table_service_date_input('开始月份')),
                self.is_element_visible(self.add_contract_table_service_date_input('结束月份'))]):
            self.type_to_add_contract_table_service_date_input('开始月份', start_date)
            self.type_to_add_contract_table_service_date_input('结束月份', end_date)

    def input_normal_detail(self, label, text):
        """
        输入合同编号
        @param label:
        @param text:
        @return:
        """
        self.type(self.contract_input(label), text)
        self.wait(0.5)

    def click_contract_num_search_button(self, label):
        """
        点击合同编号输入框，旁边的搜索按钮
        @param label:
        @return:
        """
        self.click(self.search_button(label))
        self.wait(1)

    def check_contract_inputbox(self, contract_id):
        """
        勾选合同
        @param contract_id:
        @return:
        """
        self.click(self.contract_checkbox(contract_id))
        self.wait(1)

    def click_contract_id_by_company_name(self, contract_id):
        self.click(self.contract_id_by_company_name(contract_id))

    def click_modify_contract_buttons(self, button):
        self.click(self.modify_contract_buttons(button))
        self.wait(1)

    def type_modify_contract_service_total_amount(self, line, amount):
        self.type(self.modify_contract_service_total_amount(line), amount)

    def click_delete_contract_button(self):
        """
        点击删除按钮
        @return:
        """
        self.click(self.normal_contract_button('删除'))

    def click_confirm_delete_button(self):
        """
        点击删除后出现弹框，再点击确认删除
        @return:
        """
        self.click(self.contract_confirm_delete('删除'))

    def click_contract_check_button(self):
        """
        点击合同审核按钮
        @return:
        """
        self.click(self.normal_contract_button('审核'))

    def click_return_contract_check_button(self, button):
        """
        点击反审核按钮
        @return:
        """
        self.click(self.button_in_table(button))

    def click_contract_more_button(self):
        """
        点击合同页面的更多按钮（下拉框）
        @return:
        """
        self.click(self.dropdown_contract_button('更多'))

    def click_contract_derive_button(self):
        """
        点击更多下拉框下面的导出按钮
        @return:
        """
        self.click(self.dropdown_contract_dropdown_button('导出'))

    def click_dropdown_buttons(self, button, dropdown_button):
        self.click(self.dropdown_contract_button(button))
        self.click(self.dropdown_contract_dropdown_button(dropdown_button))

    def click_derive_button(self):
        """
        点击导出后，再次点击导出
        @return:
        """
        self.click(self.derive_button('导出'))
        self.wait(3)

    def click_contract_change(self):
        self.click(self.dropdown_contract_button("合同变更"))

    def click_early_stop(self):
        self.click(self.dropdown_contract_dropdown_button("提前终止"))

    def click_stop_date_button(self):
        self.click(self.stop_date)

    def click_continue_contract_button(self, button):
        self.click(self.button_in_table(button))
        self.wait(1)

    def click_normal_button(self, button):
        self.click(self.normal_button(button))

    def click_normal_dropdown_items(self, item):
        self.click(self.normal_dropdown_items(item))

    def click_contract_checkbox_by_period(self, period):
        self.click(self.contract_checkbox_by_period(period))

    def change_person(self, person):
        self.click(self.change_person_area_input())
        self.click(self.change_person_area_selector(person))
        self.click(self.area_buttons('变更业务员', '确定'))

    def termination_contract(self, label, mon, text=None):
        self.click(self.termination_area_inputs_by_label(label))
        self.click(self.termination_area_month_selector(mon))
        if text:
            self.type(self.termination_area_textarea(), text)
        self.click(self.area_buttons('提前终止', '确定'))

    def click_area_buttons(self, area, button):
        self.click(self.area_buttons(area, button))

    def click_button_in_table_by_company_name(self, company, button):
        self.click(self.button_in_table_by_company_name(company, button))
        self.wait(0.5)

    def change_collection(self, label, mon, text=None):
        self.click(self.change_collection_area_inputs_by_label(label))
        self.click(self.termination_area_month_selector(mon))
        if text:
            self.type(self.change_collection_area_textarea(), text)
        self.click_area_buttons('收款变更', '下一步')

    def get_text_from_change_collection_step_2_inputs(self, label):
        return self.get_text(self.change_collection_step_2_inputs(label))

    def type_to_apply_invoice_area_inputs_by_label(self, label, text):
        self.type(self.apply_invoice_area_inputs_by_label(label), text)
        self.wait(1)

    def click_apply_invoice_area_button(self):
        self.click(self.apply_invoice_area_button())

    def adj_type(self, item):
        self.click(self.adj_type_area_input())
        self.wait(0.5)
        self.click(self.adj_type_area_dropdown_items(item))
        self.wait(0.5)
        self.click(self.adj_type_area_buttons())
        self.wait(0.5)

    def get_text_from_contract_type_in_line_by_company_name(self, company):
        return self.get_text(self.contract_type_in_line_by_company_name(company))


class ContractInvoicePage(BaseTestCase, ContractInvoiceBase):
    def click_checkbox_in_line_by_company_name(self, company):
        self.click(self.checkbox_in_line_by_company_name(company))

    def click_buttons_in_line_by_company_name(self, company, button):
        self.click(self.buttons_in_line_by_company_name(company, button))

    def overrule_invoice(self, text):
        self.type(self.overrule_invoice_textarea(), text)
        self.click(self.overrule_invoice_buttons('确定'))

    def click_complete_invoice_button(self):
        self.click(self.complete_invoice_button())


class ContractChangeRecordPage(BaseTestCase, ContractChangeRecordBase):
    def is_record_list_change_type_visible(self):
        return self.is_element_visible(self.record_list_change_type())


class ContractExpirePage(BaseTestCase, ContractExpireBase):
    def click_filter_item_by_label(self, label, item):
        self.click(self.filter_item_by_label(label, item))

    def search_company(self, company):
        self.type(self.filter_inputs_by_placeholder('客户名称'), company)
        self.click(self.company_search_button())

    def click_normal_buttons(self, button):
        self.click(self.normal_buttons(button))

    def click_checkbox_in_line_by_company_name_or_contract_id(self, name):
        self.click(self.checkbox_in_line_by_company_name_or_contract_id(name))

    def click_buttons_in_ling_by_company_name_or_contract_id(self, name, button):
        self.click(self.buttons_in_ling_by_company_name_or_contract_id(name, button))

    def export(self, export_type):
        self.click(self.export_type_button(export_type))
        self.click(self.export_buttons('导出'))
        self.wait(3)
