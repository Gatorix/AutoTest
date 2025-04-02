import allure
import pytest

from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_home import ManagerHomePage

from config.config import MENU_CASE_REPEAT_TIME


@pytest.mark.ui
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

    @allure.severity('trivial')
    @allure.title('商机管理')
    def test_manager_menu_0(self):
        level_one_menu = list(self.ALL_MENUS.keys())[0]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[0])
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
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
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)


    @allure.title('代账服务&工商服务')
    def test_manager_menu_2(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
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
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[3]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[3])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)

    @allure.title('财务管理')
    def test_manager_menu_4(self):
        level_one_menu = list(self.ALL_MENUS.keys())[4]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[4])
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)

    @allure.title('报表中心')
    def test_manager_menu_5(self):
        level_one_menu = list(self.ALL_MENUS.keys())[5]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[5])
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)

    @allure.title('智能财税')
    def test_manager_menu_6(self):
        level_one_menu = list(self.ALL_MENUS.keys())[6]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[6])
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)

    @allure.title('微信运营')
    def test_manager_menu_7(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
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
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[8]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[8])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)
                level_one_menu = list(self.ALL_MENUS.keys())[10]
                level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[10])
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)

    @allure.title('系统设置')
    def test_manager_menu_9(self):
        level_one_menu = list(self.ALL_MENUS.keys())[9]
        level_two_menu = self.ALL_MENUS.get(list(self.ALL_MENUS.keys())[9])
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in level_two_menu:
                    with allure.step('点击菜单'):
                        self.click_manager_menu(level_one_menu, _)
                    with allure.step('移走鼠标'):
                        self.click_logo()
                    with allure.step('检查页签'):
                        assert self.is_top_label_appear(_)
                        self.click_tag_close_button(_)
                        assert not self.is_top_label_appear(_)
