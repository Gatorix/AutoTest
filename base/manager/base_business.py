class BusinessServiceBase:
    @staticmethod
    def service_management_normal_button(button_name):
        return f'//span[text()="{button_name}"]//parent::button'

    @staticmethod
    def service_management_dropdown_button(button):
        if '导出' in button:
            return f'//li/span[text()="{button}"]'
        else:
            return f'//li[text()="{button}"]'

    @staticmethod
    def conform_stop_service():
        return '//div[@aria-label="停止服务"]//button/span[text()="确 定"]'

    @staticmethod
    def service_input(placeholder):
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def business_service_search_button():
        return '//div[@id="bus-control"]//button//i[@class="el-icon-search"]'

    @staticmethod
    def checkbox_in_line_by_company(company):
        return f'//span[text()="{company}"]/parent::div/preceding-sibling::div//input//preceding-sibling::span'

    @staticmethod
    def buttons_in_line_by_company(company, button):
        return f'//span[text()="{company}"]/parent::div/following-sibling::div//span[text()="{button}"]'

    @staticmethod
    def collect_file_tooltip_buttons(button):
        return f'//div[@role="tooltip" and @aria-hidden="false"]//span[contains(text(),"{button}")]'

    @staticmethod
    def collect_file_tooltip_labels(label):
        # return f'//div[@role="tooltip" and @aria-hidden="false"]//label[@title="{label}"]//input//preceding-sibling::span'
        return f'//div[@role="tooltip" and @aria-hidden="false"]//label[@title="{label}"]'

    @staticmethod
    def collection_file_tooltip_textarea():
        return f'//div[@role="tooltip" and @aria-hidden="false"]//textarea'

    @staticmethod
    def conform_tips_on_top_buttons(button):
        return f'//div[@class="el-dialog el-dialog--small"]//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def new_customer_input():
        return '(//div[@aria-label="新增客户"]//input)[1]'

    @staticmethod
    def new_customer_type():
        return '(//div[@aria-label="新增客户"]//input)[2]'

    @staticmethod
    def customer_exist():
        return '//div[@aria-label="客户已存在提醒"]//div[text()="当前客户已存在！"]'

    @staticmethod
    def new_customer_type_selector(customer_type):
        return f'//ul//li//span[text()="{customer_type}"]'

    @staticmethod
    def new_customer_buttons(button_name):
        return f'//div[@aria-label="新增客户"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def stop_service_buttons(button):
        return f'//div[@class="button-group stopServiceBtn"]//span[text()="{button}"]'

    @staticmethod
    def conform_recover_service_buttons(button):
        return f'//div[@aria-label="恢复服务"]//button//span[contains(text(),"{button[0]}")]'


class BusinessReportBase:
    @staticmethod
    def service_management_normal_button(button_name):
        return f'//div[@class="controlLine"]//span[text()="{button_name}"]//parent::button'

    @staticmethod
    def stop_service_buttons(button):
        return f'//div[@class="button-group stopServiceBtn"]//span[text()="{button}"]'

    @staticmethod
    def filter_by_label(label, item):
        return f'//div[contains(text(),"{label}")]/parent::div//div[contains(@class,"tab-item") and contains(text(),"{item}")]'

    @staticmethod
    def service_input(placeholder):
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def business_report_search_button():
        return '//div[@class="controlLine"]//button//i[@class="el-icon-search"]'

    @staticmethod
    def report_checkbox_in_line_by_company(company):
        return f'//span[text()="{company}"]//ancestor::td//preceding-sibling::td//input//preceding-sibling::span'

    @staticmethod
    def report_buttons_in_line_by_company(company, button):
        return f'//span[text()="{company}"]//ancestor::td//following-sibling::td//span[contains(text(),"{button}")]'

    @staticmethod
    def conform_report_buttons(button):
        return f'//div[@aria-label="确认结果"]//button//span[contains(text(),"{button}")]'

    @staticmethod
    def report_type_radio(report_type):
        return f'//div[@aria-label="设置年报方式"]//span[text()="{report_type}"]/ancestor::label'

    @staticmethod
    def report_setting_buttons(button):
        return f'//div[@aria-label="设置年报方式"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def report_type_div(company):
        return f'//span[text()="{company}"]//ancestor::td//following-sibling::td[4]//div'

    @staticmethod
    def conform_already_report_button():
        return f'//div[@aria-label="确认申报"]//button//span[text()="确 定"]'
