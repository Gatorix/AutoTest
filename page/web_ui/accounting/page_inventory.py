from base.accounting.base_inventory import (InventoryDetailBase,
                                            InventorySummaryBase,
                                            InventoryOutboundEntryBase,
                                            InventoryWarehousingEntryBase,
                                            InventoryManageBase,
                                            InventorySettingBase,
                                            InventoryNewEntryBase)

from base.base_case import BaseTestCase


class InventorySettingPage(BaseTestCase, InventorySettingBase):
    def switch_to_inventory_setting_frame(self):
        self.switch_to_frame(self.inventory_setting_frame())

    def click_inventory_setting_buttons(self, button):
        button_kv = {'库存初始数据': 'initalVentory', '基础设置': 'basicSetting', '刷新': 'refresh',
                     '重算初始数据': 'retry', '保存': 'saveInitKC', '导出': 'saveAsExcel',
                     '导入': 'importBtn', '全选': 'cb_grid', '选择': 'importWages-file', '导入B': 'save-import'}
        self.click(self.inventory_setting_buttons(button_kv.get(button)))
        self.wait(1)
        if '导' in button:
            self.wait(2)

    def click_download_template(self):
        self.click(self.import_template())
        self.wait(3)

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.inventory_setting_buttons('importWages-file'), filepath)

    def get_init_quantity_input_by_num(self, num):
        return self.get_attribute(self.init_quantity_input_by_num(num), 'value')

    def set_init_quantity_input_by_num(self, num, text):
        self.type(self.init_quantity_input_by_num(num), text)

    def get_init_amount_input_by_num(self, num):
        return self.get_attribute(self.init_amount_input_by_num(num), 'value')

    def set_init_amount_input_by_num(self, num, text):
        self.type(self.init_amount_input_by_num(num), text)


class InventoryManagePage(BaseTestCase, InventoryManageBase):
    def switch_to_inventory_manage_frame(self):
        self.switch_to_frame(self.inventory_manage_frame())

    def click_inventory_manage_buttons(self, button):
        button_id = {'新增': 'btn-add', '删除': 'delete', '导入': 'btn-import', '下一步': 'step2',
                     '导出': 'saveAsExcel', '发票商品对应系统存货': 'mapCH'}
        self.js_click(self.inventory_manage_buttons(button_id.get(button)))
        if '导' in button:
            self.wait(3)

    def is_line_visible(self, num):
        return self.is_element_visible(self.inventory_sys_list_last_line_by_num(num))

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)

    def type_to_add_inventory_type_inputs(self, label, text):
        self.type(self.add_inventory_type_inputs(label), text)
        self.wait(1)

    def add_inventory_type_default(self, num):
        self.type_to_add_inventory_type_inputs('编码', num)
        self.type_to_add_inventory_type_inputs('名称', num)
        self.type_to_add_inventory_type_inputs('规格', 'test')
        self.type_to_add_inventory_type_inputs('单位', '台')

    def click_input_buttons(self, button):
        self.click(self.input_buttons(button))

    def click_in_line_buttons_by_id(self, num, button):
        self.click(self.in_line_buttons_by_id(num, button))
        self.wait(1)

    def click_in_line_checkbox_by_id(self, num):
        self.click(self.in_line_checkbox_by_id(num))

    def get_verify_text(self, label):
        return self.get_text(self.add_inventory_type_verify_label(label))

    def inventory_manage_click_download_template(self):
        self.click(self.download_template())
        self.wait(3)

    def get_import_success_result(self):
        return self.get_text(self.import_result_success())

    def click_buttons_text(self, button):
        self.click(self.buttons_text(button))
        self.wait(1)


class InventoryWarehousingEntryPage(BaseTestCase, InventoryWarehousingEntryBase):
    def switch_to_warehousing_entry_frame(self):
        self.switch_to_frame(self.warehousing_entry_frame())

    def click_inventory_warehousing_entry_buttons(self, button):
        button_id = {'产品入库单': 'addStockCP', '材料入库单': 'addStockCL', '周转材料入库单': 'addStockZYCL',
                     '自动生成入库单': 'create', '复制': 'copy', '删除': 'delete', '编号整理': 'numArrange',
                     '导入': 'importBtn', '导出': 'saveAsExcel', '打印': 'print', '更改单据类型': 'changeBillType',
                     '导入B': 'save-import', '确定': 'save-select-bills-type', '刷新': 'refresh', '全选': 'cb_grid'}
        self.js_click(self.inventory_warehousing_entry_buttons(button_id.get(button)))
        if '导' in button:
            self.wait(1)
        self.wait(1)

    def click_text_buttons(self, button):
        self.click(self.text_buttons(button))
        self.wait(3)

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)

    def click_import_type_radio(self, value):
        self.click(self.import_type_radio(value))

    def click_list_checkbox_by_bill_number(self, num):
        self.click(self.list_checkbox_by_bill_number(num))

    def click_input_buttons(self, button):
        self.click(self.input_buttons(button))

    def change_bill_type(self, bill):
        self.click(self.change_type_input())
        self.click(self.change_type_dropdown_items(bill))

    def get_list_bill_type(self, bill):
        return self.get_text(self.list_bill_type_cell(bill))

    def click_list_bill_type(self, bill):
        self.click(self.list_bill_type_cell(bill))

    def click_auto_gen_bill_by_type_radio(self, type_radio):
        self.click(self.auto_gen_bill_by_type_radio(type_radio))

    def click_auto_gen_bill_step_span(self, step):
        self.click(self.auto_gen_bill_step_span(step))
        self.wait(0.2)

    def get_text_from_warehousing_entry_table_customer_td_by_bill_num(self, bill_num):
        return self.get_text(self.warehousing_entry_table_customer_td_by_bill_num(bill_num))

    def get_text_from_warehousing_entry_table_customer_td_by_voucher_num(self, voucher_num):
        return self.get_text(self.warehousing_entry_table_customer_td_by_voucher_num(voucher_num))

    def click_warehousing_entry_select_all(self):
        self.click(self.warehousing_entry_select_all())


class InventoryNewEntryPage(BaseTestCase, InventoryNewEntryBase):
    def switch_to_new_entry_frame(self):
        self.switch_to_frame(self.new_entry_frame())
        self.wait(2)

    def click_inventory_new_entry_buttons(self, button):
        button_id = {'产品入库单': 'addStockCP', '材料入库单': 'addStockCL', '周转材料入库单': 'addStockZYCL',
                     '产品出库单': 'addStockCP', '材料出库单': 'addStockCL', '周转材料出库单': 'addStockZYCL',
                     '保存': 'save', '复制': 'copy'}
        self.js_click(self.inventory_new_entry_buttons(button_id.get(button)))

    def type_to_table_cells(self, cell, text, line=1):
        cell_id = {'存货编码': 'query-type-inv', '数量': 'qty', '金额': 'amount', '单价': 'unitPrice', '备注': 'remark'}
        if cell == '存货编码':
            self.type(self.table_inputs(cell_id.get(cell), line), text)
            self.click(self.table_query_class_items(text))
            self.wait(1)
        else:
            self.type(self.table_inputs(cell_id.get(cell), line), text)
            self.wait(1)

    def get_table_cells_value(self, cell, line=1):
        cell_id = {'存货编码': 'query-type-inv', '数量': 'qty', '金额': 'amount', '单价': 'unitPrice', '备注': 'remark'}
        return self.get_text(self.table_inputs(cell_id.get(cell), line))

    def type_to_table_head_inputs(self, cell, text):
        cell_id = {'单据日期': 'pickupPicker', '往来单位': 'customerH', '单据编号': 'docNoH', '摘要': 'remarkH'}
        self.type(self.table_head_inputs(cell_id.get(cell)), text)
        self.wait(1)

    def get_table_head_inputs_value(self, cell):
        cell_id = {'单据日期': 'pickupPicker', '往来单位': 'customerH', '单据编号': 'docNoH', '摘要': 'remarkH'}
        return self.get_text(self.table_head_inputs(cell_id.get(cell)))


class InventoryOutboundEntryPage(BaseTestCase, InventoryOutboundEntryBase):
    def switch_to_outbound_entry_frame(self):
        self.switch_to_frame(self.outbound_entry_frame())

    def click_inventory_outbound_entry_buttons(self, button):
        button_id = {'产品出库单': 'addStockCP', '材料出库单': 'addStockCL', '周转材料出库单': 'addStockZYCL',
                     '自动生成入库单': 'create', '复制': 'copy', '删除': 'delete', '编号整理': 'numArrange',
                     '导入': 'importBtn', '导出': 'saveAsExcel', '打印': 'print', '更改单据类型': 'changeBillType',
                     '导入B': 'save-import', '确定': 'save-select-bills-type', '刷新': 'refresh', '全选': 'cb_grid'}
        self.js_click(self.inventory_outbound_buttons(button_id.get(button)))
        if '导' in button:
            self.wait(1)
        self.wait(1)

    def click_text_buttons(self, button):
        self.click(self.text_buttons(button))
        self.wait(3)

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)

    def click_import_type_radio(self, value):
        self.click(self.import_type_radio(value))

    def click_list_checkbox_by_bill_number(self, num):
        self.click_inventory_outbound_entry_buttons('刷新')
        self.click(self.list_checkbox_by_bill_number(num))

    def click_input_buttons(self, button):
        self.click(self.input_buttons(button))

    def change_bill_type(self, bill):
        self.click(self.change_type_input())
        self.click(self.change_type_dropdown_items(bill))

    def get_list_bill_type(self, bill):
        return self.get_text(self.list_bill_type_cell(bill))

    def click_list_bill_type(self, bill):
        self.click(self.list_bill_type_cell(bill))


class InventorySummaryPage(BaseTestCase, InventorySummaryBase):
    def switch_to_inventory_summary_frame(self):
        self.switch_to_frame(self.inventory_summary_frame())

    def click_inventory_summary_buttons(self, button):
        self.js_click(self.inventory_summary_buttons(button))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def click_checkbox(self, box_name):
        self.click(self.checkboxes(box_name))
        self.wait(1)

    def select_period(self, start, end):
        self.type(self.start_period_input(), f'{start}\n')
        self.wait(1)
        self.type(self.end_period_input(), f'{end}\n')
        self.wait(1)

    def click_inventory_detail_link(self, num):
        self.click(self.inventory_detail_link(num))

    def get_total_num_grid_table_tr(self):
        return len(self.find_elements(self.grid_table_tr()))

    def wait_for_loading_finish(self):
        self.wait_for_element_not_visible(self.loading_div())


class InventoryDetailPage(BaseTestCase, InventoryDetailBase):
    def switch_to_inventory_detail_frame(self):
        self.switch_to_frame(self.inventory_detail_frame())

    def click_inventory_detail_buttons(self, button):
        self.js_click(self.inventory_detail_buttons(button))
        if '导出' in button:
            self.wait(3)
        self.wait(1)

    def click_detail_checkbox(self):
        self.check_if_unchecked(self.show_price_checkbox())

    def select_period(self, start, end):
        self.type(self.start_period_input(), f'{start}\n')
        self.wait(1)
        self.type(self.end_period_input(), f'{end}\n')
        self.wait(1)

    def click_bill_link(self, bill):
        self.click(self.bill_link(bill))

    def click_voucher_link(self, bill):
        self.click(self.voucher_link_by_bill(bill))

    def select_inventory(self, name):
        self.type(self.inventory_input(), name)
        self.wait(0.5)
        self.click(self.inventory_dropdown_item(name))

    def type_to_inventory(self, name):
        self.type(self.inventory_input(), name)

    def get_inventory_class(self):
        return self.get_text(self.inventory_input())
