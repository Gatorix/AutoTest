class SettingsCommonBase:
    @staticmethod
    def settings_common_details_focus_table_buttons(button):
        return f'//table[contains(@class,"ui_state_lock")]//input[@value="{button}"]'

    @staticmethod
    def settings_common_details_focus_table_input_by_label(label):
        return f'//label[contains(text(),"{label}")]//parent::div//following-sibling::div//input'

    @staticmethod
    def settings_common_details_focus_table_error_label_by_label(label):
        return f'//label[contains(text(),"{label}")]//parent::div' \
               f'//following-sibling::div//input//following-sibling::label'

    @staticmethod
    def settings_common_details_focus_table_radio_by_label(label, value):
        return f'//label[contains(text(),"{label}")]//parent::div//following-sibling::div//input[@value="{value}"]'


class AdvanceSettingsSystemArgsBase:
    @staticmethod
    def sys_args_frame():
        return 'setting-parameter'

    @staticmethod
    def sys_args_subject_demo_button():
        return '//div[@id="useDescription"]'

    @staticmethod
    def sys_args_subject_demo_box():
        return '//div[@class="use-description-box useDescription-QY"]'

    @staticmethod
    def sys_args_subject_demo_box_text():
        return '(//div[@class="use-description-box useDescription-QY"]//div[@class="description-content"]/div)[5]'


class AdvanceSettingsBackupAndRecoverBase:
    @staticmethod
    def backup_frame():
        return f'setting-backup'

    @staticmethod
    def backup_button(button):
        button_kv = {'开始备份': 'start-backup', '上传本地备份': 'localRecover'}
        return f'//a[@id="{button_kv.get(button)}"]'

    @staticmethod
    def input_buttons(button):
        return f'//input[@type="button" and @value="{button}"]'

    @staticmethod
    def latest_backup_line_operate_buttons(button):
        button_kv = {'删除': 'btn-del', '恢复': 'btn-recover', '下载': 'btn-download'}
        return f'(//div[@class="ui-jqgrid-bdiv"]//table//tr[@tabindex])[1]//a[@class="{button_kv.get(button)}"]'

    @staticmethod
    def backup_alert_div():
        return '//tbody//td//div[@class="ui_content" and contains(text(),"正在备份")]'


class SettingsVoucherTypeBase:
    @staticmethod
    def settings_voucher_type_frame():
        return 'setting-voucherWord'

    @staticmethod
    def settings_voucher_type_add_button():
        return f'//a[@id="add-word"]'

    @staticmethod
    def settings_voucher_type_operate_button_in_line_by_type(voucher_type, button):
        return f'//table[@id="grid"]//td[@title="{voucher_type}"]//following-sibling::td/p/a[text()="{button}"]'

    @staticmethod
    def settings_voucher_type_text_in_line_by_type(voucher_type, text):
        return f'//table[@id="grid"]//td[@title="{voucher_type}"]//following-sibling::td[text()="{text}"]'


class SettingsSubjectBase:
    @staticmethod
    def settings_subject_frame():
        return 'setting-subjectList'

    @staticmethod
    def settings_subject_buttons(button):
        button_kv = {
            '新增': 'add',
            '导入': 'import',
            '导出': 'export',
            '删除': 'delete'
        }
        return f'//a[@id="{button_kv.get(button)}"]'

    @staticmethod
    def settings_subject_class(subject_class):
        return f'//strong[text()="类别"]//following-sibling::ul//li[text()="{subject_class}"]'

    @staticmethod
    def settings_subject_checkbox_by_id(subject_id):
        return f'//table[@id="grid"]//tr[@id="{subject_id}"]/td/input'

    @staticmethod
    def settings_subject_operating_buttons_by_id(subject_id, button):
        return f'//table[@id="grid"]//tr[@id="{subject_id}"]/td//a[@title="{button}"]'

    @staticmethod
    def settings_subject_name_by_id(subject_id):
        return f'//table[@id="grid"]//tr[@id="{subject_id}"]/td[contains(@aria-describedby,"name")]'

    @staticmethod
    def settings_subject_focus_table_buttons(button):
        return f'//table[contains(@class,"ui_state_lock")]//input[@value="{button}"]'

    @staticmethod
    def settings_subject_focus_table_iframe():
        return f'//table[contains(@class,"ui_state_lock")]//table//td[@class="ui_main"]//iframe'

    @staticmethod
    def settings_subject_focus_table_input_by_label(label):
        return f'//label[text()="{label}"]//parent::div//following-sibling::div//input'

    @staticmethod
    def settings_subject_focus_table_radio_by_label(value, label='余额方向'):
        return f'//label[text()="{label}"]//parent::div//following-sibling::div//input[@value="{value}"]'

    @staticmethod
    def settings_subject_focus_table_options_by_label(label):
        return f'//label[text()="{label}"]//preceding-sibling::input'


class SettingsCurrencyBase:
    @staticmethod
    def settings_currency_frame():
        return 'setting-currency'

    @staticmethod
    def settings_currency_add_button():
        return '//a[@id="btn-add"]'

    @staticmethod
    def settings_currency_operating_buttons_in_line_by_code(code, button):
        return f'//td[@title="{code}"][1]//following-sibling::td//a[text()="{button}"]'


class SettingsSubAccountBase:
    @staticmethod
    def settings_sub_accounting_frame():
        return 'setting-assisting'

    @staticmethod
    def settings_sub_accounting_types(sub_type):
        return f'//strong[text()="{sub_type}"]'

    @staticmethod
    def settings_sub_accounting_new_type():
        return '//li[@id="add-custom-assisting"]//a'

    @staticmethod
    def settings_sub_accounting_customize_type_operating_buttons(customize_type, button):
        return f'//strong[text()="{customize_type}"]//ancestor::a//following-sibling::span/a[@title="{button}"]'

    @staticmethod
    def settings_sub_accounting_custom_li():
        return '//li[@class="custom"]'


class SettingsSubAccountDetailsBase:
    @staticmethod
    def settings_sub_accounting_details_frame():
        return 'setting-assistingCategory'

    @staticmethod
    def settings_sub_accounting_details_buttons(button):
        button_kv = {
            '新增': 'btn-add',
            '导入': 'btn-import',
            '导出': 'saveAsExcel',
            '删除': 'delete',
            '查询': 'search'
        }
        return f'//a[@id="{button_kv.get(button)}"]'

    @staticmethod
    def settings_sub_accounting_details_line_num():
        return f'//table[@id="grid"]//tr[@id]'

    @staticmethod
    def settings_sub_accounting_details_tab_li(tab_name):
        return f'//strong[text()="类别"]//following-sibling::ul[contains(@class,"tab")]//li[text()="{tab_name}"]'

    @staticmethod
    def settings_sub_accounting_details_customize_type_selector():
        return '//strong[text()="类别"]//following-sibling::span'

    @staticmethod
    def settings_sub_accounting_details_customize_dropdown_items(item):
        return f'//div[@id="COMBO_WRAP"]/div[not(contains(@style,"display: none;"))]' \
               f'/div[@class="droplist"]//div[text()="{item}"]'

    @staticmethod
    def settings_sub_accounting_details_search_input():
        return '//strong[text()="类别"]//following-sibling::ul[contains(@class,"search")]//input'

    @staticmethod
    def settings_sub_accounting_details_checkbox_in_line_by_code(code):
        return f'//td[text()="{code}"]//preceding-sibling::td//input'

    @staticmethod
    def settings_sub_accounting_details_operate_buttons_in_line_by_code(code, button):
        # edit, del
        return f'//td[text()="{code}"]//following-sibling::td//a[contains(@class,"{button}")]'

    @staticmethod
    def settings_sub_accounting_details_button_by_name(name):
        return f'//div[contains(@id,"import-step")]//a[text()="{name}"]'

    @staticmethod
    def settings_sub_accounting_details_download_template():
        return '//div[@id="import-step1"]//a[@class="link"]'

    @staticmethod
    def settings_sub_accounting_details_upload_file_input():
        return '//div[@id="import-step2"]//input[@type="file"]'

    @staticmethod
    def settings_sub_accounting_details_import_result(num):
        return f'(//div[contains(@id,"import-step")]//div[@id="import-result"]//font)[{num}]'

    @staticmethod
    def settings_sub_accounting_details_import_result_text():
        return f'//div[contains(@id,"import-step")]//div[@id="import-result"]'


class SettingsInitAcctBalanceBase:
    pass


class SettingsInitCashFlowBalanceBase:
    pass


class SettingsCashFlowItemBase:
    pass


class SettingsVoucherTemplateBase:
    pass


class SettingsInvoiceVoucherTemplateBase:
    @staticmethod
    def settings_invoice_voucher_template_frame():
        return 'setting-voucherTemplate'

    @staticmethod
    def settings_invoice_voucher_template_buttons(button):
        button_kv = {
            '复制至其他账套': 'btn-copy',
            '新增': 'addAccTemp',
            '复制模板': 'copyAccTemp',
            '同步最新模板': 'cover-accountrule'
        }
        return f'//a[@id="{button_kv.get(button)}"]'

    @staticmethod
    def settings_new_invoice_voucher_template_inputs_by_label(label):
        return f'//div[@id="pop-up"]//label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def settings_new_invoice_voucher_template_input_items_by_label(label, item):
        return f'//div[@id="pop-up"]//label[contains(text(),"{label}")]' \
               f'//following-sibling::div//input//following-sibling::ul//li[text()="{item}"]'

    @staticmethod
    def settings_new_invoice_voucher_template_summary_span(summary):
        return f'//div[@id="pop-up"]//div[@id="fabfixed"]//span[contains(text(),"{summary}")]'

    @staticmethod
    def settings_new_invoice_voucher_template_dc_selector_by_line(line):
        return f'(//div[@id="pop-up"]//div[@class="add_data"])[{line}]//select[@id="account-dc"]'

    @staticmethod
    def settings_new_invoice_voucher_template_subject_input_by_line(line):
        return f'(//div[@id="pop-up"]//div[@class="add_data"])[{line}]//input[@id="assets-subject"]'

    @staticmethod
    def settings_new_invoice_voucher_template_subject_dropdown_items(item):
        return f'//div[@class="droplist"]/parent::div[not(contains(@style,"display: none;"))]//div[contains(text(),"{item}")]'

    @staticmethod
    def settings_new_invoice_voucher_template_amount_source_input_by_line(line):
        return f'(//div[@id="pop-up"]//div[@class="add_data"])[{line}]//input[@id="account-money"]'

    @staticmethod
    def settings_new_invoice_voucher_template_amount_source_items_by_line(line, item):
        return f'(//div[@id="pop-up"]//div[@class="add_data"])[{line}]' \
               f'//input[@id="account-money"]//following-sibling::ul//li[text()="{item}"]'

    @staticmethod
    def settings_new_invoice_voucher_template_operating_buttons_in_line(line, button):
        return f'(//div[@id="pop-up"]//div[@class="add_data"])[{line}]//span[contains(text(),"{button}")]'

    @staticmethod
    def settings_new_invoice_voucher_template_buttons_by_id(button):
        button_kv = {
            '保存': 'addTemp-save',
            '取消': 'addTemp-cancel'
        }
        return f'//div[@id="pop-up"]//input[@id="{button_kv.get(button)}"]'

    @staticmethod
    def settings_invoice_voucher_template_buttons_in_line_by_method(method, button):
        button_kv = {
            '删除': 'delete',
            '编辑模板': '_edit',
            '编辑摘要': '_abstract'
        }
        return f'//tbody[@id="info-list"]//input[@title="{method}"]//ancestor::tr//i[contains(@class,"{button_kv.get(button)}")]'

    @staticmethod
    def settings_invoice_voucher_template_tr():
        return f'//tbody[@id="info-list"]//tr'

    @staticmethod
    def settings_invoice_voucher_template_sync_radio(value):
        # 增量：2
        # 覆盖：1
        return f'//div[@id="pop-up"]//input[@type="radio" and @value="{value}"]'

    @staticmethod
    def settings_invoice_voucher_template_sync_save_button():
        return f'//div[@id="pop-up"]//input[@type="button" and @value="保存"]'

    @staticmethod
    def settings_invoice_voucher_template_acct_search_input():
        return f'//input[@id="temp-acct-search-input"]'

    @staticmethod
    def settings_invoice_voucher_template_acct_search_result(result):
        return f'//label[contains(text(),"{result}")]//preceding-sibling::input'

    @staticmethod
    def settings_invoice_voucher_template_copy_submit_button():
        return '//a[@id="copy-submit"]'
