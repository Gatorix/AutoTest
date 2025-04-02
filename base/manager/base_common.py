class ManagerCommonBase:
    @staticmethod
    def floating_tips():
        return '//div[@role="alert"]//p'

    @staticmethod
    def txt_tips():
        """创建账套页面的提示语信息"""
        return '//div[@id="establish-wrap"]//h1//span[text()="创建账套，开始您的在线会计之旅吧！"]'

    @staticmethod
    def accounting_txt_tips():
        """会计页面的提示语信息"""
        # return '//div[@id="hd"]//p[@class="fl welcome" and contains(text(), "您现在可以录入初始数据")]'
        return '//div[@id="hd"]//a[text()="数据测算"]'

    @staticmethod
    def my_order():
        return '//span[@class="title" and text()="我的订单"]'

    @staticmethod
    def manager_bottom_line_list_total_line():
        return '//div[@class="pagination-wrap"]//span[contains(@class,"total")]'

    @staticmethod
    def manager_bottom_line_show_num_input():
        return '//div[@class="pagination-wrap"]//input[@type="text"]'

    @staticmethod
    def manager_bottom_line_show_num_popper(text):
        return f'//div[contains(@class,"el-select-dropdown el-popper") and not(contains(@style,"display: none;"))]' \
               f'//span[contains(text(),"{text}")]'
