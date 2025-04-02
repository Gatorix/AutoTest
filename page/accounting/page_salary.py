from base.accounting.base_salary import SalaryBase

from base.base_case import BaseTestCase


class SalaryPage(SalaryBase, BaseTestCase):
    def switch_to_salary_frame(self):
        self.switch_to_frame(self.salary_frame())
        self.wait(3)

    def click_buttons(self, button):
        id_kv = {'导入': 'importBtn', '复制上月': 'copyLastMonth', '保存': 'save-wages',
                 '计提工资': 'jtgz', '发放工资': 'ffgz', '导出': 'saveAsExcel'}
        self.js_click(self.buttons(id_kv.get(button)))
        self.wait(1)
        if '导出' in button:
            self.wait(5)

    def get_text_from_salary_voucher_info(self):
        voucher_info = self.get_text(self.salary_voucher_info()).split(' ')
        provision_of_wages_info = voucher_info[1] if '计提工资' in voucher_info[1] else voucher_info[2]
        pay_salary_info = voucher_info[1] if '发放工资' in voucher_info[1] else voucher_info[2]
        return provision_of_wages_info, pay_salary_info

    def click_import_area_buttons(self, button):
        self.click(self.import_area_buttons(button))
        self.wait(1)

    def click_salary_template(self):
        self.click(self.import_radio())
        self.click(self.salary_template())
        self.wait(3)

    def click_import_radio(self, import_type=None):
        self.click(self.import_radio(import_type))

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)

    def click_del_button_in_table(self, name):
        self.click(self.del_button_in_table(name))
