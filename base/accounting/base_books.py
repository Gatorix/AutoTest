class SubsidiaryLedgerBase:
    @staticmethod
    def subsidiary_ledger_frame():
        return 'book-subsidiaryLedger'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def subject_box_level_one(subject):
        return f'//a[@title="{subject}"]//span[text()="{subject}"]'

    @staticmethod
    def subject_box_level_one_expand_button(subject):
        return f'(//a[@title="{subject}"]//preceding-sibling::span)[1]'

    @staticmethod
    def subject_box_level_two(subject_one, subject_two):
        return f'//a[@title="{subject_one}"]//parent::li//span[contains(text(),"{subject_two}")]'

    @staticmethod
    def filter_checkbox(item):
        return f'//ul[@id="more-conditions"]//label[text()="{item}"]//preceding-sibling::input'

    @staticmethod
    def filter_inputs(label, from_or_to=None):
        if label == '会计期间':
            return f'//div[@class="con"]//label[contains(text(),"{label}")]' \
                   f'//following-sibling::span[contains(@id,"{from_or_to}")]//input'
        else:
            return f'//div[@class="con"]//label[contains(text(),"{label}")]//following-sibling::span//input'

    @staticmethod
    def year_selector():
        return f'//div[@class="zwy-period-year js-zwy-period-year"]'

    @staticmethod
    def year_items(year):
        return f'//div[contains(@class,"zwy-period-year-li") and @data-value="{year}"]'

    @staticmethod
    def period_item_selector(value):
        # return f'//div[@id="COMBO_WRAP"]/div[contains(@style,"display: block;")]//div[@data-value="{value}"]'
        return f'//div[contains(@class,"zwyPeriod-box")]//div[@data-value="{value}"]'

    @staticmethod
    def period_trigger(from_or_to):
        return f'//div[@class="con"]//label[contains(text(),"会计期间")]//following-sibling::span[contains(@id,"{from_or_to}")]'

    @staticmethod
    def filter_span():
        return '//span[@id="selected-period2"]'


class GeneralLedgerBase:
    @staticmethod
    def general_ledger_frame():
        return 'book-generalLedger'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'


class VoucherSummaryBase:
    @staticmethod
    def voucher_summary_frame():
        return 'book-voucherSummary'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'


class BalanceBase:
    @staticmethod
    def balance_frame():
        return 'book-subjectBalance'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def filter_span():
        return '//span[@id="selected-period"]'

    @staticmethod
    def filter_more():
        return '//span[@id="selected-period2"]'

    @staticmethod
    def subject_level():
        return f'//ul[@id="more-conditions"]//input[@id="filter-toLevel"]'

    @staticmethod
    def filter_checkbox(item):
        return f'//ul[@id="more-conditions"]//label[text()="{item}"]//preceding-sibling::input'

    @staticmethod
    def filter_inputs_accounting_period(from_or_to):
        ele_id_kv = {
            '开始': 'filter-fromPeriod',
            '结束': 'filter-fromPeriod',
        }
        return f'//*[@id="{ele_id_kv.get(from_or_to)}"]//input'

    @staticmethod
    def filter_inputs_by_id(ele_id):
        id_kv = {
            '起始科目': 'filter-fromSubject',
            '结束科目': 'filter-toSubject',
            '科目级次': 'filter-fromLevel',
            '至': 'filter-toLevel',
        }
        return f'//*[@id="{id_kv.get(ele_id)}"]'

    @staticmethod
    def balance_loading():
        return '//*[@id="load_grid"]'

    @staticmethod
    def balance_total_line():
        return '//*[@id="page_right"]/div'

    @staticmethod
    def balance_page_buttons(button):
        page_button_id = {
            '首页': 'first_page',
            '上一页': 'prev_page',
            '下一页': 'next_page',
            '尾页': 'last_page'
        }
        return f'//*[@id="{page_button_id.get(button)}"]'

    @staticmethod
    def balance_page_total_pages():
        return '//*[@id="page_center"]//td[@dir="ltr"]/span'

    @staticmethod
    def balance_page_current_page():
        return '//*[@id="page_center"]//td[@dir="ltr"]/input'


class QuantityAmountLedgerBase:
    @staticmethod
    def quantity_amount_ledger_frame():
        return 'book-qtyAmountDetail'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def subject_box_level_one(subject):
        return f'//a[@title="{subject}"]//span[text()="{subject}"]'

    @staticmethod
    def subject_box_level_one_expand_button(subject):
        return f'(//a[@title="{subject}"]//preceding-sibling::span)[1]'

    @staticmethod
    def subject_box_level_two(subject_one, subject_two):
        return f'//a[@title="{subject_one}"]//parent::li//span[contains(text(),"{subject_two}")]'

    @staticmethod
    def filter_span():
        return f'//div[@id="filter-menu"]'

    @staticmethod
    def filter_inputs_by_label(label):
        return f'//label[text()="{label}"]//preceding-sibling::input'


class QuantityAmountGeneralLedgerBase:
    @staticmethod
    def quantity_amount_general_ledger_frame():
        return 'book-qtyAmountGeneral'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'


class MultiColumnLedger:
    @staticmethod
    def multi_column_ledger_frame():
        return 'book-multicolacct'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def filter_span():
        return '//span[@id="selected-period2"]'

    @staticmethod
    def subject_input():
        return '//input[@id="filter-subject"]'

    @staticmethod
    def subject_selector(subject):
        return f'//div[contains(@style,"display: block;")]//div[contains(text(),"{subject}")]'


class AccountingBalanceBase:
    @staticmethod
    def accounting_balance_frame():
        return 'book-accountingBalance'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def accounting_filter_trigger():
        return '//span[@id="filter-auxiliaryType"]//input//following-sibling::span[@class="trigger"]'

    @staticmethod
    def accounting_items(item):
        return f'//div[contains(@style,"display: block;")]//div[text()="{item}"]'


class AccountingDetailBase:
    @staticmethod
    def accounting_detail_frame():
        return 'book-accountingLedger'

    @staticmethod
    def buttons(button):
        return f'//a[@id="{button}"]'

    @staticmethod
    def accounting_filter_trigger():
        return '//span[@id="filter-auxiliaryType"]//input//following-sibling::span[@class="trigger"]'

    @staticmethod
    def accounting_items(item):
        return f'//div[contains(@style,"display: block;")]//div[text()="{item}"]'

    @staticmethod
    def subject_box(subject):
        return f'//ul[@id="subsidiary-subject-tree"]//span[text()="{subject}"]'
