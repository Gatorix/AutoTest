from base.manager.base_home import ManagerHomeBase

from base.base_case import BaseTestCase


class ManagerHomePage(BaseTestCase, ManagerHomeBase):
    def is_logo_appear(self):
        """
        检查主页左上角logo是否显示
        @return: bool
        """
        if self.is_element_visible(self.logo()):
            return True

    def is_avatar_visible(self):
        if self.is_element_visible(self.user_avatar()):
            return True

    def click_logo(self):
        self.click(self.logo())

    def close_popup(self):
        """
        关闭弹窗
        @return:
        """
        popups = [self.announcement(),
                  self.role_notice(),
                  self.class_notice(),
                  self.password_notice(),
                  self.float_notice(),
                  self.tex_period_end_notice(),
                  self.ask_robot(),
                  self.consultation(),
                  self.notice_area(),
                  self.big_announcement(),
                  self.skip_new_menu()]
        for _ in popups:
            self.wait(0.2)
            self.__close_popup(_)
        if self.is_element_visible(self.assistant_div()):
            self.block_zwy_assistant()

    def __close_popup(self, xpath):
        try:
            if self.is_element_visible(xpath):
                self.click(xpath)
        except Exception:
            pass

    def switch_menu(self, menu='旧版'):
        # 检查当前是否新版菜单
        if self.is_element_visible(self.switch_menu_span()):
            if menu in self.get_text(self.switch_menu_span()):
                self.click(self.switch_menu_span())
                self.close_popup()

    def click_manager_menu(self, level_one_menu_name, level_two_menu_name):
        """
        点击左侧菜单
        @param level_one_menu_name: 一级菜单名称
        @param level_two_menu_name: 二级菜单名称
        @return:
        """
        self.switch_menu()
        self.click(self.level_one_menu(level_one_menu_name))
        self.click(self.level_two_menu(level_one_menu_name, level_two_menu_name))
        self.wait(0.2)
        if level_two_menu_name in ['服务管理']:
            self.click_mask_div()

    def click_mask_div(self):
        if self.is_element_visible(self.confirm_no_ticket_mask()):
            self.click(self.confirm_no_ticket_mask())

    def switch_group(self, group_name):
        self.click(self.group_switch())
        self.click(self.group_select(group_name))

    def is_top_label_appear(self, label):
        self.wait(1)
        return self.is_element_visible(self.top_label(label))

    def log_out(self):
        self.click(self.user_avatar())
        self.click(self.avatar_button('退出账号'))

    def zoom(self, zoom: float):
        self.execute_script(f'document.body.style.zoom="{zoom}"')

    def click_tag_close_button(self, tag):
        # self.click(self.top_tag(tag))
        self.click(self.tag_close_button(tag))

    def click_tag_refresh_button(self, tag):
        self.click(self.tag_refresh_button(tag))

    def block_zwy_assistant(self):
        # self.drag_and_drop_with_offset(self.assistant_img(), 0, 50)
        self.set_attribute(self.assistant_div(), 'style', 'display: none;')
