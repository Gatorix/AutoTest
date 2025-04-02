from base.accounting.base_fixed_asset import (FixedAssetClassBase,
                                              FixedAssetCardBase,
                                              FixedAssetDepreciationSummaryBase,
                                              FixedAssetDepreciationDetailBase,
                                              FixedAssetAddCardBase,
                                              FixedAssetModifyCardBase)

from base.base_case import BaseTestCase


class FixedAssetClassPage(FixedAssetClassBase, BaseTestCase):
    def switch_to_fixed_asset_class_frame(self):
        self.switch_to_frame(self.fixed_asset_class_frame())

    def switch_to_add_class_frame(self):
        self.switch_to_frame(self.add_class_frame())

    def click_class_buttons(self, button):
        button_id = {'新增': 'add', '删除': 'delete'}
        self.click(self.buttons(button_id.get(button)))
        self.wait(1)

    def click_buttons_in_line_by_num(self, num, button):
        self.click(self.buttons_in_line_by_num(num, button))

    def click_checkbox_in_line_by_num(self, num):
        self.click(self.checkbox_in_line_by_num(num))

    def type_add_class_inputs(self, label, text):
        self.type(self.add_class_inputs(label), text)
        self.wait(1)

    def get_add_class_inputs_errors(self, label):
        return self.get_text(self.add_class_inputs_errors(label))

    def click_add_class_buttons(self, button):
        self.click(self.add_class_buttons(button))
        self.wait(1)


class FixedAssetCardPage(FixedAssetCardBase, BaseTestCase):
    def switch_to_fixed_asset_card_frame(self):
        self.switch_to_frame(self.fixed_asset_card_frame())

    def click_card_buttons(self, button):
        button_id = {'新增': 'add',
                     '删除': 'delete',
                     '导入': 'import',
                     '导出': 'export',
                     '刷新': 'refresh',
                     '导入B': 'btn-import',
                     '保存并新增': 'renew',
                     '保存': 'save',
                     '复制': 'copy',
                     '清理': 'clear',
                     '全选': 'cb_grid'}
        self.click(self.buttons(button_id.get(button)))
        self.wait(1)
        if '导入' in button or '导出' in button:
            self.wait(3)

    def is_list_empty(self):
        return '无数据' in self.get_text(self.page_foot_right())

    def click_conform_buttons(self, button):
        self.click(self.conform_buttons(button))

    def click_buttons_in_line_by_num(self, num, button):
        self.click(self.buttons_in_line_by_num(num, button))

    def click_checkbox_in_line_by_num(self, num):
        self.click(self.checkbox_in_line_by_num(num))

    def click_all_checkbox_by_same_name(self, name):
        checkboxes = self.find_visible_elements(self.checkbox_in_line_by_name(name))
        for idx, _ in enumerate(checkboxes):
            self.click(f'({self.checkbox_in_line_by_name(name)})[{idx + 1}]')
            self.wait(1)

    def click_next_step_button(self):
        self.click(self.next_step_button())

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.import_file_input(), filepath)
        self.wait(3)

    def get_import_result(self):
        return self.get_text(self.import_result())

    def click_return_to_list(self):
        self.click(self.return_to_list())

    def click_check_all(self):
        self.click(self.check_all())

    def click_standard_template(self):
        self.click(self.standard_template())
        self.wait(3)


class FixedAssetAddCardPage(FixedAssetAddCardBase, BaseTestCase):
    def switch_to_fixed_asset_add_card_frame(self):
        self.switch_to_frame(self.fixed_asset_add_card_frame())

    def click_buttons(self, button):
        button_id = {'保存并新增': 'renew', '保存': 'save', '复制': 'copy', '清理': 'clear', '删除': 'delete'}
        self.click(self.buttons(button_id.get(button)))
        self.wait(1)

    def type_add_card_input(self, label, text):
        self.type(self.add_card_inputs(label), text)
        self.wait(1)

    def click_conform_buttons(self, button):
        self.click(self.conform_buttons(button))

    def click_dropdown_list(self, item):
        self.click(self.dropdown_list(item))
        self.wait(1)

    def add_card(self, num, amount='30000', residual_rate='5%'):
        self.type_add_card_input('资产编码', num)
        self.type_add_card_input('资产名称', num)
        self.type_add_card_input('资产类别', '001_房屋、建筑物')
        self.click_dropdown_list('001_房屋、建筑物')
        self.type_add_card_input('使用部门', '研发部')
        self.click_dropdown_list('研发部')
        self.type_add_card_input('原值', amount)
        self.type_add_card_input('残值率', residual_rate)
        self.click_buttons('保存')

    def type_to_copy_card_input(self, num):
        self.type(self.copy_card_input(), num)

    def get_text_from_line_edit(self, label):
        return self.get_text(self.line_edit_value(label))

    def get_text_from_list_texts_by_table_head(self, card_name, th):
        return self.get_text(self.list_texts_by_table_head(card_name, th))


class FixedAssetModifyCardPage(FixedAssetModifyCardBase, BaseTestCase):
    def switch_to_fixed_asset_modify_card_frame(self):
        self.switch_to_frame(self.fixed_asset_modify_card_frame())


class FixedAssetDepreciationSummaryPage(FixedAssetDepreciationSummaryBase, BaseTestCase):
    def switch_to_fixed_asset_depreciation_summary_frame(self):
        self.switch_to_frame(self.fixed_asset_depreciation_summary_frame())


class FixedAssetDepreciationDetailPage(FixedAssetDepreciationDetailBase, BaseTestCase):
    def switch_to_fixed_asset_depreciation_detail_frame(self):
        self.switch_to_frame(self.fixed_asset_depreciation_detail_frame())

    def double_click_fixed_asset_depreciation_detail_line_td_by_asset_name(self, asset_name):
        self.double_click(self.fixed_asset_depreciation_detail_line_td_by_asset_name(asset_name))

    def doubleclick_fixed_asset_depreciation_sum_line_td(self):
        self.double_click(self.fixed_asset_depreciation_sum_line_td())

    def click_buttons(self, button):
        self.click(self.buttons(button))

    def switch_to_print_settings_frame(self):
        self.switch_to_frame(self.print_settings_frame())
