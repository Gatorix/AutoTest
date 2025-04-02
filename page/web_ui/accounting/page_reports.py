from base.base_case import BaseTestCase
from base.accounting.base_reports import BalanceSheetBase, StandardCashFlowStatementBase
from base.accounting.base_reports import IncomeStatementBase
from base.accounting.base_reports import CashFlowStatementBase


class BalanceSheetPage(BaseTestCase, BalanceSheetBase):
    def switch_to_balance_sheet_frame(self):
        self.switch_to_frame(self.balance_sheet_frame())
        self.wait(2)

    def click_balance_sheet_buttons(self, button, start=None, end=None):
        id_kv = {'EXCEL格式': 'saveAsExcel', '税局格式导出': 'export_sj', '刷新': 'refresh', '批量导出': 'batchExport',
                 '导出': 'exportBtn'}
        self.js_click(self.buttons(id_kv.get(button)))
        self.close_or_conform_balance_tips()
        if button == '批量导出':
            self.select_period_between(start, end)
            self.js_click(self.buttons_b(id_kv.get('导出')))
            self.wait(7)
        elif any(['EXCEL格式' == button,
                  '导出' == button,
                  '税局格式导出' == button]):
            self.wait(7)

    def get_text_from_copy_button_span(self):
        return self.get_text(self.copy_button_span())

    def close_or_conform_balance_tips(self):
        if self.is_element_visible(self.balance_tips_button()):
            self.click(self.balance_tips_button())

    def select_period(self, period):
        self.click(self.period_selector())
        self.click(self.period_items(period))

    def select_period_between(self, start, end):
        self.type(self.period_start_input(), f'{start}\n')
        self.type(self.period_end_input(), f'{end}\n')
        self.wait(1)


class IncomeStatementPage(BaseTestCase, IncomeStatementBase):
    def switch_to_income_statement_frame(self):
        self.switch_to_frame(self.income_statement_frame())

    def click_income_statement_buttons(self, button, start=None, end=None, report_type=None):
        id_kv = {'EXCEL格式': 'saveAsExcel', '税局格式导出': 'export_sj', '刷新': 'refresh', '批量导出': 'batchExport',
                 '导出': 'exportBtn'}
        self.js_click(self.buttons(id_kv.get(button)))
        self.conform_export()
        if button == '批量导出':
            self.select_period_between(start, end)
            self.select_report_type(report_type)
            self.js_click(self.buttons_b(id_kv.get('导出')))
            self.wait(7)
        elif any(['EXCEL格式' == button,
                  '导出' == button,
                  '税局格式导出' == button]):
            self.wait(7)

    def conform_export(self):
        if self.is_element_visible(self.conform_export_button()):
            self.click(self.conform_export_button())

    def select_period_between(self, start, end):
        self.type(self.period_start_input(), f'{start}\n')
        self.type(self.period_end_input(), f'{end}\n')
        self.wait(1)

    def select_period(self, period):
        self.click(self.period_selector())
        self.click(self.period_items(period))

    def select_report_type(self, report_period):
        kv = {'月报': 'bymonth', '季报': 'byseason'}
        self.click(self.report_type(kv.get(report_period)))

    def get_text_from_copy_button_span(self):
        return self.get_text(self.copy_button_span())


class CashFlowStatementPage(BaseTestCase, CashFlowStatementBase):
    def switch_to_cash_flow_statement_frame(self):
        self.switch_to_frame(self.cash_flow_statement_frame())
        self.wait(1)

    def click_cash_flow_statement_buttons(self, button, start=None, end=None, report_type=None):
        id_kv = {'EXCEL格式': 'saveAsExcel', '税局格式导出': 'export_sj', '刷新': 'refresh', '批量导出': 'batchExport',
                 '导出': 'exportBtn'}
        self.js_click(self.buttons(id_kv.get(button)))
        self.conform_export()
        if button == '批量导出':
            self.select_period_between(start, end)
            self.select_report_type(report_type)
            self.js_click(self.buttons_b(id_kv.get('导出')))
            self.wait(7)
        elif any(['EXCEL格式' == button,
                  '导出' == button,
                  '税局格式导出' == button]):
            self.wait(7)

    def close_balance_verify(self):
        if self.is_element_visible(self.close_balance_tips()):
            self.click(self.close_balance_tips())

    def conform_export(self):
        if self.is_element_visible(self.conform_export_button()):
            self.click(self.conform_export_button())

    def select_period_between(self, start, end):
        self.type(self.period_start_input(), f'{start}\n')
        self.type(self.period_end_input(), f'{end}\n')
        self.wait(1)

    def select_period(self, period):
        self.click(self.period_selector())
        self.click(self.period_items(period))

    def select_report_type(self, report_period):
        kv = {'月报': 'bymonth', '季报': 'byseason'}
        self.click(self.report_type(kv.get(report_period)))


class StandardCashFlowStatementPage(BaseTestCase, StandardCashFlowStatementBase):
    def switch_to_standard_cash_flow_statement_frame(self):
        self.switch_to_frame(self.standard_cash_flow_statement_frame())
        self.wait(0.5)

    def click_standard_cash_flow_statement_buttons(self, button):
        button_kv = {
            '报表调整': 'adjust'
        }
        self.click(self.standard_cash_flow_statement_buttons(button_kv.get(button)))

    def click_standard_cash_flow_statement_report_voucher_dialog_elements(self, ele):
        ele_id_kv = {
            '重置': 'clearSearchBtn',
            '查询': 'searchBtn',
            '导出': 'exportXjllbBtn'
        }
        self.click(self.standard_cash_flow_statement_report_voucher_dialog_elements(ele_id_kv.get(ele)))
        if '导出' in ele:
            self.wait(2)

    def type_to_standard_cash_flow_statement_report_voucher_dialog_voucher_num_input(self, voucher_num):
        self.type(self.standard_cash_flow_statement_report_voucher_dialog_elements('voucherNumberInput'), voucher_num)
