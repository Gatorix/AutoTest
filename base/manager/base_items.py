class BaseItems:
    @staticmethod
    def tab_item(head_items):
        return f'//div[contains(text(),"{head_items}")]'

    @staticmethod
    def inventory_input_box(placeholder):
        return f'//div[@class="itemInventoryDetails"]//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def inventory_search_button(placeholder):
        return f'//div[@class="itemInventoryDetails"]' \
               f'//input[contains(@placeholder,"{placeholder}")]//following-sibling::div//button'

    @staticmethod
    def inventory_buttons(button_name):
        return f'//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def inventory_dropdown_buttons(button_name):
        return f'//li[@class="el-dropdown-menu__item" and contains(text(),"{button_name}")]'

    @staticmethod
    def inventory_table_checkbox(company_name):
        return f'//td[contains(text(),"{company_name}")]' \
               f'//preceding-sibling::td//span[contains(@class,"input")]'

    @staticmethod
    def receive_or_return_items_close_button():
        return '//button//span[text()="关闭页面"]'

    @staticmethod
    def receive_or_return_items_submit_button():
        return f'//button//span[contains(text(),"提")]'

    @staticmethod
    def receiving_items_input_box(placeholder):
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def receiving_items_table_input():
        return f'(//tbody//td[@class="td-item"])[1]'

    @staticmethod
    def receiving_items_select(item):
        return f'(//div[@class="item-search-list"])[5]//span[text()="{item}"]'

    @staticmethod
    def table_buttons(button_name):
        return f'(//td[not(contains(@class,"hidden"))]//span[text()="内部移交"]' \
               f'//ancestor::td//following-sibling::td//' \
               f'span[@class="td-operations-item" and text()="{button_name}"])[1]'

    @staticmethod
    def company_list(company_name):
        return f'//div[@class="customerList-container"]//li[contains(text(),"{company_name}")]'

    @staticmethod
    def ads():
        return '//button//span[text()="我知道了"]'

    @staticmethod
    def trans_inputs(placeholder):
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def trans_list(person):
        return f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//span[contains(text(),"{person}")]'

    @staticmethod
    def receiving_table_button(company_name):
        return f'//td[contains(text(),"{company_name}")]//following-sibling::td[@class="td-operate"]'

    @staticmethod
    def check_all():
        return '(//span[@class="el-checkbox__inner"])[1]'

    @staticmethod
    def trans_conform():
        return '//button//span[text()="接 收"]'

    @staticmethod
    def trans_submit():
        return '//div[@class="el-dialog__footer"]//button[@class="el-button el-button--primary"]//span[text()="确认提交"]'

    @staticmethod
    def input_box(placeholder):
        return f'//div[@class="itemInventoryDetails"]//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def search_button():
        return '//div[@class="itemInventoryDetails"]//input[contains(@placeholder,"客户名称")]//following-sibling::div//button'

    @staticmethod
    def download_items_template():
        return '//div[@aria-label="导入客户物品清单"]//a[text()="下载客户物品清单模板"]'

    @staticmethod
    def transfer_record_button(company):
        return f'//td[text()="{company}"]//following-sibling::td[text()="交接记录"]'

    @staticmethod
    def transfer_record_list_button(button):
        # return f'//td[not(contains(@class,"is-hidden"))]//span[text()="内部移交"]' \
        #        f'//ancestor::td//following-sibling::td//span[text()="{button}"]'
        return f'//td[not(contains(@class,"is-hidden"))]//div[@class="cell"]//span[text()="{button}"]'

    @staticmethod
    def transfer_record_conform_delete():
        return f'//div[@aria-label="提示"]//div[@class="el-message-box__btns"]//button//span[contains(text(),"确定")]'

    @staticmethod
    def upload_file_input():
        return f'//div[@aria-label="导入客户物品清单"]//input[@type="file"]'

    @staticmethod
    def upload_file_buttons(button):
        return f'//div[@aria-label="导入客户物品清单"]//button/span[text()="{button}"]'

    @staticmethod
    def dropdown_buttons(button):
        return f'//ul[contains(@class,"el-dropdown-menu")]//li[text()[contains(.,"{button}")]]'

    @staticmethod
    def area_buttons(area, button):
        return f'//div[@aria-label="{area}"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def area_textarea(area):
        return f'//div[@aria-label="{area}"]//textarea'

    @staticmethod
    def conform_alert():
        return f'//*[not(contains(@style,"none"))]/div[@aria-label="提示"]//button/span[contains(text(),"确定")]'

    @staticmethod
    def button_in_line_by_company(company):
        return f'//td[text()="{company}"]//following-sibling::td[text()="交接记录"]'

    @staticmethod
    def company_name_in_line(company):
        return f'//td[not(contains(@class,"hidden"))]//p[text()="{company}"]'