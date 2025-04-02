from selenium.common import NoSuchElementException

from base.manager.base_agency import (AgencyAccountBase,
                                      ServiceAuditBase,
                                      ReceiveInvoiceRecordBase,
                                      BookkeepingBase,
                                      FileTaxesBase,
                                      ReceiveInvoiceBase)

from base.base_case import BaseTestCase


class AgencyAccountPage(AgencyAccountBase, ServiceAuditBase, BaseTestCase):
    def search_company(self, company_name):
        """
        输入“客户名称”-点击搜索按钮
        """
        self.type(self.service_input('客户名称'), company_name)
        self.click(self.service_search_button())
        self.wait(1)

    def search_agency_company(self, company_name):
        """
        输入“客户名称”-点击搜索按钮
        """
        self.type(self.service_input('客户名称'), company_name)
        self.click(self.service_search_button())
        self.wait(1)

    def click_agency_title(self, title):
        self.click(self.agency_title(title))

    def tax_search_company(self, company_name):
        """
        代账服务-服务管理-报税选项卡页面-输入“客户名称”-点击搜索按钮
        """
        self.type(self.service_input('客户名称'), company_name)
        self.click(self.tax_search_button())

    def click_table_button(self, company_name, operation):
        """
        点击表格中“客户名称”所在行的某个操作按钮
        """
        self.wait_for_element_clickable(self.service_table_line_buttons(company_name, operation))
        if self.is_element_clickable(self.service_table_line_buttons(company_name, operation)):
            self.click(self.service_table_line_buttons(company_name, operation))
            if operation == '进账簿':
                self.wait(3)
        else:
            self.click(self.service_table_line_buttons(company_name, operation))
            if operation == '进账簿':
                self.wait(3)

    def stop_or_not_services(self, service_stop_or_not_text):
        """点击【正常服务】【已停止服务】选项卡页面"""
        self.click(self.agency_account_stop_services(service_stop_or_not_text))

    def select_service_month(self, service_type, month):
        """
        填写报税信息-选择报税/收票账期等
        """
        self.click(self.service_details_month_select(service_type, month))

    def upload_tax_picture(self, file_path):
        self.choose_file(self.tax_upload_file_input(), file_path)
        self.wait(2)

    def select_begin_month(self, month):
        """选择收票开始期"""
        self.click(self.locate_months_dropdownbox())  # 点击日期下拉框
        self.click(self.begin_month_select(month))  # 以点击方式选择下拉框中的月份

    def select_service_type(self, service):
        """选择服务管理、收票、报税等某一个服务选型"""
        self.click(self.agency_account_service(service))

    def select_service_type_droplist(self, service):
        """选择表格上排的【更多】下拉列表中的某一个服务选型"""
        # ele = self.find_visible_elements(self.agency_account_service_droplist(service))
        # self.execute_script("arguments[0].click();", ele[0])
        self.click(self.agency_account_service_droplist(service))

    def is_delete_success(self, company):
        return self.is_element_visible(self.delete_book(company))

    def click_collection_details_button(self, button_name):
        self.click(self.collection_details_buttons(button_name))

    def click_service_details_bottom_button(self, button_name):
        self.click(self.service_details_bottom_buttons(button_name))

    def click_page_popups_bottom_button(self, button_name, types):
        self.click(self.page_popups_bottom_buttons(button_name, types))
        self.wait(2)

    def select_dropdown_item(self, types, placeholder, item):
        self.click(self.agency_input_box(types, placeholder))
        self.click(self.dropdown_item(item))

    def type_textarea(self, types, text):
        self.type(self.agency_textarea(types), text)

    def click_followup_table_button(self, title, button):
        self.click(self.agency_followup_table_buttons(title, button))

    def click_tip_bottom_button(self, button_name):
        """当前岗位已派工，是否继续派工？"""
        self.click(self.tip_bottom_buttons(button_name))

    def select_service(self, label, service_type):
        """
        ”添加服务“弹框中，点击【服务类型】下拉框，并选择某一个服务类型，如个体工商户报税
        """
        self.click(self.click_service_type_droplist(label))
        self.click(self.add_service_select_type(service_type))

    def select_tax_type(self, label):
        """
        选择【纳税性质】:一般纳税人、小规模纳税人
        """
        self.click(self.click_tax_type_droplist())
        self.click(self.click_select_tax_type(label))

    def select_accounting_standards(self, standards):
        self.click(self.accounting_standards_input())
        self.click(self.accounting_standards_list_items(standards))
        # self.select_option_by_text(self.accounting_standards_selector(), standards)

    def input_taxes_details(self, index, text):
        """获取报税业务数据"""
        self.type(self.taxes_details_input(index), text)

    def input_receipt_details(self, label, text, index):
        """获取收票业务数据"""
        self.type(self.receipt_details_input(label, index), text)
        # 点击旁边位置，恢复状态
        self.click('//div[@class="el-dialog__header"]//span[text()="收票"]')

    def input_enable_year(self, year):
        """创建账套页面，填写启用期间"""
        self.type(self.input_enable_period_year(), year)  # 输入启用期间-年份

    def input_enable_month(self, month):
        """创建账套页面，填写启用期间"""
        self.type(self.input_enable_period_month(), month)  # 输入启用期间-月份（期数）

    def click_create_button(self, label):
        """创建账套_点击开始创建"""
        self.click(self.begin_create_accounts(label))
        self.wait(10)

    def get_company_name(self):
        return self.get_text(self.accounting_title())

    def click_dispatch_button(self, label):
        """选择人员派工或部门派工"""
        self.click(self.person_or_department_dispatch(label))

    def click_dispatch_or_query_button(self, label):
        """选择派工或派工查询"""
        self.click(self.dispatch_or_query(label))

    def click_dispatch_change_button(self, stuff, button):
        """选择转派工or删除"""
        self.click(self.dispatch_change(stuff, button))

    def click_dispatch_delete_button(self):
        """转派工后，再点击【删除】按钮"""
        self.click(self.dispatch_delete())

    def get_line_num_from_dispatch_record_table(self):
        return len(self.find_visible_elements(self.dispatch_record_row()))

    def click_dispatch_department_select_button(self, dep):
        """转派工-点击部门选择框, 选择xx部门"""
        self.click(self.dispatch_department())
        self.click(self.select_department(dep))

    def is_tip_visible(self):
        return self.is_element_visible(self.exist_dispatch_tip())

    def click_dispatch_staff_select_button(self, staff):
        """转派工-点击转入职员选择框, 选择xx职员"""
        self.click(self.dispatch_staff())
        self.click(self.select_staff(staff))

    def click_dispatch_ok_button(self, button):
        """点击转派工确定或取消按钮"""
        self.click(self.dispatch_ok_button(button))

    def is_tips_show_up(self):
        return self.is_element_visible(self.collection_details_tips())

    def ignore_tips(self):
        if self.is_element_visible(self.collection_details_tips()):
            self.click(self.collection_details_tips())

    def click_audit_table_button(self, operation):
        self.click(self.audit_collection_operations(operation))

    def click_conform_button(self, button_name):
        """点击弹框中跳出的确认、取消等按钮"""
        self.click(self.audit_conform_button(button_name))

    def click_conform_cancel(self):
        self.click(self.audit_collection_conform_cancel('确定'))

    def click_conform_delete(self):
        self.click(self.audit_collection_conform_delete('确定'))

    def click_conform_collect(self, button_name):
        self.click(self.audit_conform_collection_button(button_name))

    def click_audit_button(self, button_name):
        """点击表格右上方的那排按钮"""
        self.click(self.tax_audit_buttons(button_name))

    def click_service_button(self, button_name):
        """点击表格右上方的那排按钮"""
        self.click(self.audit_buttons(button_name))

    def click_service_button_droplist(self, button_name):
        """点击表格右上方的那排按钮-【更多】下拉框"""
        self.click(self.audit_buttons_droplist(button_name))

    def select_audit_company(self, company_name):
        """点击checkbox，选择表格中审计公司"""
        self.click(self.audit_table_checkbox(company_name))
        self.wait(0.5)

    def click_company_label(self, company_name):
        self.click(self.audit_table_company_name(company_name))

    def select_audit_taxes(self, label):
        """审税金弹框中选择某一账期的税金"""
        self.click(self.select_table_first_checkbox(label))

    def input_overrule_text(self, text):
        self.type(self.audit_overrule_reason(), text)

    def click_overrule_button(self, button_name):
        self.click(self.audit_overrule_buttons(button_name))

    def click_add_tips_button(self, button_name):
        if self.is_element_visible(self.add_tips(button_name)):
            self.click(self.add_tips(button_name))

    def dispatch_search_name(self, dispatch_style, name):
        """
        派工-人员-输入人名-点击搜索
        @param dispatch_style: 部门派工or人员派工
        @param name:部门名or人员名
        @return:
        """
        self.type(self.dispatch_input(dispatch_style), name)
        self.wait(0.5)
        self.click(self.dispatch_search_button(dispatch_style))
        self.wait(0.5)

    def dispatch_add_name(self, button_name):
        """
        搜索出名字后，点击添加按钮
        @param button_name: 比如添加按钮
        @return:
        """
        self.click(self.dispatch_add_button(button_name))
        self.wait(1)

    def dispatch_select_style(self, style_name):
        """
        派工-人员-选择人名类型，进行点击
        """
        self.click(self.dispatch_style(style_name))

    def click_ignore_set_tip(self):
        if self.is_element_visible(self.ignore_set_tip()):
            self.click(self.ignore_set_tip())

    def click_add_tax_line_button(self):
        self.click(self.add_tax_line_button())

    def click_tax_select_input_box(self):
        self.click(self.tax_select_input_box())

    def click_tax_type(self):
        self.click(self.tax_type())

    def click_follow_up_already(self):
        self.click(self.follow_up_already())

    def click_export_type_button(self, method):
        self.click(self.export_type_button(method))

    def click_export_buttons(self, button):
        self.click(self.export_buttons(button))
        if button == '导出':
            self.wait(3)

    def dispatch_query_checkbox_by_company_amount(self, company):
        return len(self.find_visible_elements(self.dispatch_query_checkbox_by_company(company)))

    def dispatch_query_checkbox_amount(self):
        return len(self.find_visible_elements(self.dispatch_query_checkbox()))


class ReceiveInvoiceRecordPage(ReceiveInvoiceRecordBase, BaseTestCase):
    def click_checkbox_in_table_by_company(self, company):
        self.click(self.checkbox_in_table_by_company(company))

    def is_checkbox_in_table_by_company_visible(self, company):
        return self.is_element_visible(self.checkbox_in_table_by_company(company))

    def click_operate_button_in_table_by_company(self, company, button):
        self.click(self.operate_button_in_table_by_company(company, button))

    def click_conform_delete_buttons(self, button):
        self.click(self.conform_delete_buttons(button))

    def query_data_by_label(self, label, condition):
        self.type(self.filter_inputs_by_label(label), condition)
        self.click(self.query_button())


class ReceiveInvoicePage(ReceiveInvoiceBase, BaseTestCase):
    def receive_invoice_click_checkbox_in_table_by_company(self, company):
        self.click(self.receive_invoice_checkbox_in_table_by_company(company))

    def switch_role(self, person):
        self.type(self.company_filter(), person)
        self.wait(1)
        self.click(self.org_tree_person(person))

    def switch_root_role(self):
        self.click(self.company_filter())
        self.wait(1)
        self.click(self.root_org())

    def click_normal_buttons(self, button):
        self.click(self.normal_buttons(button))
        if '导出' in button:
            self.wait(3)

    def click_dropdown_buttons(self, button):
        self.click(self.dropdown_buttons(button))

    def receive_invoice_click_operate_button_in_table_by_company(self, company, button):
        self.click(self.receive_invoice_operate_button_in_table_by_company(company, button))

    def receive_invoice_search_company(self, text):
        self.type(self.inputs_by_placeholder(), text)
        self.click(self.search_button())


class BookkeepingPage(BookkeepingBase, BaseTestCase):
    def click_buttons_in_line_by_company(self, company, button):
        self.click(self.buttons_in_line_by_company(company, button))

    def bookkeeping_search_company(self, text):
        self.type(self.bookkeeping_search_input(), text)
        self.click(self.bookkeeping_search_button())

    def click_checkbox_in_line_by_company(self, company):
        self.check_if_unchecked(self.checkbox_in_line_by_company(company))

    def get_text_from_lark_invoice_mark_in_line(self, company):
        return self.get_text(self.lark_invoice_mark_in_line(company))

    def is_lark_invoice_mark_in_line_visible(self, company):
        return self.is_element_visible(self.lark_invoice_mark_in_line(company))

    def click_lark_invoice_mark_inputs_by_label(self, label):
        self.click(self.lark_invoice_mark_inputs_by_label(label))

    def click_lark_invoice_mark_month_selector(self, mon):
        self.click(self.lark_invoice_mark_month_selector(mon))

    def click_lark_invoice_mark_conform_button(self):
        self.click(self.lark_invoice_mark_conform_button())

    def lark_invoice_mark_select_month(self, mon):
        self.click_lark_invoice_mark_month_selector(mon)
        self.click_lark_invoice_mark_conform_button()

    def type_to_lark_invoice_mark_memo(self, text):
        self.type(self.lark_invoice_mark_memo(), text)

    def clear_lark_invoice_mark_memo(self):
        self.clear(self.lark_invoice_mark_memo())
        self.click(self.lark_invoice_mark_label())

    def click_lark_invoice_mark_buttons(self, button):
        self.click(self.lark_invoice_mark_buttons(button))


class FileTaxesPage(FileTaxesBase, BaseTestCase):
    pass
