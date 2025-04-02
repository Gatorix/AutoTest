from base.manager.base_common import ManagerCommonBase

from base.base_case import BaseTestCase


class ManagerCommonPage(ManagerCommonBase, BaseTestCase):
    def get_tip_text(self):
        text = self.get_text(self.floating_tips())
        self.wait(3)
        return text

    def get_page_text(self):
        """
        跳转进入创建账套页面，在创建账套页面获取定位信息
        @return:
        """
        return self.get_text(self.txt_tips())

    def get_accounting_page_text(self):
        """
        跳转进入会计页面，在会计页面获取定位信息
        @return:
        """
        return self.get_text(self.accounting_txt_tips())

    def is_my_order_visible(self):
        return self.is_element_visible(self.my_order())

    def switch_to_accounting_window(self):
        self.driver.close()
        self.switch_to_newest_window()
        self.wait(2)

    def get_text_from_manager_bottom_line_total_line(self):
        return self.get_text(self.manager_bottom_line_list_total_line())

    def manager_bottom_line_switch_show_num(self, text):
        self.click(self.manager_bottom_line_show_num_input())
        self.click(self.manager_bottom_line_show_num_popper(text))
        self.wait(3)
