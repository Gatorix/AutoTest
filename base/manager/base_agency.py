class AgencyAccountBase:

    @staticmethod
    def agency_account_service(service):
        """
        服务管理页面，切换服务类型
        """
        return f'//div[@class="tab_list"]//span[text()="{service}"]'

    @staticmethod
    def agency_title(title):
        return f'//span[@title="{title}"]'

    @staticmethod
    def agency_account_service_droplist(service):
        """
        服务管理页面，切换服务类型
        """
        return f'//ul[@class="el-dropdown-menu el-popper"]//*[text()="{service}"]'

    @staticmethod
    def accounting_title():
        return '//span[@id="myCompany"]'

    @staticmethod
    def delete_book(company):
        return f'//div[@aria-label="删除账套"]//div[text()="{company}"]' \
               f'//parent::div//following-sibling::div//span[text()="删除成功"]'

    @staticmethod
    def follow_up_buttons(button_name):
        """
        收款跟进，主页面按钮
        """
        return f'//div[@id="account-follow-control"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def follow_up_dropdown_buttons(button_name):
        """
        下拉按钮
        """
        return f'//ul[contains(@id,"dropdown-menu")]//li[contains(text(),"{button_name}")]'

    @staticmethod
    def service_input(placeholder):
        """
        代账服务-服务管理-客户名称输入框
        """
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def service_search_button():
        """
        代账服务-服务管理-客户名称搜索按钮
        """
        return '//div[@id="service-control-con"]//button//i[@class="el-icon-search"]'

    @staticmethod
    def tax_search_button():
        """
        代账服务-服务管理-报税选项卡页面-客户名称搜索按钮
        """
        return '//div[@class="taxMenuOrigin"]//button//i[@class="el-icon-search"]'

    @staticmethod
    def service_table_line_buttons(company_name, button_name):
        """
        根据客户名字确定所在行的某个按钮名称
        """
        return f'//div[@class="table_con"]//span[contains(text(),"{company_name}")]' \
               f'//ancestor::div[@class="table_line"]//span[text()="{button_name}"]'

    @staticmethod
    def follow_up_table_line_check_box(company_name):
        return f'//div[@class="table_con"]//span[contains(text(),"{company_name}")]' \
               f'//ancestor::div[@class="table_line"]//span[@class="el-checkbox__input"]'

    @staticmethod
    def taxes_details_input(index):
        """
        根据税名确定税金输入按钮：只用“增值税（一般纳税人）”即可定位类似多行控件，只需要要变换下标值即可：1/2/3/4/5
        """
        return f'//li[@class="el-select-dropdown__item selected"]//span//ancestor::div' \
               f'//div[@class="txsj_conItem"][{index}]' \
               f'//input[@class="el-input__inner" and not(contains(@placeholder, "请选择"))]'

    @staticmethod
    def click_service_type_droplist(label):
        """
        ”添加服务“弹框中，点击【服务类型】后的下拉框
        """
        return f'//div[@class="fwsd_con"]//label[contains(text(),"{label}")]' \
               f'//following-sibling::div//input[@class="el-input__inner"]'

    @staticmethod
    def click_tax_type_droplist():
        """
        创建账套页面，点击纳税性质下拉框
        """
        return f'//label[text()="纳税性质:"]//following::input'

    @staticmethod
    def click_select_tax_type(label):
        """
        选择【纳税性质】:一般纳税人、小规模纳税人
        """
        return f'//div[text()="{label}"]'

    @staticmethod
    def accounting_standards_input():
        return '//label[contains(text(),"会计制度")]//parent::div//following-sibling::div//input'

    @staticmethod
    def accounting_standards_list_items(item):
        return f'//div[@class="droplist"]//div[contains(@class,"list-item") and text()="{item}"]'

    @staticmethod
    def accounting_standards_selector():
        return '//select[@id="system-sel"]'

    @staticmethod
    def add_service_select_type(service_type):
        """
        ”添加服务“弹框中，选择某一个服务类型，如个体工商户报税
        """
        return f'//div[@class="el-select-dropdown el-popper" and not(contains(@style,"display"))]//span[text()="{service_type}"]'

    @staticmethod
    def receipt_details_input(label, index):
        """
        收票业务，根据票据名称输入数量、金额、税额
        index:从1开始，1-2-3
        """
        return f'//div[@class="sp_con_wraper"]//label[contains(text(),"{label}")]' \
               f'//following-sibling::div//input[@class="sp_item_txt"][{index}]'

    @staticmethod
    def input_enable_period_year():
        """创建账套页面，填写启用期间-年份"""
        return f'//input[@id="invocation-year"]'

    @staticmethod
    def input_enable_period_month():
        """创建账套页面，填写启用期间-期数（月份）"""
        return f'//input[@id="invocation-period"]'

    @staticmethod
    def begin_create_accounts(label):
        """创建账套页面，开始创建按钮"""
        return f'//div//a[@id="btn-establish" and text()="{label}"]'

    @staticmethod
    def collection_details_input_dropdown_items(item):
        return f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//span[text()="{item}"]'

    @staticmethod
    def collection_details_buttons(button_name):
        return f'//div[@class="charge-content"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def service_details_month_select(service_type, month):
        return f'//div[@class="el-dialog__body"]//label[contains(text(),"{service_type}")]' \
               f'//following-sibling::div//span[text()="{month}"]'

    @staticmethod
    def locate_months_dropdownbox():
        return f'//input[@placeholder="首次确认后不允许修改"]'

    @staticmethod
    def begin_month_select(month):
        return f'//table[@class="el-month-table"]//div//a[@class="cell" and text()="{month}"]'

    @staticmethod
    def page_popups_bottom_buttons(button_name, types):
        """
        填写税金页面弹框底部的【取 消】按钮、【确 定】按钮
        """
        return f'//div[@aria-label="{types}"]//parent::div[not(contains(@style,"display"))]' \
               f'//div[@aria-label="{types}"]//button//span[text()="{button_name}"]'

    @staticmethod
    def invoice_aria_bottom_buttons(button, label):
        # return f'//div[@aria-label="{label}"]//button//span[text()="{button}"]'
        return f'//div[@aria-label="{label}"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def agency_input_box(types, placeholder):
        return f'//div[@aria-label="{types}"]//parent::div[not(contains(@style,"display"))]' \
               f'//div[@aria-label="{types}"]//input[@placeholder="{placeholder}"]'

    @staticmethod
    def agency_textarea(types):
        return f'//div[@aria-label="{types}"]//parent::div[not(contains(@style,"display"))]' \
               f'//div[@aria-label="{types}"]//textarea'

    @staticmethod
    def agency_followup_table_buttons(title, button):
        return f'//table[@class="el-table__body"]//div[@title="{title}"]//ancestor::tr//span[text()="{button}"]'

    @staticmethod
    def dropdown_item(item):
        return f'//ul[@class="el-select-group"]//li//span[text()="{item}"]'

    @staticmethod
    def audit_page_popups_bottom_buttons(button_name, types):
        """
        审税金页面弹框底部的【取 消】按钮、【确 定】按钮
        types：决定审税金页面、填写税金页面，或其他页面
        """
        return f'//div[@aria-label="{types}"]//div[@class="el-dialog__footer"]//' \
               f'span[text()="{button_name}"]'

    @staticmethod
    def service_details_bottom_buttons(button_name):
        """
        不需报税按钮、重新报税按钮、取消按钮、确定按钮等相关按钮
        """
        return f'//div[@class="el-dialog__footer"]//span[text(' \
               f')="温馨提示：给非本岗位的职员派工后，该职员就拥有派工岗位的权限"]//parent::div//following::button//span[text()="{button_name}"] '

    @staticmethod
    def tip_bottom_buttons(button_name):
        """弹框提示：当前岗位已派工，是否继续派工？"""
        return f'//div[text()="当前岗位已派工，是否继续派工？"]//parent::div//parent::div//parent::div//' \
               f'div[@class="el-dialog__footer"]//span[text()="{button_name}"]'

    @staticmethod
    def collection_details_tips():
        return '//div[@aria-label="提示"]//parent::div[not(contains(@style,"display: none;"))]' \
               '//div[@aria-label="提示"]//span[text()="忽略，直接收款"]'

    @staticmethod
    def dispatch_input(placeholder):
        """
        派工-人员-人名/部门输入框
        """
        return f'//input[contains(@placeholder,"{placeholder}")]'

    @staticmethod
    def dispatch_search_button(dispatch_style):
        """
        @param dispatch_style:请输入部门/请输入人员
        派工-人员/部门-搜索按钮，根据输入框定位其后的搜索按钮
        """
        return f'//input[@placeholder="{dispatch_style}"]//following-sibling::div' \
               '//button[@class="el-button el-button--default"]//i[@class="el-icon-search"]'

    @staticmethod
    def dispatch_add_button(button_name):
        """
        派工-人员/部门-添加按钮
        """
        return f'//div[@class="pg_bt_l_list_item" and @style=""]//child::div[1]//span//span[text()="{button_name}"]'

    @staticmethod
    def dispatch_style(style_name):
        """
        派工-人员-选择人名类型：报税员、记账员等
        """
        return f'//div[@class="pg_bt_hd"]//span[contains(text(),"{style_name}")]'

    @staticmethod
    def person_or_department_dispatch(label):
        """人员派工or部门派工"""
        return f'//div[@class="pg_bt_l_hd"]//span[text()="{label}"]'

    @staticmethod
    def dispatch_or_query(label):
        """派工查询 or 派工"""
        return f'//div[@class="el-dialog__body"]//span[text()="{label}"]'

    @staticmethod
    def dispatch_change(stuff, button):
        """转派工or删除按钮"""
        return f'//div[@aria-label="派工"]//span[text()="{button}"]//parent::div' \
               f'//preceding-sibling::div[text()="{stuff}"]//following-sibling::div//span[text()="{button}"]'

    @staticmethod
    def dispatch_record_row():
        return '//div[@aria-label="派工"]//div[@class="pgTable_con"]/div'

    @staticmethod
    def dispatch_delete():
        """操作玩转派工后，此时的【删除】按钮"""
        return f'//span[text()="派工"]//parent::div//following-sibling::div//span[text()="删除"]'

    @staticmethod
    def dispatch_department():
        """转派工_部门选择框"""
        return f'//div[@aria-label="派工"]//div[@class="pgTable_line" and not(contains(@style,"none"))]' \
               f'//label[text()="部门"]//following-sibling::span//input'

    @staticmethod
    def select_department(dep):
        """转派工_选择要转派工的新部门"""
        return f'//div[@role="tooltip" and @aria-hidden="false"]//span[contains(.,"{dep}")]'

    @staticmethod
    def dispatch_staff():
        """转派工_转入职员选择框"""
        return f'//div[@class="pgTable_line" and not(contains(@style,"display: none;"))]' \
               f'//span//label[text()="转入职员"]//following-sibling::div//input'

    @staticmethod
    def exist_dispatch_tip():
        return '//div[@aria-label="提示"]//p[contains(text(),"已存在")]'

    @staticmethod
    def select_staff(staff):
        """转派工_选择要转入的职员（选择下拉列表中的第一个，即li[1]）"""
        return f'//div[@class="el-select-dropdown el-popper" and not(contains(@style,"display: none;"))]' \
               f'//ul//li//span[contains(text(),"{staff}")]'

    @staticmethod
    def dispatch_ok_button(button):
        """转派工最后的确定或取消按钮"""
        return f'//div[not(contains(@style,"none")) and @class="pgTable_line"]//span[text()="{button}"]'

    @staticmethod
    def follow_up_already():
        return '//span[@class="td-followup"]'

    @staticmethod
    def export_type_button(method):
        return f'//span[text()="{method}"]'

    @staticmethod
    def export_buttons(button):
        return f'//div[@aria-label="导出"]//button//span[text()="{button}"]'

    @staticmethod
    def dispatch_query_checkbox_by_company(company):
        return f'//div[text()="{company}"]//preceding-sibling::div//input//preceding-sibling::span'

    @staticmethod
    def dispatch_query_checkbox():
        return f'//div[text()=""]//preceding-sibling::div//input//preceding-sibling::span'


class ServiceAuditBase:
    """服务审计"""

    @staticmethod
    def audit_buttons(button_name):
        """表格上排右侧按钮"""
        return f'//div[@id="service-control"]//button[@class="el-button el-button--primary el-button--small"]//span[' \
               f'text()="{button_name}"]'

    @staticmethod
    def agency_account_stop_services(service_stop_or_not_text):
        """表格上排左侧按钮：【正常服务】、【已停止服务】选项卡页面"""
        return f'//div[@class="control_line clearfix"]//span[text()="{service_stop_or_not_text}"]'  # 正常服务or已停止服务

    @staticmethod
    def audit_buttons_droplist(button_name):
        """表格上排按钮-【更多】下拉框"""
        return f'//div[@id="service-control"]//div[@class="control_right"]' \
               f'//div//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def tax_audit_buttons(button_name):
        """代账服务-服务管理-报账选项页面-表格上排按钮"""
        return f'//div[@id="taxMenuCenter"]//button[@class="el-button el-button--primary el-button--small"]//span[' \
               f'text()="{button_name}"]'

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
    def audit_table_checkbox(company_name):
        """选择某公司：通过点击checkbox按钮"""
        return f'//div[@class="table_con"]//span[text()="{company_name}"]//parent::div//parent::div//preceding' \
               '-sibling::div//label'

    @staticmethod
    def audit_table_company_name(company_name):
        return f'//div[@class="table_con"]//span[text()="{company_name}"]'

    @staticmethod
    def tax_upload_file_input():
        return '//div[not(contains(@style,"display"))]/div[@aria-label="报税"]//input[@type="file"]'

    @staticmethod
    def select_table_first_checkbox(label):
        """审税金弹框中选择某一账期的税金，默认选择第一行账期的税金"""
        # return f'//div[@class="ssjTable_line_item"]//label'
        return f'//div[@class="ssjTable_line_item"]//ancestor::div//div[@aria-label="{label}"]' \
               f'//div[@class="ssjTable_con"]//span[@class="el-checkbox__inner"]'

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
    def add_tips(button_name):
        return f'//div[@aria-label="添加提示"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def audit_conform_button(button_name):
        """弹框中跳出的确认、取消等按钮"""
        return f'//div[@class="el-message-box"]//button//span[contains(text(),"{button_name}")]'

    @staticmethod
    def audit_conform_collection_button(button_name):
        return f'(//div[@class="charge-content"]//button//span[text()="{button_name}"])[2]'

    @staticmethod
    def ignore_set_tip():
        return '//div[@aria-label="账套剩余数量不足"]//button//span[text()="继续创建"]'

    @staticmethod
    def add_tax_line_button():
        return '//div[@aria-label="填写税金"]//div[@class="txsj_con"]//span[text()="+"]'

    @staticmethod
    def tax_select_input_box():
        return '//div[@aria-label="填写税金"]//input[@placeholder="请选择"]'

    @staticmethod
    def tax_type():
        return '//div[contains(@class,"el-select-dropdown el-popper") and not(contains(@style,"display: none;"))]' \
               '//span[text()="增值税（小规模纳税人）"]'


class ReceiveInvoiceRecordBase:
    @staticmethod
    def checkbox_in_table_by_company(company):
        return f'//div[@class="cell" and text()="{company}"]//parent::td[not(contains(@class,"hidden"))]' \
               f'//preceding-sibling::td//input//parent::span'

    @staticmethod
    def operate_button_in_table_by_company(company, button):
        return f'//div[@class="cell" and text()="{company}"]//parent::td' \
               f'//following-sibling::td[not(contains(@class,"hidden"))]//span[@class="opeitem" and text()="{button}"]'

    @staticmethod
    def conform_delete_buttons(button):
        return f'//div[@aria-label="删除提示"]//button//span[contains(text(),"{button[0]}")]'

    @staticmethod
    def filter_inputs_by_label(label):
        return f'//label[text()="{label}："]//following-sibling::span//input'

    @staticmethod
    def query_button():
        return f'//button//span[text()="查询"]'


class ReceiveInvoiceBase:
    @staticmethod
    def receive_invoice_checkbox_in_table_by_company(company):
        return f'//span[text()="{company}"]//parent::div//preceding-sibling::div//input//preceding-sibling::span'

    @staticmethod
    def inputs_by_placeholder():
        return f'//input[contains(@placeholder,"客户名称")]'

    @staticmethod
    def search_button():
        return f'//input[contains(@placeholder,"客户名称")]//following-sibling::div//i'

    @staticmethod
    def normal_buttons(button):
        return f'//button//span[text()="{button}"]'

    @staticmethod
    def dropdown_buttons(button):
        return f'//ul[@class="ul-more"]//li[contains(text(),"{button}")]'

    @staticmethod
    def company_filter():
        return '//input[@placeholder="组织架构"]'

    @staticmethod
    def org_tree_company():
        return '//span[contains(@class,"company")]//following-sibling::span[@class="el-tree-node__label"]'

    @staticmethod
    def org_tree_person(person):
        return f'//span[contains(@class,"person")]' \
               f'//following-sibling::span[contains(@class,"el-tree-node") and contains(.,"{person}")]'

    @staticmethod
    def root_org():
        # return '(//div[@class="organization-popover bottom-popover"]//div[contains(@class,"el-tree-node__content")])[1]'
        return '(//div[@class="organization-popover bottom-popover isAutoWidth" and not(contains(@style,"none"))]//span[@class="el-tree-node__label"])[1]'

    @staticmethod
    def receive_invoice_operate_button_in_table_by_company(company, button):
        return f'//span[text()="{company}"]//parent::div//following-sibling::div//span[text()="{button}"]'


class BookkeepingBase:
    @staticmethod
    def buttons_in_line_by_company(company, button):
        return f'//span[text()="{company}"]//parent::div' \
               f'/parent::div/following-sibling::div//div[@class="operateList"]//span[text()="{button}"]'

    @staticmethod
    def bookkeeping_search_input():
        return f'//input[contains(@placeholder,"客户名称")]'

    @staticmethod
    def bookkeeping_search_button():
        return '//input[contains(@placeholder,"客户名称")]//following-sibling::div//button//i[@class="el-icon-search"]'

    @staticmethod
    def checkbox_in_line_by_company(company):
        return f'//span[text()="{company}"]//parent::div/' \
               f'parent::div/preceding-sibling::div//input//preceding-sibling::span'

    @staticmethod
    def lark_invoice_mark_in_line(company):
        return f'//span[text()="{company}"]//parent::div/parent::div/following-sibling::div//span[contains(@class,"lackInfo")]'

    @staticmethod
    def lark_invoice_mark_inputs_by_label(label):
        return f'//div[@aria-label="缺票"]//label[contains(text(),"{label}")]' \
               f'//following-sibling::div//input[not(@readonly="readOnly")]'

    @staticmethod
    def lark_invoice_mark_month_selector(mon):
        return f'//div[@aria-label="缺票"]//div[@class="multiList" and not(contains(@style,"none"))]' \
               f'//span[text()="{mon}"]'

    @staticmethod
    def lark_invoice_mark_conform_button():
        return '//div[@aria-label="缺票"]//div[@class="multiList" and not(contains(@style,"none"))]' \
               '//span[contains(text(),"确")]'

    @staticmethod
    def lark_invoice_mark_label():
        return f'//div[@aria-label="缺票"]//label[contains(text(),"备注")]'

    @staticmethod
    def lark_invoice_mark_memo():
        return '//div[@aria-label="缺票"]//textarea'

    @staticmethod
    def lark_invoice_mark_buttons(button):
        return f'//div[@aria-label="缺票"]//span[@class="dialog-footer"]//button//span[contains(text(),"{button[0]}")]'


class FileTaxesBase:
    pass


class GatherInvoiceBase:
    @staticmethod
    def gather_frame():
        return f'//div[@id="app"]/following-sibling::iframe'

    @staticmethod
    def invoice_tab():
        return '//a[text()="发票导入设置"]/parent::li'

    @staticmethod
    def in_line_buttons_by_invoice_name(name, button):
        return f'//td[text()="{name}"]//preceding-sibling::td/a[@class="{button}"]'

    @staticmethod
    def conform_box_cancel_buttons():
        return f'//div[@id="confirmBoxWrapper"]//span/button[@id="cancelDelBtn"]'
