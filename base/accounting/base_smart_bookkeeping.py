class OrganizeInvoiceBase:
    @staticmethod
    def organize_invoice_buttons(button_name):
        return f'//div[@id="pageOne" and @class="organizeBills"]//span[@class="ui-btn ui-btn-sp" and text()="{button_name}"]'

    @staticmethod
    def organize_invoice_upload_page_buttons(button_name):
        return f'//div[@id="upload-attachment-dia"]//div[@class="btns upload-file"]/div[text()="{button_name}"]'

    @staticmethod
    def organize_invoice_upload_page_input():
        return f'//div[@id="upload-attachment-dia"]//div[@class="upload-file2"]//following-sibling::input[@type="file"]'

    @staticmethod
    def upload_tips():
        return f'//div[@id="uploadAttachTips"]//div[text()="我知道了"]'

    @staticmethod
    def organize_invoice_frame():
        return 'bill-bill'

    @staticmethod
    def more_button():
        return '//div[@class="organizeBills"]//a//parent::div[contains(@class,"btn")]'

    @staticmethod
    def more_button_items(item):
        return f'//div[@class="organizeBills"]//div[contains(@class,"more-operate")]//div[text()="{item}"]'

    @staticmethod
    def organize_invoice_check_all_button():
        return f'//input[@id="all-check"]'

    @staticmethod
    def list_checkbox_by_invoice_num(invoice_num):
        return f'//span[contains(text(),"{invoice_num}")]//parent::span//preceding-sibling::span//input[@type="checkbox"]'

    @staticmethod
    def list_template_type_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//parent::div//input[@type="text"]'

    @staticmethod
    def list_template_type_items_by_invoice_num(invoice_num):
        return f'//div[@id="hd-type-list1"]//parent::div[contains(@style,"display: block;")]//div[text()="{invoice_num}"]'

    @staticmethod
    def list_voucher_mark_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//preceding-sibling::div//img[contains(@src,"acct")]'

    @staticmethod
    def list_voucher_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//following-sibling::span//a[@tabid="voucherDetail"]'

    @staticmethod
    def list_return_mark_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//parent::div//img[contains(@src,"return")]'

    @staticmethod
    def list_no_booking_mark_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//parent::div//img[contains(@src,"nobooking")]'

    @staticmethod
    def list_mark_cross_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//parent::div//img[contains(@src,"mark_cross")]'

    @staticmethod
    def list_mark_acct_by_invoice_num(invoice_num):
        return f'//span[text()="{invoice_num}"]//parent::span//parent::div//img[contains(@src,"mark_acct")]'

    @staticmethod
    def refresh():
        return '//span[@id="drop-query"]'

    @staticmethod
    def list_select_all():
        return '//input[@id="all-check"]'

    @staticmethod
    def specified_template_type_input_box():
        return '//div[@aria-hidden="false"]//input[@id="add-skfptype-value"]'

    @staticmethod
    def specified_template_type_dropdown_items(item):
        return f'//div[@aria-hidden="false"]//div[text()="{item}"]'

    @staticmethod
    def specified_template_type_buttons(button="保存"):
        return f'//div[@aria-hidden="false"]//button[text()="{button}"]'

    @staticmethod
    def conform_buttons(button="取消"):
        return f'//div[contains(@style,"visibility: visible;")]//input[@value="{button}"]'

    @staticmethod
    def switch_to_list_or_graphic(button):
        if button == '列表':
            return '//span[@id="switch-list"]'
        elif button == '图像':
            return '//span[@id="switch-graphic"]'
        else:
            raise Exception('无效类型')

    @staticmethod
    def list_view_img_by_number(num):
        return f'//div[@id="con-list"]//span[text()="{num}"]//preceding-sibling::span/img'

    @staticmethod
    def edit_bill_table_input():
        return f'//input[@id="i-type-txt"]'

    @staticmethod
    def edit_bill_table_drop_items(text):
        return f'//div[@id="i-type-list"]//div[text()="{text}"]'

    @staticmethod
    def edit_bill_scroll_bar():
        return f'//div[@id="money-wraper" and contains(@style,"")]'

    @staticmethod
    def edit_bill_table_inputs_by_label(label):
        return f'//div[@id="errInfoTable"]//span[contains(text(),"{label}")]/following-sibling::input'

    @staticmethod
    def edit_bill_table_save_button():
        return f'//button[@id="saveBillGetPdt"]'

    @staticmethod
    def edit_bill_tags_by_class(tag):
        return f'//div[@id="i-info-tag"]/img[contains(@class,"{tag}")]'

    @staticmethod
    def bill_list_tags_by_class(num, tag):
        return f'//div[@id="con-list"]//div[@data-billno="{num}"]//div[@class="bill_tag_wraper"]/img[contains(@class,"{tag}")]'

    @staticmethod
    def edit_bill_close_button():
        return '//div[@id="i-info-close"]'

    @staticmethod
    def adj_period_select():
        return '//div[@id="pop-up"]//select[@id="multiPeriod-period"]'

    @staticmethod
    def adj_reason():
        return '//div[@id="pop-up"]//textarea'

    @staticmethod
    def adj_buttons(button='确定'):
        return f'//div[@id="pop-up"]//input[@type="button" and @value="{button}"]'

    @staticmethod
    def return_choice(choice_idx):
        return f'(//div[@id="pop-up"]//input[@type="radio"])[{choice_idx}]'

    @staticmethod
    def return_invoice_buttons(button='确定'):
        return f'//div[@id="pop-up"]//input[@type="button" and @value="{button}"]'

    @staticmethod
    def return_reason():
        return '//div[@id="pop-up"]//textarea'

    @staticmethod
    def query_period():
        return '//input[@id="query-period"]'

    @staticmethod
    def period_item(period):
        return f'//div[@data-value="{period}"]'

    @staticmethod
    def query_account():
        return '//input[@id="query-account"]'

    @staticmethod
    def account_item(item):
        return f'//input[@id="query-account"]//parent::div//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def summary_settings_dropdown_button():
        return '//div[@class="organizeBills"]//span//div[@class="hd_arrows"]'

    @staticmethod
    def dropdown_button_item():
        return '//div[@class="organizeBills"]//div[text()="凭证汇总选项"]'

    @staticmethod
    def generate_voucher_settings_checkbox(setting):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//label[text()="{setting}"]//preceding-sibling::input'

    @staticmethod
    def generate_voucher_settings_buttons(button='确定'):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//input[@value="{button}"]'

    @staticmethod
    def generate_voucher_manually_button():
        return '//input[@id="i-createMultiple"]'

    @staticmethod
    def close_invoice_detail():
        return '//div[@id="i-info-close"]'

    @staticmethod
    def invoice_wrapper_buttons(button):
        kv = {'生成凭证': 'i-createMultiple', '关闭': 'i-info-close'}
        return f'//*[@id="{kv.get(button)}"]'


class OutputInvoiceBase:
    @staticmethod
    def output_invoice_frame():
        return 'bill-taxInvoice'

    @staticmethod
    def output_invoice_more_button():
        return '//span[@id="more4"]'

    @staticmethod
    def output_invoice_filters_input_source():
        return f'//input[@id="query-source"]'

    @staticmethod
    def output_invoice_filters_input_drop_down_items(item):
        return f'//input[@id="query-source"]/parent::div//following-sibling::div//div[contains(text(),"{item}")]'

    @staticmethod
    def popup_box_button():
        return '//span[@id="yunInvoiceKnow"]'

    @staticmethod
    def normal_buttons(button_name):
        return f'//span[contains(text(),"{button_name}")]'

    @staticmethod
    def smart_collection():
        return '//a[contains(text(),"智能采集")]'

    @staticmethod
    def smart_collection_import():
        return '//*[@id="importBtn"]'

    @staticmethod
    def smart_collection_cloud_collection():
        return '//*[@id="getBillYQP"]'

    @staticmethod
    def smart_collection_digital_file_tips():
        return f'//div[@class="swszzh-tip"]'

    @staticmethod
    def smart_collection_digital_file_img():
        return f'//img[@alt="exportExample1.png" and contains(@style,"transform: none;")]'

    @staticmethod
    def smart_collection_digital_file_show_img_button():
        return '//a[@id="exportExample"]'

    @staticmethod
    def smart_collection_digital_file_img_close_button():
        return '//div[@class="viewer-button viewer-close"]'

    @staticmethod
    def smart_collection_key_collection():
        return '//*[@id="getBillZN"]'

    @staticmethod
    def smart_collection_import_type_checkbox(text):
        """
        @param text: 开票软件导出后直接导入 或 按标准模板导入
        @return:
        """
        if text == "开票软件导出后直接导入":
            return f'(//div[@id="import-type"]//input)[1]'
        else:
            return f'(//div[@id="import-type"]//input)[2]'

    @staticmethod
    def smart_collection_import_method_checkbox(text):
        """
        @param text: 新增方式 或 覆盖方式
        @return:
        """
        if text == "新增方式":
            return f'(//div[@id="import-method"]//input)[1]'
        else:
            return f'(//div[@id="import-method"]//input)[2]'

    @staticmethod
    def smart_collection_import_buttons(text):
        """
        @param text: 取消、导入
        @return:
        """
        return f'//div[@id="importWages"]//button[contains(text(),"{text}")]'

    @staticmethod
    def smart_collection_import_select_button():
        return f'//span[@id="importWages-btn"]'

    @staticmethod
    def file_input():
        return f'//input[@id="importWages-file"]'

    @staticmethod
    def refresh():
        return '//a[@id="refresh"]'

    @staticmethod
    def invoice_checkbox(bill_code):
        return (f'//td[@aria-describedby="grid_code"]/span[text()="{bill_code}"]'
                f'//parent::td//preceding-sibling::td//input[@type="checkbox"]')

    @staticmethod
    def list_generate_voucher_button(bill_code):
        return f'//span[contains(@class,"billcode") and text()="{bill_code}"]' \
               f'//preceding-sibling::span//span[text()="生成凭证"]'

    @staticmethod
    def list_generate_voucher_button_new(bill_code):
        return f'//span[text()="{bill_code}"]/parent::td//preceding-sibling::td//span[text()="生成凭证"]'

    @staticmethod
    def list_output_invoice_voucher_link_by_bill_code(bill_code):
        return f'//span[contains(@class,"billcode") and text()="{bill_code}"]//preceding-sibling::span//a[@tabid]'

    @staticmethod
    def list_output_invoice_voucher_link_by_bill_code_new(bill_code):
        return f'//span[text()="{bill_code}"]/parent::td//preceding-sibling::td//a[@tabid]'

    @staticmethod
    def output_invoice_status_input():
        return f'//input[@id="query-account"]'

    @staticmethod
    def output_invoice_status_items(item):
        return f'//input[@id="query-account"]//parent::div//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def invoice_bill_code(bill_code):
        return f'//span[contains(@class,"billcode") and text()="{bill_code}"]'

    @staticmethod
    def normal_button(button_name):
        return f'//span[text()="{button_name}"]'

    @staticmethod
    def dropdown_button():
        return '//div[@id="pageOne"]//span//div[@class="hd_arrows"]'

    @staticmethod
    def dropdown_button_item():
        return '//div[@id="pageOne"]//div[text()="凭证汇总选项"]'

    @staticmethod
    def generate_voucher_settings_checkbox(setting):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//label[text()="{setting}"]//preceding-sibling::input'

    @staticmethod
    def generate_voucher_settings_buttons(button):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//input[@value="{button}"]'

    # @staticmethod
    # def list_select_all():
    #     return '//input[@id="select-all"]'

    @staticmethod
    def more_button():
        return '//a[contains(text(),"更多")]'

    @staticmethod
    def more_dropdown_button(button_name):
        return f'//div[contains(@class,"more")]//div[text()="{button_name}"]'

    @staticmethod
    def download_template():
        return '//a[text()="下载销项发票模板"]'

    @staticmethod
    def import_software_output_input():
        return '//div[@id="importWages" and not(@aria-hidden="true")]//' \
               'label[contains(text(),"发票")]//following-sibling::div//input'

    @staticmethod
    def import_software_output_type(output_type):
        return f'//div[@id="importWages" and not(@aria-hidden="true")]' \
               f'//label[contains(text(),"发票")]//following-sibling::div' \
               f'//div[@id="import-skfptype-list"]//div[contains(text(),"{output_type}")]'

    @staticmethod
    def list_select_all():
        return '//div[@id="pageOne"]//input[@id="select-all"]'

    @staticmethod
    def list_voucher_template(bill_code):
        return f'//span[text()="{bill_code}"]//parent::div//input[@id="query-type"]'

    @staticmethod
    def list_voucher_template_new(bill_code):
        return f'//span[text()="{bill_code}"]/parent::td//preceding-sibling::td[@aria-describedby="grid_billTypeName"]'

    @staticmethod
    def list_voucher_template_type(bill_code, template_type):
        return f'//span[text()="{bill_code}"]//parent::div//div[text()="{template_type}"]'

    @staticmethod
    def list_voucher_template_type_new(bill_code, template_type):
        return f'//span[text()="{bill_code}"]/parent::td//preceding-sibling::td//div[text()="{template_type}"]'

    @staticmethod
    def list_billing_method(bill_code, method):
        return f'//span[text()="{bill_code}"]//parent::div//span[contains(@title,"{method}")]'

    @staticmethod
    def list_billing_method_new(bill_code, method):
        return (f'//span[text()="{bill_code}"]/parent::td'
                f'//preceding-sibling::td[@aria-describedby="grid_settlementName"]//span[@title="{method}"]')

    @staticmethod
    def list_billing_method_span_new(bill_code):
        return (f'//span[text()="{bill_code}"]/parent::td'
                f'//preceding-sibling::td[@aria-describedby="grid_settlementName"]/span')

    @staticmethod
    def specified_billing_method_input():
        return '//div[@id="addDepartment"]//input//following-sibling::span'

    @staticmethod
    def specified_billing_method_dropdown_items(item):
        return f'//div[@id="addDepartment"]//div[text()="{item}"]'

    @staticmethod
    def specified_billing_method_buttons(button):
        return f'//div[@id="addDepartment"]//button[text()="{button}"]'

    @staticmethod
    def clear_billing_method_buttons(button):
        return f'//input[@value="{button}"]'

    @staticmethod
    def start_date():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def clear_start_date():
        return '//input[@id="prevPicker"]//following-sibling::span'

    @staticmethod
    def end_date():
        return '//input[@id="endPicker"]'

    @staticmethod
    def page_size_input():
        return f'//input[@id="page-size"]'

    @staticmethod
    def page_size_list(item):
        return f'//div[@id="page-size-list"]/div[text()="{item}"]'

    @staticmethod
    def page_size_li(page_num):
        return f'//*[@id="page"]//li[@jp-data="{page_num}"]'

    @staticmethod
    def current_page_num():
        return f'//*[@id="page"]//li[@class="active"]'

    @staticmethod
    def clear_end_date():
        return '//input[@id="endPicker"]//following-sibling::span'

    @staticmethod
    def outcome_invoice_inputs_by_label(label):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def outcome_invoice_inputs_drop_down_items(label, item):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def outcome_invoice_total_amount():
        return f'//*[@id="totalAmount"]'


class BankBillBase:
    @staticmethod
    def bank_bill_frame():
        return 'bill-bankBills'

    @staticmethod
    def bank_bill_popup():
        return '//*[@id="icbc-pop-iknow"]'

    @staticmethod
    def bank_bill_collection_popup():
        return f'//*[@id="expBankCollectBtn"]'

    @staticmethod
    def bank_bill_collection_background():
        return f'//*[@id="bankCollectPopTipsWrapper"]'

    @staticmethod
    def normal_buttons(button):
        return f'//span[text()="{button}" and not(contains(@style,"display:none;"))]'

    @staticmethod
    def bank_bill_import_type_by_value(value):
        return f'//input[@name="importFileType" and  @value="{value}"]'

    @staticmethod
    def bank_bill_filter_div_inputs_by_id(inputs_id):
        return f'//div[@id="filterCon"]//input[@id="{inputs_id}"]'

    @staticmethod
    def bank_bill_filter_div_dropdown_items_by_label(label, item):
        return f'//div[@id="filterCon"]//label[contains(text(),"{label}")]//following-sibling::div//*[text()="{item}"]'

    @staticmethod
    def bank_bill_filter_div_buttons_by_id(button_id):
        return f'//div[@id="filterCon"]//button[@id="{button_id}"]'

    @staticmethod
    def dropdown_button():
        return '//span[not(contains(@style,"display:none;"))]//div[@class="hd_arrows"]'

    @staticmethod
    def white_dropdown_buttons(button):
        return f'//a[contains(text(),"{button}")]'

    @staticmethod
    def white_dropdown_items(button, item):
        if button == '智能提取':
            return f'//a[contains(text(),"{button}")]//following-sibling::div//span[contains(text(),"{item}")]'
        else:
            return f'//a[contains(text(),"{button}")]//following-sibling::div//div[contains(text(),"{item}")]'

    @staticmethod
    def popup_box_button():
        return '//span[@id="icbc-pop-iknow"]'

    @staticmethod
    def import_box_buttons(button):
        return f'//div[@aria-hidden="false"]//div[@class="modal-footer"]//button[text()="{button}"]'

    @staticmethod
    def start_date():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def clear_start_date():
        return '//input[@id="prevPicker"]//following-sibling::span'

    @staticmethod
    def end_date():
        return '//input[@id="endPicker"]'

    @staticmethod
    def clear_end_date():
        return '//input[@id="endPicker"]//following-sibling::span'

    @staticmethod
    def bank_bill_inputs_by_label(label):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def bank_bill_inputs_drop_down_items(label, item):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def bank_bill_date_time_picker_activate_day_td():
        return ('//div[contains(@class,"datetimepicker") and contains(@class,"menu") '
                'and contains(@style,"display: block;")]//td[@class="day active"]')

    @staticmethod
    def bank_bill_voucher_link_by_voucher_number(voucher_number):
        return f'//a[@tabtxt="凭证" and text()="{voucher_number}"]'

    @staticmethod
    def bank_bill_generate_voucher_button_by_summary(summary):
        return (f'//div[contains(@title,"{summary}")]//parent::div'
                f'//preceding-sibling::div[contains(@class,"voucher")]/span')

    @staticmethod
    def bank_bill_generate_voucher_button_by_input_summary(summary):
        return (f'//input[contains(@value,"{summary}")]//parent::div'
                f'//preceding-sibling::div[contains(@class,"voucher")]/span')

    @staticmethod
    def refresh():
        return '//a[@id="refresh"]'

    @staticmethod
    def list_checkbox(value):
        return f'//input[contains(@value,"{value}")]//parent::div//preceding-sibling::div//input[@type="checkbox"]'

    @staticmethod
    def list_checkbox_display_mode(value):
        return f'//*[text()="{value}"]//parent::div[@class="table_line bankBillSource"]//input[@type="checkbox"]'

    @staticmethod
    def list_query_type_by_summary(summary):
        return f'//input[@value="{summary}"]//parent::div//preceding-sibling::div//input[@id="query-type"]'

    @staticmethod
    def list_query_type_by_summary_display_mode(summary):
        return f'//*[text()="{summary}"]//parent::div//preceding-sibling::div//input[@id="query-type"]'

    @staticmethod
    def list_query_type_selector(summary, query_type):
        return f'//input[@value="{summary}"]//parent::div//preceding-sibling::div//div[text()="{query_type}"]'

    @staticmethod
    def list_query_type_selector_new(query_type):
        # return f'//div[@class="htmlBaseInputDialogStr scrollThin"]//*[contains(text(),"{query_type}")]'
        return f'//div[@class="J_drop_con_list billTypeStr scrollThin"]//*[contains(text(),"{query_type}")]'

    @staticmethod
    def list_query_type_selector_display_mode(summary, query_type):
        return f'//*[text()="{summary}"]//parent::div//preceding-sibling::div//div[text()="{query_type}"]'

    @staticmethod
    def list_generate_voucher_button(summary):
        return f'//input[@value="{summary}"]//parent::div//preceding-sibling::div//span[text()="生成凭证"]'

    @staticmethod
    def list_generate_voucher_button_by_summary_display_mode(summary):
        return f'//*[text()="{summary}"]//parent::div//preceding-sibling::div//span[text()="生成凭证"]'

    @staticmethod
    def specified_voucher_template_input_box():
        return '//input[@id="add-bills-type-value"]'

    @staticmethod
    def specified_voucher_template_items(template):
        return f'//div[@id="add-bills-type-list"]//div[text()="{template}"]'

    @staticmethod
    def specified_voucher_template_buttons(button):
        return f'//div[@aria-hidden="false"]//div[@class="modal-footer" ]//button[text()="{button}"]'

    @staticmethod
    def conform_clear_voucher_template(button='确定'):
        return f'//input[@type="button" and @value="{button}"]'

    @staticmethod
    def summary_settings_dropdown_button():
        return '//div[@id="bankBill"]//span//div[@class="hd_arrows"]'

    @staticmethod
    def dropdown_button_item():
        return '//div[@id="bankBill"]//div[text()="凭证汇总选项"]'

    @staticmethod
    def generate_voucher_settings_checkbox(setting):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//label[text()="{setting}"]//preceding-sibling::input'

    @staticmethod
    def generate_voucher_settings_buttons(button='确定'):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//input[@value="{button}"]'

    @staticmethod
    def list_select_all():
        return f'//input[@id="select-all"]'

    @staticmethod
    def download_standard_template():
        return '//div[@aria-hidden="false"]//a[contains(text(),"下载银行对账单模板")]'

    @staticmethod
    def select_file_input():
        return '//input[@id="importWages-file-new"]'

    @staticmethod
    def select_bank_input():
        return '//input[@id="import-bank-value-new"]'

    @staticmethod
    def select_bank_span(bank):
        return f'//div[@id="import-bank-list-new"]//span[text()="{bank}"]'

    @staticmethod
    def select_subject_input():
        return f'//div[@id="importWagesNew"]//label[contains(text(),"指定银行科目")]//following-sibling::div//input'

    @staticmethod
    def select_subject_list_div(subject):
        return f'//div[@id="import-banks-list-new"]//div[text()="{subject}"]'

    @staticmethod
    def import_bank_bill_conform_button():
        return f'//button[@id="save-import-new"]'

    @staticmethod
    def bank_bill_password_input():
        return f'//div[@id="PDFPasswordModal"]//input[@id="pdfPasswordInput"]'

    @staticmethod
    def bank_bill_password_conform_button():
        return f'//div[@id="PDFPasswordModal"]//*[@id="confirmPasswordBtn"]'

    @staticmethod
    def import_bank_bill_wait_img():
        return f'//table[@class="ui_border ui_state_tips ui_state_visible ui_state_focus ui_state_lock"]//td[@class="ui_icon"]/img'

    @staticmethod
    def list_total_num():
        return '//span[@id="totalNum"]'

    @staticmethod
    def import_bank_bill_radio(radio_type):
        # 0:add, 1:override
        return f'//div[@id="importWagesNew"]//label[contains(text(),"导入方式")]' \
               f'//following-sibling::div//input[@value="{radio_type}"]'

    @staticmethod
    def select_bank_items(bank):
        return f'//input[@id="import-bank-value-new"]//parent::div//following-sibling::div//span[text()="{bank}"]'

    @staticmethod
    def select_account_input():
        return '//input[@id="add-bank-value-new"]'

    @staticmethod
    def select_account_items(item='银行存款'):
        return f'//input[@id="add-bank-value-new"]//parent::div//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def input_file():
        return f'//input[@id="importWages-file-new"]'

    @staticmethod
    def conform_input_buttons(button="确定"):
        return f'//div[@aria-hidden="false"]//button[text()="{button}"]'

    @staticmethod
    def bank_bill_total_num():
        return '//span[@id="totalNum"]'

    @staticmethod
    def bank_bill_pdf_import_result_table():
        return f'//table[@class="ui_border ui_state_visible ui_state_focus ui_state_lock"]'

    @staticmethod
    def bank_bill_import_result(idx):
        return f'(//table//div[@class="preview-item-top"]/div/span[2])[{idx}]'

    @staticmethod
    def bank_bill_page_size_input():
        return f'//input[@id="page-size"]'

    @staticmethod
    def bank_bill_page_size_selector(page_size):
        return f'//input[@id="page-size"]/parent::div//following-sibling::div//div[@data-value="{page_size}"]'

    @staticmethod
    def bank_bill_select_all():
        return '//input[@id="select-all"]'

    @staticmethod
    def bank_bill_operate_buttons_in_line(line, button):
        # add, del
        return f'//div[@id="bank-con"]//div[@class="table_line"][{line}]//span[@class="operate operate_{button}"]'

    @staticmethod
    def bank_bill_inputs_in_line(line, input_class):
        input_kv = {
            '交易日期': 'dealDate',
            '对方': 'customer-other',
            '摘要': 'remark-val',
            '收入': 'inAmount',
            '支出': 'outAmount',
            '余额': 'amount',
        }

        return f'//div[@id="bank-con"]//div[@class="table_line"][{line}]//input[contains(@class,"{input_kv.get(input_class)}")]'

    @staticmethod
    def bank_bill_standard_import_config_iframe():
        return '//div[text()="配置导入银行对账单"]/ancestor::tr//td[@class="ui_main"]//iframe'

    @staticmethod
    def bank_bill_standard_import_config_auto_button():
        return f'//span[@id="autoRecognition"]'

    @staticmethod
    def bank_bill_standard_import_config_radios(radio_name):
        return f'//span[text()="{radio_name}"]//preceding-sibling::input'

    @staticmethod
    def bank_bill_standard_import_config_tips(num):
        return f'//button[@id="next{num + 1}"]'

    @staticmethod
    def bank_bill_table_head_sort_div_by_name(name):
        return f'//div[@id="bank-hd"]//div[@data-type="filterhd"]/text()[contains(.,"{name}")]/parent::div'

    @staticmethod
    def bank_bill_table_row_input_values_by_class(line, class_name):
        class_kv = {
            '银行': 'item_7',
            # '银行': 'bank-kind',
            '交易日期': 'item_8',
            # '对方': 'customer-other',
            '对方': 'item_9',
            # '摘要': 'remark-val',
            '摘要': 'item_10',
            # '收入': 'inAmount',
            '收入': 'item_11',
            # '支出': 'outAmount',
            '支出': 'item_12',
            # '余额': 'amount',
            '余额': 'item_13',
            # '交易备注': 'comment-val',
            '交易备注': 'item_14',
        }
        # return f'(//div[@id="bank-con"]/div)[{line}]/div//input[contains(@class,"{class_kv.get(class_name)}")]'
        return f'(//div[@id="bank-con"]/div)[{line}]/div[contains(@class,"{class_kv.get(class_name)}")]//input'

    @staticmethod
    def bank_bill_table_row_div_values_by_class(line, class_name):
        class_kv = {
            '银行': 'bank-kind',
            '交易日期': 'dealDate',
            # '对方': 'customer-other',
            '对方': 'item_9',
            # '摘要': 'remark-val',
            '摘要': 'item_10',
            # '收入': 'inAmount',
            '收入': 'item_11',
            # '支出': 'outAmount',
            '支出': 'item_12',
            # '余额': 'amount',
            '余额': 'item_13',
            # '交易备注': 'comment-val',
            '交易备注': 'item_14',
        }
        return f'(//div[@id="bank-con"]/div)[{line}]/div[contains(@class,"{class_kv.get(class_name)}")]'

    @staticmethod
    def bank_bill_table_voucher_num_value(line):
        return f'(//div[@id="bank-con"]/div)[{line}]/div[contains(@class,"voucher-id")]/*'


class IncomeInvoiceBase:
    @staticmethod
    def bill_income_frame():
        return 'bill-incomeInvoice'

    @staticmethod
    def income_invoice_more_button():
        return '//span[@id="more4"]'

    @staticmethod
    def income_invoice_filters_input_source():
        return f'//input[@id="query-source"]'

    @staticmethod
    def income_invoice_filters_input_drop_down_items(item):
        return f'//input[@id="query-source"]/parent::div//following-sibling::div//div[contains(text(),"{item}")]'

    @staticmethod
    def normal_buttons(button):
        return f'//span[text()="{button}" and not(contains(@style,"display:none;"))]'

    @staticmethod
    def dropdown_button(idx=0):
        if idx == 1:
            return '(//span[text()="匹配系统商品" and not(contains(@style,"display:none;"))]//following-sibling::div//div[@class="hd_arrows"])[1]'
        else:
            return '//span[text()="汇总生成凭证" and not(contains(@style,"display:none;"))]//following-sibling::div//div[@class="hd_arrows"]'

    @staticmethod
    def page_size_input():
        return f'//input[@id="page-size"]'

    @staticmethod
    def page_size_list(item):
        return f'//div[@id="page-size-list"]/div[text()="{item}"]'

    @staticmethod
    def page_size_li(page_num):
        return f'//*[@id="page"]//li[@jp-data="{page_num}"]'

    @staticmethod
    def current_page_num():
        return f'//*[@id="page"]//li[@class="active"]'

    @staticmethod
    def dropdown_button_item():
        return '//div[@id="vhrSumChoice"]'

    @staticmethod
    def generate_voucher_settings_checkbox(setting):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//label[text()="{setting}"]//preceding-sibling::input'

    @staticmethod
    def generate_voucher_settings_buttons(button='确定'):
        return f'//div[text()="汇总凭证选项"]//ancestor::tr//input[@value="{button}"]'

    @staticmethod
    def summary_dropdown_item():
        return '//div[@id="vhrSumChoice"]'

    @staticmethod
    def system_goods_dropdown_item():
        return '//input[@id="templateSub"]'

    @staticmethod
    def import_type_radio(value):
        return f'//input[@type="radio" and @name="importType" and @value="{value}"]'

    @staticmethod
    def import_type_img_button():
        return '//a[@id="exportImg"]'

    @staticmethod
    def import_type_img_button_2():
        return '//a[@id="exportExample"]'

    @staticmethod
    def import_type_img():
        return '//div[@id="viewer0"]//div[@class="viewer-canvas"]'

    @staticmethod
    def import_type_img_close_button():
        return '//div[@id="viewer0"]//div[@role="button"]'

    @staticmethod
    def file_input():
        return '//input[@id="importWages-file"]'

    @staticmethod
    def import_button():
        return '//button[@id="save-import"]'

    @staticmethod
    def close_get_invoice_details_button():
        return '//h3[text()="获取商品明细"]//parent::div//following-sibling::div//button[text()="关闭"]'

    @staticmethod
    def import_result():
        return '//p//span[@id="susCount"]'

    @staticmethod
    def import_process():
        return '//div[@id="progerssTip"]//div[@class="progress-text"]'

    @staticmethod
    def import_result_button():
        return '//div[@id="progerssTip"]//button'

    @staticmethod
    def buttons(button):
        return f'//div[@id="{button}"]'

    @staticmethod
    def buttons_a(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def import_method_radio(value):
        """
        @param value: 新增：0，覆盖：1
        @return:
        """
        return f'//li[not(contains(@style,"none"))]/div[@id="import-method"]//input[@value="{value}"]'

    @staticmethod
    def import_param_selector():
        return '//input[@id="import-skfptype-value"]'

    @staticmethod
    def import_param_items(item):
        return f'//div[@id="import-skfptype-list"]//div[text()="{item}"]'

    @staticmethod
    def download_template():
        return '//a[text()="下载进项发票模板"]'

    @staticmethod
    def white_dropdown_buttons(button):
        return f'//a[contains(text(),"{button}")]'

    @staticmethod
    def white_dropdown_items(button, item):
        return f'//a[contains(text(),"{button}")]//following-sibling::div//div[text()="{item}"]'

    @staticmethod
    def start_date():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def clear_start_date():
        return '//input[@id="prevPicker"]//following-sibling::span'

    @staticmethod
    def end_date():
        return '//input[@id="endPicker"]'

    @staticmethod
    def clear_end_date():
        return '//input[@id="endPicker"]//following-sibling::span'

    @staticmethod
    def query_account():
        return '//input[@id="query-account"]'

    @staticmethod
    def query_account_items(item):
        return f'//input[@id="query-account"]//parent::div//following-sibling::div//div[contains(text(),"{item}")]'

    @staticmethod
    def refresh():
        return '//a[@id="refresh"]'

    @staticmethod
    def list_checkbox(value):
        return f'//span[contains(text(),"{value}")]//parent::div//input[@type="checkbox"]'

    @staticmethod
    def list_checkbox_new(value):
        return f'//span[contains(text(),"{value}")]//parent::td//preceding-sibling::td//input[@type="checkbox"]'

    @staticmethod
    def list_generate_voucher(value):
        return f'//span[contains(text(),"{value}")]//parent::div//span[text()="生成凭证"]'

    @staticmethod
    def list_generate_voucher_new(value):
        return f'//span[contains(text(),"{value}")]/parent::td//preceding-sibling::td[@aria-describedby="grid_voucherId"]//span[text()="生成凭证"]'

    @staticmethod
    def list_specified_voucher_template(invoice_num):
        return f'//span[text()="{invoice_num}"]//preceding-sibling::span//input[@id="query-type"]'

    @staticmethod
    def list_specified_voucher_template_new(invoice_num):
        return f'//span[text()="{invoice_num}"]/parent::td//preceding-sibling::td[@aria-describedby="grid_billTypeName"]'

    @staticmethod
    def list_specified_voucher_template_items(invoice_num, item):
        return f'//span[text()="{invoice_num}"]//preceding-sibling::span//div[text()="{item}"]'

    @staticmethod
    def list_specified_voucher_template_items_new(invoice_num, item):
        return f'//span[text()="{invoice_num}"]/parent::td//preceding-sibling::td//div[text()="{item}"]'

    @staticmethod
    def list_link_to_voucher_details(invoice_num):
        return f'//span[contains(text(),"{invoice_num}")]/parent::td//preceding-sibling::td//a[@tabtxt="凭证"]'

    @staticmethod
    def list_specified_company_name(num):
        return (f'//span[contains(text(),"{num}")]/parent::td'
                f'//following-sibling::td[@aria-describedby="grid_name"]/span')

    @staticmethod
    def popup_box_button():
        return '//span[@id="yunInvoiceKnow"]'

    @staticmethod
    def specified_voucher_template_input():
        return '//input[@id="add-skfptype-value"]'

    @staticmethod
    def specified_voucher_template_items(item):
        return f'//div[@id="add-skfptype-list"]//div[text()="{item}"]'

    @staticmethod
    def specified_voucher_template_buttons(button="保存"):
        return f'//div[@aria-hidden="false"]//button[text()="{button}"]'

    @staticmethod
    def conform_clear_template_buttons(button="确定"):
        return f'//div[contains(@style,"visible")]//input[@type="button" and @value="{button}"]'

    @staticmethod
    def conform_certified_message(value):
        return f'//span[text()="本次勾选："]//following-sibling::div//span[text()="{value}"]'

    @staticmethod
    def conform_certified_buttons(button='确定'):
        return f'//div[contains(@style,"visible")]//input[@value="{button}"]'

    @staticmethod
    def income_invoice_inputs_by_label(label):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def income_invoice_inputs_drop_down_items(label, item):
        return f'//label[contains(text(),"{label}")]//following-sibling::div//div[text()="{item}"]'


class CostInvoiceBase:
    @staticmethod
    def cost_invoice_frame():
        return 'bill-costInvoice'

    @staticmethod
    def cost_invoice_buttons(button):
        button_kv = {
            '刷新': 'refresh',
            '全选': 'select-all',
            '保存': 'save',
            '导入': 'importBtn',
            '导出': 'saveAsExcel',
            '删除': 'delete',
            '指定凭证模板': 'designationBillType',
            '按单生成凭证': 'save-wages-single',
            '汇总生成凭证': 'save-wages',
            '凭证汇总选项': 'vhrSumChoice'
        }
        return f'//*[@id="{button_kv.get(button)}"]'

    @staticmethod
    def cost_invoice_generate_voucher_settings_arrows_button():
        return '//div[@class="hd_arrows"]'

    @staticmethod
    def cost_invoice_filter_input_by_label(label):
        return (f'//div[@class="wages_hd clearfix wages_hd_costInvoice"]'
                f'//label[contains(text(),"{label}")]//following-sibling::*//input')

    @staticmethod
    def cost_invoice_table_input_by_line_num(line_num, input_cls):
        input_cls_kv = {
            '对方': 'textEllipsis name',
            '金额': 'amount',
            '税额': 'taxamount',
            '价税合计': 'total',
            '备注': 'remark',
        }
        return f'(//div[@id="con-list"]/div)[{line_num}]//input[@class="{input_cls_kv.get(input_cls)}"]'

    @staticmethod
    def cost_invoice_table_operate_buttons_by_line_num(line_num, button):
        button_kv = {
            '增行': 'add',
            '删行': 'del',
            '生成凭证': 'create_voucher'
        }
        return f'(//div[@id="con-list"]/div)[{line_num}]//span[contains(@class,"{button_kv.get(button)}")]'
