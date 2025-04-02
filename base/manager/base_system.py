class DepartmentAndStaffBase:
    @staticmethod
    def department_and_staff_normal_button(button_name):
        return f'//div[@class="operatebtn-wrap"]//span[text()="{button_name}"]//parent::button'

    @staticmethod
    def new_staff_input_boxes(label):
        return f'//div[@aria-label="新增职员"]//label[contains(text(),"{label}")]//parent::div//input'

    @staticmethod
    def new_staff_buttons(button):
        return f'//div[@aria-label="新增职员"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def new_staff_alert():
        return '//div[@aria-label="提示"]//button//span[text()="我知道了"]'

    @staticmethod
    def search_staff_input_box():
        return '//input[@placeholder="职员名称/手机号"]'

    @staticmethod
    def search_staff_button():
        return '//input[@placeholder="职员名称/手机号"]//following-sibling::div//button'

    @staticmethod
    def list_checkbox(staff):
        return f'//span[text()="{staff}"]//ancestor::td//preceding-sibling::td//span[contains(@class,"input")]'

    @staticmethod
    def conform_delete_buttons(button):
        return f'//div[@aria-label="删除职员"]//button//span[contains(text(),"{button[0]}")]'


class SystemBinBase:
    @staticmethod
    def system_bin_inputs_by_label(label):
        return f'//label[contains(text(),"{label}")]//following-sibling::span//input'

    @staticmethod
    def system_bin_buttons(button):
        return f'//button/span[text()="{button}"]'

    @staticmethod
    def system_bin_check_all_span():
        return '//div[@class="table_hd"]//label[@class="el-checkbox"]/span/span'

    @staticmethod
    def system_bin_conform_delete(button):
        return f'//div[@aria-label="彻底删除账套"]//button//span[text()="{button}"]'

    @staticmethod
    def system_bin_conform_again_input():
        return '//div[@aria-label="再次提醒"]//input'

    @staticmethod
    def system_bin_conform_again_button():
        return '//div[@aria-label="再次提醒"]//button//span[contains(text(),"确")]'

    @staticmethod
    def system_bin_button_in_line_by_company(company, button):
        return (f'(//span[text()="{company}"]//ancestor::div[@class="table_line_item"]'
                f'//following-sibling::div)//span[text()="{button}"]')

    @staticmethod
    def system_bin_conform_recover_buttons(button):
        return f'//div[@aria-label="恢复账套"]//span[text()="{button}"]'
