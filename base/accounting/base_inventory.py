class InventorySettingBase:
    @staticmethod
    def inventory_setting_frame():
        return 'inventory-basicSetting'

    @staticmethod
    def inventory_setting_buttons(button_id):
        return f'//*[@id="{button_id}"]'

    @staticmethod
    def import_template():
        return '//a[text()="下载导入模板"]'

    @staticmethod
    def init_quantity_input_by_num(num):
        return f'//td[text()="{num}"]//following-sibling::td//input[@id="qty"]'

    @staticmethod
    def init_amount_input_by_num(num):
        return f'//td[text()="{num}"]//following-sibling::td//input[@id="amount"]'


class InventoryManageBase:
    @staticmethod
    def inventory_manage_frame():
        return 'inventory-management'

    @staticmethod
    def inventory_manage_buttons(button_id):
        if 'step' in button_id:
            return f'//a[@rel="{button_id}"]'
        else:
            return f'//*[@id="{button_id}"]'

    @staticmethod
    def inventory_sys_list_last_line_by_num(num):
        return f'//div[@id="pageThree"]//span[@class="accountNumber"]//input[@id="pdtCodeMatch" and @value="{num}"]'

    @staticmethod
    def buttons_text(button):
        return f'//a[text()="{button}"]'

    @staticmethod
    def add_inventory_type_inputs(label):
        return f'//label[contains(text(),"{label}")]//parent::div//following-sibling::div//input'

    @staticmethod
    def add_inventory_type_verify_label(label):
        return f'//label[contains(text(),"{label}")]//parent::div//following-sibling::div//label'

    @staticmethod
    def input_buttons(button):
        return f'//input[@type="button" and @value="{button}"]'

    @staticmethod
    def in_line_buttons_by_id(num, button):
        return f'//td[@title="{num}"]//following-sibling::td//a[text()="{button}"]'

    @staticmethod
    def in_line_checkbox_by_id(num):
        return f'//td[@title="{num}"]//preceding-sibling::td//input'

    @staticmethod
    def download_template():
        return '//a[text()="下载模版"]'

    @staticmethod
    def file_input():
        return '//input[@id="import-file-info"]'

    @staticmethod
    def import_result_success():
        return '(//div[@id="import-result"]//font)[1]'

    @staticmethod
    def import_result_fail():
        return '(//div[@id="import-result"]//font)[2]'


class InventoryWarehousingEntryBase:
    @staticmethod
    def warehousing_entry_frame():
        return 'inventory-stockIn'

    @staticmethod
    def inventory_warehousing_entry_buttons(button):
        return f'//*[@id="{button}"]'

    @staticmethod
    def text_buttons(button):
        return f'//a[text()="{button}"]'

    @staticmethod
    def import_type_radio(value):
        return f'//input[@name="importType" and @value="{value}"]'

    @staticmethod
    def file_input():
        return '//input[@id="importWages-file"]'

    @staticmethod
    def list_checkbox_by_bill_number(num):
        return f'//a[text()="{num}"]//parent::td//preceding-sibling::td//input'

    @staticmethod
    def input_buttons(button):
        return f'//input[@type="button" and @value="{button}"]'

    @staticmethod
    def change_type_input():
        return '//input[@id="add-skfptype-value"]'

    @staticmethod
    def change_type_dropdown_items(item):
        return f'//div[@id="add-skfptype-list"]/div[text()="{item}"]'

    @staticmethod
    def list_bill_type_cell(bill):
        return f'(//a[text()="{bill}"]//parent::td//following-sibling::td)[1]'

    @staticmethod
    def auto_gen_bill_by_type_radio(type_radio):
        radio_kv = {
            '按凭证自动生成入库单': 'voucher_radio',
            '按进项发票自动生成入库单': 'income_radio'
        }
        return f'//input[@id="{radio_kv.get(type_radio)}"]'

    @staticmethod
    def auto_gen_bill_step_span(step):
        step_kv = {
            '上一步': 'lastStep',
            '下一步': 'nextStep'
        }
        return f'//span[@id="{step_kv.get(step)}"]'

    @staticmethod
    def warehousing_entry_table_customer_td_by_bill_num(bill_num):
        return f'//*[text()="{bill_num}"]/parent::td//following-sibling::td[@aria-describedby="grid_customer"]'

    @staticmethod
    def warehousing_entry_table_customer_td_by_voucher_num(voucher_num):
        return f'//*[text()="{voucher_num}"]/parent::td//preceding-sibling::td[@aria-describedby="grid_customer"]'

    @staticmethod
    def warehousing_entry_select_all():
        return '//*[@id="cb_grid"]'


class InventoryNewEntryBase:
    @staticmethod
    def new_entry_frame():
        return 'stockBill'

    @staticmethod
    def inventory_new_entry_buttons(button):
        return f'//*[@id="{button}"]'

    @staticmethod
    def table_inputs(cell_id, line=1):
        return f'(//input[@id="{cell_id}"])[{line}]'

    @staticmethod
    def table_head_inputs(input_id):
        return f'//input[@id="{input_id}"]'

    @staticmethod
    def table_query_class_items(item):
        return f'//div[@style="display: block;"]//div[contains(text(),"{item}")]'


class InventoryOutboundEntryBase:
    @staticmethod
    def outbound_entry_frame():
        return 'inventory-stockOut'

    @staticmethod
    def inventory_outbound_buttons(button):
        return f'//*[@id="{button}"]'

    @staticmethod
    def text_buttons(button):
        return f'//a[text()="{button}"]'

    @staticmethod
    def import_type_radio(value):
        return f'//input[@name="importType" and @value="{value}"]'

    @staticmethod
    def file_input():
        return '//input[@id="importWages-file"]'

    @staticmethod
    def list_checkbox_by_bill_number(num):
        return f'//a[text()="{num}"]//parent::td//preceding-sibling::td//input'

    @staticmethod
    def input_buttons(button):
        return f'//input[@type="button" and @value="{button}"]'

    @staticmethod
    def change_type_input():
        return '//input[@id="add-skfptype-value"]'

    @staticmethod
    def change_type_dropdown_items(item):
        return f'//div[@id="add-skfptype-list"]/div[text()="{item}"]'

    @staticmethod
    def list_bill_type_cell(bill):
        return f'(//a[text()="{bill}"]//parent::td//following-sibling::td)[1]'


class InventorySummaryBase:
    @staticmethod
    def inventory_summary_frame():
        return 'inventory-summarySheet'

    @staticmethod
    def inventory_summary_buttons(button):
        button_id = {'打印': 'print', '导出': 'saveAsExcel', '刷新': 'refresh'}
        return f'//*[@id="{button_id.get(button)}"]'

    @staticmethod
    def checkboxes(name):
        box_id = {'按月汇总': 'showByMonth', '显示全部': 'showAll', '显示金额': 'showAmount'}
        return f'//input[@id="{box_id.get(name)}"]'

    @staticmethod
    def start_period_input():
        return '(//label[contains(text(),"日期")]//following-sibling::span//input)[1]'

    @staticmethod
    def end_period_input():
        return '(//label[contains(text(),"日期")]//following-sibling::span//input)[2]'

    @staticmethod
    def inventory_detail_link(num):
        return f'//a[@class="link" and text()="{num}"]'

    @staticmethod
    def grid_table_tr():
        return '//table[@id="grid"]//tr'

    @staticmethod
    def loading_div():
        return '//div[@id="load_grid"]'


class InventoryDetailBase:
    @staticmethod
    def inventory_detail_frame():
        return 'inventory-detailSheet'

    @staticmethod
    def inventory_detail_buttons(button):
        button_id = {'打印': 'print', '导出当前存货': 'saveThisAsExcel', '导出全部存货': 'saveAllAsExcel',
                     '连续打印': 'continuous-print', '刷新': 'refresh'}
        return f'//*[@id="{button_id.get(button)}"]'

    @staticmethod
    def show_price_checkbox():
        return '//input[@id="isShowPriceAndAmount"]'

    @staticmethod
    def start_period_input():
        return '(//label[contains(text(),"日期")]//following-sibling::span//input)[1]'

    @staticmethod
    def end_period_input():
        return '(//label[contains(text(),"日期")]//following-sibling::span//input)[2]'

    @staticmethod
    def bill_link(bill):
        return f'//td/a[text()="{bill}"]'

    @staticmethod
    def voucher_link_by_bill(bill):
        return f'//td/a[text()="{bill}"]//parent::td//following-sibling::td//a'

    @staticmethod
    def inventory_input():
        return '//input[@id="query-type"]'

    @staticmethod
    def inventory_dropdown_item(item):
        return f'//div[@title="{item}"]'
