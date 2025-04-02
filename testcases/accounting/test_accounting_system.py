import allure
import pytest

from page.accounting.page_common import AccountingCommonPage
from page.accounting.page_home import AccountingHomePage
from page.accounting.page_lookup_voucher import LookupVoucherPage
from page.accounting.page_voucher import VoucherPage
from page.manager.page_agency import AgencyAccountPage
from page.manager.page_common import ManagerCommonPage
from page.manager.page_home import ManagerHomePage
from page.page_login import LoginPage
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


class TestAccountingStandardsForSmallBusinesses:
    pass


class TestNewAccountingStandards:
    pass


class TestNewAccountingStandardsForBusinessEnterprisesExecuted:
    pass


class TestNewAccountingStandardsForBusinessEnterprises:
    pass


class TestAccountingStandardsForPrivateNonProfitOrganizations:
    pass


class TestAccountingStandardsForVillageCollectiveEconomicOrganizations:
    pass


@pytest.mark.accounting
@pytest.mark.accounting_voucher
@allure.epic('会计')
@allure.feature('录凭证')
@allure.tag('政府制度会计准则')
class TestAccountingStandardsForGovernment(
    LoginPage,
    ManagerHomePage,
    ManagerCommonPage,
    AccountingHomePage,
    AccountingCommonPage,
    LookupVoucherPage,
    VoucherPage,
    AgencyAccountPage
):

    @allure.story('财务凭证')
    @allure.title('平行记账-未保存')
    def test_finance_sync_bookkeeping_unsaved(self):
        company = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证', '财务凭证')
            self.switch_to_voucher_frame()
        with allure.step('平行记账'):
            self.click_buttons('平行记账')
            assert '请先保存凭证！' in self.get_all_floating_tip()

    @allure.story('财务凭证')
    @allure.title('保存并平行记账-不需平行记账')
    def test_finance_sync_bookkeeping_no_need(self):
        company = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证', '财务凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '100101 库存现金_受托代理现金', debit='500')
            self.type_voucher_entry('2', voucher_summary, '1002 银行存款', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '保存凭证成功' in self.get_all_floating_tip()
        with allure.step('平行记账'):
            self.click_buttons('平行记账')
            assert '该凭证不需平行记账' in self.get_all_floating_tip()
        with allure.step('删除凭证'):
            self.switch_to_default_content()
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            self.delete_voucher_by_summary(voucher_summary)
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.story('预算凭证')
    @allure.title('同步记账-未保存')
    def test_budget_sync_bookkeeping_unsaved(self):
        company = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证', '预算凭证')
            self.switch_to_voucher_frame()
        with allure.step('平行记账'):
            self.click_buttons('平行记账')
            assert '请先保存凭证！' in self.get_all_floating_tip()

    @allure.story('预算凭证')
    @allure.title('保存-预算凭证只允许录入预算科目')
    def test_budget_save_voucher_not_budget_subject(self):
        company = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('录凭证', '预算凭证')
            self.switch_to_voucher_frame()
        with allure.step('录入凭证分录'):
            voucher_summary = random_string_generator()
            self.type_voucher_entry('1', voucher_summary, '100101 库存现金_受托代理现金', debit='500')
            self.type_voucher_entry('2', voucher_summary, '1002 银行存款', credit='500')
        with allure.step('保存凭证'):
            self.click_buttons('保存')
            self.click_conform_save_voucher_buttons()
            assert '保存失败，预算凭证只允许录入预算科目' in self.get_all_floating_tip()


class TestAccountingStandardsForFarmersProfessionalCooperatives:
    pass
