from base.accounting.base_books import (SubsidiaryLedgerBase,
                                        QuantityAmountLedgerBase,
                                        QuantityAmountGeneralLedgerBase,
                                        MultiColumnLedger,
                                        AccountingBalanceBase,
                                        AccountingDetailBase)
from base.accounting.base_books import GeneralLedgerBase
from base.accounting.base_books import VoucherSummaryBase
from base.accounting.base_books import BalanceBase
from base.base_case import BaseTestCase


class SubsidiaryLedgerPage(SubsidiaryLedgerBase, BaseTestCase):
    def switch_to_subsidiary_ledger_frame(self):
        self.switch_to_frame(self.subsidiary_ledger_frame())

    def click_subsidiary_ledger_buttons(self, button):
        kv_id = {'打印': 'print', '连续打印': 'printAll',
                 '导出当前科目': 'exportNow', '导出全部科目': 'exportAll',
                 '确定': 'filter-submit'}
        self.js_click(self.buttons(kv_id.get(f"{button}")))
        if '导出' in button:
            self.wait(7)
        self.wait(1)

    def click_subsidiary_ledger_subjects(self, level_one, level_two=''):
        self.click(self.subject_box_level_one(level_one))
        if level_two:
            self.click(self.subject_box_level_one_expand_button(level_one))
            self.click(self.subject_box_level_two(level_one, level_two))

    def type_to_filter_inputs(self, label, text, from_or_to=None):
        self.type(self.filter_inputs(label, from_or_to), text)

    def click_period_trigger(self, from_or_to):
        self.click(self.period_trigger(from_or_to))

    def click_period_item_selector(self, item):
        self.click(self.period_item_selector(item))

    def select_period(self, from_or_to, item):
        self.click_period_trigger(from_or_to)
        self.click_period_item_selector(item)

    def check_filter_checkbox(self, item):
        self.check_if_unchecked(self.filter_checkbox(item))

    def click_filter_span(self):
        self.click(self.filter_span())


class GeneralLedgerPage(GeneralLedgerBase, BaseTestCase):
    def switch_to_general_ledger_frame(self):
        self.switch_to_frame(self.general_ledger_frame())

    def click_general_ledger_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)


class VoucherSummaryPage(VoucherSummaryBase, BaseTestCase):
    def switch_to_voucher_summary_frame(self):
        self.switch_to_frame(self.voucher_summary_frame())

    def click_voucher_summary_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)


class BalancePage(BalanceBase, BaseTestCase):
    def switch_to_balance_frame(self):
        self.switch_to_frame(self.balance_frame())

    def click_balance_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export', '确定': 'filter-submit', '重置': 'filter-reset'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def subject_filtration(self, item, level=9):
        self.click(self.filter_span())
        self.click_balance_buttons('重置')
        for _ in ['显示辅助核算',
                  '只显示最明细科目',
                  '余额为0不显示',
                  '本期无发生额且余额为0不显示',
                  '本年累计无发生额且余额为0不显示']:
            self.uncheck_if_checked(self.filter_checkbox(_))
        self.type(self.subject_level(), level)
        self.check_if_unchecked(self.filter_checkbox(item))
        self.click_balance_buttons('确定')
        self.wait(0.5)


class QuantityAmountLedgerPage(QuantityAmountLedgerBase, BaseTestCase):
    def switch_to_quantity_amount_ledger_frame(self):
        self.switch_to_frame(self.quantity_amount_ledger_frame())

    def click_quantity_amount_ledger_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)


class QuantityAmountGeneralLedgerPage(QuantityAmountGeneralLedgerBase, BaseTestCase):
    def switch_to_quantity_amount_general_ledger_frame(self):
        self.switch_to_frame(self.quantity_amount_general_ledger_frame())

    def click_quantity_amount_general_ledger_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)


class MultiColumnLedgerPage(MultiColumnLedger, BaseTestCase):
    def switch_to_multi_column_ledger_frame(self):
        self.switch_to_frame(self.multi_column_ledger_frame())

    def click_multi_column_ledger_buttons(self, button):
        kv_id = {'打印': 'print', '导出': 'export', '确定': 'filter-submit', '重置': 'filter-reset'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def multi_subject_filtration(self, short_subject, subject):
        self.click(self.filter_span())
        self.type(self.subject_input(), short_subject)
        self.click(self.subject_selector(subject))
        self.click_multi_column_ledger_buttons('确定')
        self.wait(1)


class AccountingBalancePage(AccountingBalanceBase, BaseTestCase):
    def switch_to_accounting_balance_frame(self):
        self.switch_to_frame(self.accounting_balance_frame())

    def click_accounting_balance_buttons(self, button):
        kv_id = {'查询': 'refresh', '打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def accounting_balance_filtration(self, accounting_item):
        self.click(self.accounting_filter_trigger())
        self.click(self.accounting_items(accounting_item))
        self.click_accounting_balance_buttons('查询')


class AccountingDetailPage(AccountingDetailBase, BaseTestCase):
    def switch_to_accounting_detail_frame(self):
        self.switch_to_frame(self.accounting_detail_frame())

    def click_accounting_detail_buttons(self, button):
        kv_id = {'查询': 'refresh', '打印': 'print', '导出': 'export'}
        self.js_click(self.buttons(kv_id.get(button)))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def accounting_detail_filtration(self, accounting_item):
        self.click(self.accounting_filter_trigger())
        self.click(self.accounting_items(accounting_item))
        self.click_accounting_detail_buttons('查询')

    def select_subject(self, subject):
        self.click(self.subject_box(subject))
