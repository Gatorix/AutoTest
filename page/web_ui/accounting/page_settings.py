from base.accounting.base_common import AccountingCommonBase
from base.accounting.base_settings import (AdvanceSettingsBackupAndRecoverBase,
                                           SettingsVoucherTypeBase,
                                           SettingsSubjectBase,
                                           SettingsCurrencyBase,
                                           SettingsSubAccountBase,
                                           SettingsInitAcctBalanceBase,
                                           SettingsInitCashFlowBalanceBase,
                                           SettingsCashFlowItemBase,
                                           SettingsVoucherTemplateBase,
                                           SettingsInvoiceVoucherTemplateBase,
                                           SettingsSubAccountDetailsBase,
                                           SettingsCommonBase, AdvanceSettingsSystemArgsBase)
from base.base_case import BaseTestCase
from page.web_ui.accounting.page_common import AccountingCommonPage


class SettingsCommonPage(SettingsCommonBase, BaseTestCase):
    def click_settings_common_details_focus_table_buttons(self, button):
        self.click(self.settings_common_details_focus_table_buttons(button))

    def type_to_settings_common_details_focus_table_input_by_label(self, label, text):
        self.type(self.settings_common_details_focus_table_input_by_label(label), text)

    def get_text_from_settings_common_details_focus_table_error_label_by_label(self, label):
        return self.get_text(self.settings_common_details_focus_table_error_label_by_label(label))

    def click_settings_common_details_focus_table_radio_by_label(self, label, value):
        self.click(self.settings_common_details_focus_table_radio_by_label(label, value))


class AdvanceSettingsSystemArgsPage(AdvanceSettingsSystemArgsBase, BaseTestCase):
    def switch_to_sys_args_frame(self):
        self.switch_to_frame(self.sys_args_frame())
        self.wait_for_ready_state_complete()

    def move_to_sys_args_subject_demo_button(self):
        self.move_mouse_to_element(self.sys_args_subject_demo_button())

    def get_text_from_sys_args_subject_demo_box(self):
        return self.get_text(self.sys_args_subject_demo_box())


class AdvanceSettingsBackupAndRecoverPage(AdvanceSettingsBackupAndRecoverBase, BaseTestCase):
    def switch_to_backup_frame(self):
        self.switch_to_frame(self.backup_frame())
        self.wait_for_ready_state_complete()
        self.wait(2)

    def click_backup_buttons(self, button):
        self.click(self.backup_button(button))

    def click_backup_input_buttons(self, button):
        self.click(self.input_buttons(button))

    def click_latest_backup_line_operate_buttons(self, button):
        self.click(self.latest_backup_line_operate_buttons(button))

    def wait_for_backup_finished(self):
        self.wait_for_element_not_present(self.backup_alert_div())


class SettingsVoucherTypePage(SettingsVoucherTypeBase, BaseTestCase):
    def switch_to_settings_voucher_type_frame(self):
        self.switch_to_frame(self.settings_voucher_type_frame())

    def click_settings_voucher_type_add_button(self):
        self.click(self.settings_voucher_type_add_button())

    def click_settings_voucher_type_operate_button_in_line_by_type(self, voucher_type, button):
        self.click(self.settings_voucher_type_operate_button_in_line_by_type(voucher_type, button))


class SettingsSubjectPage(SettingsSubjectBase, BaseTestCase, AccountingCommonBase):
    def switch_to_settings_subject_frame(self):
        self.switch_to_frame(self.settings_subject_frame())

    def close_menu(self):
        self.switch_to_default_content()
        self.click(self.accounting_my_company_span())
        self.switch_to_settings_subject_frame()

    def click_settings_subject_buttons(self, button):
        self.click(self.settings_subject_buttons(button))

    def click_settings_subject_class(self, subject_class):
        self.close_menu()
        self.click(self.settings_subject_class(subject_class))

    def check_settings_subject_checkbox_by_id(self, subject_id):
        self.check_if_unchecked(self.settings_subject_checkbox_by_id(subject_id))

    def click_settings_subject_operating_buttons_by_id(self, subject_id, button):
        self.click(self.settings_subject_operating_buttons_by_id(subject_id, button))

    def get_text_from_settings_subject_name_by_id(self, subject_id):
        return self.get_text(self.settings_subject_name_by_id(subject_id))

    def click_settings_subject_focus_table_buttons(self, button):
        self.click(self.settings_subject_focus_table_buttons(button))
        self.wait(0.3)

    def switch_to_settings_subject_focus_table_iframe(self):
        self.switch_to_frame(self.settings_subject_focus_table_iframe())

    def type_to_settings_subject_focus_table_input_by_label(self, label, text):
        self.clear(self.settings_subject_focus_table_input_by_label(label))
        self.type(self.settings_subject_focus_table_input_by_label(label), text)

    def click_settings_subject_focus_table_radio_by_label(self, value):
        self.click(self.settings_subject_focus_table_radio_by_label(value))

    def click_settings_subject_focus_table_options_by_label(self, label):
        self.click(self.settings_subject_focus_table_options_by_label(label))


class SettingsCurrencyPage(SettingsCurrencyBase, BaseTestCase):
    def switch_to_settings_currency_frame(self):
        self.switch_to_frame(self.settings_currency_frame())

    def click_settings_currency_add_button(self):
        self.click(self.settings_currency_add_button())

    def click_settings_currency_operating_buttons_in_line_by_code(self, code, button):
        self.click(self.settings_currency_operating_buttons_in_line_by_code(code, button))


class SettingsSubAccountPage(SettingsSubAccountBase, BaseTestCase):
    def switch_to_settings_sub_accounting_frame(self):
        self.switch_to_frame(self.settings_sub_accounting_frame())

    def click_settings_sub_accounting_types(self, sub_type):
        self.click(self.settings_sub_accounting_types(sub_type))
        self.switch_to_default_content()

    def click_settings_sub_accounting_new_type(self):
        self.click(self.settings_sub_accounting_new_type())

    def click_settings_sub_accounting_customize_type_operating_buttons(self, customize_type, button):
        self.set_attribute_all(self.settings_sub_accounting_custom_li(), 'class', 'custom on')
        self.click(self.settings_sub_accounting_customize_type_operating_buttons(customize_type, button))


class SettingsSubAccountDetailsPage(SettingsSubAccountDetailsBase, BaseTestCase):
    def switch_to_settings_sub_accounting_details_frame(self):
        self.switch_to_frame(self.settings_sub_accounting_details_frame())

    def click_settings_sub_accounting_details_buttons(self, button):
        self.click(self.settings_sub_accounting_details_buttons(button))

    def get_all_settings_sub_accounting_details_line_num(self):
        return len(self.find_visible_elements(self.settings_sub_accounting_details_line_num()))

    def click_settings_sub_accounting_details_tab_li(self, tab_name):
        self.click(self.settings_sub_accounting_details_tab_li(tab_name))

    def select_customize_sub_accounting(self, item):
        self.click(self.settings_sub_accounting_details_customize_type_selector())
        self.click(self.settings_sub_accounting_details_customize_dropdown_items(item))

    def search_sub_accounting_item(self, itme):
        self.type(self.settings_sub_accounting_details_search_input(), itme)
        self.click_settings_sub_accounting_details_buttons('查询')

    def click_settings_sub_accounting_details_checkbox_in_line_by_code(self, code):
        self.check_if_unchecked(self.settings_sub_accounting_details_checkbox_in_line_by_code(code))

    def click_settings_sub_accounting_details_operate_buttons_in_line_by_code(self, code, button):
        self.click(self.settings_sub_accounting_details_operate_buttons_in_line_by_code(code, button))

    def click_settings_sub_accounting_details_button_by_name(self, name):
        self.click(self.settings_sub_accounting_details_button_by_name(name))

    def click_settings_sub_accounting_details_download_template(self):
        self.click(self.settings_sub_accounting_details_download_template())
        self.wait(3)

    def upload_file_to_settings_sub_accounting_details_upload_file_input(self, file_path):
        self.choose_file(self.settings_sub_accounting_details_upload_file_input(), file_path)

    def get_text_from_settings_sub_accounting_details_import_result(self, num):
        return self.get_text(self.settings_sub_accounting_details_import_result(num))

    def get_text_from_settings_sub_accounting_details_import_result_text(self):
        return self.get_text(self.settings_sub_accounting_details_import_result_text())


class SettingsInitAcctBalancePage(SettingsInitAcctBalanceBase, BaseTestCase):
    pass


class SettingsInitCashFlowBalancePage(SettingsInitCashFlowBalanceBase, BaseTestCase):
    pass


class SettingsCashFlowItemPage(SettingsCashFlowItemBase, BaseTestCase):
    pass


class SettingsVoucherTemplatePage(SettingsVoucherTemplateBase, BaseTestCase):
    pass


class SettingsInvoiceVoucherTemplatePage(SettingsInvoiceVoucherTemplateBase, BaseTestCase):
    def switch_to_settings_invoice_voucher_template_frame(self):
        self.switch_to_frame(self.settings_invoice_voucher_template_frame())

    def click_settings_invoice_voucher_template_buttons(self, button):
        self.click(self.settings_invoice_voucher_template_buttons(button))

    def select_settings_new_invoice_voucher_template_inputs_by_label(self, label, item):
        self.click(self.settings_new_invoice_voucher_template_inputs_by_label(label))
        self.click(self.settings_new_invoice_voucher_template_input_items_by_label(label, item))

    def type_to_settings_new_invoice_voucher_template_inputs_by_label(self, label, text):
        self.type(self.settings_new_invoice_voucher_template_inputs_by_label(label), text)

    def click_settings_new_invoice_voucher_template_summary_span(self, summary):
        self.click(self.settings_new_invoice_voucher_template_summary_span(summary))

    def select_settings_new_invoice_voucher_template_dc_selector_by_line(self, line, option):
        self.select_option_by_text(self.settings_new_invoice_voucher_template_dc_selector_by_line(line), option)

    def type_to_settings_new_invoice_voucher_template_subject_input_by_line(self, line, subject):
        if subject:
            self.type(self.settings_new_invoice_voucher_template_subject_input_by_line(line), subject)
            self.wait(0.5)
            self.click(self.settings_new_invoice_voucher_template_subject_dropdown_items(subject))

    def select_settings_new_invoice_voucher_template_amount_source_input_by_line(self, line, item):
        self.click(self.settings_new_invoice_voucher_template_amount_source_input_by_line(line))
        self.click(self.settings_new_invoice_voucher_template_amount_source_items_by_line(line, item))

    def click_settings_new_invoice_voucher_template_operating_buttons_in_line(self, line, button_name):
        self.click(self.settings_new_invoice_voucher_template_operating_buttons_in_line(line, button_name))

    def fill_one_line_of_voucher_template(self, line, dc, subject, amount_source):
        self.select_settings_new_invoice_voucher_template_dc_selector_by_line(line, dc)
        self.type_to_settings_new_invoice_voucher_template_subject_input_by_line(line, subject)
        self.select_settings_new_invoice_voucher_template_amount_source_input_by_line(line, amount_source)

    def click_settings_new_invoice_voucher_template_buttons_by_id(self, button):
        self.click(self.settings_new_invoice_voucher_template_buttons_by_id(button))
        self.wait(1)

    def click_settings_invoice_voucher_template_buttons_in_line_by_method(self, method, button):
        self.click(self.settings_invoice_voucher_template_buttons_in_line_by_method(method, button))
        self.wait(2)

    def is_settings_invoice_voucher_template_line_empty(self):
        return self.find_visible_elements(self.settings_invoice_voucher_template_tr())

    def click_settings_invoice_voucher_template_sync_radio(self, value):
        self.click(self.settings_invoice_voucher_template_sync_radio(value))

    def click_settings_invoice_voucher_template_sync_save_button(self):
        self.click(self.settings_invoice_voucher_template_sync_save_button())

    def type_to_settings_invoice_voucher_template_acct_search_input(self, text):
        self.type(self.settings_invoice_voucher_template_acct_search_input(), text)

    def click_settings_invoice_voucher_template_acct_search_result(self, text):
        self.click(self.settings_invoice_voucher_template_acct_search_result(text))

    def click_settings_invoice_voucher_template_copy_submit_button(self):
        self.click(self.settings_invoice_voucher_template_copy_submit_button())
