class OldHomeBase:
    @staticmethod
    def old_home_menu_button(menu):
        return f'//div[@id="Menu"]//a[text()="{menu}"]'

    @staticmethod
    def old_home_search_input(input_id):
        kv = {'输入框': 'searchText', '搜索': 'btnSearch'}
        return f'//label[contains(text(),"企业编号")]//following-sibling::span//input[@id="{kv.get(input_id)}"]'

    @staticmethod
    def old_home_buttons_in_line_by_company(company, button):
        return f'//a[text()="{company}"]//parent::td//following-sibling::td/span/*[contains(text(),"{button}")]'
