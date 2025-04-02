from base.accounting.base_lookup_voucher import LookupVoucherBase
from base.base_case import BaseTestCase


class LookupVoucherPage(BaseTestCase, LookupVoucherBase):
    def switch_to_lookup_voucher_frame(self):
        self.switch_to_frame(self.voucher_list_frame())
        self.wait_for_ready_state_complete()
        self.wait(3)
        self.close_voucher_tips()

    def close_voucher_tips(self):
        if self.is_element_visible(self.voucher_merge_tips()):
            self.click(self.voucher_merge_tips())
        if self.is_element_visible(self.voucher_tips()):
            self.click(self.voucher_tips())

    def click_list_voucher_checkbox(self, summary):
        self.check_if_unchecked(self.voucher_list_checkbox(summary))

    def get_text_from_voucher_list_audit_cell(self, summary):
        return self.get_text(self.voucher_list_audit_cell(summary))

    def is_voucher_exist(self, summary):
        return self.is_element_visible(self.voucher_list_checkbox(summary))

    def click_multiple_voucher_checkbox(self, summary_list):
        for _ in summary_list:
            if self.is_voucher_exist(_):
                self.click_list_voucher_checkbox(_)

    def click_voucher_buttons(self, button):
        kv_id = {'新增': 'voucherAdd',
                 '批量复制': 'copyVoucher',
                 '整月复制': 'copyAllMonth',
                 '凭证打印': 'voucherPrint',
                 '列表打印': 'printAll',
                 '导出': 'exportImpotMod',
                 '审核': 'audit',
                 '反审核': 'revAudit',
                 '凭证号整理': 'tidy',
                 '凭证号移动': 'vch-insert',
                 '导入凭证': 'import',
                 '导出列表': 'export',
                 '删除': 'delete',
                 '刷新': 'refresh',
                 '确认删除': 'delFjzSure',
                 '全选': 'cb_grid'}
        self.js_click(self.voucher_buttons(kv_id.get(f"{button}")))
        if '导出' in button:
            self.wait(3)

    def click_voucher_list_conform_delete_buttons(self, button='确定'):
        self.click(self.conform_delete_buttons(button))

    def delete_voucher_by_summary(self, summary):
        if isinstance(summary, str):
            self.click_list_voucher_checkbox(summary)
        else:
            self.click_multiple_voucher_checkbox(summary)
        self.click_voucher_buttons('删除')
        self.click_voucher_list_conform_delete_buttons()

    def click_refresh(self):
        self.click(self.refresh_button())

    def click_voucher_template_download_button(self, button):
        self.click(self.voucher_import_buttons(button))
        if button == '下载模版' or button == '导入':
            self.wait(2)

    def send_file_to_voucher_import_file_select_input(self, file_path):
        self.choose_file(self.voucher_import_file_select_input(), file_path)

    def get_text_from_voucher_list_total_line(self):
        return self.get_text(self.voucher_list_total_line())

    def get_text_from_voucher_import_result(self):
        return self.get_text(self.voucher_import_result())
