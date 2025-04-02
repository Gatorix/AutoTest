from seleniumbase.common.exceptions import NoSuchElementException

from base.accounting.base_smart_bookkeeping import OrganizeInvoiceBase
from base.accounting.base_smart_bookkeeping import OutputInvoiceBase
from base.accounting.base_smart_bookkeeping import BankBillBase
from base.accounting.base_smart_bookkeeping import IncomeInvoiceBase
from base.accounting.base_smart_bookkeeping import CostInvoiceBase
from base.base_case import BaseTestCase


class OrganizeInvoicePage(OrganizeInvoiceBase, BaseTestCase):
    def click_organize_invoice_button(self, button_name):
        self.click(self.organize_invoice_buttons(button_name))

    def click_organize_invoice_upload_page_buttons(self, button_name):
        self.click(self.organize_invoice_upload_page_buttons(button_name))

    def upload_file_to_organize_invoice_upload_page_input(self, filepath):
        self.choose_file(self.organize_invoice_upload_page_input(), filepath)

    def close_organize_invoice_tips(self):
        if self.is_element_visible(self.upload_tips()):
            self.click(self.upload_tips())

    def switch_to_organize_invoice_frame(self):
        self.switch_to_frame(self.organize_invoice_frame())
        self.wait(3)
        self.close_organize_invoice_tips()

    def click_more_button(self):
        self.click(self.more_button())
        self.wait(1)

    def click_more_items(self, item):
        self.click(self.more_button_items(item))
        if '导出' in item:
            self.wait(5)

    def click_organize_invoice_check_all_button(self):
        self.click(self.organize_invoice_check_all_button())

    def specified_template_list(self, invoice_num, template_type):
        self.click(self.list_template_type_by_invoice_num(invoice_num))
        self.wait(1)
        self.click(self.list_template_type_items_by_invoice_num(template_type))

    def switch_visual_type(self, button):
        self.click(self.switch_to_list_or_graphic(button))

    def click_list_view_img_by_number(self, num):
        self.click(self.list_view_img_by_number(num))

    def click_edit_bill_table_input(self):
        self.click(self.edit_bill_table_input())

    def click_edit_bill_table_drop_items(self, text):
        self.click(self.edit_bill_table_drop_items(text))

    def is_edit_bill_scroll_bar_exist(self):
        return self.is_element_visible(self.edit_bill_scroll_bar())

    def sent_text_to_edit_bill_table_inputs_by_label(self, label, text):
        self.type(self.edit_bill_table_inputs_by_label(label), text)

    def click_edit_bill_table_save_button(self):
        self.click(self.edit_bill_table_save_button())
        self.wait(1)

    def is_edit_bill_tags_visible(self, tag):
        return self.is_element_visible(self.edit_bill_tags_by_class(tag))

    def is_bill_list_tags_by_class_visible(self, num, tag):
        return self.is_element_visible(self.bill_list_tags_by_class(num, tag))

    def click_edit_bill_close_button(self):
        self.click(self.edit_bill_close_button())

    def specified_template_by_button(self, invoice_num, template_type):
        self.click(self.list_checkbox_by_invoice_num(invoice_num))
        self.click_organize_invoice_button('指定票据模板')
        self.wait(0.5)
        self.click(self.specified_template_type_input_box())
        self.click(self.specified_template_type_dropdown_items(template_type))
        self.click(self.specified_template_type_buttons())
        self.wait(1)

    def clear_template(self, invoice_num):
        self.click(self.list_checkbox_by_invoice_num(invoice_num))
        self.click_organize_invoice_button('指定票据模板')
        self.wait(0.5)
        self.click(self.specified_template_type_buttons('清除已指定模板'))
        self.click(self.conform_buttons('确定'))
        self.wait(1)

    def click_list_check_box(self, invoice_num):
        self.wait_for_element_clickable(self.list_checkbox_by_invoice_num(invoice_num))
        self.click(self.list_checkbox_by_invoice_num(invoice_num))
        self.wait(1)

    def click_multiple_checkbox(self, invoice_list):
        for _ in invoice_list:
            self.click(self.list_checkbox_by_invoice_num(_))
            self.wait(0.5)

    def is_invoice_related_to_voucher(self, invoice_num):
        return self.find_visible_elements(self.list_voucher_mark_by_invoice_num(invoice_num))
        # return self.is_element_visible(self.list_voucher_mark_by_invoice_num(invoice_num))

    def match_system_items(self, invoice_num):
        self.click(self.list_checkbox_by_invoice_num(invoice_num))
        self.click_organize_invoice_button('匹配系统商品')

    def check_return_mark(self, invoice_num):
        return self.is_element_visible(self.list_return_mark_by_invoice_num(invoice_num))

    def check_no_booking_mark(self, invoice_num):
        return self.is_element_visible(self.list_no_booking_mark_by_invoice_num(invoice_num))

    def check_cross_mark(self, invoice_num):
        return self.is_element_visible(self.list_mark_cross_by_invoice_num(invoice_num))

    def check_acct_mark(self, invoice_num):
        return self.is_element_visible(self.list_mark_acct_by_invoice_num(invoice_num))

    def click_return_choice(self, idx, reason=''):
        self.click(self.return_choice(idx))
        if idx == 3:
            self.type(self.return_reason(), reason)
        self.click(self.return_invoice_buttons())

    def adj_period(self, period, reason=''):
        self.select_option_by_value(self.adj_period_select(), period)
        self.wait(0.5)
        self.type(self.adj_reason(), reason)
        self.click(self.adj_buttons())

    def select_period(self, period):
        self.click(self.query_period())
        self.click(self.period_item(period))
        self.click_refresh()
        self.wait(1)

    def select_account_status(self, status):
        self.click(self.query_account())
        self.click(self.account_item(status))
        self.click_refresh()
        self.wait(1)

    def click_refresh(self):
        self.click(self.refresh())
        self.wait(1)

    def click_list_voucher_link(self, num):
        self.click(self.list_voucher_by_invoice_num(num))

    def set_generate_voucher_summary_setting(self, setting):
        self.click(self.summary_settings_dropdown_button())
        self.click(self.dropdown_button_item())
        self.click(self.generate_voucher_settings_checkbox(setting))
        self.click(self.generate_voucher_settings_buttons())
        self.wait(1)

    def click_generate_voucher_manually_button(self):
        self.click(self.generate_voucher_manually_button())
        self.wait(1)

    def click_close_invoice_detail(self):
        self.click(self.close_invoice_detail())

    def click_invoice_wrapper_buttons(self, button):
        self.click(self.invoice_wrapper_buttons(button))


class OutputInvoicePage(OutputInvoiceBase, BaseTestCase):
    def switch_to_output_invoice_iframe(self):
        self.switch_to_frame(self.output_invoice_frame())
        self.wait(1)
        self.close_output_invoice_popup()

    def click_output_invoice_more_button(self):
        self.click(self.output_invoice_more_button())

    def click_output_invoice_filters_input_source(self):
        self.click(self.output_invoice_filters_input_source())

    def is_output_invoice_filters_input_drop_down_items_present(self, item):
        return self.is_element_present(self.output_invoice_filters_input_drop_down_items(item))

    def output_invoice_switch_status(self, item):
        self.click(self.output_invoice_status_input())
        self.click(self.output_invoice_status_items(item))

    def click_smart_collection(self):
        self.click(self.smart_collection())

    def click_smart_collection_import(self):
        self.click(self.smart_collection_import())
        self.wait(5)

    def is_smart_collection_digital_file_tips_visible(self):
        return self.is_element_visible(self.smart_collection_digital_file_tips())

    def is_smart_collection_digital_file_img_visible(self):
        return self.is_element_visible(self.smart_collection_digital_file_img())

    def click_smart_collection_digital_file_show_img_button(self):
        self.click(self.smart_collection_digital_file_show_img_button())
        self.wait(1)

    def click_smart_collection_digital_file_img_close_button(self):
        self.click(self.smart_collection_digital_file_img_close_button())

    def click_smart_collection_import_method_checkbox(self, method):
        self.click(self.smart_collection_import_method_checkbox(method))
        self.wait(0.5)

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)
        self.wait(1)

    def click_smart_collection_import_select_button(self):
        self.wait(0.5)
        self.execute_script('document.getElementById("importWages-file").click()')
        self.wait(0.5)
        # self.click(self.smart_collection_import_select_button())

    def click_smart_collection_import_buttons(self):
        self.wait(1)
        self.execute_script('document.getElementById("save-import").click()')
        self.wait(3)

    def close_output_invoice_popup(self):
        if self.is_element_visible(self.popup_box_button()):
            self.click(self.popup_box_button())
        self.wait(1)

    def type_date(self, start_date, end_date):
        self.type(self.start_date(), f'{start_date}\n')
        self.wait(1)
        self.type(self.end_date(), f'{end_date}\n')
        self.wait(0.5)

    def change_page_size(self, per):
        self.click(self.page_size_input())
        self.click(self.page_size_list(per))

    def select_page(self, page_num):
        self.click(self.page_size_li(str(page_num)))

    def get_current_page_num(self):
        return self.get_text(self.current_page_num())

    def click_refresh(self):
        self.click(self.refresh())
        self.wait(0.5)

    def click_invoice_checkbox(self, bill_code="88888888"):
        self.click(self.invoice_checkbox(bill_code))

    def click_multiple_invoice_checkbox(self, bill_list):
        for idx, _ in enumerate(bill_list):
            self.click(self.invoice_checkbox(_))
            self.wait(0.5)

    def is_bill_code_exist(self, bill_code="88888888"):
        return self.is_element_visible(self.invoice_bill_code(bill_code))

    def click_normal_button(self, button_name):
        self.click(self.normal_button(button_name))
        self.wait(0.5)

    def click_more_buttons(self, button_name):
        self.click(self.more_button())
        self.click(self.more_dropdown_button(button_name))
        if '导出' in button_name:
            self.wait(2)

    def click_download_template(self):
        self.click(self.download_template())
        self.wait(3)

    def click_type_checkbox(self, text):
        self.click(self.smart_collection_import_type_checkbox(text))

    def click_import_type(self, import_type):
        self.click(self.import_software_output_input())
        self.click(self.import_software_output_type(import_type))

    def click_select_all(self):
        self.click(self.list_select_all())

    def click_voucher_template(self, bill_code):
        if self.is_element_visible(self.list_voucher_template(bill_code)):
            self.click(self.list_voucher_template(bill_code))
        else:
            self.click(self.list_voucher_template_new(bill_code))

    def select_voucher_template(self, bill_code, template_type):
        if self.is_element_visible(self.list_voucher_template_type(bill_code, template_type)):
            self.click(self.list_voucher_template_type(bill_code, template_type))
            self.wait(0.5)
        else:
            self.click(self.list_voucher_template_type_new(bill_code, template_type))
            self.wait(0.5)

    def is_billing_method_visible(self, bill_code, method):
        return self.is_element_present(self.list_billing_method_new(bill_code, method))

    def click_specified_billing_method_input(self):
        self.click(self.specified_billing_method_input())

    def click_specified_billing_method_dropdown_items(self, item):
        self.click(self.specified_billing_method_dropdown_items(item))

    def click_specified_billing_method_buttons(self, button):
        self.click(self.specified_billing_method_buttons(button))

    def click_clear_billing_method_buttons(self, button):
        self.click(self.clear_billing_method_buttons(button))

    def click_list_generate_voucher_button(self, bill_code):
        if self.is_element_visible(self.list_generate_voucher_button(bill_code)):
            self.click(self.list_generate_voucher_button(bill_code))
            self.wait(0.5)
        else:
            self.click(self.list_generate_voucher_button_new(bill_code))
            self.wait(0.5)

    def is_output_invoice_voucher_exist(self, bill_code):
        if any([self.is_element_visible(self.list_generate_voucher_button(bill_code)),
                self.is_element_visible(self.list_generate_voucher_button_new(bill_code))]):
            return True

    def click_list_output_invoice_voucher_link_by_bill_code(self, bill_code):
        if self.is_element_visible(self.list_output_invoice_voucher_link_by_bill_code(bill_code)):
            self.click(self.list_output_invoice_voucher_link_by_bill_code(bill_code))
        else:
            self.click(self.list_output_invoice_voucher_link_by_bill_code_new(bill_code))

    def click_dropdown_button(self):
        self.click(self.dropdown_button())

    def click_dropdown_item(self):
        self.click(self.dropdown_button_item())

    def click_generate_voucher_settings_checkbox(self, setting):
        self.click(self.generate_voucher_settings_checkbox(setting))

    def click_generate_voucher_settings_button(self, button):
        self.click(self.generate_voucher_settings_buttons(button))

    def click_list_select_all(self):
        self.click(self.list_select_all())

    def clear_date(self):
        self.click(self.start_date())
        if self.is_element_visible(self.clear_start_date()):
            self.click(self.clear_start_date())
            self.wait(0.5)
        self.click(self.end_date())
        if self.is_element_visible(self.clear_end_date()):
            self.click(self.clear_end_date())
            self.wait(0.5)

    def outcome_invoice_input_select_drop_down_item(self, label, item):
        self.click(self.outcome_invoice_inputs_by_label(label))
        self.click(self.outcome_invoice_inputs_drop_down_items(label, item))

    def get_text_from_outcome_invoice_total_amount(self):
        return self.get_text(self.outcome_invoice_total_amount())


class BankBillPage(BankBillBase, BaseTestCase):
    def switch_to_bank_bill_frame(self):
        self.switch_to_frame(self.bank_bill_frame())
        self.wait(1)
        self.close_bank_bill_popup()

    def close_bank_bill_popup(self):
        if self.is_element_visible(self.bank_bill_popup()):
            self.click(self.bank_bill_popup())
        if self.is_element_visible(self.bank_bill_collection_popup()):
            self.click(self.bank_bill_collection_popup())
            self.click(self.bank_bill_collection_background())

    def click_bank_bill_buttons(self, button):
        self.click(self.normal_buttons(button))
        self.wait(1)

    def click_bank_bill_import_type_by_value(self, value):
        self.click(self.bank_bill_import_type_by_value(value))

    def click_bank_bill_filter_div_inputs_by_id(self, input_label):
        label_id = {
            '凭证字': 'filter-zi'
        }
        self.click(self.bank_bill_filter_div_inputs_by_id(label_id.get(input_label)))

    def type_to_bank_bill_filter_div_inputs_by_id(self, input_label, text):
        label_id = {
            '凭证号': 'filter-num'
        }
        self.type(self.bank_bill_filter_div_inputs_by_id(label_id.get(input_label)), text)

    def click_bank_bill_filter_div_dropdown_items_by_label(self, label, item):
        self.click(self.bank_bill_filter_div_dropdown_items_by_label(label, item))

    def click_bank_bill_filter_div_buttons_by_id(self, button):
        button_id = {
            '重置': 'resetCdt',
            '查询': 'refreshNew'
        }
        self.click(self.bank_bill_filter_div_buttons_by_id(button_id.get(button)))
        self.wait(1)

    def click_bank_bill_dropdown_button(self):
        self.click(self.dropdown_button())

    def click_bank_bill_white_dropdown_buttons(self, button):
        self.click(self.white_dropdown_buttons(button))
        self.wait(0.5)

    def click_bank_bill_white_dropdown_items(self, button, item):
        self.click(self.white_dropdown_items(button, item))
        self.wait(1)

    # def close_bank_bill_popup(self):
    #     if self.is_element_visible(self.popup_box_button()):
    #         self.click(self.popup_box_button())
    #     self.wait(1)

    def click_bank_bill_import_buttons(self, button):
        self.click(self.import_box_buttons(button))

    def send_filepath_to_input(self, filepath):
        self.wait(1)
        self.execute_script('document.getElementById("importWages-file-new").removeAttribute("type")')
        self.wait(1)
        self.execute_script(f'document.getElementById("importWages-file-new").value="{filepath}"')
        self.wait(1)

    def select_bank(self, bank):
        self.click(self.select_bank_input())
        self.click(self.select_bank_items(bank))

    def select_account(self):
        self.click(self.select_account_input())
        self.click(self.select_account_items())

    def click_conform_input_buttons(self):
        self.click(self.conform_input_buttons())
        self.wait(5)

    def type_date(self, start_date, end_date):
        self.type(self.start_date(), start_date)
        self.click_bank_bill_date_time_picker_activate_day_td()
        self.wait(0.5)
        self.type(self.end_date(), end_date)
        self.click_bank_bill_date_time_picker_activate_day_td()
        self.wait(0.5)

    def click_bank_bill_voucher_link_by_voucher_number(self, voucher_number):
        self.click(self.bank_bill_voucher_link_by_voucher_number(voucher_number))

    def click_bank_bill_generate_voucher_button_by_summary(self, summary):
        try:
            self.click(self.bank_bill_generate_voucher_button_by_summary(summary))
        except NoSuchElementException:
            self.click(self.bank_bill_generate_voucher_button_by_input_summary(summary))

    def clear_date(self):
        self.click(self.start_date())
        self.click(self.clear_start_date())
        self.wait(1)
        self.click(self.end_date())
        self.click(self.clear_end_date())
        self.wait(0.5)

    def click_bank_bill_inputs_by_label(self, label):
        self.click(self.bank_bill_inputs_by_label(label))

    def click_bank_bill_inputs_drop_down_items(self, label, item):
        self.click(self.bank_bill_inputs_drop_down_items(label, item))

    def bank_bill_input_select_drop_down_item(self, label, item):
        self.click_bank_bill_inputs_by_label(label)
        self.click_bank_bill_inputs_drop_down_items(label, item)

    def click_bank_bill_date_time_picker_activate_day_td(self):
        self.click(self.bank_bill_date_time_picker_activate_day_td())

    def click_refresh(self):
        self.click(self.refresh())
        self.wait(0.5)

    def click_list_query_type_by_summary(self, summary):
        self.click(self.list_query_type_by_summary(summary))

    def click_list_query_type_selector(self, summary, query_type):
        self.click(self.list_query_type_selector(summary, query_type))

    def click_list_query_type_selector_new(self, query_type):
        self.click(self.list_query_type_selector_new(query_type))

    def click_list_generate_voucher_button(self, summary):
        if self.is_element_visible(self.list_generate_voucher_button(summary)):
            self.click(self.list_generate_voucher_button(summary))
        else:
            self.click(self.list_generate_voucher_button_by_summary_display_mode(summary))

    def click_single_list_checkbox_by_summary(self, summary):
        if self.is_element_visible(self.list_checkbox_display_mode(summary)):
            self.click(self.list_checkbox_display_mode(summary))
        else:
            self.click(self.list_checkbox(summary))

    def click_multiple_list_checkbox_by_diff_summary(self, summary_list):
        for _ in summary_list:
            self.click(self.list_checkbox(_))
            self.wait(1)

    def click_multiple_checkbox_by_same_summary(self, summary):
        ele_len = 0
        if self.is_element_visible(self.list_checkbox_display_mode(summary)):
            ele_len = len(self.find_visible_elements(self.list_checkbox_display_mode(summary)))
        else:
            ele_len = len(self.find_visible_elements(self.list_checkbox(summary)))
        if ele_len > 1:
            for _ in range(ele_len):
                if self.is_element_visible(self.list_checkbox_display_mode(summary)):
                    self.click(f'({self.list_checkbox_display_mode(summary)})[{_ + 1}]')
                else:
                    self.click(f'({self.list_checkbox(summary)})[{_ + 1}]')
                self.wait(0.5)
        else:
            if self.is_element_visible(self.list_checkbox_display_mode(summary)):
                self.click(self.list_checkbox_display_mode(summary))
            else:
                self.click(self.list_checkbox(summary))

    def list_specified_voucher_template(self, summary, query_type):
        if self.is_element_visible(self.list_query_type_by_summary(summary)):
            self.click_list_query_type_by_summary(summary)
            self.wait(1.5)
            if self.is_element_visible(self.list_query_type_selector_new(query_type)):
                self.click(self.list_query_type_selector_new(query_type))
            # else:
            # self.click_list_query_type_selector(summary, query_type)
        else:
            self.click(self.list_query_type_by_summary_display_mode(summary))
            # self.click(self.list_query_type_selector_display_mode(summary, query_type))
            self.wait(1.5)
            if self.is_element_visible(self.list_query_type_selector_new(query_type)):
                self.click(self.list_query_type_selector_new(query_type))

    def specified_multiple_voucher_template(self, summary_list, query_type):
        for _ in summary_list:
            self.list_specified_voucher_template(_, query_type)

    def button_specified_voucher_template(self, template, button='保存'):
        self.click(self.specified_voucher_template_input_box())
        self.click(self.specified_voucher_template_items(template))
        self.click(self.specified_voucher_template_buttons(button))
        self.wait(1)

    def clear_voucher_template(self):
        self.click(self.specified_voucher_template_buttons('清除已指定模板'))
        self.click(self.conform_clear_voucher_template())

    def set_generate_voucher_summary_setting(self, setting):
        self.click(self.summary_settings_dropdown_button())
        self.click(self.dropdown_button_item())
        self.click(self.generate_voucher_settings_checkbox(setting))
        self.click(self.generate_voucher_settings_buttons())
        self.wait(1)

    def click_select_all(self):
        self.click(self.list_select_all())

    def click_download_standard_template(self):
        self.click(self.download_standard_template())
        self.wait(3)

    def click_select_file_button(self):
        # self.click(self.select_file_button())
        self.wait(1)
        self.execute_script('document.getElementById("importWages-file-new").click()')
        self.wait(1)

    def get_text_from_bank_bill_total_num(self):
        return self.get_text(self.bank_bill_total_num())

    def get_text_from_bank_bill_import_result(self):
        actual_result = []
        self.wait_for_element_visible(self.bank_bill_pdf_import_result_table())
        for _ in range(3):
            actual_result.append(self.get_text(self.bank_bill_import_result(_ + 1)))
        return tuple(actual_result)

    def switch_bank_bill_page_size(self, page_size='1000'):
        self.click(self.bank_bill_page_size_input())
        self.click(self.bank_bill_page_size_selector(page_size))

    def click_bank_bill_select_all(self):
        self.click(self.bank_bill_select_all())

    def click_bank_bill_operate_buttons_in_line(self, line, button):
        self.click(self.bank_bill_operate_buttons_in_line(line, button))

    def type_to_bank_bill_inputs_in_line(self, line, input_class, value):
        self.type(self.bank_bill_inputs_in_line(line, input_class), value)

    def choose_file_to_select_file(self, file):
        self.choose_file(self.select_file_input(), file)

    def click_select_bank(self, bank):
        self.click(self.select_bank_input())
        self.click(self.select_bank_span(bank))

    def click_select_subject(self, subject):
        self.click(self.select_subject_input())
        self.click(self.select_subject_list_div(subject))

    def click_import_bank_bill_conform_button(self):
        self.click(self.import_bank_bill_conform_button())
        self.wait(3)
        self.wait_for_import_img_not_visible()

    def type_to_bank_bill_password_input(self, password):
        self.type(self.bank_bill_password_input(), password)

    def click_bank_bill_password_conform_button(self):
        self.click(self.bank_bill_password_conform_button())
        self.wait(1)

    def wait_for_import_img_not_visible(self):
        self.wait_for_element_not_visible(self.import_bank_bill_wait_img(), timeout=30)

    def get_list_total_num(self):
        return self.get_text(self.list_total_num())

    def click_import_bank_bill_radio(self, radio):
        self.click(self.import_bank_bill_radio(radio))

    def switch_to_bank_bill_standard_import_config_iframe(self):
        self.switch_to_frame(self.bank_bill_standard_import_config_iframe())

    def click_bank_bill_standard_import_config_auto_button(self):
        self.click(self.bank_bill_standard_import_config_auto_button())
        self.wait(0.5)

    def click_bank_bill_standard_import_config_radios(self, radio_name):
        self.click(self.bank_bill_standard_import_config_radios(radio_name))

    def click_bank_bill_standard_import_config_tips(self):
        for _ in range(4):
            if self.is_element_visible(self.bank_bill_standard_import_config_tips(_)):
                self.click(self.bank_bill_standard_import_config_tips(_))

    def click_bank_bill_table_head_sort_div_by_name(self, name):
        self.click(self.bank_bill_table_head_sort_div_by_name(name))
        self.wait(0.5)

    def get_text_from_bank_bill_table_row_input_values_by_class(self, line, class_name):
        if self.is_element_visible(self.bank_bill_table_row_input_values_by_class(line, class_name)):
            return self.get_text(self.bank_bill_table_row_input_values_by_class(line, class_name))
        else:
            return self.get_text(self.bank_bill_table_row_div_values_by_class(line, class_name))

    def get_text_from_bank_bill_table_voucher_num_value(self, line):
        return self.get_text(self.bank_bill_table_voucher_num_value(line))


class IncomeInvoicePage(IncomeInvoiceBase, BaseTestCase):
    def switch_to_bill_income_frame(self):
        self.switch_to_frame(self.bill_income_frame())
        self.wait(2)
        self.close_income_invoice_popup()

    def click_income_invoice_more_button(self):
        self.click(self.income_invoice_more_button())

    def click_income_invoice_filters_input_source(self):
        self.click(self.income_invoice_filters_input_source())

    def is_income_invoice_filters_input_drop_down_items_present(self, item):
        return self.is_element_present(self.income_invoice_filters_input_drop_down_items(item))

    def send_filepath_to_input(self, filepath):
        self.choose_file(self.file_input(), filepath)
        self.wait(1)

    def close_income_invoice_popup(self):
        if self.is_element_visible(self.popup_box_button()):
            self.click(self.popup_box_button())
        self.wait(1)

    def click_income_invoice_buttons(self, button):
        self.click(self.normal_buttons(button))

    def click_income_invoice_white_dropdown_button(self, button, item):
        self.click(self.white_dropdown_buttons(button))
        self.click(self.white_dropdown_items(button, item))
        self.wait(0.5)
        if '导出' in item:
            self.wait(2)

    def change_page_size(self, per):
        self.click(self.page_size_input())
        self.click(self.page_size_list(per))

    def select_page(self, page_num):
        self.click(self.page_size_li(str(page_num)))

    def get_current_page_num(self):
        return self.get_text(self.current_page_num())

    def click_import_type_radio(self, value):
        self.click(self.import_type_radio(value))

    def click_import_type_img_button(self):
        self.click(self.import_type_img_button())

    def click_import_type_img_button_2(self):
        self.click(self.import_type_img_button_2())

    def is_import_img_visible(self):
        self.wait(1)
        return self.is_element_visible(self.import_type_img())

    def click_import_type_img_close_button(self):
        self.click(self.import_type_img_close_button())

    def is_type_radio_visible(self, value):
        return self.is_element_visible(self.import_type_radio(value))

    def click_income_invoice_import_button(self):
        self.click(self.import_button())
        self.wait(3)

    def click_close_get_invoice_details_button(self):
        self.click(self.close_get_invoice_details_button())

    def get_import_result(self):
        self.get_text(self.import_result())

    def close_import_result(self):
        # self.wait(10)
        self.wait_for_text_visible('100%', self.import_process(), timeout=60)
        self.wait(0.5)
        self.click(self.import_result_button())

    def click_organize_invoice_buttons(self, button):
        button_kv = {'删除': 'delete', '刷新': 'refresh'}
        if '刷新' == button:
            self.wait(3)
            self.js_click(self.buttons_a(button_kv.get(f'{button}')))
        else:
            self.js_click(self.buttons(button_kv.get(f'{button}')))

    def click_import_method_radio(self, value):
        self.click(self.import_method_radio(value))

    def select_import_param(self, item):
        self.click(self.import_param_selector())
        self.click(self.import_param_items(item))

    def click_income_invoice_download_standard_template(self):
        self.click(self.download_template())
        self.wait(3)

    def click_list_checkbox(self, invoice_num):
        if self.is_element_visible(self.list_checkbox(invoice_num)):
            self.click(self.list_checkbox(invoice_num))
            self.wait(0.5)
        else:
            self.click(self.list_checkbox_new(invoice_num))
            self.wait(0.5)

    def is_checkbox_exist(self, invoice_num):
        if any([self.is_element_visible(self.list_checkbox(invoice_num)),
                self.is_element_visible(self.list_checkbox_new(invoice_num))]):
            return True

    def click_list_link_to_voucher_details(self, invoice_num):
        self.click(self.list_link_to_voucher_details(invoice_num))

    def click_multiple_list_checkbox(self, invoice_list):
        for _ in invoice_list:
            if self.is_element_visible(self.list_checkbox(_)):
                self.click(self.list_checkbox(_))
                self.wait(0.5)
            else:
                self.click(self.list_checkbox_new(_))
                self.wait(0.5)

    def specified_voucher_template_by_list(self, invoice_num, item):
        if self.is_element_visible(self.list_specified_voucher_template(invoice_num)):
            self.click(self.list_specified_voucher_template(invoice_num))
            self.wait(0.5)
        else:
            self.click(self.list_specified_voucher_template_new(invoice_num))
            self.wait(0.5)

        if self.is_element_visible(self.list_specified_voucher_template_items(invoice_num, item)):
            self.click(self.list_specified_voucher_template_items(invoice_num, item))
        else:
            self.click(self.list_specified_voucher_template_items_new(invoice_num, item))

    def get_text_from_list_specified_company_name(self, num):
        return self.get_text(self.list_specified_company_name(num))

    def generate_voucher_by_list(self, invoice_num):
        if self.is_element_visible(self.list_generate_voucher(invoice_num)):
            self.click(self.list_generate_voucher(invoice_num))
        else:
            self.click(self.list_generate_voucher_new(invoice_num))

    def specified_voucher_template_by_menu(self, item):
        self.click_income_invoice_buttons('指定凭证模板')
        self.wait(0.5)
        self.click(self.specified_voucher_template_input())
        self.click(self.specified_voucher_template_items(item))
        self.click(self.specified_voucher_template_buttons())

    def clear_voucher_template_by_menu(self):
        self.click_income_invoice_buttons('指定凭证模板')
        self.wait(0.5)
        self.click(self.specified_voucher_template_buttons('清除已指定模板'))
        self.click(self.conform_clear_template_buttons())

    def click_dropdown_button(self, idx=0):
        self.click(self.dropdown_button(idx))

    def check_system_goods_dropdown_item(self):
        self.click(self.system_goods_dropdown_item())

    def uncheck_system_goods_dropdown_item(self):
        self.uncheck_if_checked(self.system_goods_dropdown_item())

    def click_summary_dropdown_item(self):
        self.click(self.summary_dropdown_item())

    def is_certified_message_visible(self, value):
        return self.is_element_visible(self.conform_certified_message(value))

    def click_conform_certified_buttons(self):
        self.click(self.conform_certified_buttons())

    def click_refresh(self):
        self.click(self.refresh())
        self.wait(1)

    def query_account_status(self, status):
        self.click(self.query_account())
        self.click(self.query_account_items(status))
        self.click_refresh()

    def set_generate_voucher_summary_setting(self, setting):
        self.click(self.dropdown_button())
        self.click(self.dropdown_button_item())
        self.click(self.generate_voucher_settings_checkbox(setting))
        self.click(self.generate_voucher_settings_buttons())
        self.wait(1)

    def clear_date(self):
        self.click(self.start_date())
        if self.is_element_visible(self.clear_start_date()):
            self.click(self.clear_start_date())
            self.wait(0.5)
        self.click(self.end_date())
        if self.is_element_visible(self.clear_end_date()):
            self.click(self.clear_end_date())
            self.wait(0.5)

    def income_invoice_input_select_drop_down_item(self, label, item):
        self.click(self.income_invoice_inputs_by_label(label))
        self.click(self.income_invoice_inputs_drop_down_items(label, item))


class CostInvoicePage(CostInvoiceBase, BaseTestCase):
    def switch_to_cost_invoice_page(self):
        self.switch_to_frame(self.cost_invoice_frame())
        self.wait(0.5)

    def click_cost_invoice_buttons(self, button):
        self.click(self.cost_invoice_buttons(button))

    def click_cost_invoice_generate_voucher_settings_arrows_button(self):
        self.click(self.cost_invoice_generate_voucher_settings_arrows_button())

    def type_to_cost_invoice_filter_input_by_label(self, label, text):
        self.type(self.cost_invoice_filter_input_by_label(label), text)

    def type_to_cost_invoice_table_input_by_line_num(self, line, cls, text):
        self.type(self.cost_invoice_table_input_by_line_num(line, cls), text)

    def get_text_from_cost_invoice_table_input_by_line_num(self, line, cls):
        return self.get_text(self.cost_invoice_table_input_by_line_num(line, cls))

    def click_cost_invoice_table_operate_buttons_by_line_num(self, line, button):
        self.click(self.cost_invoice_table_operate_buttons_by_line_num(line, button))
