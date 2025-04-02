import allure
import pytest

from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.page_login import LoginPage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_common import AccountingCommonPage
from page.web_ui.accounting.page_lookup_voucher import LookupVoucherPage
from page.web_ui.accounting.page_voucher import VoucherPage
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_voucher
@allure.epic('会计')
@allure.feature('录凭证')
@allure.story('录凭证')
class TestVoucher(LoginPage,
                  ManagerHomePage,
                  ManagerCommonPage,
                  AccountingHomePage,
                  AccountingCommonPage,
                  LookupVoucherPage,
                  VoucherPage,
                  AgencyAccountPage):
    @pytest.mark.p1
    @allure.title('新增凭证')
    def test_add_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '1001 库存现金', debit='500')
            self.type_voucher_entry('2', voucher_summary, '1002 银行存款', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '保存凭证成功' in self.get_all_floating_tip()
            self.switch_to_default_content()
        with allure.step('删除凭证'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            self.delete_voucher_by_summary(voucher_summary)
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.tag('【管家】12月项目')
    @allure.tag('R20231116-034')
    @allure.title('新增凭证-摘要过长看不到提示')
    def test_add_voucher_line_too_lang_tips_not_visible(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary * 100, '1001 库存现金', debit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存B')
            self.click_conform_save_voucher_buttons()
            assert '录入借贷不平' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230922-030')
    @allure.title('复制凭证没带现金流')
    def test_copy_voucher_without_cash_flow(self):
        company = GetYamlData().get_company('company_accounting_voucher_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '1001 库存现金', debit='500')
            self.type_voucher_entry('2', voucher_summary, '1601 固定资产', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '保存凭证成功' in self.get_all_floating_tip()
        with allure.step('复制凭证'):
            self.click_buttons('复制')
            self.click_buttons('保存')
            assert '保存凭证成功' in self.get_all_floating_tip()
            assert self.is_button_visible('现金流量')
            self.click_buttons('删除')
            self.click_accounting_focus_table_buttons('确定')
        with allure.step('删除凭证'):
            self.switch_to_default_content()
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            self.delete_voucher_by_summary(voucher_summary)
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('新增凭证-必录项校验-摘要')
    def test_add_voucher_verify_abstract(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '第1条分录摘要不能为空' in self.get_all_floating_tip()

    @allure.title('新增凭证-必录项校验-科目')
    def test_add_voucher_verify_subject(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '', debit='500')
            self.type_voucher_entry('2', voucher_summary, '', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '请选择科目' in self.get_all_floating_tip()
        with allure.step('关闭凭证录入'):
            self.switch_to_default_content()
            self.close_top_tabs('录凭证')
            self.switch_to_voucher_frame()
            self.click_input_buttons('确定')

    @allure.title('新增凭证-必录项校验-金额不平')
    def test_add_voucher_verify_amount_diff(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '1001 库存现金', debit='')
            self.type_voucher_entry('2', voucher_summary, '1002 银行存款', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '录入借贷不平' in self.get_all_floating_tip()
        with allure.step('关闭凭证录入'):
            self.switch_to_default_content()
            self.close_top_tabs('录凭证')
            self.switch_to_voucher_frame()
            self.click_input_buttons('确定')

    @allure.title('新增凭证-必录项校验-金额未录入')
    def test_add_voucher_verify_amount_empty(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '1001 库存现金', debit='')
            self.type_voucher_entry('2', voucher_summary, '1002 银行存款', credit='')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '请录入借贷方金额' in self.get_all_floating_tip()
        with allure.step('关闭凭证录入'):
            self.switch_to_default_content()
            self.close_top_tabs('录凭证')
            self.switch_to_voucher_frame()
            self.click_input_buttons('确定')
