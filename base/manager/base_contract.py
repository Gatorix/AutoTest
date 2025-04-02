class ContractBase:
    @staticmethod
    def normal_contract_button(button_text):
        """
        合同页面所有普通按钮
        @param button_text: 普通按钮的名称，如：新增、删除等
        @return: xpath
        """
        return f'//button[@class="el-button el-button--primary"]//span[text()="{button_text}"]'

    @staticmethod
    def dropdown_contract_button(button_text):
        """
        合同页面所有下拉按钮
        @param button_text: 下拉按钮名称
        @return:
        """
        return f'//button[contains(@class,"el-button el-button--primary el-dropdown-selfdefine")]' \
               f'//span[contains(text(),"{button_text}")]//ancestor::button'

    @staticmethod
    def dropdown_contract_dropdown_button(button_text):
        """
        合同页面所有下拉按钮的二级按钮
        @param button_text: 二级按钮名称
        @return:
        """
        return f'//ul[@class="el-dropdown-menu el-popper"]//li[text()="{button_text}"]'

    @staticmethod
    def contract_id_in_table(contract_id):
        """
        合同编号所在的表格行
        @param contract_id: 合同编号
        @return:
        """
        return f'//div[@id="contractTable" and contains(@class,"el-table--scrollable-y")]' \
               f'//td[not(contains(@class,"hidden"))]//div[text()="{contract_id}"]'

    @staticmethod
    def contract_input(input_placeholder):
        """
        合同页面所有输入框，根据placeholder定位
        @param input_placeholder: 输入框默认的占位字符
        @return:
        """
        return f'//input[contains(@placeholder,"{input_placeholder}")]'

    @staticmethod
    def search_button(search_placeholder):
        """
        合同页面所有的搜索按钮（放大镜）
        @param search_placeholder: 搜索按钮旁边的输入框占位字符
        @return:
        """
        return f'//input[contains(@placeholder,"{search_placeholder}")]//following-sibling::div//button//i'

    @staticmethod
    def add_contract_input(label_text):
        """
        新增合同子页面中的输入框
        @param label_text: 新增合同页面输入框前的标签名
        @return:
        """
        return f'//div[@class="addContract_title"]//following-sibling::div[@class="addContract_content"]' \
               f'//label[contains(text(),"{label_text}")]//following-sibling::div//input'

    @staticmethod
    def add_contract_save_button():
        """
        新增合同子页面保存按钮
        @return:
        """
        return '//div[@class="addContract_title"]//button'

    @staticmethod
    def service_type(service_type):
        """
        新增合同页面服务选择按钮
        @param service_type: 代账服务或工商服务
        @return:
        """
        return f'//div[@class="addContract_title"]//following-sibling::div' \
               f'//label//span[text()="{service_type}"]'

    @staticmethod
    def bookkeeping_agency_input(label_text):
        """
        新增合同页面勾选代账服务后弹出的相关输入框
        @param label_text: 输入框前的标签名称
        @return:
        """
        return f'//div[@class="addContract_title"]//following-sibling::div' \
               f'//div[@class="sections accountService"]//label[text()="{label_text}"]//parent::div//input'

    @staticmethod
    def conform_button_in_table():
        return f'//*[@id="contractTable" and not(contains(@style,"display: none"))]' \
               f'//td[not(contains(@class,"hidden"))]//button//span[text()="审核"]'

    @staticmethod
    def continue_button_in_table():
        return f'//*[@id="contractTable" and not(contains(@style,"display: none"))]' \
               f'//td[not(contains(@class,"hidden"))]//button//span[text()="续签"]'

    @staticmethod
    def button_in_table(button_name):
        return f'//*[@id="contractTable" and not(contains(@style,"display: none"))]' \
               f'//td[not(contains(@class,"hidden"))]//button//span[text()="{button_name}"]'

    @staticmethod
    def button_in_table_by_company_name(company, button):
        return f'//div[@id="contractTable" and not(contains(@style,"none"))]' \
               f'//div[text()="{company}"]//ancestor::td//following-sibling::td[not(contains(@class,"hidden"))]' \
               f'//button/span[text()="{button}"]'

    @staticmethod
    def contract_type_in_line_by_company_name(company):
        return f'//div[@id="contractTable" and not(contains(@style,"none"))]//div[text()="{company}"]' \
               f'//ancestor::td//following-sibling::td[not(contains(@class,"hidden"))][15]/div/div'

    @staticmethod
    def spacial_dropdown_button(line):
        """
        特殊的下拉菜单
        """
        return f'(//div[@class="el-table el-table--fit el-table--striped el-table--border ' \
               f'el-table--enable-row-hover el-table--enable-row-transition"]//tbody//tr)[{line}]//input[@placeholder="请选择"][1]'

    @staticmethod
    def contract_business_service_table_amount_input_by_line(line):
        return (f'(//div[@class="el-table el-table--fit el-table--striped el-table--border '
                f'el-table--enable-row-hover el-table--enable-row-transition"]//tbody//tr)[{line}]//td[4]//input')

    @staticmethod
    def normal_button(button):
        return f'//span[@class="operateBtn"]//button//span[contains(text(),"{button}")]'

    @staticmethod
    def normal_dropdown_items(item):
        return f'//li[text()="{item}"]'

    @staticmethod
    def spacial_dropdown_drop_button(business_type):
        """
        特殊下拉菜单下面的二级按钮
        @return:
        """
        return (f'//div[@class="el-select-dropdown el-popper" and not(contains(@style,"display"))]'
                f'//div[@class="el-scrollbar"]//span[text()="{business_type}"]')

    @staticmethod
    def add_contract_table_service_date_input(placeholder, line=1):
        return f'//table//tr[{line}]//input[@placeholder="{placeholder}"]'

    @staticmethod
    def contract_inputbox(contract_id):
        return f'//div[@id="contractTable" and contains(@class,"el-table--scrollable-y")]' \
               f'//td[not(contains(@class,"hidden"))]//div[text()="{contract_id}"]' \
               f'//ancestor::td//preceding-sibling::td//span[@class="el-checkbox__input"]'

    @staticmethod
    def contract_checkbox(contract_id):
        return f'//div[@id="contractTable" and not(contains(@style,"display: none;"))]' \
               f'//td[not(contains(@class,"hidden"))]//div[text()="{contract_id}"]' \
               f'//ancestor::td//preceding-sibling::td//span[@class="el-checkbox__input"]'

    @staticmethod
    def contract_id_by_company_name(company_name):
        return f'//div[@id="contractTable" and not(contains(@style,"display: none;"))]' \
               f'//td[not(contains(@class,"hidden"))]//div[text()="{company_name}"]' \
               f'//ancestor::td//preceding-sibling::td//div[@class="cell"]/div/div[text()]'

    @staticmethod
    def modify_contract_buttons(button):
        return f'//div[@class="edit-contract"]//div[@class="edit-btn"]//span[text()="{button}"]'

    @staticmethod
    def modify_contract_service_total_amount(line):
        return f'//div[@class="edit-contract"]//tr[{line}]/td[4]//input'

    @staticmethod
    def contract_confirm_delete(button_name):
        """
        点击删除后，弹出界面中的删除按钮
        @param button_name:
        @return:
        """
        return f'//div[@class="el-dialog__footer"]//button//span[text()="{button_name}"]'

    @staticmethod
    def return_contract_check(button_name):
        """
        合同反审核按钮
        @param button_name:
        @return:
        """
        return f'//*[@id="contractTable"]/div[5]/div[2]/table/tbody/tr/td[20]/div/div/div/div[2]/button//span[text()="{button_name}"]'

    @staticmethod
    def derive_button(button_name):
        return f'//div[@class="el-dialog__wrapper exportDialog" and not(contains(@style,"display"))]//div[@class="dialog-footer"]//span[text()="{button_name}"]'

    @staticmethod
    def stop_date():
        return f'//div[@class="item-content"]//span[@class="el-input__prefix"]'

    @staticmethod
    def continue_contract(button_name):
        return f'//*[@id="contractTable"]/div[5]/div[2]/table/tbody/tr/td[20]/div/div/div/div[4]/button/span[text()="{button_name}"]'

    @staticmethod
    def contract_checkbox_by_period(period):
        return f'//div[contains(@class,"mainTable") and not(contains(@style,"display: none;"))]' \
               f'//div[text()="{period}"]//ancestor::td//preceding-sibling::td[not(contains(@class,"hidden"))]' \
               f'//input//preceding-sibling::span'

    @staticmethod
    def change_person_area_input():
        return f'//div[@aria-label="变更业务员"]//input'

    @staticmethod
    def change_person_area_selector(person):
        return f'//div[@class="organization-popover bottom-popover isAutoWidth" and not(contains(@style,"none"))]' \
               f'//span[contains(@class,"label") and contains(.,"{person}")]'

    @staticmethod
    def area_buttons(area, button):
        return f'//div[@aria-label="{area}"]//button/span[contains(text(),"{button}")]'

    @staticmethod
    def termination_area_inputs_by_label(label):
        return f'//div[@aria-label="提前终止"]//span[text()="{label}"]//following-sibling::div//input'

    @staticmethod
    def change_collection_area_inputs_by_label(label):
        return f'//div[@aria-label="收款变更"]//span[text()="{label}"]//following-sibling::div//input'

    @staticmethod
    def termination_area_month_selector(mon):
        return f'//div[@class="el-picker-panel el-date-picker el-popper" and not(contains(@style,"none"))]' \
               f'//table[contains(@class,"month")]//a[text()="{mon}"]'

    @staticmethod
    def termination_area_textarea():
        return f'//div[@aria-label="提前终止"]//textarea'

    @staticmethod
    def change_collection_area_textarea():
        return f'//div[@aria-label="收款变更"]//textarea'

    @staticmethod
    def change_collection_step_2_inputs(label):
        return f'//section[@id="contractInfor"]//label[text()="{label}"]//following-sibling::div//input'

    @staticmethod
    def apply_invoice_area_inputs_by_label(label):
        return f'//div[@class="el-drawer__wrapper contractBillApplyDrawer"]' \
               f'//label[text()="{label}"]//following-sibling::div//input'

    @staticmethod
    def apply_invoice_area_button():
        return '//div[@class="el-drawer__wrapper contractBillApplyDrawer"]//button/span'

    @staticmethod
    def adj_type_area_input():
        return '//div[@aria-label="调整续费类型"]//label//following-sibling::div//input'

    @staticmethod
    def adj_type_area_dropdown_items(item):
        return f'//div[@class="el-select-dropdown el-popper" and not(contains(@style,"none"))]//li/span[text()="{item}"]'

    @staticmethod
    def adj_type_area_buttons():
        return f'//div[@aria-label="调整续费类型"]//button/span[contains(text(),"确定")]'


class ContractChangeRecordBase:
    @staticmethod
    def record_list_change_type():
        return '//div[@class="cell" and text()="合同修改"]'


class ContractInvoiceBase:
    @staticmethod
    def checkbox_in_line_by_company_name(company_name):
        return f'//div[text()="{company_name}"]/parent::td//preceding-sibling::td//input//preceding-sibling::span'

    @staticmethod
    def buttons_in_line_by_company_name(company_name, button):
        return f'//div[@class="mainTable"]//div[text()="{company_name}"]' \
               f'/parent::td//following-sibling::td//button/span[text()="{button}"]'

    @staticmethod
    def overrule_invoice_textarea():
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="驳回收款"]//textarea'

    @staticmethod
    def overrule_invoice_buttons(button):
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="驳回收款"]//button/span[contains(text(),"{button[0]}")]'

    @staticmethod
    def complete_invoice_button():
        return '//button/span[text()="完成开票"]'


class ContractExpireBase:
    @staticmethod
    def filter_item_by_label(label, item):
        return f'//label[contains(text(),"{label}")]//following-sibling::span/span[contains(text(),"{item}")]'

    @staticmethod
    def filter_inputs_by_placeholder(placeholder):
        return f'//div[@id="control"]//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def company_search_button():
        return '//div[@id="control"]//button/i'

    @staticmethod
    def normal_buttons(button):
        return f'(//div[@class="select_list"]//button/span[contains(text(),"{button}")]' \
               f' | //div[@id="control"]//button/span[contains(text(),"{button}")])[1]'

    @staticmethod
    def checkbox_in_line_by_company_name_or_contract_id(name):
        return f'//*[text()="{name}"]//ancestor::td[not(contains(@class,"hidden"))]' \
               f'//preceding-sibling::td//input//preceding-sibling::span'

    @staticmethod
    def buttons_in_ling_by_company_name_or_contract_id(name, button):
        return f'//*[text()="{name}"]//ancestor::td[not(contains(@class,"hidden"))]' \
               f'//following-sibling::td//span[text()="{button}"]'

    @staticmethod
    def export_type_button(method):
        return f'//span[text()="{method}"]'

    @staticmethod
    def export_buttons(button):
        return f'//div[@aria-label="导出"]//button//span[text()="{button}"]'
