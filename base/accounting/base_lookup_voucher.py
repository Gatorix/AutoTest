class LookupVoucherBase:
    @staticmethod
    def voucher_list_frame():
        return 'voucherList'

    @staticmethod
    def voucher_tips():
        return f'//div[@id="uploadAttachTipsList"]//div[text()="我知道了"]'

    @staticmethod
    def voucher_merge_tips():
        return f'//*[@class="voucherMerge-tips"]//button[@id="voucherMergeOprateTips"]'

    @staticmethod
    def tips_mask():
        return f'//div[@id="uploadAttachTipsList"]'

    @staticmethod
    def voucher_list_checkbox(summary):
        return f'//p[contains(text(),"{summary}")]//parent::td//preceding-sibling::td//input'

    @staticmethod
    def voucher_list_audit_cell(summary):
        return f'//p[contains(text(),"{summary}")]//parent::td//following-sibling::td[contains(@aria-describedby,"auditor")]'

    @staticmethod
    def dropdown_buttons(button_name):
        return f'//div[@class="ui-btn-menu"]//a[text()="{button_name}"]'

    @staticmethod
    def dropdown_button_items(button_name, item):
        return f'//div[@class="ui-btn-menu"]//a[text()="{button_name}"]//following-sibling::div//a[text()="{item}"]'

    @staticmethod
    def normal_buttons(button_name):
        return f'//div[@class="right"]//a[text()="{button_name}"]'

    @staticmethod
    def conform_delete_buttons(button='确定'):
        return f'//div[@id="delFjzAll"]//button[text()="{button}"]'

    @staticmethod
    def refresh_button():
        return '//a[@id="refresh"]'

    @staticmethod
    def voucher_buttons(button):
        return f'//*[@id="{button}"]'

    @staticmethod
    def voucher_import_buttons(button_name):
        return f'//a[text()="{button_name}"]'

    @staticmethod
    def voucher_import_file_select_input():
        return f'//*[@id="import-file-info"]'

    @staticmethod
    def voucher_list_total_line():
        return f'//*[@id="page_right"]//div'

    @staticmethod
    def voucher_import_result():
        return f'//*[@id="import-result"]'
