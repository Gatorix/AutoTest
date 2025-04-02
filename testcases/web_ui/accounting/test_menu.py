import allure
import pytest

from config.config import MENU_CASE_REPEAT_TIME
from page.web_ui.accounting.page_common import AccountingCommonPage, ACCOUNTING_MENU
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.page_login import LoginPage
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.menu
@pytest.mark.accounting_menu
@allure.epic('会计')
@allure.feature('菜单遍历')
@allure.story('企业会计准则')
class TestStandardMenu(LoginPage,
                       AccountingHomePage,
                       AccountingCommonPage):
    company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')

    @allure.title('智能记账')
    def test_smart_bookkeeping_menu(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('智能记账'):
                    self.click_accounting_menu('智能记账', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('录凭证&查凭证&工资&结账')
    def test_edit_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            menu_list = ['录凭证', '查凭证', '工资', '结账']
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in menu_list:
                    self.click_accounting_menu(_)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('账簿')
    def test_books(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('账簿'):
                    self.click_accounting_menu('账簿', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('报表')
    def test_reports(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('报表'):
                    self.click_accounting_menu('报表', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('库存')
    def test_inventory(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('库存'):
                    self.click_accounting_menu('库存', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('固定资产')
    def test_fixed_asset(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('资产'):
                    self.click_accounting_menu('资产', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('设置_1')
    def test_settings_1(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('设置')[:5]:
                    if _ == '现金流量初始金额':
                        pass
                    else:
                        self.click_accounting_data_menu('设置', _)
                        assert self.is_top_tab_visible(_)
                        self.close_tab_by_tab_name(_)
                        assert not self.is_top_tab_visible(_)

    @allure.title('设置_2')
    def test_settings_2(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('设置')[6:10]:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)

    @allure.title('高级设置')
    def test_settings_advance(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for x in range(MENU_CASE_REPEAT_TIME):
                for _ in ACCOUNTING_MENU.get('设置')[11:]:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
                    assert not self.is_top_tab_visible(_)


@pytest.mark.ui
@pytest.mark.accounting
@allure.epic('会计')
@allure.feature('菜单遍历')
@allure.story('非盈利组织')
class TestNonProfitMenu(LoginPage,
                        AccountingHomePage,
                        AccountingCommonPage):
    company = GetYamlData().get_company('company_accounting_standards_non_profit_001')

    @allure.title('智能记账')
    def test_smart_bookkeeping_menu(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('智能记账'):
                self.click_accounting_menu('智能记账', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('录凭证')
    def test_edit_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('录凭证')
            assert self.is_top_tab_visible('录凭证')

    @allure.title('查凭证')
    def test_query_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('查凭证')
            assert self.is_top_tab_visible('查凭证')

    @allure.title('账簿')
    def test_books(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('账簿'):
                self.click_accounting_menu('账簿', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('报表')
    def test_reports(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('非盈利报表'):
                self.click_accounting_menu('报表', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('工资')
    def test_salary(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('工资')
            assert self.is_top_tab_visible('工资')

    @allure.title('库存')
    def test_inventory(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            assert not self.is_element_visible(self.menu('库存'))

    @allure.title('固定资产')
    def test_fixed_asset(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('资产'):
                self.click_accounting_menu('资产', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('结账')
    def test_query_closure(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('结账')
            assert self.is_top_tab_visible('结账')

    @allure.title('设置_1')
    def test_settings_1(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[:5]:
                if _ == '现金流量初始金额':
                    pass
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)

    @allure.title('设置_2')
    def test_settings_2(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[6:10]:
                self.click_accounting_data_menu('设置', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('高级设置')
    def test_settings_advance(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[11:]:
                if _ == '明细科目转核算项目':
                    pass
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)


@pytest.mark.ui
@pytest.mark.accounting
@allure.epic('会计')
@allure.feature('菜单遍历')
@allure.story('政府会计')
class TestGovernmentMenu(LoginPage,
                         AccountingHomePage,
                         AccountingCommonPage):
    company = GetYamlData().get_company('company_accounting_standards_government_001')

    @allure.title('智能记账')
    def test_smart_bookkeeping_menu(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('智能记账'):
                self.click_accounting_menu('智能记账', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('录凭证')
    def test_edit_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('政府录凭证'):
                self.click_accounting_menu('录凭证', _)
                assert self.is_top_tab_visible('录凭证')
                self.close_tab_by_tab_name('录凭证')

    @allure.title('查凭证')
    def test_query_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('查凭证')
            assert self.is_top_tab_visible('查凭证')

    @allure.title('账簿')
    def test_books(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('账簿'):
                self.click_accounting_menu('账簿', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('报表')
    def test_reports(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('政府报表'):
                self.click_accounting_menu('报表', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('工资')
    def test_salary(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('工资')
            assert self.is_top_tab_visible('工资')

    @allure.title('库存')
    def test_inventory(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            assert not self.is_element_visible(self.menu('库存'))

    @allure.title('固定资产')
    def test_fixed_asset(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('资产'):
                self.click_accounting_menu('资产', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('结账')
    def test_query_closure(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('结账')
            assert self.is_top_tab_visible('结账')

    @allure.title('设置_1')
    def test_settings_1(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[:5]:
                if _ == '现金流量初始金额':
                    pass
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)

    @allure.title('设置_2')
    def test_settings_2(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[6:10]:
                self.click_accounting_data_menu('设置', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('高级设置')
    def test_settings_advance(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[11:]:
                if _ in ['明细科目转核算项目', '增值服务']:
                    assert not self.is_element_visible(_)
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)


@pytest.mark.ui
@pytest.mark.accounting
@allure.epic('会计')
@allure.feature('菜单遍历')
@allure.story('村集体会计')
class TestVillageMenu(LoginPage,
                      AccountingHomePage,
                      AccountingCommonPage):
    company = GetYamlData().get_company('company_accounting_standards_village_001')

    @allure.title('智能记账')
    def test_smart_bookkeeping_menu(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('智能记账'):
                self.click_accounting_menu('智能记账', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('录凭证')
    def test_edit_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('录凭证')
            assert self.is_top_tab_visible('录凭证')

    @allure.title('查凭证')
    def test_query_voucher(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('查凭证')
            assert self.is_top_tab_visible('查凭证')

    @allure.title('账簿')
    def test_books(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('账簿'):
                self.click_accounting_menu('账簿', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('报表')
    def test_reports(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('村集体报表'):
                self.click_accounting_menu('报表', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('工资')
    def test_salary(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('工资')
            assert self.is_top_tab_visible('工资')

    @allure.title('库存')
    def test_inventory(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            assert not self.is_element_visible(self.menu('库存'))

    @allure.title('固定资产')
    def test_fixed_asset(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('资产'):
                self.click_accounting_menu('资产', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('结账')
    def test_query_closure(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            self.click_accounting_menu('结账')
            assert self.is_top_tab_visible('结账')

    @allure.title('设置_1')
    def test_settings_1(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[:5]:
                if _ == '现金流量初始金额':
                    pass
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)

    @allure.title('设置_2')
    def test_settings_2(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[6:10]:
                self.click_accounting_data_menu('设置', _)
                assert self.is_top_tab_visible(_)
                self.close_tab_by_tab_name(_)

    @allure.title('高级设置')
    def test_settings_advance(self):
        with allure.step('登录'):
            self.login(company=self.company)
        with allure.step('点击菜单'):
            for _ in ACCOUNTING_MENU.get('设置')[11:]:
                if _ == '明细科目转核算项目':
                    assert not self.is_element_visible(_)
                else:
                    self.click_accounting_data_menu('设置', _)
                    assert self.is_top_tab_visible(_)
                    self.close_tab_by_tab_name(_)
