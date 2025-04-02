class VoucherDetailBase:
    @staticmethod
    def voucher_detail_frame():
        return 'voucherDetail'

    @staticmethod
    def voucher_details_tips():
        return f'//div[@id="uploadAttachTipsSingle"]//div[text()="我知道了"]'

    @staticmethod
    def view_voucher_buttons(button_id):
        return f'//div[@id="isCashBtn"]//a[@id="{button_id}"]'

    @staticmethod
    def voucher_conform_delete_buttons(button):
        return f'//div[text()="系统提示"]//ancestor::tr//input[@type="button" and @value="{button}"]'

    @staticmethod
    def voucher_entry_abstract(abstract):
        return f'//table[@id="voucher"]//div[contains(text(),"{abstract}")]'

    @staticmethod
    def voucher_summary(line):
        return f'(//td[@data-edit="summary"]//div)[{line}]'

    @staticmethod
    def voucher_details_sub_account_input_by_label(label):
        return f'//label[contains(text(),"{label}")]//following-sibling::span//input'

    @staticmethod
    def voucher_details_sub_account_dropdown_items(item):
        return f'//div[@class="droplist"]//div[text()="{item}"]'


class VoucherBase:
    @staticmethod
    def voucher_frame():
        return 'voucher'

    @staticmethod
    def voucher_entry_div(class_name, idx):
        return f'(//table[@id="voucher"]//td[@class="{class_name}"])[{idx}]'

    @staticmethod
    def voucher_entry_current_balance(idx):
        return f'(//table[@id="voucher"]//tr[contains(@class,"entry_item")])[{idx}]//div[@class="curBalance"]//a'

    @staticmethod
    def voucher_entry_subject_input(idx):
        return f'(//table[@id="voucher"]//tr[contains(@class,"entry_item")])[{idx}]//td[contains(@class,"subject")]//input'

    @staticmethod
    def voucher_entry_input(class_name, idx):
        if 'col_summary' in class_name:
            return f'(//table[@id="voucher"]//td[@class="{class_name}"])[{idx}]//textarea'
        else:
            return f'(//table[@id="voucher"]//td[@class="{class_name}"])[{idx}]//input'

    @staticmethod
    def voucher_entry_subject_selector(subject):
        return f'//div[@id="COMBO_WRAP"]//div[contains(text(),"{subject}")]'

    @staticmethod
    def conform_save_voucher_buttons(button='确定'):
        return f'//div[contains(@style,"visible")]//input[@value="{button}"]'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def input_buttons(button):
        return f'//input[@type="button" and @value="{button}"]'
