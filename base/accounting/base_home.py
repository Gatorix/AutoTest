class AccountingHomeBase:
    @staticmethod
    def home_frame():
        return 'index'

    @staticmethod
    def home_report_link(report_name):
        return f'//ul[@id="quick-links"]//a[@tabtxt="{report_name}"]'

    @staticmethod
    def home_report_cal_result(report_name):
        return f'//ul[@id="quick-links"]//a[@tabtxt="{report_name}"]//span[@class="box-right"]/span[1]'

    @staticmethod
    def home_blue_buttons(button):
        return f'//a[text()="{button}"]'

    @staticmethod
    def __measure_title_id(measure_title):
        measure_kv = {
            '年收入测算': 'annual-income-calc',
            '月收入测算': 'monthly-income-calc',
            '所得税测算': 'income-tax-calc'
        }
        return measure_kv.get(measure_title)

    def home_measure_div_month_adj_buttons(self, measure_title, adj_button):
        # adj_button: +1 -1
        return f'//div[@id="{self.__measure_title_id(measure_title)}"]//span[@operate="{adj_button}"]'

    def home_measure_div_month_span(self, measure_title):
        return f'//div[@id="{self.__measure_title_id(measure_title)}"]//span[contains(@class,"current-month")]'

    def home_measure_div_loading_span(self, measure_title):
        return f'//div[@id="{self.__measure_title_id(measure_title)}"]' \
               f'//span[contains(@class,"current-month")]//following-sibling::span[2]'

    @staticmethod
    def home_measure_div_buttons(button):
        button_kv = {
            '年收入测算-设置': 'set-income-ceiling',
            '所得税测算-提示': 'showSdscs',
            '所得税测算-设置': 'set-income-tax-rate',
            '本期财务指标-管理': 'manage',
            '本期财务指标-刷新': 'report-refresh'
        }
        return f'//*[@id="{button_kv.get(button)}"]'

    @staticmethod
    def home_financial_indices_list_item(span):
        return f'//div[@class="box financial-indices"]//ul[@id="ajaxList"]//span[@title="{span}"]//preceding-sibling::b'

    @staticmethod
    def home_financial_indices_add_new_item():
        return '//a[text()="(+ 新增报表项...)"]'

    @staticmethod
    def home_financial_indices_input_by_label(label):
        return f'//label[contains(text(),"{label}")]/parent::span//input'

    @staticmethod
    def home_financial_indices_add_button():
        return '//a[@id="add-formula"]'

    @staticmethod
    def home_financial_indices_table_buttons(name, button):
        return f'//td[text()="{name}"]//following-sibling::td//a[text()="{button}"]'

    @staticmethod
    def home_title(company_name):
        return f'//div[@class="tit"]//span[contains(@title,"{company_name}")]//text()'

    @staticmethod
    def menu(menu_name):
        return f'//div[@id="col-side"]//a[text()="{menu_name}"]'

    @staticmethod
    def company_title():
        return f'//span[@id="myCompany"]'

    @staticmethod
    def data_menu(menu_name):
        return f'//div[@id="col-side"]//a[@data-menuname="{menu_name}"]'

    @staticmethod
    def top_tabs(tab_name):
        return f'//a[text()="{tab_name}"]//following-sibling::div[contains(@class,"close")]'

    @staticmethod
    def acct_switch_button():
        return '//*[@id="triggerZT"]'

    @staticmethod
    def search_input():
        return '//input[@id="acctList-input"]'

    @staticmethod
    def search_button():
        return '//*[@id="acct-search-btn"]'

    @staticmethod
    def company_line(company):
        return f'//div[@id="default-acct-list"]//a[contains(text(),"{company}")]'

    @staticmethod
    def my_company_span():
        return '//span[@id="myCompany"]'
