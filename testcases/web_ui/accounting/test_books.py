import allure
import pytest

from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_books import (SubsidiaryLedgerPage,
                                               GeneralLedgerPage,
                                               VoucherSummaryPage,
                                               BalancePage,
                                               QuantityAmountLedgerPage,
                                               QuantityAmountGeneralLedgerPage,
                                               MultiColumnLedgerPage,
                                               AccountingBalancePage,
                                               AccountingDetailPage)
from page.web_ui.accounting.page_common import AccountingCommonPage

from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_subsidiary_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('明细账')
class TestSubsidiaryLedgerExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    SubsidiaryLedgerPage,
    AccountingCommonPage
):

    @allure.title('导出明细账-当前科目')
    def test_subsidiary_ledger_export_current_subject(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开明细账菜单'):
            self.click_accounting_menu('账簿', '明细账')
            self.switch_to_subsidiary_ledger_frame()
        with allure.step('导出原材料科目'):
            self.click_subsidiary_ledger_subjects('1211 原材料')
            self.click_subsidiary_ledger_buttons('导出当前科目')
            self.click_accounting_focus_table_radio_items_by_span('合并导出')
            self.click_accounting_focus_table_buttons('确定')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\明细账-当前科目-原材料-001.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('R20230613-021')
    @allure.tag('【管家】2023-07-27')
    @allure.title('导出明细账-勾选日合计后明细账显示错误-01')
    def test_subsidiary_ledger_check_cash_sub_account_details_wrong_01(self):
        company = GetYamlData().get_company('proj_R20230613-021')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开明细账菜单'):
            self.click_accounting_menu('账簿', '明细账')
            self.switch_to_subsidiary_ledger_frame()
        with allure.step('过滤'):
            self.click_filter_span()
            self.select_period('from', '2022', '01')
            self.select_period('to', '2022', '12')
            self.check_filter_checkbox('现金、银行存款科目显示日合计')
            self.click_subsidiary_ledger_buttons('确定')
        with allure.step('导出银行存款-广发'):
            self.click_subsidiary_ledger_subjects('1002 银行存款', '1002001 广发行-1080')
            self.click_subsidiary_ledger_buttons('导出当前科目')
            self.click_accounting_focus_table_radio_items_by_span('合并导出')
            self.click_accounting_focus_table_buttons('确定')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\明细账_R20230613-021_广发.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('R20230613-021')
    @allure.tag('【管家】2023-07-27')
    @allure.title('导出明细账-勾选日合计后明细账显示错误-02')
    def test_subsidiary_ledger_check_cash_sub_account_details_wrong_02(self):
        company = GetYamlData().get_company('proj_R20230613-021')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开明细账菜单'):
            self.click_accounting_menu('账簿', '明细账')
            self.switch_to_subsidiary_ledger_frame()
        with allure.step('过滤'):
            self.click_filter_span()
            self.select_period('from', '2022', '01')
            self.select_period('to', '2022', '12')
            self.check_filter_checkbox('现金、银行存款科目显示日合计')
            self.click_subsidiary_ledger_buttons('确定')
        with allure.step('导出银行存款-民生'):
            self.click_subsidiary_ledger_subjects('1002 银行存款', '1002002 民生行/7934')
            self.click_subsidiary_ledger_buttons('导出当前科目')
            self.click_accounting_focus_table_radio_items_by_span('合并导出')
            self.click_accounting_focus_table_buttons('确定')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\明细账_R20230613-021_民生.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('R20230607-041')
    @allure.tag('【管家】2023-07-27')
    @allure.title('导出明细账-负数金额导出未按数字格式显示')
    def test_subsidiary_ledger_export_negative_number(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开明细账菜单'):
            self.click_accounting_menu('账簿', '明细账')
            self.switch_to_subsidiary_ledger_frame()
        with allure.step('导出原材料科目'):
            self.click_subsidiary_ledger_subjects('1131 应收账款', '1131_0019 ETNTechnologyCo.,Ltd')
            self.click_subsidiary_ledger_buttons('导出当前科目')
            self.click_accounting_focus_table_radio_items_by_span('合并导出')
            self.click_accounting_focus_table_buttons('确定')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\明细账_R20230607-041.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出明细账-全部科目')
    def test_subsidiary_ledger_export_all_subject(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开明细账菜单'):
            self.click_accounting_menu('账簿', '明细账')
            self.switch_to_subsidiary_ledger_frame()
        with allure.step('导出全部科目'):
            self.click_subsidiary_ledger_buttons('导出全部科目')
            self.click_accounting_focus_table_radio_items_by_span('合并导出')
            self.click_accounting_focus_table_buttons('确定')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\明细账_全部科目-002.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_general_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('总账')
class TestGeneralLedgerExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    GeneralLedgerPage,
):
    @allure.title('导出总账')
    def test_general_ledger_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开总账菜单'):
            self.click_accounting_menu('账簿', '总账')
            self.switch_to_general_ledger_frame()
        with allure.step('导出'):
            self.click_general_ledger_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\总账_会计自动化测试-智能记账-050_2023年第3期.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_voucher_summary
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('凭证汇总表')
class TestVoucherSummaryExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    VoucherSummaryPage
):
    @allure.title('导出凭证汇总表')
    def test_voucher_summary_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '凭证汇总表')
            self.switch_to_voucher_summary_frame()
        with allure.step('导出'):
            self.click_voucher_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\凭证汇总表-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_balance
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('科目余额表')
class TestBalanceExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    BalancePage
):
    @pytest.mark.p1
    @allure.title('导出科目余额表-勾选辅助核算-9级科目')
    def test_balance_export_accounting(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '科目余额表')
            self.switch_to_balance_frame()
        with allure.step('设置过滤条件'):
            self.subject_filtration('显示辅助核算')
        with allure.step('导出'):
            self.click_balance_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\科目余额表-勾选辅助核算-9-001.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出科目余额表-只显示最明细科目-9级科目')
    def test_balance_export_detail_subject_only(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '科目余额表')
            self.switch_to_balance_frame()
        with allure.step('设置过滤条件'):
            self.subject_filtration('只显示最明细科目')
        with allure.step('导出'):
            self.click_balance_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\科目余额表-只显示最明细科目-9-001.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230817-044')
    @allure.title('科目余额表超过一万行翻页')
    def test_balance_line_over_10000_split(self):
        company = GetYamlData().get_company('proj_R20230817-044')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '科目余额表')
            self.switch_to_balance_frame()
            self.wait_for_balance_loading_finish()
        with allure.step('设置过滤条件'):
            self.subject_filtration('显示辅助核算')
            self.wait_for_balance_loading_finish()
        with allure.step('翻页'):
            assert '13,318' in self.get_text_from_balance_total_line()
            assert '2' == self.get_text_from_balance_page_total_pages()
            self.click_balance_page_buttons('下一页')
            self.wait_for_balance_loading_finish()
            assert '10,001' in self.get_text_from_balance_total_line()
            assert '2' == self.get_text_from_balance_page_current_page()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_quantity_amount_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('数量金额明细账')
class TestQuantityAmountLedgerExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    QuantityAmountLedgerPage
):

    @allure.tag('【管家】2023-10-26')
    @allure.title('导出数量金额明细账-导出全部')
    def test_quantity_amount_ledger_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '数量金额明细账')
            self.switch_to_quantity_amount_ledger_frame()
        with allure.step('导出'):
            self.click_quantity_amount_ledger_buttons('导出全部科目')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\数量金额明细账_会计自动化测试-智能记账-050_2023年第3期 (1).xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230808-013')
    @allure.title('导出数量金额明细账-导出当前科目')
    def test_quantity_amount_ledger_export_specific_subject(self):
        company = GetYamlData().get_company('proj_R20230808-013')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '数量金额明细账')
            self.switch_to_quantity_amount_ledger_frame()
            self.click_quantity_amount_ledger_buttons('重置')
            self.click_quantity_amount_ledger_buttons('确定')
        with allure.step('导出'):
            self.click_subsidiary_ledger_subjects('1404 材料成本差异', '140401 test1')
            self.click_quantity_amount_ledger_buttons('导出当前科目')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\数量金额明细账_R20230808-013_2023年第2期.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230808-013')
    @allure.title('导出数量金额明细账-导出当前科目-勾选明细科目')
    def test_quantity_amount_ledger_export_specific_subject_only_show_details(self):
        company = GetYamlData().get_company('proj_R20230808-013')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '数量金额明细账')
            self.switch_to_quantity_amount_ledger_frame()
            self.click_filter_span()
            self.click_quantity_amount_ledger_buttons('重置')
            self.click_filter_inputs_by_label('只显示最明细科目')
            self.click_quantity_amount_ledger_buttons('确定')
        with allure.step('导出'):
            self.click_subsidiary_ledger_subjects('14040201 test2test2')
            self.click_quantity_amount_ledger_buttons('导出当前科目')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\数量金额明细账_R20230808-013_2023年第2期-明细.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_quantity_amount_general_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('数量金额总账')
class TestQuantityAmountGeneralLedgerExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    QuantityAmountGeneralLedgerPage
):
    @allure.title('导出数量金额总账')
    def test_quantity_amount_general_ledger_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '数量金额总账')
            self.switch_to_quantity_amount_general_ledger_frame()
        with allure.step('导出'):
            self.click_quantity_amount_general_ledger_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\数量金额总账_会计自动化测试-智能记账-050_2023年第3期.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_multi_column_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('多栏账')
class TestMultiColumnLedgerExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    MultiColumnLedgerPage
):
    @allure.title('导出多栏账')
    def test_multi_column_ledger_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '多栏账')
            self.switch_to_multi_column_ledger_frame()
        with allure.step('选择科目'):
            self.multi_subject_filtration('1002', '1002 银行存款')
        with allure.step('导出'):
            self.click_multi_column_ledger_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\books\\多栏账-银行存款-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_sub_accounting_balance
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('核算项目余额表')
class TestSubAccountingBalanceExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingBalancePage
):
    @allure.title('导出核算项目余额表')
    def test_accounting_balance_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '核算项目余额表')
            self.switch_to_accounting_balance_frame()
        with allure.step('过滤核算维度'):
            self.accounting_balance_filtration('往来单位')
        with allure.step('导出'):
            self.click_accounting_balance_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\核算项目余额表_会计自动化测试-智能记账-050_2023年第3期.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_books
@pytest.mark.accounting_books_sub_accounting_detail
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('核算项目明细账')
class TestSubAccountingDetailExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingDetailPage
):
    @allure.title('导出核算项目明细账')
    def test_accounting_detail_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开菜单'):
            self.click_accounting_menu('账簿', '核算项目明细账')
            self.switch_to_accounting_detail_frame()
        with allure.step('过滤核算维度'):
            self.accounting_detail_filtration('往来单位')
            self.select_subject('0033 苏州云燕和精密金属材料有限公司')
        with allure.step('导出'):
            self.click_accounting_detail_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\books\\核算项目明细账_会计自动化测试-智能记账-050_2023年第3期.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
