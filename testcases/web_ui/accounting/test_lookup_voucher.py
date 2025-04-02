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
from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_lookup_voucher
@allure.epic('会计')
@allure.feature('查凭证')
@allure.story('查凭证')
class TestLookupVoucher(LoginPage,
                        ManagerHomePage,
                        AgencyAccountPage,
                        ManagerCommonPage,
                        LookupVoucherPage,
                        AccountingCommonPage,
                        AccountingHomePage,
                        VoucherPage):

    @allure.title('凭证查询-空列表')
    def test_view_voucher_empty(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_048')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            self.click_voucher_buttons('刷新')
            assert '当前期间还没有数据' in self.get_all_floating_tip()

    @allure.title('凭证审核-未勾选')
    def test_audit_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_voucher_buttons('审核')
            assert '请先选择你想要审核的凭证' in self.get_all_floating_tip()

    @allure.title('凭证反审核-未勾选')
    def test_anti_audit_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_048')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_voucher_buttons('反审核')
            assert '请先选择你想要反审核的凭证' in self.get_all_floating_tip()

    @allure.title('批量删除-未勾选')
    def test_delete_multiple_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_voucher_buttons('删除')
            assert '请先选择你想要删除的凭证' in self.get_all_floating_tip()

    @allure.title('批量复制-未勾选')
    def test_delete_multiple_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('批量复制'):
            self.click_voucher_buttons('批量复制')
            assert '请选择要复制的凭证' in self.get_all_floating_tip()

    @pytest.mark.p1
    @allure.title('凭证审核')
    def test_audit_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查是否已审核'):
            if self.get_text_from_voucher_list_audit_cell('审核001') != '未审核':
                self.click_list_voucher_checkbox('审核001')
                self.click_voucher_buttons('反审核')
                assert all(self.multiple_assert_in_tip(['反审核完成', '成功：1']))
        with allure.step('凭证审核'):
            self.click_list_voucher_checkbox('审核001')
            self.click_voucher_buttons('审核')
            assert all(self.multiple_assert_in_tip(['审核完成', '成功：1']))
        with allure.step('还原数据'):
            self.click_voucher_buttons('刷新')
            self.click_list_voucher_checkbox('审核001')
            self.click_voucher_buttons('反审核')
            assert all(self.multiple_assert_in_tip(['反审核完成', '成功：1']))

    @allure.title('凭证审核-重复审核')
    def test_re_audit_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_list_voucher_checkbox('审核002')
            self.click_voucher_buttons('审核')
            assert all(self.multiple_assert_in_tip(
                ['审核完成', '失败：1', '凭证：2023年第01期记-2失败（已审核）！']))

    @allure.title('凭证审核-批量')
    def test_audit_multiple_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查是否已审核'):
            for _ in ['审核004', '审核005']:
                if self.get_text_from_voucher_list_audit_cell(_) != '未审核':
                    self.click_list_voucher_checkbox(_)
                    self.click_voucher_buttons('反审核')
                    assert all(self.multiple_assert_in_tip(['反审核完成', '成功：1']))
                    self.click_refresh()
        with allure.step('凭证审核'):
            self.click_multiple_voucher_checkbox(['审核004', '审核005'])
            self.click_voucher_buttons('审核')
            assert all(self.multiple_assert_in_tip(['审核完成', '成功：2']))
        with allure.step('凭证反审核'):
            self.click_refresh()
            self.click_multiple_voucher_checkbox(['审核004', '审核005'])
            self.click_voucher_buttons('反审核')
            assert all(self.multiple_assert_in_tip(['反审核完成', '成功：2']))

    @allure.title('凭证审核-批量重复审核')
    def test_re_audit_multiple_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_multiple_voucher_checkbox(['审核006', '审核007'])
            self.click_voucher_buttons('审核')
            assert all(self.multiple_assert_in_tip(
                ['审核完成', '失败：2', '2023年第01期记-6失败（已审核）！', '2023年第01期记-7失败（已审核）！']))

    @allure.title('凭证审核-批量重复反审核')
    def test_re_anti_audit_multiple_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('凭证审核'):
            self.click_multiple_voucher_checkbox(['审核008', '审核009'])
            self.click_voucher_buttons('反审核')
            assert all(self.multiple_assert_in_tip(
                ['审核完成', '失败：2', '2023年第01期记-8失败（未审核）！', '2023年第01期记-9失败（未审核）！']))

    @pytest.mark.p1
    @allure.title('新增凭证')
    def test_add_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_049')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('新增凭证'):
            self.click_voucher_buttons('新增')
            self.switch_to_default_content()
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


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_lookup_voucher
@allure.epic('会计')
@allure.feature('查凭证')
@allure.story('凭证导出')
class TestLookupVoucherExport(LoginPage,
                              AgencyAccountPage,
                              ManagerCommonPage,
                              ManagerHomePage,
                              AccountingHomePage,
                              LookupVoucherPage):

    @allure.title('导出凭证-按列表')
    def test_export_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('导出凭证'):
            self.click_voucher_buttons('导出列表')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}\\template\\accounting\\voucher\\凭证列表#2023年第3期-050.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出凭证-按导入模板')
    def test_export_voucher_by_import_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('导出凭证'):
            self.click_voucher_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\voucher\\凭证导入模板-050.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_lookup_voucher
@allure.epic('会计')
@allure.feature('查凭证')
@allure.story('凭证导入')
class TestLookupVoucherImport(LoginPage,
                              AccountingHomePage,
                              LookupVoucherPage,
                              AccountingCommonPage):
    @allure.title('导入凭证-下载凭证导入模板')
    def test_voucher_import_template(self):
        company = GetYamlData().get_company('company_accounting_voucher_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('导入凭证'):
            self.click_voucher_buttons('导入凭证')
            self.click_voucher_template_download_button('下载模版')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\voucher\\凭证导入模板.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导入凭证')
    def test_voucher_import_success(self):
        company = GetYamlData().get_company('company_accounting_voucher_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('清空凭证'):
            if '无数据' not in self.get_text_from_voucher_list_total_line():
                self.click_voucher_buttons('全选')
                self.click_voucher_buttons('删除')
                self.click_voucher_buttons('确认删除')
                self.wait(1)
        with allure.step('导入凭证'):
            self.click_voucher_buttons('导入凭证')
            self.click_voucher_template_download_button('下一步')
            self.send_file_to_voucher_import_file_select_input(
                rf'{get_project_path()}/template/accounting/voucher/凭证导入模板-001.xls'
            )
            self.click_voucher_template_download_button('导入')
            assert '记-1成功导入' in self.get_text_from_voucher_import_result()

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230822-031')
    @allure.title('导入凭证-日期字段错误')
    def test_voucher_import_success(self):
        company = GetYamlData().get_company('company_accounting_voucher_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('清空凭证'):
            if '无数据' not in self.get_text_from_voucher_list_total_line():
                self.click_voucher_buttons('全选')
                self.click_voucher_buttons('删除')
                self.click_voucher_buttons('确认删除')
                self.wait(1)
        with allure.step('导入凭证'):
            self.click_voucher_buttons('导入凭证')
            self.click_voucher_template_download_button('下一步')
            self.send_file_to_voucher_import_file_select_input(
                rf'{get_project_path()}/template/accounting/voucher/凭证导入模板-002.xls'
            )
            self.click_voucher_template_download_button('导入')
            assert '第2行1列日期格式有误！' in self.get_text_from_voucher_import_result()
