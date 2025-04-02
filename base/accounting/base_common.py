class AccountingCommonBase:
    @staticmethod
    def accounting_floating_errors():
        return '//body//div[@class="ui-tips ui-tips-error"]'

    @staticmethod
    def accounting_floating_tips():
        return '//body//div[@class="ui-tips ui-tips-success"]'

    @staticmethod
    def accounting_floating_warning():
        return '//body//div[@class="ui-tips ui-tips-warning"]'

    @staticmethod
    def accounting_all_floating_tips():
        return '//body//div[contains(@class,"ui-tips ui-tips")]'

    @staticmethod
    def top_tabs_close_button(tab):
        return f'//div[@id="page-tab"]//li//a[text()="{tab}"]//following-sibling::div[contains(@class,"close")]'

    @staticmethod
    def top_tabs_label(tab):
        return f'//div[@id="page-tab"]//li//a[text()="{tab}"]'

    @staticmethod
    def accounting_focus_table_buttons(button):
        return f'//table[contains(@class,"ui_state_lock")]//input[@value="{button}"]'

    @staticmethod
    def accounting_focus_table_close_button():
        return '//table[contains(@class,"ui_state_lock")]//a[contains(@title,"关闭")]'

    @staticmethod
    def accounting_focus_table_sys_tips():
        return f'//table[contains(@class,"ui_state_lock")]//div[@class="ui_content"]'

    @staticmethod
    def accounting_focus_table_radio_items_by_span(span):
        return f'//table[contains(@class,"ui_state_lock")]//span[text()="{span}"]//preceding-sibling::input'

    @staticmethod
    def accounting_focus_table_inner_frame(title):
        return f'//div[text()="{title}"]/ancestor::tr//td[@class="ui_main"]//iframe'

    @staticmethod
    def accounting_subject_drop_down_list_item(subject):
        return f'//div[@id="COMBO_WRAP"]//div[contains(text(),"{subject}")]'

    @staticmethod
    def accounting_focus_table_input_radio_by_label(label):
        return f'//label[text()="{label}"]/preceding-sibling::input[1]'

    @staticmethod
    def accounting_iframe_error_h1():
        return '//h1'

    @staticmethod
    def accounting_current_period():
        return '//*[@id="period"]'

    @staticmethod
    def accounting_my_company_span():
        return '//span[@id="myCompany"]'
