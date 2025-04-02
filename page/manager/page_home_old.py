from base.manager.base_home_old import OldHomeBase
from base.base_case import BaseTestCase


class OldHomePage(OldHomeBase, BaseTestCase):
    def close_alert(self):
        try:
            self.switch_to_alert()
            self.dismiss_alert()
        except Exception:
            pass

    def click_old_home_menu_button(self, button):
        self.click(self.old_home_menu_button(button))

    def old_home_search_company(self, company):
        self.type(self.old_home_search_input('输入框'), company)
        self.click(self.old_home_search_input('搜索'))

    def click_old_home_buttons_in_line_by_company(self, company, button):
        self.click(self.old_home_buttons_in_line_by_company(company, button))
        if button=='进账簿':
            self.wait(3)
