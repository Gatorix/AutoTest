class CustomerBase:
    @staticmethod
    def customer_buttons(button_name):
        return f'//div[@id="customerMenuCenter"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def customer_dropdown_buttons(button_name):
        return f'//ul[contains(@id,"dropdown-menu")]//li[text()="{button_name}"]'

    @staticmethod
    def customer_middle_input(placeholder):
        return f'//div[@class="middle-wrap"]//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def customer_middle_search_button():
        return '//div[@class="middle-wrap"]//button//i[@class="el-icon-search"]'

    @staticmethod
    def customer_table_checkbox(company_name):
        return f'//div[@class="editCustomerName" and text()="{company_name}"]' \
               f'//ancestor::td//preceding-sibling::td//span[contains(@class,"input")]'

    @staticmethod
    def customer_list_select_all_span():
        return '//div[@id="customerRouter"]//table//thead//label/span/span'

    @staticmethod
    def customer_list_total_line():
        return '//div[@class="pagination-wrap"]//span[contains(@class,"total")]'

    @staticmethod
    def customer_list_show_num_input():
        return '//div[@class="pagination-wrap"]//input[@type="text"]'

    @staticmethod
    def customer_list_show_num_popper(text):
        return f'//div[contains(@class,"el-select-dropdown el-popper") and not(contains(@style,"display: none;"))]' \
               f'//span[contains(text(),"{text}")]'

    @staticmethod
    def customer_table_button(company_name, button_name):
        return f'//div[@class="editCustomerName" and text()="{company_name}"]' \
               f'//ancestor::td//following-sibling::td//span[text()="{button_name}"]'

    @staticmethod
    def customer_ads():
        return '//div[@class="desc-img"]//button//span[text()="我知道了"]'

    @staticmethod
    def new_customer_input():
        return '(//div[@aria-label="新增客户"]//input)[1]'

    @staticmethod
    def new_customer_type():
        return '(//div[@aria-label="新增客户"]//input)[2]'

    @staticmethod
    def delete_followup_record(record):
        return f'//div[@aria-label="跟进记录"]//div[text()="{record}"]//ancestor::td' \
               f'//following-sibling::td//span[text()="删除"]'

    @staticmethod
    def conform_delete_followup_record():
        return '//div[@aria-label="提示"]//span[text()="确定删除"]'

    @staticmethod
    def customer_exist():
        return '//div[@aria-label="客户已存在提醒"]//div[text()="当前客户已存在！"]'

    @staticmethod
    def new_customer_type_selector(customer_type):
        return f'//ul//li//span[text()="{customer_type}"]'

    @staticmethod
    def new_customer_buttons(button_name):
        return f'//div[not(contains(@style,"display"))]/div[contains(@aria-label,"客户")]' \
               f'/div[@class="el-dialog__footer"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def new_customer_more_info_button():
        return '//div[contains(@aria-label,"客户")]//span[text()="更多信息"]'

    @staticmethod
    def new_customer_more_info_tax_properties():
        return f'//div[not(contains(@style,"display"))]/div[contains(@aria-label,"客户")]' \
               f'//label[text()="纳税性质"]//following-sibling::div//input'

    @staticmethod
    def new_customer_more_info_labels(label):
        return f'//div[contains(@aria-label,"客户")]//div[contains(@class,"addRightFix")]//div[text()="{label}"]'

    @staticmethod
    def new_customer_more_info_inputs_by_label(label):
        return f'//div[@aria-label="新增客户"]//label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def new_customer_more_info_tax_add_line_button():
        return '//div[contains(@aria-label,"客户")]//button//span[text()="新增行"]'

    @staticmethod
    def new_customer_more_info_tax_type_table(line, cell=1):
        return f'//div[contains(@aria-label,"客户")]//table//tr[{line}]//input[{cell}]'

    @staticmethod
    def new_customer_more_info_popper_span(text):
        return f'//div[@class="el-select-dropdown el-popper" and not(contains(@style,"display"))]//span[text()="{text}"]'

    @staticmethod
    def delete_customer_buttons(button_name):
        return f'//div[@aria-label="删除客户"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def mark_conform():
        return '//div[@aria-label="标记"]//div[@class="el-dialog__footer"]//button//span[contains(text(),"确")]'

    @staticmethod
    def follow_up_detail():
        return '//textarea[@id="followupInputtxt"]'

    @staticmethod
    def followup_detail_buttons(button):
        return f'//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def close_followup():
        return '//div[@aria-label="跟进记录"]//button[@aria-label="Close"]'

    @staticmethod
    def grant_permission_buttons(button):
        return f'//div[@aria-label="授权客户看账"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def close_grant_permission():
        return '//div[@aria-label="授权客户看账"]//button[@aria-label="Close"]'

    @staticmethod
    def tax_box_buttons(button):
        return f'//div[@aria-label="标记税控盘"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def customer_manager_buttons(button):
        return f'//div[@aria-label="分配客户经理"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def close_customer_manager():
        return '//div[@aria-label="分配客户经理"]//button[@aria-label="Close"]'

    @staticmethod
    def customer_area_label_buttons(area_label, button_name):
        return f'//div[@aria-label="{area_label}"]//span[text()="{button_name}"]//parent::button'

    @staticmethod
    def customer_area_label_textarea(area_label):
        return f'//div[@aria-label="{area_label}"]//textarea'

    @staticmethod
    def customer_area_label_inputs(area_label, placeholder, index=1):
        if '日期' in placeholder:
            return f'//div[@aria-label="{area_label}"]//input[@placeholder="{placeholder}"]'
        else:
            return f'(//div[@aria-label="{area_label}"]//input[@placeholder="{placeholder}"])[{index}]'

    @staticmethod
    def customer_date_table(date):
        return f'//td[@class="available today current"]//span[contains(normalize-space(),"{date}")]'

    @staticmethod
    def customer_dropdown_list_1_item(item):
        return f'//ul[@class="el-select-group__wrap"]//span[text()="{item}"]'

    @staticmethod
    def re_dispatch_customer_manager_alert_buttons(button):
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="提示"]//button/span[contains(text(),"{button[0]}")]'

    @staticmethod
    def add_dispatch_button_by_name(name):
        return f'//span[text()="{name}"]//ancestor::div[@class="pg_bt_l_list_itemCon"]//span[text()="添加"]'

    @staticmethod
    def merge_customer_area_buttons(button):
        return f'//div[@aria-label="合并客户"]//button/span[contains(text(),"{button[0]}")]'

    @staticmethod
    def merge_customer_area_input():
        return '//div[@aria-label="合并客户"]//input'

    @staticmethod
    def merge_customer_area_dropdown(item):
        return f'//div[@class="el-scrollbar"]//span[text()="{item}"]'

    @staticmethod
    def modify_customer_inputs_by_label(label):
        return f'//div[@aria-label="修改客户"]//label[text()="{label}"]//following-sibling::div//input'

    @staticmethod
    def customer_in_line(customer):
        return f'//div[text()="{customer}"]'

    @staticmethod
    def modify_customer_conform_button():
        return f'(//div[@aria-label="修改客户"]//button/span[contains(text(),"确")])[4]'


class LostManageBase:
    @staticmethod
    def company_search_inputs():
        return f'//input[contains(@placeholder,"客户名称")]'

    @staticmethod
    def search_button():
        return '//div[@id="control"]//i[@class="el-icon-search"]'

    @staticmethod
    def lost_manage_normal_buttons(button):
        return f'//div[@id="control"]//button/span[text()="{button}"]'

    @staticmethod
    def checkbox_in_line_by_company_name(company):
        return f'//div[text()="{company}"]/parent::td//preceding-sibling::td//input//preceding-sibling::span'

    @staticmethod
    def buttons_in_line_by_company_name(company, button):
        return f'//div[text()="{company}"]/parent::td//following-sibling::td//span[text()="{button}"]'

    @staticmethod
    def area_buttons(area, button):
        return f'//div[@aria-label="{area}"]//button/span[contains(text(),"{button[0]}")]'
