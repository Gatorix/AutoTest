import allure
import pytest

from page.accounting.page_lookup_voucher import LookupVoucherPage
from page.manager.page_agency import AgencyAccountPage
from page.manager.page_common import ManagerCommonPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.accounting.page_home import AccountingHomePage
from page.accounting.page_common import AccountingCommonPage
from page.accounting.page_salary import SalaryPage

from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.accounting
@pytest.mark.accounting_salary
@allure.epic('会计')
@allure.feature('工资')
@allure.story('工资')
class TestSalary(
    LookupVoucherPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    SalaryPage
):
    @allure.title('工资查询-无数据-保存')
    def test_salary_empty_save(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_052')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('保存')
            assert '职员不能为空' in self.get_all_floating_tip()

    @allure.title('导入上月工资-启用期间')
    def test_import_last_month_error(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_052')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('复制上月')
            assert '账套启用期，不支持该操作' in self.get_all_floating_tip()

    @allure.title('计提工资-无数据')
    def test_provision_of_wages_empty(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_052')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('计提工资')
            assert '生成凭证失败,工资表（取数账期：202301）无数据' in self.get_all_floating_tip()

    @allure.title('发放工资-无数据')
    def test_pay_salary_error(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_052')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('发放工资')
            assert '生成凭证失败,工资表（取数账期：202212）无数据' in self.get_all_floating_tip()

    @allure.title('复制上月')
    def test_import_from_last_month(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_056')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('复制上月')
            assert '复制上月成功，共复制记录 1 条' in self.get_all_floating_tip()

    @allure.title('复制上月-已存在')
    def test_import_from_last_month_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_054')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('复制上月')
            assert '此工资表已生成凭证，不支持该操作' in self.get_all_floating_tip()

    @allure.title('计提工资')
    def test_provision_of_wages(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_051')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
        with allure.step('检查是否存在凭证'):
            provision_of_wages_info, pay_salary_info = self.get_text_from_salary_voucher_info()
            if '未生成' not in provision_of_wages_info:
                with allure.step('删除凭证'):
                    self.switch_default_frame()
                    self.click_accounting_menu('查凭证')
                    self.switch_to_lookup_voucher_frame()
                    self.click_list_voucher_checkbox('计提2月工资')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_floating_tips()
                    self.switch_default_frame()
                    self.close_top_tabs('查凭证')
        with allure.step('打开工资菜单'):
            self.switch_default_frame()
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('计提工资')
            assert '计提工资生成凭证成功' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('计提2月工资')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_floating_tips()

    @allure.title('发放工资')
    def test_pay_salary(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_051')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
        with allure.step('检查是否存在凭证'):
            provision_of_wages_info, pay_salary_info = self.get_text_from_salary_voucher_info()
            if '未生成' not in pay_salary_info:
                with allure.step('删除凭证'):
                    self.switch_default_frame()
                    self.click_accounting_menu('查凭证')
                    self.switch_to_lookup_voucher_frame()
                    self.click_list_voucher_checkbox('发放1月工资')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_floating_tips()
                    self.switch_default_frame()
                    self.close_top_tabs('查凭证')
        with allure.step('打开工资菜单'):
            self.switch_default_frame()
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('发放工资')
            assert '发放工资生成凭证成功' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('发放1月工资')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_floating_tips()

    @allure.title('计提工资-已存在')
    def test_provision_of_wages_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_054')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('计提工资')
            assert '凭证已存在' in self.get_all_floating_tip()

    @allure.title('发放工资-已存在')
    def test_pay_salary_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_054')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('发放工资')
            assert '凭证已存在' in self.get_all_floating_tip()

    @allure.title('导入工资表-空表')
    def test_import_salary_detail_empty(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_055')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('导入')
            self.click_import_radio()
            self.send_filepath_to_input(f'{get_project_path()}/template/accounting/salary/工资表导入.xls')
            self.click_import_area_buttons('导入')
            assert '导入文件有误，请下载标准模板维护数据后再导入' in self.get_all_floating_tip()

    @allure.title('导入工资表-文件类型错误')
    def test_import_salary_detail_error(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_055')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('导入')
            self.click_import_radio('按个税申报表导入')
            self.send_filepath_to_input(f'{get_project_path()}/template/accounting/salary/工资表导入.xls')
            self.click_import_area_buttons('导入')
            assert '导入文件有误，请下载标准模板维护数据后再导入' in self.get_all_floating_tip()

    @allure.title('导入工资表')
    def test_import_salary_detail(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_055')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('导入')
            self.click_import_radio()
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/salary/工资表导入-001.xls')
            self.click_import_area_buttons('导入')
            self.click_import_area_buttons('取消')
            assert '导入成功，共导入1条记录' in self.get_all_floating_tip()
        with allure.step('还原数据'):
            self.click_del_button_in_table('张三')
            assert '删除成功' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_salary
@allure.epic('会计')
@allure.feature('工资')
@allure.story('工资-导出')
class TestSalaryExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    SalaryPage
):

    @allure.title('工资模板下载')
    def test_salary_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_052')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('导入')
            self.click_salary_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/salary/工资表导入.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出')
    def test_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_053')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开工资菜单'):
            self.click_accounting_menu('工资')
            self.switch_to_salary_frame()
            self.click_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/salary/工资表-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
