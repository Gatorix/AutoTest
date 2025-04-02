import allure
import pytest

from page.web_ui.accounting.page_common import AccountingCommonPage
from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_reports import (BalanceSheetPage,
                                                 IncomeStatementPage,
                                                 CashFlowStatementPage,
                                                 StandardCashFlowStatementPage)

from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_reports
@pytest.mark.accounting_reports_balance
@allure.epic('会计')
@allure.feature('报表')
@allure.story('资产负债表')
class TestReportsBalanceSheetExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    BalanceSheetPage,
    IncomeStatementPage,
    CashFlowStatementPage
):
    @allure.title('导出资产负债表-税局格式')
    def test_balance_sheet_export_sj(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '资产负债表')
            self.switch_to_balance_sheet_frame()
        with allure.step('过滤期间'):
            self.close_or_conform_balance_tips()
            self.select_period('01')
            self.click_balance_sheet_buttons('刷新')
        with allure.step('税局格式导出'):
            self.click_balance_sheet_buttons('税局格式导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/资产负债表-税局格式-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @pytest.mark.p1
    @allure.title('导出资产负债表-excel格式')
    def test_balance_sheet_export_excel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '资产负债表')
            self.switch_to_balance_sheet_frame()
        with allure.step('过滤期间'):
            self.close_or_conform_balance_tips()
            self.select_period('01')
            self.click_balance_sheet_buttons('刷新')
        with allure.step('EXCEL格式'):
            self.click_balance_sheet_buttons('EXCEL格式')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/资产负债表-Excel格式-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出资产负债表-批量导出')
    def test_balance_sheet_export_batch(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '资产负债表')
            self.switch_to_balance_sheet_frame()
        with allure.step('过滤期间'):
            self.close_or_conform_balance_tips()
        with allure.step('批量导出'):
            self.click_balance_sheet_buttons('批量导出', start='2023-01', end='2023-01')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/资产负债表-批量导出-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230925-012')
    @allure.title('精斗云账套会计制度为空-资产负债表提示')
    def test_jdy_empty_accounting_system_balance_sheet_tips(self):
        company = GetYamlData().get_company('proj_R20230925-012')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '资产负债表')
            self.switch_to_balance_sheet_frame()
            assert '请在设置-系统参数界面选择会计制度' in self.get_text_from_accounting_focus_table_sys_tips()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230913-018')
    @allure.title('资产负债表复制按钮更改名称')
    def test_balance_sheet_copy_button_change_name(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '资产负债表')
            self.switch_to_balance_sheet_frame()
            assert '复制至其他账套' == self.get_text_from_copy_button_span()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_reports
@pytest.mark.accounting_reports_income
@allure.epic('会计')
@allure.feature('报表')
@allure.story('利润表')
class TestReportsIncomeStatementExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    IncomeStatementPage,
    CashFlowStatementPage
):
    @allure.title('导出利润表-税局格式')
    def test_income_statement_export_sj(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '利润表')
            self.switch_to_income_statement_frame()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_income_statement_buttons('刷新')
        with allure.step('税局格式导出'):
            self.click_income_statement_buttons('税局格式导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/利润表-税局格式-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230913-018')
    @allure.title('利润表复制按钮更改名称')
    def test_income_statement_copy_button_change_name(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '利润表')
            self.switch_to_income_statement_frame()
            assert '复制至其他账套' == self.get_text_from_copy_button_span()

    @allure.title('导出利润表-Excel格式')
    def test_income_statement_export_excel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '利润表')
            self.switch_to_income_statement_frame()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_income_statement_buttons('刷新')
        with allure.step('EXCEL格式'):
            self.click_income_statement_buttons('EXCEL格式')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/利润表-Excel格式-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出利润表-批量导出-月报')
    def test_income_statement_export_batch_monthly(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '利润表')
            self.switch_to_income_statement_frame()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_income_statement_buttons('刷新')
        with allure.step('批量导出'):
            self.click_income_statement_buttons('批量导出', start='2023-03', end='2023-03', report_type='月报')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/利润表-批量导出-月报-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出利润表-批量导出-季报')
    def test_income_statement_export_batch_quarterly(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '利润表')
            self.switch_to_income_statement_frame()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_income_statement_buttons('刷新')
        with allure.step('批量导出'):
            self.click_income_statement_buttons('批量导出', start='2023-03', end='2023-03', report_type='季报')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/利润表-批量导出-季报-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_reports
@pytest.mark.accounting_reports_cash_flow
@allure.epic('会计')
@allure.feature('报表')
@allure.story('现金流量表')
class TestReportsCashFlowStatementExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    IncomeStatementPage,
    CashFlowStatementPage
):
    @allure.title('导出现金流量表-税局格式')
    def test_cash_flow_statement_export_sj(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '现金流量表')
            self.switch_to_cash_flow_statement_frame()
            self.close_balance_verify()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_cash_flow_statement_buttons('刷新')
        with allure.step('税局格式导出'):
            self.click_cash_flow_statement_buttons('税局格式导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/现金流量表-税局格式-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出现金流量表-Excel格式')
    def test_cash_flow_statement_export_excel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '现金流量表')
            self.switch_to_cash_flow_statement_frame()
            self.close_balance_verify()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_cash_flow_statement_buttons('刷新')
        with allure.step('EXCEL格式'):
            self.click_cash_flow_statement_buttons('EXCEL格式')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/reports/现金流量表-Excel格式-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出现金流量表-批量导出-月报')
    def test_cash_flow_statement_export_batch_monthly(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '现金流量表')
            self.switch_to_cash_flow_statement_frame()
            self.close_balance_verify()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_cash_flow_statement_buttons('刷新')
        with allure.step('批量导出'):
            self.click_cash_flow_statement_buttons('批量导出', start='2023-03', end='2023-03', report_type='月报')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/reports/现金流量表-批量导出-月报-001.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出现金流量表-批量导出-季报')
    def test_cash_flow_statement_export_batch_quarterly(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '现金流量表')
            self.switch_to_cash_flow_statement_frame()
            self.close_balance_verify()
        with allure.step('过滤期间'):
            self.select_period('03')
            self.click_cash_flow_statement_buttons('刷新')
        with allure.step('批量导出'):
            self.click_cash_flow_statement_buttons('批量导出', start='2023-03', end='2023-03', report_type='季报')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/reports/现金流量表-批量导出-季报-001.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230925-012')
    @allure.title('精斗云账套会计制度为空-现金流量表提示')
    def test_jdy_empty_accounting_system_cash_flow_statement_tips(self):
        company = GetYamlData().get_company('proj_R20230925-012')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '现金流量表')
            self.switch_to_cash_flow_statement_frame()
            assert '请在设置-系统参数界面选择会计制度' in self.get_text_from_accounting_focus_table_sys_tips()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_reports
@pytest.mark.accounting_reports_standard_cash_flow
@allure.epic('会计')
@allure.feature('报表')
@allure.story('标准现金流量表')
class TestReportsStandardCashFlowStatementExport(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    StandardCashFlowStatementPage
):

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230805-008')
    @allure.title('标准现金流量表-报表调整-导出功能')
    def test_standard_cash_flow_statement_report_adjust_export(self):
        company = GetYamlData().get_company('proj_R20230805-008')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '标准现金流量表')
            self.switch_to_standard_cash_flow_statement_frame()
        with allure.step('报表调整'):
            self.click_standard_cash_flow_statement_buttons('报表调整')
        with allure.step('报表调整-导出'):
            self.click_standard_cash_flow_statement_report_voucher_dialog_elements('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/reports/标准现金流量表_R20230805-008_2023年第7期 至 2023年第7期-.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230805-008')
    @allure.title('标准现金流量表-报表调整-导出功能-凭证号过滤')
    def test_standard_cash_flow_statement_report_adjust_export_filter_voucher(self):
        company = GetYamlData().get_company('proj_R20230805-008')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('报表', '标准现金流量表')
            self.switch_to_standard_cash_flow_statement_frame()
        with allure.step('报表调整'):
            self.click_standard_cash_flow_statement_buttons('报表调整')
        with allure.step('报表调整-导出'):
            self.type_to_standard_cash_flow_statement_report_voucher_dialog_voucher_num_input('1,9,13-22')
            self.click_standard_cash_flow_statement_report_voucher_dialog_elements('查询')
            self.click_standard_cash_flow_statement_report_voucher_dialog_elements('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/reports/标准现金流量表_R20230805-008_过滤凭证号-.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
