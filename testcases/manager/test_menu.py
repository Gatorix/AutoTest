import allure
import pytest

from page.manager.page_common import ManagerCommonPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage

from config.config import MENU_CASE_REPEAT_TIME

@pytest.mark.manager
@pytest.mark.menu
@pytest.mark.manager_menu
@allure.epic('管家')
@allure.feature('菜单遍历')
@allure.story('5.0')
class TestMenu(ManagerCommonPage,
               LoginPage,
               ManagerHomePage):
    ALL_MENUS = {
        '商机管理': ['商机池', '我的商机', '商机成交', '商机报表', '商机回收站', '商机设置'],
        '客户管理': ['合同', '服务到期明细', '客户', '流失管理', '客户物品管理', '合同发票'],
        '代账服务': ['服务管理', '批量打印', '极简户智能工作台'],
        '工商服务': ['服务管理', '工商年报'],
        '财务管理': ['收款跟进', '收款审核', '线上收款', '银行对账'],
        '报表中心': ['工作量分析', '进度汇总表', '人员进度表', '收款分析', '续费分析', '回款预测', '进度看板'],
        '智能财税': ['智能记账', '智能采集', '智能税务', '票据管理', '开票设置', '发票开具', '开票统计'],
        '微信运营': ['公众号管理', '微信消息记录', '企业微信'],
        '外勤管理': ['外勤任务'],
        '系统设置': ['部门职员', '岗位', '权限', '参数设置', '服务设置', '操作日志', '回收站'],
        '增值服务': ['服务商城', '余额扣费记录']
    }

    @allure.title('商机管理')
    def test_manager_menu_0(self):
        level_one_menu = list(self.ALL_MENUS.keys())[0]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert any([self.is_top_label_appear(_),
                                    self.is_top_label_appear(level_one_menu)])

    @allure.title('客户管理')
    def test_manager_menu_1(self):
        level_one_menu = list(self.ALL_MENUS.keys())[1]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    @allure.title('代账服务&工商服务')
    def test_manager_menu_2(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                level_one_menu = list(self.ALL_MENUS.keys())[2]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[3]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[3])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    # @allure.title('工商服务')
    # def test_manager_menu_3(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[3]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[3])
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #         for _ in level_two_menu:
    #             with allure.step('点击菜单'):
    #                 self.click_manager_menu(level_one_menu, _)
    #             with allure.step('移走鼠标'):
    #                 self.click_logo()
    #             with allure.step('检查页签'):
    #                 assert self.is_top_label_appear(_)

    @allure.title('财务管理')
    def test_manager_menu_4(self):
        level_one_menu = list(self.ALL_MENUS.keys())[4]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    @allure.title('报表中心')
    def test_manager_menu_5(self):
        level_one_menu = list(self.ALL_MENUS.keys())[5]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    @allure.title('智能财税')
    def test_manager_menu_6(self):
        level_one_menu = list(self.ALL_MENUS.keys())[6]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    @allure.title('微信运营')
    def test_manager_menu_7(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                level_one_menu = list(self.ALL_MENUS.keys())[7]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[7])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[8]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[8])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[10]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)


    # @allure.title('外勤管理')
    # def test_manager_menu_8(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[8]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[8])
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #         for _ in level_two_menu:
    #             with allure.step('点击菜单'):
    #                 self.click_manager_menu(level_one_menu, _)
    #             with allure.step('移走鼠标'):
    #                 self.click_logo()
    #             with allure.step('检查页签'):
    #                 assert self.is_top_label_appear(_)

    @allure.title('系统设置')
    def test_manager_menu_9(self):
        level_one_menu = list(self.ALL_MENUS.keys())[9]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])
        with allure.step('登录'):
            self.login()
            self.close_popup()
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)

    # @allure.title('增值服务')
    # def test_manager_menu_10(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[10]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #         for _ in level_two_menu:
    #             with allure.step('点击菜单'):
    #                 self.click_manager_menu(level_one_menu, _)
    #             with allure.step('移走鼠标'):
    #                 self.click_logo()
    #             with allure.step('检查页签'):
    #                 assert self.is_top_label_appear(_)

    # @pytest.mark.menu
    # @allure.title('管家菜单遍历')
    # def test_manager_menu(self):
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         for level_one_menu in list(self.ALL_MENUS.keys()):
    #             for level_two_menu in self.ALL_MENUS.get(level_one_menu):
    #                 self.click_manager_menu(level_one_menu, level_two_menu)
    #                 if level_one_menu == '商机管理':
    #                     self.click_logo()
    #                     assert any([self.is_top_label_appear(level_two_menu),
    #                                 self.is_top_label_appear(level_one_menu)])
    #                 else:
    #                     assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[10])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[10])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[10]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[10])[1]}')
    # def test_menu_102(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[10]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[10])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[10])[1])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[10]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[10])[1]}')
    # # def test_menu_101(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[10]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])[1]
    # #     with allure.step('登录'):
    # #         self.login()
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         ori_window = self.driver.current_window_handle
    # #         self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         for _ in self.driver.window_handles:
    # #             if _ is not ori_window:
    # #                 self.switch_to_window(_)
    # #         assert self.is_my_order_visible()
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[10])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[10])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[10]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[10])[0]}')
    # def test_menu_100(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[10]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[9])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[6])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[6]}')
    # # def test_menu_96(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[6]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[5])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[5]}')
    # def test_menu_95(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[5]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[4])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[4]}')
    # def test_menu_94(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[4]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[3]}')
    # def test_menu_93(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[2]}')
    # def test_menu_92(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[1]}')
    # def test_menu_91(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[9])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[9])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[9]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[9])[0]}')
    # def test_menu_90(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[9]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[8])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[8])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[8]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[8])[0]}')
    # def test_menu_80(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[8]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[8])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[7])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[7])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[7]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[7])[2]}')
    # def test_menu_72(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[7]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[7])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[7])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[7])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[7]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[7])[1]}')
    # def test_menu_71(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[7]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[7])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[7])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[7])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[7]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[7])[0]}')
    # def test_menu_70(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[7]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[7])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[6])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[6]}')
    # def test_menu_66(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[6]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[5])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[5]}')
    # def test_menu_65(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[5]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[4])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[4]}')
    # def test_menu_64(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[4]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[3]}')
    # def test_menu_63(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[2]}')
    # def test_menu_62(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[1]}')
    # def test_menu_61(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[6])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[6])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[6]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[6])[0]}')
    # def test_menu_60(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[6]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[6])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[6]}')
    # def test_menu_56(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[6]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[5])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[5]}')
    # def test_menu_55(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[5]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[4])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[4]}')
    # def test_menu_54(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[4]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[3]}')
    # def test_menu_53(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[2]}')
    # def test_menu_52(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[1]}')
    # def test_menu_51(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[5])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[5])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[5]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[5])[0]}')
    # def test_menu_50(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[5]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[4])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[4])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[4]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[4])[3]}')
    # def test_menu_43(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[4]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[4])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[4])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[4]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[4])[2]}')
    # def test_menu_42(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[4]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[4])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[4])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[4]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[4])[1]}')
    # def test_menu_41(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[4]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[4])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[4])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[4]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[4])[0]}')
    # def test_menu_40(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[4]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[3])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[3])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[3]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[3])[1]}')
    # def test_menu_31(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[3]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[3])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[3])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[3])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[3]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[3])[0]}')
    # def test_menu_30(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[3]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[3])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[2])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[2])[4])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[2]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[2])[4]}')
    # # def test_menu_24(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[2]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])[4]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    # #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[2])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[2])[3])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[2]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[2])[3]}')
    # # def test_menu_23(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[2]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])[3]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    # #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[2])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[2])[2])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[2]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[2])[2]}')
    # # def test_menu_22(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[2]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])[2]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[2])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[2])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[2]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[2])[1]}')
    # def test_menu_21(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[2]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[2])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[2])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[2]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[2])[0]}')
    # def test_menu_20(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[2]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[2])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[1])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[6])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[6]}')
    # # def test_menu_16(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[6]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[1])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[5])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[5]}')
    # def test_menu_15(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[5]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[1])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[4])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[4]}')
    # def test_menu_14(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[4]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[1])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[3]}')
    # def test_menu_13(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[1])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[2]}')
    # def test_menu_12(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # # @allure.epic('管家')
    # # @allure.feature(list(ALL_MENUS.keys())[1])
    # # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[1])
    # # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[1]}')
    # # def test_menu_11(self):
    # #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    # #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[1]
    # #     with allure.step('登录'):
    # #         self.login()
    # #     with allure.step('关闭弹窗'):
    # #         self.close_popup()
    # #     with allure.step('点击菜单'):
    # #         if self.is_logo_appear():
    # #             self.click_manager_menu(level_one_menu, level_two_menu)
    # #     with allure.step('检查页签'):
    # #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[1])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[1])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[1]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[1])[0]}')
    # def test_menu_10(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[1]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[1])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('检查页签'):
    #         assert self.is_top_label_appear(level_two_menu)
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[5])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[5]}')
    # def test_menu_05(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[5]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[4])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[4]}')
    # def test_menu_04(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[4]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[3])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[3]}')
    # def test_menu_03(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[3]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[2])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[2]}')
    # def test_menu_02(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[2]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[1])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[1]}')
    # def test_menu_01(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[1]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
    #
    # @allure.epic('管家')
    # @allure.feature(list(ALL_MENUS.keys())[0])
    # @allure.story(ALL_MENUS.get(list(ALL_MENUS.keys())[0])[0])
    # @allure.title(f'菜单遍历-{list(ALL_MENUS.keys())[0]}-{ALL_MENUS.get(list(ALL_MENUS.keys())[0])[0]}')
    # def test_menu_00(self):
    #     level_one_menu = list(self.ALL_MENUS.keys())[0]
    #     level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])[0]
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu(level_one_menu, level_two_menu)
    #     with allure.step('移走鼠标'):
    #         self.click_logo()
    #     with allure.step('检查页签'):
    #         assert any([self.is_top_label_appear(level_two_menu),
    #                     self.is_top_label_appear(level_one_menu)])
