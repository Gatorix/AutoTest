class BalanceSheetBase:
    @staticmethod
    def balance_sheet_frame():
        return 'report-balanceSheets'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def copy_button_span():
        return '//a[@id="btn-copy"]//span'

    @staticmethod
    def balance_tips_button():
        return '//input[@value="确定"]'

    @staticmethod
    def buttons_b(button):
        return f'//button[@id="{button}"]'

    @staticmethod
    def period_selector():
        # return '//span[@id="period"]//span[@class="trigger"]'
        return '//span[@id="period" and contains(@class,"single-period")]'

    @staticmethod
    def period_items(item):
        # return f'//div[not(contains(@style,"none"))]/div/div[@data-value="{item}"]'
        return f'//div[contains(@class,"zwyPeriod-box")]//div[@class="zwy-period-body"]//div[@data-value="{item}"]'

    @staticmethod
    def period_start_input():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def period_end_input():
        return '//input[@id="endPicker"]'


class IncomeStatementBase:
    @staticmethod
    def income_statement_frame():
        return 'report-profitSheets'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def conform_export_button():
        return '//input[@value="确定"]'

    @staticmethod
    def buttons_b(button):
        return f'//button[@id="{button}"]'

    @staticmethod
    def period_selector():
        # return '//span[@id="period"]//span[@class="trigger"]'
        return '//span[@id="period" and contains(@class,"single-period")]'

    @staticmethod
    def period_items(item):
        # return f'//div[not(contains(@style,"none"))]/div/div[@data-value="{item}"]'
        return f'//div[contains(@class,"zwyPeriod-box")]//div[@class="zwy-period-body"]//div[@data-value="{item}"]'
    @staticmethod
    def period_start_input():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def period_end_input():
        return '//input[@id="endPicker"]'

    @staticmethod
    def report_type(radio):
        return f'//input[@id="{radio}"]'

    @staticmethod
    def copy_button_span():
        return '//a[@id="btn-copy"]//span'

class CashFlowStatementBase:
    @staticmethod
    def cash_flow_statement_frame():
        return 'report-cashFlowSheets'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def conform_export_button():
        return '//input[@value="确定"]'

    @staticmethod
    def close_balance_tips():
        return '//input[@value="关闭"]'

    @staticmethod
    def buttons_b(button):
        return f'//button[@id="{button}"]'

    @staticmethod
    def period_selector():
        return '//span[@id="period"]//span[@class="trigger"]'

    @staticmethod
    def period_items(item):
        return f'//div[not(contains(@style,"none"))]/div/div[@data-value="{item}"]'

    @staticmethod
    def period_start_input():
        return '//input[@id="prevPicker"]'

    @staticmethod
    def period_end_input():
        return '//input[@id="endPicker"]'

    @staticmethod
    def report_type(radio):
        return f'//input[@id="{radio}"]'


class StandardCashFlowStatementBase:
    @staticmethod
    def standard_cash_flow_statement_frame():
        return 'report-standardCashFlowSheets'

    @staticmethod
    def standard_cash_flow_statement_buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def standard_cash_flow_statement_report_voucher_dialog_elements(ele_id):
        return f'//div[@id="reportVoucherDialog"]//*[@id="{ele_id}"]'
