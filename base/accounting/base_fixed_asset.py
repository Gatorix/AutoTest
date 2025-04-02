class FixedAssetClassBase:
    @staticmethod
    def fixed_asset_class_frame():
        return 'asset-fixedAssetsClass'

    @staticmethod
    def add_class_frame():
        return '//table//iframe'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def buttons_in_line_by_num(num, button):
        return f'//td[text()="{num}"]//preceding-sibling::td//a[@title="{button}"]'

    @staticmethod
    def checkbox_in_line_by_num(num):
        return f'//td[text()="{num}"]//preceding-sibling::td//input'

    @staticmethod
    def add_class_inputs(label):
        return f'(//label[text()="{label}"]//parent::div//following-sibling::div//input)[1]'

    @staticmethod
    def add_class_inputs_errors(label):
        return f'(//label[text()="{label}"]//parent::div//following-sibling::div//input)[1]' \
               f'//following-sibling::label[@class="valid-error"]'

    @staticmethod
    def add_class_buttons(button):
        return f'//input[@value="{button}"]'


class FixedAssetCardBase:
    @staticmethod
    def fixed_asset_card_frame():
        return 'asset-fixedAssetsCards'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def page_foot_right():
        return f'//td[@id="page_right"]/div'

    @staticmethod
    def buttons_in_line_by_num(num, button):
        return f'//a[text()="{num}"]//parent::td//preceding-sibling::td//a[@title="{button}"]'

    @staticmethod
    def checkbox_in_line_by_num(num):
        return f'//a[text()="{num}"]//parent::td//preceding-sibling::td//input'

    @staticmethod
    def conform_buttons(button):
        return f'//input[@value="{button}"]'

    @staticmethod
    def checkbox_in_line_by_name(name):
        return f'//td[text()="{name}"]//parent::td//preceding-sibling::td//input'

    @staticmethod
    def copy_card_input():
        return f'//input[@id="copy-number"]'

    @staticmethod
    def next_step_button():
        return '//a[text()="下一步"]'

    @staticmethod
    def import_file_input():
        return '//input[@id="import-file-info"]'

    @staticmethod
    def import_result():
        return '(//div[@id="import-result"]//font)[1]'

    @staticmethod
    def return_to_list():
        return '//div[@class="left mod-crumb"]//a[text()="卡片"]'

    @staticmethod
    def check_all():
        return '//input[@id="cb_grid"]'

    @staticmethod
    def standard_template():
        return '//div[@id="import-step1"]//a[@class="link"]'


class FixedAssetAddCardBase:
    @staticmethod
    def fixed_asset_add_card_frame():
        return 'addCardsManage'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def add_card_inputs(label):
        if label == '资产类别':
            return f'//a[text()="资产类别"]//ancestor::div[@class="label-wrap"]//following-sibling::div//input'
        else:
            return f'//label[text()="{label}"]//parent::div//following-sibling::div//input'

    @staticmethod
    def dropdown_list(item):
        return f'//div[@class="droplist"]/div[text()="{item}"]'

    @staticmethod
    def conform_buttons(button):
        return f'//input[@value="{button}"]'

    @staticmethod
    def copy_card_input():
        return f'//input[@id="copy-number"]'

    @staticmethod
    def line_edit_value(label):
        return f'//label[text()="{label}"]/parent::div//following-sibling::div/input'

    @staticmethod
    def list_texts_by_table_head(card_name, th):
        return f'//td[text()="{card_name}"]//following-sibling::td[contains(@aria-describedby,"{th}")]'


class FixedAssetModifyCardBase:
    @staticmethod
    def fixed_asset_modify_card_frame():
        return 'editCardsManage'


class FixedAssetDepreciationSummaryBase:
    @staticmethod
    def fixed_asset_depreciation_summary_frame():
        return 'asset-depreciationSummarySheets'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'


class FixedAssetDepreciationDetailBase:
    @staticmethod
    def fixed_asset_depreciation_detail_frame():
        return 'asset-depreciationDetailSheets'

    @staticmethod
    def print_settings_frame():
        return f'//table//iframe'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def fixed_asset_depreciation_detail_line_td_by_asset_name(asset_name):
        return f'//td[text()="{asset_name}"]'

    @staticmethod
    def fixed_asset_depreciation_sum_line_td():
        return '(//*[text()="总计"]/parent::td//following-sibling::td//strong)[1]'

    @staticmethod
    def print_settings_label_text():
        return '//label[text()="内容过长自动换行"]'
