class CollectionFollowUpBase:
    @staticmethod
    def follow_up_services(service):
        """
        收款跟进页面，切换服务类型
        @param service:
        @return:
        """
        return f'//div[@class="tab_list"]//span[text()="{service}"]'

    @staticmethod
    def follow_up_buttons(button_name):
        """
        收款跟进，主页面按钮
        @param button_name:
        @return:
        """
        return f'//div[contains(@id,"follow-control")]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def follow_up_dropdown_buttons(button_name):
        """
        下拉按钮
        @param button_name:
        @return:
        """
        return f'//ul[contains(@id,"dropdown-menu")]//li[contains(text(),"{button_name}")]'

    @staticmethod
    def follow_up_input(placeholder):
        """
        输入框
        @param placeholder:
        @return:
        """
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def follow_up_search_button():
        return '//div[contains(@id,"follow-control")]//button//i[@class="el-icon-search"]'

    @staticmethod
    def follow_up_table_line_buttons(company_name, button_name):
        return f'//div[@class="table_con"]//span[contains(text(),"{company_name}")]' \
               f'//ancestor::div[@class="table_line"]//span[text()="{button_name}"]'

    @staticmethod
    def follow_up_table_line_check_box(company_name):
        return f'//div[@class="table_con"]//span[contains(text(),"{company_name}")]' \
               f'//ancestor::div[@class="table_line"]//span[@class="el-checkbox__input"]'

    @staticmethod
    def collection_details_input(label):
        return f'//div[@class="charge-content"]//label[contains(text(),"{label}")]' \
               f'//following-sibling::div//input[not(@disabled)]'

    @staticmethod
    def collection_details_input_dropdown_items(item):
        return f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//span[text()="{item}"]'

    @staticmethod
    def collection_details_buttons(button_name):
        return f'//div[@class="charge-content"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def collection_details_month_select(month):
        return f'//div[@class="charge-content"]//label[contains(text(),"收款期间")]' \
               f'//following-sibling::div//span[text()="{month}"]'

    @staticmethod
    def collection_details_bottom_buttons(button_name):
        return f'//div[@class="charge-content"]//div[@class="charge-btn"]//button//span[text()="{button_name}"]'

    @staticmethod
    def collection_details_tips():
        return '//div[@aria-label="提示"]//parent::div[not(contains(@style,"display: none;"))]' \
               '//div[@aria-label="提示"]//span[text()="忽略，直接收款"]'

    @staticmethod
    def collection_renew_contract_area_buttons(button):
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="续签合同提示"]' \
               f'//span[@class="dialog-footer"]//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def select_collection_class_in_table(line):
        return f'(//div[@aria-modal="true"]//div[not(contains(@style,"none"))]//table//input[@placeholder="请选择"])[{line}]'

    @staticmethod
    def select_collection_class_in_table_items(item, biz_type):
        """
        @param item:
        @param biz_type: bussIcon:工商，acctIcon:财务
        @return:
        """
        return f'//div[not(contains(@style,"display: none;")) and @class="el-select-dropdown el-popper"]' \
               f'//ul[contains(@class,"select-dropdown")]//span[contains(@title,"{item}")]//span[@class="{biz_type}"]'

    @staticmethod
    def add_line_button():
        return '//button/span[contains(text(),"增加收款项目")]'

    @staticmethod
    def delete_line_button(line):
        return f'(//tr//div[@class="cell"]//div[text()="删除"])[{line}]'

    @staticmethod
    def service_year_selector(direction):
        """
        @param direction:">","<"
        @return:
        """
        return f'//span[contains(@class,"year") and text()="{direction}"]'

    @staticmethod
    def service_year():
        return '//span[contains(@class,"sf_time_year_con")]'

    @staticmethod
    def amount_input_in_table(item, cell):
        """
        @param item:
        @param cell: 本次收款：1，本次折扣：2
        @return:
        """
        return f'(//div[@aria-modal="true"]//div[not(contains(@style,"none"))]' \
               f'//table//div[contains(@title,"{item}")]//ancestor::td//following-sibling::td//input)[{cell}]'

    @staticmethod
    def del_button_in_table(line):
        return f'(//div[@aria-modal="true"]//div[not(contains(@style,"none"))]' \
               f'//table//input//ancestor::td' \
               f'//following-sibling::td//div[@class="deleteAble"])[{line}]'

    @staticmethod
    def switch_biz_type_on_top(biz_name):
        return f'//div[@class="tab_list"]//span[text()="{biz_name}"]'

    @staticmethod
    def select_year_in_table():
        return '//table//input[@placeholder="选择年份"]'

    @staticmethod
    def year_selector(year):
        return f'//a[@class="cell" and text()="{year}"]'

    @staticmethod
    def amount_input_in_table_bookkeeping(cell):
        """
        @param cell: 本次收款：2，本次折扣：3
        @return:
        """
        return f'(//div[text()="账本费"]//ancestor::td//following-sibling::td//input)[{cell}]'

    @staticmethod
    def add_collection_class_button():
        return '//ul[@class="el-select-group"]//span[text()="新增"]'

    @staticmethod
    def collection_class_select_div():
        return '//div[@class="el-select-dropdown el-popper" and not(contains(@style,"display"))]'

    @staticmethod
    def collection_class_popup_scroll_bar():
        return 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-scrollbar__bar.is-vertical > div'

    @staticmethod
    def add_collection_class_inputs(span):
        """
        @param span: 收费项目名称/服务类型归属
        @return:
        """
        return f'//div[@aria-label="新增"]//span[text()="{span}："]//following-sibling::div//input'

    @staticmethod
    def add_collection_class_belong_to(biz_type):
        return f'//div[not(contains(@style,"none"))]/div[@class="el-scrollbar"]//span[text()="{biz_type}"]'

    @staticmethod
    def add_collection_class_buttons(button):
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="新增"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def collection_class_operate_button(item_title, button):
        """

        @param item_title:
        @param button: delete,editor
        @return:
        """
        return f'//ul[@class="el-select-group"]//span[@title="{item_title}"]' \
               f'//following-sibling::div//a[contains(@class,"{button}")]'

    @staticmethod
    def conform_delete_collection_class_buttons(button):
        return f'//div[not(contains(@style,"none"))]/div[@aria-label="提示"]' \
               f'//span[@class="dialog-footer"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def collection_filters(label, item):
        return f'//label[contains(text(),"{label}：")]//following-sibling::span//span[text()="{item}"]'

    @staticmethod
    def collection_checkboxes_by_company(company):
        return f'//span[text()="{company}"]//ancestor::div[contains(@class,"table_line_item")]' \
               f'//preceding-sibling::div//input[@type="checkbox"]//preceding-sibling::span'

    @staticmethod
    def collection_switch_year(direction=None):
        """
        @param direction:1:left,3:right
        @return:
        """
        if direction:
            return f'(//div[@class="table_switchYear"]//child::span)[{direction}]'
        else:
            return f'(//div[@class="table_switchYear"]//child::span)[2]'

    @staticmethod
    def collection_status_in_table_by_company(company, mon, status):
        """
        @param company:
        @param mon:
        @param status: 已审核——audited，未收款——waitFee，未审核——waitAudit
        @return:
        """
        return f'//span[text()="{company}"]//ancestor::div[contains(@class,"table_line_item")]' \
               f'//following-sibling::div//span[text()="{mon}" and contains(@class,"{status}")]'

    @staticmethod
    def collection_list_next_period_item_by_company(company, index):
        return (f'(//span[text()="{company}"]//ancestor::div[@class="table_line"]'
                f'//div[contains(@class,"table_line_item")]//div[contains(@class,"nextCollection_item")])[{index}]')


class CollectionAuditBase:
    @staticmethod
    def collection_audit_buttons(button_name):
        return f'//div[@class="collection_audit"]//button//span[text()="{button_name}"]'

    @staticmethod
    def audit_customer_input():
        return f'//div[@class="collection_audit"]//label[contains(text(),"客户")]//following-sibling::span//input'

    @staticmethod
    def audit_overrule_reason():
        return f'//div[@aria-label="驳回收款"]//textarea'

    @staticmethod
    def audit_overrule_buttons(button_name):
        return f'//div[@aria-label="驳回收款"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def collection_audit_table_checkbox(company_name):
        return f'//div[@class="table_con"]//td[not(contains(@class,"is-hidden"))]' \
               f'//div[text()="{company_name}"]//ancestor::td//preceding-sibling::td//label'

    @staticmethod
    def audit_collection_operations(operation):
        return f'(//div[text()="{operation}"]//ancestor::td[not(contains(@class,"hidden")) ' \
               f'and contains(@class,"col-opt")]//div[text()="{operation}"])[1]'

    @staticmethod
    def audit_collection_conform_cancel(button_name):
        return f'//div[@aria-label="取消收费"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def audit_collection_conform_delete(button_name):
        return f'//div[@aria-label="确认删除"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def audit_conform_collection_button(button_name):
        return f'//div[@class="el-drawer__wrapper charge-wrap" and not(contains(@style,"display"))]' \
               f'//div[@class="charge-content"]//button//span[text()="{button_name}"]'

    @staticmethod
    def audit_conform_delete_buttons(button):
        return f'//div[@aria-label="确认删除"]//button//span[contains(text(),"{button[0]}")]'
