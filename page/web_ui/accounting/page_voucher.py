from base.accounting.base_voucher import VoucherDetailBase, VoucherBase

from base.base_case import BaseTestCase


class VoucherDetailPage(VoucherDetailBase, BaseTestCase):
    def switch_to_voucher_detail_frame(self):
        self.switch_to_frame(self.voucher_detail_frame())
        self.close_voucher_details_tips()

    def close_voucher_details_tips(self):
        if self.is_element_visible(self.voucher_details_tips()):
            self.click(self.voucher_details_tips())

    def click_buttons(self, button_id):
        self.click(self.view_voucher_buttons(button_id))

    def click_voucher_conform_delete_buttons(self, button):
        self.click(self.voucher_conform_delete_buttons(button))

    def is_voucher_entry_visible(self, abstract):
        return self.is_element_visible(self.voucher_entry_abstract(abstract))

    def get_voucher_summary(self, line):
        return self.get_text(self.voucher_summary(line))

    def voucher_details_select_sub_account_by_label(self, label, item):
        self.type(self.voucher_details_sub_account_input_by_label(label), f'{item}\n')


class VoucherPage(VoucherBase, BaseTestCase):
    def switch_to_voucher_frame(self):
        self.switch_to_frame(self.voucher_frame())

    def type_voucher_entry_by_class_name(self, class_name, idx, summary):
        self.click(self.voucher_entry_div(class_name, idx))
        self.type(self.voucher_entry_input(class_name, idx), summary)

    def get_text_from_voucher_entry_current_balance(self, idx):
        return self.get_text(self.voucher_entry_current_balance(idx))

    def select_voucher_entry_subject(self, idx, subject, class_name='col_subject'):
        self.click(self.voucher_entry_div(class_name, idx))
        if subject:
            self.click(self.voucher_entry_subject_selector(subject))

    def select_voucher_entry_subject_by_idx(self, idx, subject, class_name='col_subject'):
        self.click(self.voucher_entry_div(class_name, idx))
        self.type(self.voucher_entry_subject_input(idx), f'{subject}\n')
        self.wait(0.5)

    def type_voucher_entry(self, idx, summary, subject, debit=0, credit=0):
        self.type_voucher_entry_by_class_name('col_summary', idx, summary)
        self.select_voucher_entry_subject(idx, subject)
        if debit:
            self.type_voucher_entry_by_class_name('col_debite', idx, debit)
        elif credit:
            self.type_voucher_entry_by_class_name('col_credit', idx, credit)

    def click_conform_save_voucher_buttons(self):
        if self.is_element_visible(self.conform_save_voucher_buttons()):
            self.click(self.conform_save_voucher_buttons())

    def click_buttons(self, button):
        kv_id = {'保存并新增': 'renew',
                 '保存': 'save',
                 '复制': 'copy',
                 '现金流量': 'isCash',
                 '保存为凭证模板': 'saveAsTemp',
                 '从模板生成凭证': 'createWithTemp',
                 '红字冲销': 'writeOff',
                 '选项': 'userSetting',
                 '保存并新增B': 'renewB',
                 '保存B': 'saveB',
                 '平行记账': 'parallel',
                 '删除': 'delete'}
        self.js_click(self.buttons(kv_id.get(f"{button}")))

    def is_button_visible(self, button):
        kv_id = {'保存并新增': 'renew',
                 '保存': 'save',
                 '复制': 'copy',
                 '现金流量': 'isCash',
                 '保存为凭证模板': 'saveAsTemp',
                 '从模板生成凭证': 'createWithTemp',
                 '红字冲销': 'writeOff',
                 '选项': 'userSetting',
                 '保存并新增B': 'renewB',
                 '保存B': 'save',
                 '平行记账': 'parallel',
                 '删除': 'delete'}
        return self.is_element_visible(self.buttons(kv_id.get(button)))

    def click_input_buttons(self, button):
        if self.is_element_visible(self.input_buttons(button)):
            self.click(self.input_buttons(button))
