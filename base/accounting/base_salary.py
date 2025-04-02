class SalaryBase:
    @staticmethod
    def buttons(button_id):
        return f'//*[@id="{button_id}"]'

    @staticmethod
    def salary_frame():
        return 'wages'

    @staticmethod
    def salary_voucher_info():
        return f'//span[@id="voucher-info"]'

    @staticmethod
    def del_button_in_table(name):
        return f'//input[@value="{name}"]//parent::div//preceding-sibling::div//span[contains(@class,"del")]'

    @staticmethod
    def add_button_in_table(name):
        return f'//input[@value="{name}"]//parent::div//preceding-sibling::div//span[contains(@class,"add")]'

    @staticmethod
    def salary_template():
        return '//a[text()="工资表.xls"]'

    @staticmethod
    def import_radio(import_type=None):
        if import_type:
            return '//input[@id="gssbb"]'
        else:
            return '//input[@id="wage"]'

    @staticmethod
    def file_input():
        return '//input[@id="importWages-file"]'

    @staticmethod
    def import_area_buttons(button):
        return f'//button[text()="{button}"]'
