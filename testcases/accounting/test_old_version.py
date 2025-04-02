import allure
import pytest

from config.config import MENU_CASE_REPEAT_TIME
from page.accounting.page_common import AccountingCommonPage, ACCOUNTING_MENU
from page.accounting.page_home import AccountingHomePage
from page.manager.page_common import ManagerCommonPage
from page.page_login import LoginPage
from page.manager.page_home_old import OldHomePage


@pytest.mark.accounting
@pytest.mark.menu
@pytest.mark.accounting_menu_old
@allure.epic('会计')
@allure.feature('菜单遍历')
@allure.story('1.0版本')
class TestOldVersionMenu(LoginPage,
                         OldHomePage,
                         ManagerCommonPage,
                         AccountingHomePage,
                         AccountingCommonPage):
    company = '007大内密探'


    # @allure.title('全部')
    # def test_smart_bookkeeping_menu(self):
    #     with allure.step('登录'):
    #         self.login(env='old')
    #     with allure.step('进入账套'):
    #         self.close_alert()
    #         self.click_old_home_menu_button('客户管理')
    #         self.old_home_search_company(self.company)
    #         self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
    #     with allure.step('点击菜单'):
    #         all_old_menus=list(ACCOUNTING_MENU.keys())
    #         for level_one_menu in all_old_menus:
    #
    #             for level_two_menu in ACCOUNTING_MENU.get(level_one_menu):
    #                 if level_two_menu == '票据附件':
    #                     self.click_accounting_menu(level_one_menu, level_two_menu)
    #                     assert self.is_top_tab_visible(level_two_menu)
    #                 else:
    #                     assert not self.is_element_visible(self.menu(level_two_menu))

    @allure.title('智能记账')
    def test_smart_bookkeeping_menu(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('智能记账'):
                    if _ == '票据附件':
                        self.click_accounting_menu('智能记账', _)
                        assert self.is_top_tab_visible(_)
                    else:
                        assert not self.is_element_visible(self.menu(_))

    @allure.title('录凭证&查凭证&结账')
    def test_edit_voucher(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                self.click_accounting_menu('录凭证')
                assert self.is_top_tab_visible('录凭证')
                self.click_accounting_menu('查凭证')
                assert self.is_top_tab_visible('查凭证')
                assert not self.is_element_visible(self.menu('工资'))
                assert not self.is_element_visible(self.menu('库存'))
                self.click_accounting_menu('结账')
                assert self.is_top_tab_visible('结账')
    #
    # @allure.title('查凭证')
    # def test_query_voucher(self):
    #     with allure.step('登录'):
    #         self.login(env='old')
    #     with allure.step('进入账套'):
    #         self.close_alert()
    #         self.click_old_home_menu_button('客户管理')
    #         self.old_home_search_company(self.company)
    #         self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
    #     with allure.step('点击菜单'):
    #         self.click_accounting_menu('查凭证')
    #         assert self.is_top_tab_visible('查凭证')

    @allure.title('账簿')
    def test_books(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('账簿'):
                self.click_accounting_menu('账簿', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('报表')
    def test_reports(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('报表'):
                    if _ == '标准现金流量表':
                        assert not self.is_element_visible(self.menu(_))
                    else:
                        self.click_accounting_menu('报表', _)
                        assert self.is_top_tab_visible(_)
                        self.close_tab_by_tab_name(_)

    # @allure.title('工资')
    # def test_salary(self):
    #     with allure.step('登录'):
    #         self.login(env='old')
    #     with allure.step('进入账套'):
    #         self.close_alert()
    #         self.click_old_home_menu_button('客户管理')
    #         self.old_home_search_company(self.company)
    #         self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
    #     with allure.step('点击菜单'):
    #         assert not self.is_element_visible(self.menu('工资'))

    # @allure.title('存货')
    # def test_inventory(self):
    #     with allure.step('登录'):
    #         self.login(env='old')
    #     with allure.step('进入账套'):
    #         self.close_alert()
    #         self.click_old_home_menu_button('客户管理')
    #         self.old_home_search_company(self.company)
    #         self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
    #     with allure.step('点击菜单'):
    #         assert not self.is_element_visible(self.menu('库存'))
            # for _ in ACCOUNTING_MENU.get('库存'):
            #     self.click_accounting_menu('库存', _)
            #     assert self.is_top_tab_visible(_)
            #     self.close_tab_by_tab_name(_)

    @allure.title('固定资产')
    def test_fixed_asset(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('资产'):
                    self.click_accounting_menu('资产', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)

    # @allure.title('结账')
    # def test_query_closure(self):
    #     with allure.step('登录'):
    #         self.login(env='old')
    #     with allure.step('进入账套'):
    #         self.close_alert()
    #         self.click_old_home_menu_button('客户管理')
    #         self.old_home_search_company(self.company)
    #         self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
    #     with allure.step('点击菜单'):
    #         self.click_accounting_menu('结账')
    #         assert self.is_top_tab_visible('结账')

    @allure.title('设置')
    def test_settings(self):
        with allure.step('登录'):
            self.login(env='old')
        with allure.step('进入账套'):
            self.close_alert()
            self.click_old_home_menu_button('客户管理')
            self.old_home_search_company(self.company)
            self.click_old_home_buttons_in_line_by_company(self.company, '进账簿')
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('设置'):
                    if _ in ['现金流量初始金额', '明细科目转核算项目']:
                        assert not self.is_element_visible(self.menu(_))
                    else:
                        self.click_accounting_data_menu('设置', _)
                        assert self.is_top_tab_visible(_)
                        self.close_tab_by_tab_name(_)
