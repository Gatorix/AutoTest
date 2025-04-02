import allure
import pytest
from seleniumbase.common.exceptions import NoSuchElementException

from base.accounting.base_common import AccountingCommonBase
from page.web_ui.accounting.page_settings import SettingsInvoiceVoucherTemplatePage
from page.web_ui.accounting.page_voucher import VoucherDetailPage, VoucherPage
from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.manager.page_customer import CustomerPage
from page.web_ui.page_login import LoginPage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_smart_bookkeeping import (OrganizeInvoicePage,
                                                           OutputInvoicePage,
                                                           BankBillPage,
                                                           IncomeInvoicePage,
                                                           CostInvoicePage)
from page.web_ui.accounting.page_common import AccountingCommonPage, VOUCHER_TEMPLATE
from page.web_ui.accounting.page_lookup_voucher import LookupVoucherPage
from utils.db_utils import ConnectDB
from page.api.accounting.page_api_download import PageApiDownload

from utils.file_utils import get_project_path
from utils.random_data import random_string_generator, random_choice_in_list
from utils.excel_utils import check_excel_diff
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_smart_bookkeeping
@pytest.mark.accounting_smart_bookkeeping_invoice
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('票据附件')
class TestOrganizeInvoice(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    OrganizeInvoicePage,
    AccountingCommonPage,
    LookupVoucherPage,
    SettingsInvoiceVoucherTemplatePage
):

    @allure.title('按单生成凭证-未勾选')
    def test_generate_voucher_by_single_invoice_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击按单生成凭证'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('按单生成凭证')
            assert '请先勾选一张票据！' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未勾选')
    def test_generate_voucher_by_multiple_invoice_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击汇总生成凭证'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('汇总生成凭证')
            assert '请先勾选一张票据！' in self.get_all_floating_tip()

    @allure.title('匹配系统商品-未勾选')
    def test_match_system_product_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击匹配系统商品'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('匹配系统商品')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('指定票据模板-未勾选')
    def test_specified_invoice_template_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击指定票据模板'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('指定票据模板')
            assert '请选择需要指定项' in self.get_all_floating_tip()

    @allure.title('获取发票商品-未勾选')
    def test_get_invoice_product_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击获取发票商品'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('获取发票商品')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('删除-未勾选')
    def test_delete_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击删除'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
            self.click_more_items('删除')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('更多-退回-未勾选')
    def test_more_rollback_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击更多-退回'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
            self.click_more_items('退回')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('更多-跨期-未勾选')
    def test_more_over_period_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击更多-跨期'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
            self.click_more_items('跨期')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('更多-不需记账-未勾选')
    def test_more_unnecessary_bookkeeping_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击更多-不需记账'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
            self.click_more_items('不需记账')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('更多-取消不需记账-未勾选')
    def test_more_cancel_unnecessary_bookkeeping_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击更多-取消不需记账'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
            self.click_more_items('取消不需记账')
            assert '请先勾选操作项' in self.get_all_floating_tip()

    @allure.title('更多-导出-空列表')
    def test_more_export(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击更多-导出'):
            self.switch_to_organize_invoice_frame()
            self.click_more_button()
        with allure.step('导出空列表'):
            self.click_more_items('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\票据列表-autotest-001.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('上传附件-未选择文件')
    def test_upload_file_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击上传附件'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('上传附件')
            self.click_organize_invoice_upload_page_buttons('确定上传')
            assert '请选择上传文件！' in self.get_all_floating_tip()

    @allure.title('上传附件并删除')
    def test_upload_file_unknown_file_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('点击上传附件'):
            self.switch_to_organize_invoice_frame()
            self.click_organize_invoice_button('上传附件')
            self.upload_file_to_organize_invoice_upload_page_input(
                fr'{get_project_path()}\template\common\Snipaste.png')
            self.click_organize_invoice_upload_page_buttons('确定上传')
            assert '上传成功，共上传1张票据！' in self.get_all_floating_tip()
        with allure.step('删除附件'):
            self.switch_visual_type('列表')
            self.click_organize_invoice_check_all_button()
            self.click_more_button()
            self.click_more_items('删除')
            self.click_accounting_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    # @pytest.mark.p1
    @allure.title('列表指定凭证模板')
    def test_specified_template_inline(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('列表指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.specified_template_list('202301001', '采购增值税普通发票-往来结算-采购商品')
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('菜单指定凭证模板')
    def test_specified_template_by_button(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.specified_template_by_button('202301002',
                                              '采购增值税普通发票-往来结算-采购商品')
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('清除指定凭证模板')
    def test_clear_specified_template_by_button(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.clear_template('202301003')
            assert '清除成功，共清除1条记录' in self.get_all_floating_tip()

    @allure.title('匹配系统商品-未指定凭证模板')
    def test_match_system_goods_unspecified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.match_system_items('202301003')
            assert '未指定票据类型，请先指定票据类型' in self.get_all_floating_tip()

    @allure.title('获取发票商品-未指定凭证模板')
    def test_get_invoice_goods_unspecified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301003')
            self.click_organize_invoice_button('获取发票商品')
            assert '存在发票号码或代码为空的发票，请核实' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-未指定凭证模板')
    def test_generate_voucher_unspecified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301003')
            self.click_organize_invoice_button('按单生成凭证')
            assert '存在未指定票据类型的票据，请先指定票据类型' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未指定凭证模板')
    def test_generate_voucher_summary_unspecified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301016')

    @allure.title('按单生成凭证-金额为空')
    def test_generate_voucher_empty_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301008')
            self.click_organize_invoice_button('按单生成凭证')
            assert '生成凭证：成功0张,失败1张。模板错误或借贷金额为空,请检查对应的票据凭证模板设置及金额取数来源' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-已生成')
    def test_generate_voucher_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            self.click_list_check_box('202301009')
            self.click_organize_invoice_button('按单生成凭证')
            assert '存在已生成凭证的票据，请核实' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-记账标记')
    def test_generate_voucher_check_mark(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('已记账')
            assert self.check_acct_mark('202301009')

    # @pytest.mark.p1
    @allure.title('按单生成凭证')
    def test_generate_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            self.click_list_check_box('202301010')
            self.click_organize_invoice_button('按单生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
        with allure.step('联查凭证'):
            self.select_account_status('已记账')
            self.click_list_voucher_link('202301010')
        with allure.step('删除凭证'):
            self.switch_to_default_content()
            self.switch_to_voucher_detail_frame()
            self.click_buttons('delete')
            self.click_voucher_conform_delete_buttons('确定')
            self.switch_to_default_content()
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-金额为空')
    def test_generate_voucher_summary_empty_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301008')
            self.click_organize_invoice_button('按单生成凭证')
            assert '生成凭证：成功0张,失败1张。模板错误或借贷金额为空,请检查对应的票据凭证模板设置及金额取数来源' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-已生成')
    def test_generate_voucher_summary_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            self.click_list_check_box('202301009')
            self.click_organize_invoice_button('汇总生成凭证')
            assert any(['存在已生成凭证的票据，请核实' in self.get_all_floating_tip(),
                        '已有票据关联凭证' in self.get_all_floating_tip()])

    @allure.title('汇总生成凭证-单张')
    def test_generate_voucher_summary_single(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            self.click_list_check_box('202301011')
            self.click_organize_invoice_button('汇总生成凭证')
            self.click_invoice_wrapper_buttons('生成凭证')
            assert '保存凭证成功' in self.get_all_floating_tip()
            self.click_invoice_wrapper_buttons('关闭')
        with allure.step('联查凭证'):
            self.select_account_status('已记账')
            self.click_list_voucher_link('202301011')
        with allure.step('删除凭证'):
            self.switch_to_default_content()
            self.switch_to_voucher_detail_frame()
            self.click_buttons('delete')
            self.click_voucher_conform_delete_buttons('确定')
            self.switch_to_default_content()
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张')
    def test_generate_voucher_summary_multiple(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            invoice_list = ['202301012', '202301013']
        with allure.step('检查是否已生成凭证'):
            for _ in invoice_list:
                if self.is_invoice_related_to_voucher(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_link(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_organize_invoice_frame()
                        self.click_refresh()
        with allure.step('生成凭证'):
            self.click_multiple_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同票据类型相同对方生成一张凭证')
            self.click_organize_invoice_button('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['333.00', '444.00'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons()
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-已有关联')
    def test_generate_voucher_summary_multiple_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            invoice_list = ['202301009']
            self.click_multiple_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('全部汇总生成一张凭证')
            self.click_organize_invoice_button('汇总生成凭证')
            assert '已有票据关联凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-全部汇总')
    def test_generate_voucher_summary_multiple_all_in_one(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('清除指定凭证模板'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('单据过滤'):
            self.select_account_status('全部')
            invoice_list = ['202301014', '202301015']
        with allure.step('检查是否已生成凭证'):
            for _ in invoice_list:
                if self.is_invoice_related_to_voucher(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_link(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_organize_invoice_frame()
                        self.click_refresh()
        with allure.step('生成凭证'):
            self.click_multiple_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('全部汇总生成一张凭证')
            self.click_organize_invoice_button('汇总生成凭证')
            self.click_generate_voucher_manually_button()
            assert '保存凭证成功' in self.get_all_floating_tip()
            self.click_close_invoice_detail()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['777.00'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('退回-不清晰')
    def test_return_unclear(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301002')
        with allure.step('更多-退回'):
            self.click_more_button()
            self.click_more_items('退回')
            self.click_return_choice(1)
            assert '保存成功' in self.get_all_floating_tip()
            assert self.check_return_mark('202301002')

    @allure.title('退回-不符合财务记账要求')
    def test_return_not_qualify(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301002')
        with allure.step('更多-退回'):
            self.click_more_button()
            self.click_more_items('退回')
            self.click_return_choice(2)
            assert '保存成功' in self.get_all_floating_tip()
            assert self.check_return_mark('202301002')

    @allure.title('退回-其他-未录入原因')
    def test_return_other_empty_reason(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301002')
        with allure.step('更多-退回'):
            self.click_more_button()
            self.click_more_items('退回')
            self.click_return_choice(3)
            assert '请输入退回原因' in self.get_all_floating_tip()

    @allure.title('退回-其他')
    def test_return_other(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301002')
        with allure.step('更多-退回'):
            self.click_more_button()
            self.click_more_items('退回')
            self.click_return_choice(3, 'test')
            assert '保存成功' in self.get_all_floating_tip()
            assert self.check_return_mark('202301002')

    @allure.title('跨期-退回票据')
    def test_adj_period_returned_invoice(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301002')
        with allure.step('更多-跨期'):
            self.click_more_button()
            self.click_more_items('跨期')
            assert '票据已退回' in self.get_all_floating_tip()

    @allure.title('跨期-未录入原因')
    def test_adj_period_empty_reason(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301003')
        with allure.step('更多-跨期'):
            self.click_more_button()
            self.click_more_items('跨期')
            self.adj_period('202303')
            assert '请输入跨期原因' in self.get_all_floating_tip()

    @allure.title('跨期')
    def test_adj_period(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.click_list_check_box('202301004')
        with allure.step('更多-跨期'):
            self.click_more_button()
            self.click_more_items('跨期')
            self.adj_period('202303', 'test')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('还原数据'):
            self.select_period('2023-03')
            self.click_list_check_box('202301004')
            self.click_more_button()
            self.click_more_items('跨期')
            self.adj_period('202301', 'test')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('检查跨期标识'):
            self.select_period('2023-01')
            assert self.check_cross_mark('202301004')

    @allure.title('更多-不需记账-单张')
    def test_unnecessary_bookkeeping_single(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('更多-不需记账'):
            self.click_refresh()
            self.click_list_check_box('202301005')
            self.click_more_button()
            self.click_more_items('取消不需记账')
            self.wait(3)
            self.click_refresh()
            self.click_list_check_box('202301005')
            self.click_more_button()
            self.click_more_items('不需记账')
            assert '操作成功，共标记1张发票' in self.get_all_floating_tip()

    @allure.title('更多-不需记账-多张')
    def test_unnecessary_bookkeeping_multiple(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
        with allure.step('选择单据'):
            invoice_list = ['202301006', '202301007']
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
        with allure.step('检查单据状态'):
            for _ in invoice_list:
                if self.check_no_booking_mark(_):
                    self.click_list_check_box(_)
                    self.click_more_button()
                    self.click_more_items('取消不需记账')
                    assert '操作成功，共取消1张发票' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231102-011')
    @allure.title('重复票检测')
    def test_check_bill_num_repeat(self):
        company = GetYamlData().get_company('proj_R20231102-011')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.select_account_status('全部')
        with allure.step('进入票据编辑-002-重复'):
            self.click_list_view_img_by_number('202301002')
            self.sent_text_to_edit_bill_table_inputs_by_label('发票号码', '88888888')
            self.click_edit_bill_table_save_button()
            assert not self.is_edit_bill_tags_visible('repeat')
            self.click_edit_bill_close_button()
            self.refresh()
            assert not self.is_bill_list_tags_by_class_visible('202301002', 'repeat')
        with allure.step('进入票据编辑-001-不重复'):
            self.click_list_view_img_by_number('202301001')
            self.click_edit_bill_table_save_button()
            assert self.is_edit_bill_tags_visible('repeat')
            self.click_edit_bill_close_button()
            self.refresh()
            assert self.is_bill_list_tags_by_class_visible('202301001', 'repeat')
        with allure.step('进入票据编辑-002-不重复'):
            self.click_list_view_img_by_number('202301002')
            self.sent_text_to_edit_bill_table_inputs_by_label('发票号码', '888888889')
            self.click_edit_bill_table_save_button()
            assert not self.is_edit_bill_tags_visible('repeat')
            self.click_edit_bill_close_button()
            self.refresh()
            assert not self.is_bill_list_tags_by_class_visible('202301002', 'repeat')

    @allure.tag('【管家】2024年01月')
    @allure.tag('R20231213-024')
    @allure.title('票据编辑页面多余滚动条')
    def test_invoice_edit_extra_scroll_bar(self):
        company = GetYamlData().get_company('proj_R20231102-011')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '票据附件')
            self.switch_to_organize_invoice_frame()
            self.switch_visual_type('列表')
            self.select_account_status('全部')
        with allure.step('进入票据编辑'):
            self.click_list_view_img_by_number('202301003')
            self.click_edit_bill_table_input()
            self.click_edit_bill_table_drop_items('销售增值税发票-往来结算')
            assert self.is_edit_bill_scroll_bar_exist()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_smart_bookkeeping
@pytest.mark.accounting_smart_bookkeeping_out_invoice
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('销项发票')
class TestOutputInvoice(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    OutputInvoicePage,
    AccountingCommonPage,
    LookupVoucherPage,
    SettingsInvoiceVoucherTemplatePage
):
    @allure.tag('【管家】12月项目')
    @allure.tag('R20231122-030')
    @allure.title('销项发票发票来源中移除智能取票')
    def test_output_remove_item(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
        with allure.step('更多'):
            self.click_output_invoice_more_button()
            self.click_output_invoice_filters_input_source()
            assert not self.is_output_invoice_filters_input_drop_down_items_present('智能取票')
            assert self.is_output_invoice_filters_input_drop_down_items_present('云取票')

    @allure.title('销项发票导入模板对比')
    def test_check_import_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('下载销项发票模板'):
            self.click_type_checkbox('按标准模板导入')
            self.click_download_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\销项发票标准模板.xlsx',
                             f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导入销项发票-开票软件导出后直接导入-未选择文件')
    def test_import_invoices_software_output_unselect_file(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_buttons()
            assert '请选择导入文件' in self.get_all_floating_tip()

    @pytest.mark.p1
    @allure.title('指定单张发票结算方式')
    def test_single_invoice_specified_billing_method(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('点击凭证模板'):
            self.click_voucher_template('87663149')
            self.select_voucher_template('87663149', '销售增值税发票-现金')
            assert '指定成功！' in self.get_all_floating_tip()
        with allure.step('检查结算方式'):
            assert self.is_billing_method_visible('87663149', '现金')
        with allure.step('还原'):
            self.click_voucher_template('87663149')
            self.select_voucher_template('87663149', '销售增值税发票-往来结算')
            assert '指定成功！' in self.get_all_floating_tip()

    @allure.title('指定多张发票结算方式')
    def test_multiple_invoice_specified_billing_method(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('勾选多张发票'):
            bill_list = ['87663101', '87663102', '87663103']
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('点击指定凭证模板按钮'):
            self.click_normal_button('指定凭证模板')
            self.click_specified_billing_method_input()
            self.click_specified_billing_method_dropdown_items('销售增值税发票-现金')
            self.click_specified_billing_method_buttons('保存')
            assert '指定成功！' in self.get_all_floating_tip()
        with allure.step('检查批量指定结果'):
            result_list = []
            for idx, _ in enumerate(bill_list):
                result_list.append(self.is_billing_method_visible(_, '现金'))
            assert all(result_list)
        with allure.step('还原'):
            self.click_refresh()
            self.click_multiple_invoice_checkbox(bill_list)
            self.click_normal_button('指定凭证模板')
            self.click_specified_billing_method_input()
            self.click_specified_billing_method_dropdown_items('销售增值税发票-往来结算')
            self.click_specified_billing_method_buttons('保存')
            assert '指定成功！' in self.get_all_floating_tip()

    @allure.title('批量清除已指定的凭证模板')
    def test_clear_specified_billing_method(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('勾选多张发票'):
            bill_list = ['87663104', '87663105', '87663106']
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('清除已指定'):
            self.click_normal_button('指定凭证模板')
            self.click_specified_billing_method_buttons('清除已指定模板')
            self.click_clear_billing_method_buttons('确定')
            assert '清除成功' in self.get_all_floating_tip()
        with allure.step('检查批量指定结果'):
            result_list = []
            for idx, _ in enumerate(bill_list):
                result_list.append(self.is_billing_method_visible(_, ''))
            assert all(result_list)
        with allure.step('还原'):
            self.click_refresh()
            self.click_multiple_invoice_checkbox(bill_list)
            self.click_normal_button('指定凭证模板')
            self.click_specified_billing_method_input()
            self.click_specified_billing_method_dropdown_items('销售增值税发票-往来结算')
            self.click_specified_billing_method_buttons('保存')
            assert '指定成功！' in self.get_all_floating_tip()

    @allure.title('指定凭证模板-未勾选')
    def test_invoice_specified_billing_method_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('点击菜单按钮'):
            self.click_normal_button('指定凭证模板')
            assert '请选择需要指定项！' in self.get_all_floating_tip()

    @allure.title('匹配系统商品-未勾选')
    def test_match_goods_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('点击菜单按钮'):
            self.click_normal_button('匹配系统商品')
            assert '请选择匹配项' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-未勾选')
    def test_generate_single_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('点击菜单按钮'):
            self.click_normal_button('按单生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    # @pytest.mark.p1
    @allure.title('按单生成凭证-列表单独生成')
    def test_generate_single_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            invoice_list = ['87663107']
            for _ in invoice_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('指定票据凭证模板'):
            self.click_voucher_template('87663107')
            self.select_voucher_template('87663107', '销售增值税发票-往来结算')
            assert '指定成功！' in self.get_all_floating_tip()
        with allure.step('点击列表生成凭证按钮'):
            self.click_list_generate_voucher_button('87663107')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('87663107')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-菜单批量生成')
    def test_generate_multiple_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663108', '87663109', '87663110']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('按单生成凭证')
            assert '生成凭证成功，共生成3张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            for idx, _ in enumerate(bill_list):
                self.click_list_voucher_checkbox(f'销售收入{_}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除3张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未勾选')
    def test_generate_multiple_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.click_refresh()
        with allure.step('点击菜单按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-默认方式多张')
    def test_summary_generate_multiple_voucher_default(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663111', '87663112', '87663113']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(''.join([f'销售收入{x};' for x in bill_list])[:-1])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-默认方式单张')
    def test_summary_generate_single_voucher_default(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663114']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663114'
            self.click_invoice_checkbox(bill_num)
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-全部汇总-勾选单张')
    def test_summary_generate_single_voucher_all_summary(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663115']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663115'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('全部汇总生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同对方-勾选单张')
    def test_summary_generate_single_voucher_same_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663116']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663116'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期与交易对手-勾选单张')
    def test_summary_generate_single_voucher_same_date_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663117']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663117'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期与票据类型-勾选单张')
    def test_summary_generate_single_voucher_same_date_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663118']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663118'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期相同票据类型生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期-勾选单张')
    def test_summary_generate_single_voucher_same_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663119']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663119'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同票据类型与交易对手-勾选单张')
    def test_summary_generate_single_voucher_same_type_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663120']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663120'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同票据类型相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同票据类型-勾选单张')
    def test_summary_generate_single_voucher_same_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663121']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选单张发票'):
            bill_num = '87663121'
            self.click_invoice_checkbox(bill_num)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同票据类型生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(f'销售收入{bill_num}')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-全部汇总-勾选多张')
    def test_summary_generate_multiple_voucher_all_summary(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663122', '87663123', '87663124', '87663125', '87663126', '87663127']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('全部汇总生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(''.join([f'销售收入{x};' for x in bill_list])[:-1])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同对方-勾选多张')
    def test_summary_generate_multiple_voucher_same_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663128', '87663129', '87663130', '87663131', '87663132', '87663133']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成4张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            summary_list = ['A公司', 'B公司', 'C公司', 'D公司']
            self.click_multiple_voucher_checkbox(summary_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除4张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期与交易对手-勾选多张')
    def test_summary_generate_multiple_voucher_same_date_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663134', '87663135', '87663136']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            summary_list = ['A公司', 'B公司']
            self.click_multiple_voucher_checkbox(summary_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期与票据类型-勾选多张')
    def test_summary_generate_multiple_voucher_same_date_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663137', '87663138', '87663139']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期相同票据类型生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(bill_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同日期-勾选多张')
    def test_summary_generate_multiple_voucher_same_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663140', '87663141', '87663142']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同日期生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(bill_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同票据类型与交易对手-勾选多张')
    def test_summary_generate_multiple_voucher_same_type_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663143', '87663144', '87663145']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同票据类型相同对方生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成3张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(bill_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除3张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-相同票据类型-勾选多张')
    def test_summary_generate_multiple_voucher_same_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-01-01', '2023-01-31')
            self.output_invoice_switch_status('全部')
            self.click_refresh()
        with allure.step('检查凭证是否已存在'):
            bill_list = ['87663146', '87663147', '87663148']
            for _ in bill_list:
                if not self.is_output_invoice_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_output_invoice_voucher_link_by_bill_code(_)
                        self.switch_to_default_content()
                        self.switch_to_voucher_detail_frame()
                        self.click_buttons('delete')
                        self.click_voucher_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
                        self.switch_to_default_content()
                        self.switch_to_output_invoice_iframe()
                        self.click_refresh()
        with allure.step('勾选多张发票'):
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('选择生成方式'):
            self.click_dropdown_button()
            self.click_dropdown_item()
            self.click_generate_voucher_settings_checkbox('相同票据类型生成一张凭证')
            self.click_generate_voucher_settings_button('确定')
        with allure.step('点击菜单生成凭证按钮'):
            self.click_normal_button('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证！' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(bill_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('导入销项发票-标准模板-覆盖')
    def test_import_invoices_standard_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2019-09-01', '2019-09-30')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('按标准模板导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板.xlsx')
            self.click_smart_collection_import_buttons()
            assert '导入成功' in self.get_all_floating_tip()
        with allure.step('检查上传的发票'):
            self.click_invoice_checkbox()
        with allure.step('删除发票'):
            self.click_more_buttons('删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-覆盖')
    def test_import_invoices_software_output_general_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_import_type('普通:通用机打发票:EXCEL')
            self.click_smart_collection_import_buttons()
        with allure.step('核对导入内容'):
            bill_list = ['01774331', '01774332', '01774333']
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('删除发票'):
            self.click_more_buttons('删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230926-028')
    @allure.title('发票文件中含有合计行导致导入后金额翻倍')
    def test_import_invoices_sum_line(self):
        company = GetYamlData().get_company('proj_R20230926-028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2023-08-01', '2023-08-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230926-028.xlsx')
            self.click_import_type('销项:税务数字账户-销项:EXCEL')
            self.click_smart_collection_import_buttons()
        with allure.step('检查发票金额'):
            self.click_refresh()
            assert self.get_text_from_outcome_invoice_total_amount() == '11805'
        with allure.step('核对导入内容'):
            bill_list = ['07240001', '07240002']
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('删除发票'):
            self.click_more_buttons('删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-未选择模板类型-覆盖')
    def test_import_invoices_software_output_unselect_type_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_smart_collection_import_buttons()
            assert '参数不能为空' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-模板类型不匹配-覆盖')
    def test_import_invoices_software_output_unmatch_type_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_import_type('销项:百旺:XML')
            self.click_smart_collection_import_buttons()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230403-006')
    @allure.title('导入销项发票-文件名中包含#')
    def test_import_invoices_file_name_contains_sharp(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230403-006-614#信达房地资产.xls')
            self.click_import_type('销项:百旺:XML')
            self.click_smart_collection_import_buttons()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230403-006')
    @allure.title('导入销项发票-文件名中包含$')
    def test_import_invoices_file_name_contains_dollar(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230403-006-614$信达房地资产.xls')
            self.click_import_type('销项:百旺:XML')
            self.click_smart_collection_import_buttons()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.title('导入销项发票-标准模板-新增')
    def test_import_invoices_standard_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2019-09-01', '2019-09-30')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('按标准模板导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板.xlsx')
            self.click_smart_collection_import_buttons()
            assert '导入成功' in self.get_all_floating_tip()
        with allure.step('检查上传的发票'):
            self.click_invoice_checkbox()
        with allure.step('删除发票'):
            self.click_more_buttons('删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-新增')
    def test_import_invoices_software_output_general_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_import_type('普通:通用机打发票:EXCEL')
            self.click_smart_collection_import_buttons()
        with allure.step('核对导入内容'):
            bill_list = ['01774331', '01774332', '01774333']
            self.click_multiple_invoice_checkbox(bill_list)
        with allure.step('删除发票'):
            self.click_more_buttons('删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-未选择模板类型-新增')
    def test_import_invoices_software_output_unselect_type_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_smart_collection_import_buttons()
            assert '参数不能为空' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-模板类型不匹配-新增导入')
    def test_import_invoices_software_output_unmatch_type_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项-机打发票模板.xlsx')
            self.click_import_type('销项:百旺:XML')
            self.click_smart_collection_import_buttons()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.title('导入销项发票-标准模板-错误文件-新增')
    def test_import_invoices_standard_error_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2019-09-01', '2019-09-30')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('按标准模板导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板-错误.xlsx')
            self.click_smart_collection_import_buttons()
            assert '文件上传失败，请检查文件和对应设置' in self.get_all_floating_tip()

    @allure.title('导入销项发票-标准模板-错误文件-覆盖')
    def test_import_invoices_standard_error_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2019-09-01', '2019-09-30')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('按标准模板导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板-错误.xlsx')
            self.click_smart_collection_import_buttons()
            assert '文件上传失败，请检查文件和对应设置' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-错误文件-新增导入')
    def test_import_invoices_software_output_error_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板-错误.xlsx')
            self.click_import_type('销项:航信:EXCEL')
            self.click_smart_collection_import_buttons()
            assert '文件上传失败，请检查文件和对应设置' in self.get_all_floating_tip()

    @allure.title('导入销项发票-开票软件导出后直接导入-错误文件-覆盖导入')
    def test_import_invoices_software_output_error_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2022-05-01', '2022-05-31')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_smart_collection_import_method_checkbox('覆盖方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\销项发票标准模板-错误.xlsx')
            self.click_import_type('销项:航信:EXCEL')
            self.click_smart_collection_import_buttons()
            assert '文件上传失败，请检查文件和对应设置' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230531-009')
    @allure.title('导入销项发票-按销项票模板导入-销项:税务数字账户-销项:EXCEL-提示语验证')
    def test_import_invoices_standard_template_digital_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
            self.click_import_type('销项:税务数字账户-销项:EXCEL')
            assert self.is_smart_collection_digital_file_tips_visible()
            self.click_import_type('销项:百旺:EXCEl')
            assert not self.is_smart_collection_digital_file_tips_visible()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230531-009')
    @allure.title('导入销项发票-按销项票模板导入-销项:税务数字账户-销项:EXCEL-图片流程')
    def test_import_invoices_standard_template_digital_img(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
            self.click_import_type('销项:税务数字账户-销项:EXCEL')
            self.click_smart_collection_digital_file_show_img_button()
            assert self.is_smart_collection_digital_file_img_visible()
            self.click_smart_collection_digital_file_img_close_button()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231103-045')
    @allure.title('选择分页后更改过滤条件页码错误')
    def test_page_number_error(self):
        company = GetYamlData().get_company('proj_R20231103-045')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2021-01-01', '2023-08-31')
            self.click_refresh()
        with allure.step('选择每页10条'):
            self.change_page_size('10条/页')
        with allure.step('选择第3页'):
            self.select_page(3)
        with allure.step('输入过滤条件'):
            self.type_date('2022-09-30', '2023-08-31')
            self.click_refresh()
        with allure.step('检查页码'):
            assert '1' == self.get_current_page_num()

    #
    # def test_create_data(self):
    #     for _ in range(27):
    #         if _ < 15:
    #             continue
    #         company = GetYamlData().get_company(f'company_accounting_smart_bookkeeping_00{_ + 1}' if _ < 10 else f'company_accounting_smart_bookkeeping_0{_ + 1}')
    #
    #         with allure.step('登录'):
    #             self.login()
    #         with allure.step('关闭弹窗'):
    #             self.close_popup()
    #         with allure.step('点击菜单'):
    #             if self.is_logo_appear():
    #                 self.click_accounting_menu('代账服务', '服务管理')
    #         with allure.step('搜索公司'):
    #             ori_window = driver.current_window_handle
    #             self.search_company(company)
    #         with allure.step('点击创建账套按钮'):
    #             ori_window = driver.current_window_handle
    #             self.click_table_button(company, '创建账套')
    #             self.click_ignore_set_tip()
    #             # 跳转至创建账套新页面
    #             self.switch_to_accounting_window()
    #         with allure.step('创建账套_填写启用期间'):
    #             self.input_enable_year('2023')  # 编写启用期间：xxx年xx期，如2022年11期
    #             self.input_enable_month('1')  # 编写启用期间：xxx年xx期，如2022年11期
    #             self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
    #         with allure.step('创建账套_点击开始创建'):
    #             self.click_create_button('开始创建')  # 后跳转至会计页面
    #             assert company == self.get_company_name()
    #         # with allure.step('进入账簿'):
    #         #     self.click_table_button(company, '进账簿')
    #         #     self.switch_to_accounting_window()
    #         with allure.step('点击会计菜单'):
    #             self.click_accounting_menu('智能记账', '销项票')
    #             self.switch_to_output_invoice_iframe()
    #             self.close_popup()
    #         with allure.step('点击智能采集-导入'):
    #             self.click_smart_collection()
    #             self.click_smart_collection_import()
    #         with allure.step('上传文件'):
    #             self.click_type_checkbox('按标准模板导入')
    #             self.click_smart_collection_import_select_button()
    #             self.upload(r'C:\Users\kingdee\Downloads\销项发票标准模板3.xlsx')
    #             self.click_smart_collection_import_buttons()
    #
    #             self.switch_default_frame()
    #             self.small_wait()
    #
    #             self.click_accounting_menu('设置')
    #             self.small_wait()
    #             self.click('//*[@id="nav"]/li[10]/div[2]/div[1]/ul/li[9]/a')
    #
    #             self.switch_to_frame('setting-voucherTemplate')
    #
    #             self.click('//*[@id="info-list"]/tr[1]/td[5]/i')
    #             self.click('//*[@id="fabfixed"]/span[3]')
    #             self.click('(//*[@id="account-save"])[5]')
    #
    #             self.small_wait()
    #             self.click('//*[@id="info-list"]/tr[2]/td[5]/i')
    #             self.click('//*[@id="fabfixed"]/span[3]')

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230807-026')
    @allure.title('导出发票的票据类型为空')
    def test_export_file_empty_invoice_type_out(self):
        company = GetYamlData().get_company('proj_R20230807-026')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.clear_date()
            self.outcome_invoice_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('下载销项发票模板'):
            self.click_more_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\R20230807-026-out-2.xls',
                             f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230822-033')
    @allure.title('导入销项发票-税额字段错误')
    def test_import_invoices_tax_col_error(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '销项票')
            self.switch_to_output_invoice_iframe()
            self.close_popup()
        with allure.step('输入过滤条件'):
            self.type_date('2019-09-01', '2019-09-30')
            self.click_refresh()
        with allure.step('点击智能采集-导入'):
            self.click_smart_collection()
            self.click_smart_collection_import()
        with allure.step('上传文件'):
            self.click_type_checkbox('开票软件导出后直接导入')
            self.click_import_type('销项:税务数字账户-销项:EXCEL')
            self.click_smart_collection_import_method_checkbox('新增方式')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230822-033.xlsx')
            self.click_smart_collection_import_buttons()
            assert '请检查发票导入文件' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_smart_bookkeeping
@pytest.mark.accounting_smart_bookkeeping_bank_bill
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('银行对账单')
class TestBankBill(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    BankBillPage,
    AccountingCommonPage,
    LookupVoucherPage,
    VoucherPage,
    SettingsInvoiceVoucherTemplatePage,
    AccountingCommonBase
):

    @allure.title('按单生成凭证-未勾选')
    def test_generate_voucher_by_single_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击按单生成凭证'):
            self.click_bank_bill_buttons('按单生成凭证')
            assert '请选择需要生成项！' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未勾选')
    def test_generate_voucher_by_summary_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击汇总生成凭证'):
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '请选择需要生成项！' in self.get_all_floating_tip()

    @allure.title('保存-空行')
    def test_save_blank_line(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击保存'):
            self.click_bank_bill_buttons('保存')
            assert '请删除空行，存在收入/支出为空记录！' in self.get_all_floating_tip()

    @allure.title('导入-未选择文件-pdf')
    def test_import_unselect_file_pdf(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.click_bank_bill_import_buttons('确定')
            assert '请添加附件！' in self.get_all_floating_tip()

    @allure.title('导入-未选择文件-excel')
    def test_import_unselect_file_excel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(1)
            self.click_bank_bill_import_buttons('确定')
            assert '请添加附件！' in self.get_all_floating_tip()

    @allure.title('指定票据模板-未勾选')
    def test_specified_billing_method_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击指定票据模板'):
            self.click_bank_bill_buttons('指定票据模板')
            assert '请先保存数据！' in self.get_all_floating_tip()

    @allure.title('删除-未勾选')
    def test_delete_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击指定票据模板'):
            self.click_bank_bill_white_dropdown_buttons('更多')
            self.click_bank_bill_white_dropdown_items('更多', '删除')
            assert '请选择删除项！' in self.get_all_floating_tip()

    @allure.title('指定银行科目-未勾选')
    def test_specified_bank_account_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击指定票据模板'):
            self.click_bank_bill_white_dropdown_buttons('更多')
            self.click_bank_bill_white_dropdown_items('更多', '指定银行科目')
            assert '请选择需要指定项！' in self.get_all_floating_tip()

    @allure.title('打印-未勾选')
    def test_print_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_028')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('点击指定票据模板'):
            self.click_bank_bill_white_dropdown_buttons('更多')
            self.click_bank_bill_white_dropdown_items('更多', '打印')
            assert '请选择需要打印项！' in self.get_all_floating_tip()

    @pytest.mark.p1
    @allure.title('按单生成凭证-列表单张')
    def test_generate_voucher_single_list(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_029')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('徐泽宇'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('徐泽宇')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_bank_bill_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.list_specified_voucher_template('130687.92', '银行票据-银行存款-收其他往来款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证'):
            self.click_list_generate_voucher_button('130687.92')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('徐泽宇')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-按钮单张')
    def test_generate_voucher_single_button(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_030')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('徐泽宇'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('徐泽宇')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.list_specified_voucher_template('130687.92', '银行票据-银行存款-收其他往来款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('菜单按钮生成凭证'):
            self.click_single_list_checkbox_by_summary('130687.92')
            self.click_bank_bill_buttons('按单生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('徐泽宇')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-汇总单张')
    def test_generate_voucher_single_summary_button(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_031')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('徐泽宇'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('徐泽宇')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.list_specified_voucher_template('130687.92', '银行票据-银行存款-收其他往来款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('菜单按钮生成凭证'):
            self.click_single_list_checkbox_by_summary('130687.92')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('徐泽宇')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('批量指定凭证类型')
    def test_specified_multiple_voucher_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_032')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('收费')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-银行手续费')
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('批量清除指定凭证类型')
    def test_clear_specified_multiple_voucher_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_033')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('收费')
            self.click_bank_bill_buttons('指定票据模板')
            self.clear_voucher_template()
            assert '清除成功，共清除5条记录' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张')
    def test_generate_voucher_multiple_summary_button(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_034')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('财务费用_手续费'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('财务费用_手续费')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('收费')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-银行手续费')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('菜单按钮生成凭证'):
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('财务费用_手续费')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同票据类型生成一张凭证')
    def test_generate_voucher_multiple_summary_same_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_035')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('财务费用_手续费'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('财务费用_手续费')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('收费')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-银行手续费')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('相同票据类型生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('财务费用_手续费')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同票据类型相同对方生成一张凭证')
    def test_generate_voucher_multiple_summary_same_type_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_036')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['2021-11-01', '2021-11-17']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('收费')
            self.click_multiple_checkbox_by_same_summary('徐泽宇')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-银行手续费')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('相同票据类型相同对方生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['2021-11-01', '2021-11-17'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期生成一张凭证')
    def test_generate_voucher_multiple_summary_same_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_037')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['2021-11-07', '2021-11-08']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('2021-11-07')
            self.click_multiple_checkbox_by_same_summary('2021-11-08')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-银行手续费')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('相同日期生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['2021-11-07', '2021-11-08'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期相同票据类型生成一张凭证')
    def test_generate_voucher_multiple_summary_same_date_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_038')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['福利费', '办公用品']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('130687.92')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('费用票据-现金-福利费')
            assert '指定成功' in self.get_all_floating_tip()
            self.click_refresh()
            self.click_multiple_checkbox_by_same_summary('36187.92')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('费用票据-现金-办公用品')
            assert '指定成功' in self.get_all_floating_tip()
            self.click_refresh()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.click_multiple_checkbox_by_same_summary('2021-11-01')
            self.set_generate_voucher_summary_setting('相同日期相同票据类型生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['福利费', '办公用品'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期相同对方生成一张凭证')
    def test_generate_voucher_multiple_summary_same_date_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_039')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['100,000.00', '94,500.00']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('2021-11-01')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('费用票据-现金-办公用品')
            assert '指定成功' in self.get_all_floating_tip()
            self.click_refresh()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.click_multiple_checkbox_by_same_summary('2021-11-01')
            self.set_generate_voucher_summary_setting('相同日期相同对方生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['100,000.00', '94,500.00'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同对方生成一张凭证')
    def test_generate_voucher_multiple_summary_same_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_040')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['徐泽宇', '深圳市卓宝工程建设有限公司']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('徐泽宇')
            self.click_multiple_checkbox_by_same_summary('深圳市卓宝工程建设有限公司')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-收客户款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('相同对方生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['徐泽宇', '深圳市卓宝工程建设有限公司'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同收支方向生成一张凭证')
    def test_generate_voucher_multiple_summary_same_cd(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_041')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['徐泽宇', '深圳市卓宝工程建设有限公司']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('徐泽宇')
            self.click_multiple_checkbox_by_same_summary('深圳市卓宝工程建设有限公司')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-收客户款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('相同收支方向生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['徐泽宇', '深圳市卓宝工程建设有限公司'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-全部汇总生成一张凭证')
    def test_generate_voucher_multiple_summary_all(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_042')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            voucher_list = ['银行存款']
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('指定凭证模板'):
            self.click_multiple_checkbox_by_same_summary('徐泽宇')
            self.click_multiple_checkbox_by_same_summary('深圳市卓宝工程建设有限公司')
            self.click_bank_bill_buttons('指定票据模板')
            self.button_specified_voucher_template('银行票据-银行存款-收客户款')
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('生成凭证-相同票据类型生成一张凭证'):
            self.set_generate_voucher_summary_setting('全部汇总生成一张凭证')
            self.click_bank_bill_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['银行存款'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('下载导入模板')
    def test_verify_download_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_042')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('下载导入模板'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(1)
            self.click_download_standard_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\银行对账单标准模板.xlsx',
                             f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导入银行对账单-未选择附件')
    def test_import_bank_bill_file_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_058')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(1)
            self.click_import_bank_bill_conform_button()
            assert '请添加附件！' in self.get_all_floating_tip()

    @allure.title('导入银行对账单-未选择银行科目')
    def test_import_bank_bill_bank_subject_unselect(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_058')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(1)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/银行对账单标准模板.xlsx')
            self.click_select_bank('招商银行')
            self.click_import_bank_bill_conform_button()

    @allure.title('导入银行对账单-招商银行-覆盖-pdf')
    def test_import_bank_bill_cmb_override_pdf(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_058')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/招行对账单-01.pdf')
            # self.click_select_bank('招商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('1')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '17'

    @allure.title('导入银行对账单-招商银行-覆盖-pdf-01')
    def test_import_bank_bill_cmb_pdf_override_01(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_059')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/招行对账单-02.pdf')
            # self.click_select_bank('招商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('1')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '83'

    @allure.title('导入银行对账单-招商银行-新增-pdf')
    def test_import_bank_bill_cmb_add_pdf(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_060')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/招行对账单-01.pdf')
            # self.click_select_bank('招商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '17'

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231117-024')
    @allure.title('导入银行对账单-华润银行-新增-pdf')
    def test_import_bank_bill_crb_add_pdf(self):
        company = GetYamlData().get_company('proj_R20231117-024')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20231117-024.pdf')
            # self.click_select_bank('华润银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '62'

    @allure.title('导入银行对账单-招商银行-新增-pdf-01')
    def test_import_bank_bill_cmb_pdf_add_01(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_061')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/招行对账单-02.pdf')
            # self.click_select_bank('招商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '83'

    @pytest.mark.p1
    @allure.title('录入新增银行对账单-收入')
    def test_manually_add_bank_bill_income(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-1-4', '2023-1-4')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2023-1-4')
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '收入', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('录入新增银行对账单-支出')
    def test_manually_add_bank_bill_outcome(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-2-5', '2023-2-5')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2023-2-5')
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '支出', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            self.click_refresh()
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('录入新增银行对账单-收入支出同时存在')
    def test_manually_add_bank_bill_income_and_outcome(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-4-5', '2023-4-5')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2023-4-5')
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '收入', '333')
            self.type_to_bank_bill_inputs_in_line('1', '支出', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '存在既有收入又有支出的记录' in self.get_all_floating_tip()

    @allure.title('录入新增银行对账单-日期为空')
    def test_manually_add_bank_bill_empty_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-4-5', '2023-4-5')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '支出', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '请删除空行，存在交易日期为空或格式不正确记录' in self.get_all_floating_tip()

    @allure.title('录入新增银行对账单-金额为空')
    def test_manually_add_bank_bill_empty_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-4-5', '2023-4-5')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2023-4-5')
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '请删除空行，存在收入/支出为空记录！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-07-27')
    @allure.tag('R20230626-023')
    @allure.title('手工新增银行对账单报错')
    def test_manually_add_bank_bill_two_lines(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_057')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.type_date('2023-3-4', '2023-3-5')
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.click_bank_bill_operate_buttons_in_line('1', 'add')
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2023-3-4')
            self.type_to_bank_bill_inputs_in_line('1', '收入', '333')
            self.type_to_bank_bill_inputs_in_line('2', '交易日期', '2023-3-5')
            self.type_to_bank_bill_inputs_in_line('2', '收入', '444')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230717-032')
    @allure.title('导入三月流水后一月二月流水消失')
    def test_manually_import_data_deleted(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_062')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('录入银行对账单'):
            self.type_to_bank_bill_inputs_in_line('1', '交易日期', '2022-12-31')
            self.type_to_bank_bill_inputs_in_line('1', '对方', '333')
            self.type_to_bank_bill_inputs_in_line('1', '摘要', '333')
            self.type_to_bank_bill_inputs_in_line('1', '收入', '333')
            self.type_to_bank_bill_inputs_in_line('1', '余额', '333')
        with allure.step('保存'):
            self.click_bank_bill_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        for _ in [fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230717-032-001.xls',
                  fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230717-032-002.xls',
                  fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230717-032-003.xls']:
            with allure.step('导入银行对账单'):
                self.click_bank_bill_buttons('导入')
                self.click_bank_bill_import_type_by_value(1)
                self.choose_file_to_select_file(_)
                self.click_select_bank('标准导入')
                self.click_select_subject('银行存款')
                self.click_import_bank_bill_radio('1')
                self.click_import_bank_bill_conform_button()
                # with allure.step('自定义模板配置'):
                #     self.switch_to_bank_bill_standard_import_config_iframe()
                #     self.click_bank_bill_standard_import_config_tips()
                #     # self.click_bank_bill_standard_import_config_auto_button()
                #     self.click_bank_bill_standard_import_config_radios('收入支出分两列区分')
                #     self.switch_to_default_content()
                #     self.switch_to_bank_bill_frame()
                self.click_accounting_focus_table_buttons('导入')
                # self.switch_to_bank_bill_standard_import_config_iframe()
                # self.click_accounting_focus_table_buttons('确认并导入')
                assert '导入成功' in self.get_all_floating_tip()
                self.switch_to_default_content()
                self.switch_to_bank_bill_frame()
        assert self.get_text_from_bank_bill_total_num() == '37'

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230718-037')
    @allure.title('银行对账单生成凭证带出的余额错误')
    def test_manually_generate_voucher_wrong_balance(self):
        company = GetYamlData().get_company('proj_R20230718-037')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-05-26', '2023-05-26')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('删除已生成的凭证'):
            if self.is_element_visible(self.bank_bill_voucher_link_by_voucher_number('2023-05_记112')):
                self.click_bank_bill_voucher_link_by_voucher_number('2023-05_记112')
                self.switch_to_default_content()
                self.switch_to_voucher_detail_frame()
                self.click_buttons('delete')
                self.click_accounting_focus_table_buttons('确定')
                assert '共删除1张凭证' in self.get_all_floating_tip()
                self.switch_to_default_content()
                self.switch_to_bank_bill_frame()
                self.click_refresh()
        with allure.step('重新生成凭证'):
            summary = '厂家退维C底价加税'
            self.click_bank_bill_generate_voucher_button_by_summary(summary)
            self.switch_to_default_content()
            self.switch_to_voucher_frame()
            self.wait(2)
            self.select_voucher_entry_subject_by_idx('2', '1221001 其他应收款_保证金')
            self.voucher_details_select_sub_account_by_label('客户', '020 深圳朗欧医药集团有限公司')
            assert '34024.16' == self.get_text_from_voucher_entry_current_balance(2)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-银行')
    def test_bank_bill_list_sort_by_bank(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '银行'
            assert '华夏银行' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '标准导入' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '标准导入' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '建设银行' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '建设银行' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '标准导入' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '华夏银行' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '标准导入' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)

    @pytest.mark.p1
    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-交易日期')
    def test_bank_bill_list_sort_by_date(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '交易日期'
            assert '2023-01-01' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '2023-01-23' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '2023-01-23' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '2023-01-01' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '2023-01-01' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '2023-01-23' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-对方')
    def test_bank_bill_list_sort_by_counterparties(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '对方'
            assert 'test001' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert 'test023' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert 'test01' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert 'test001' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert 'test023' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert 'test01' == self.get_text_from_bank_bill_table_row_input_values_by_class('10', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert 'test023' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert 'test001' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert 'test001' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert 'test023' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert 'test01' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-摘要')
    def test_bank_bill_list_sort_by_summary(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '摘要'
            assert '开帐户使用01a' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '开帐户使用23a' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert 'test211' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert 'test211' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '开帐户使用d18a' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '开帐户使用01a' == self.get_text_from_bank_bill_table_row_input_values_by_class('2', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '开帐户使用d18a' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert 'test211' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '开帐户使用01a' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '开帐户使用23a' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert 'test211' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-收入')
    def test_bank_bill_list_sort_by_income(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '收入'
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '4821' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '50000' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('16', sort_name)
            assert '50000' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '50000' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('9', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '4821' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '50000' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-支出')
    def test_bank_bill_list_sort_by_outcome(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '支出'
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '212' == self.get_text_from_bank_bill_table_row_input_values_by_class('4', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '15' == self.get_text_from_bank_bill_table_row_input_values_by_class('10', sort_name)
            assert '5654' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '5654' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '15' == self.get_text_from_bank_bill_table_row_input_values_by_class('15', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '212' == self.get_text_from_bank_bill_table_row_input_values_by_class('4', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-余额')
    def test_bank_bill_list_sort_by_amount(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '余额'
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '1817' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '-233' == self.get_text_from_bank_bill_table_row_input_values_by_class('6', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '-5578' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '300000' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '76' == self.get_text_from_bank_bill_table_row_input_values_by_class('11', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '300000' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '-5578' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '-233' == self.get_text_from_bank_bill_table_row_input_values_by_class('15', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '300' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '1817' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '-233' == self.get_text_from_bank_bill_table_row_input_values_by_class('6', sort_name)

    @allure.tag('R20230804-019')
    @allure.title('银行对账单排序-交易备注')
    def test_bank_bill_list_sort_by_memo(self):
        company = GetYamlData().get_company('proj_R20230804-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.type_date('2023-01-01', '2023-01-31')
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '交易备注'
            assert '排序01测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '排序23测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert ' ' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert ' ' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '排序23测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '排序01测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('2', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '排序23测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert ' ' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert '排序01测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('23', sort_name)
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '排序01测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', sort_name)
            assert '排序23测试' == self.get_text_from_bank_bill_table_row_input_values_by_class('24', sort_name)
            assert ' ' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', sort_name)

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230915-037')
    @allure.title('银行对账单排序-凭证号')
    def test_bank_bill_list_sort_by_voucher_num(self):
        company = GetYamlData().get_company('proj_R20230915-037')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.clear_date()
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('排序'):
            sort_name = '凭证'
            assert '生成凭证' == self.get_text_from_bank_bill_table_voucher_num_value('1')
            assert '2023-07_记62' == self.get_text_from_bank_bill_table_voucher_num_value('9')
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '生成凭证' == self.get_text_from_bank_bill_table_voucher_num_value('1')
            assert '2023-07_记1' == self.get_text_from_bank_bill_table_voucher_num_value('9')
            assert '2023-07_记89' == self.get_text_from_bank_bill_table_voucher_num_value('96')
            assert '2023-07_转1' == self.get_text_from_bank_bill_table_voucher_num_value('97')
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '生成凭证' == self.get_text_from_bank_bill_table_voucher_num_value('97')
            assert '2023-07_记1' == self.get_text_from_bank_bill_table_voucher_num_value('89')
            assert '2023-07_记89' == self.get_text_from_bank_bill_table_voucher_num_value('2')
            assert '2023-07_转1' == self.get_text_from_bank_bill_table_voucher_num_value('1')
            self.click_bank_bill_table_head_sort_div_by_name(sort_name)
            assert '生成凭证' == self.get_text_from_bank_bill_table_voucher_num_value('1')
            assert '2023-07_记62' == self.get_text_from_bank_bill_table_voucher_num_value('9')

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230915-037')
    @allure.title('银行对账单凭证字过滤')
    def test_bank_bill_list_filter_by_voucher_type(self):
        company = GetYamlData().get_company('proj_R20230915-037')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.clear_date()
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('过滤凭证字'):
            self.click_bank_bill_buttons('更多...')
            self.click_bank_bill_filter_div_inputs_by_id('凭证字')
            self.click_bank_bill_filter_div_dropdown_items_by_label('凭证字', '转')
            self.click_bank_bill_filter_div_buttons_by_id('查询')
            assert self.get_text_from_bank_bill_total_num() == '1'

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230915-037')
    @allure.title('银行对账单凭证号过滤')
    def test_bank_bill_list_filter_by_voucher_num(self):
        company = GetYamlData().get_company('proj_R20230915-037')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤日期'):
            self.clear_date()
            self.bank_bill_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('过滤凭证字'):
            self.click_bank_bill_buttons('更多...')
            self.type_to_bank_bill_filter_div_inputs_by_id('凭证号', '1,7,9-22')
            self.click_bank_bill_filter_div_buttons_by_id('查询')
            assert self.get_text_from_bank_bill_total_num() == '17'

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230928-024')
    @allure.title('导入银行对账单-标准导入-对方名称含有空格')
    def test_bank_bill_import_cell_contains_blank(self):
        company = GetYamlData().get_company('proj_R20230928-024')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤日期'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入银行对账单'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(1)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230928-024.xlsx')
            self.click_select_bank('标准导入')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('1')
            self.click_import_bank_bill_conform_button()
        with allure.step('确认导入'):
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
        with allure.step('检查导入结果'):
            row_name = '对方'
            assert '开帐户使用0001' == self.get_text_from_bank_bill_table_row_input_values_by_class('1', row_name)
            assert 'test coconut latte' == self.get_text_from_bank_bill_table_row_input_values_by_class('3', row_name)

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230926-031')
    @allure.title('导入银行对账单-常熟农商银行-新增-pdf')
    def test_import_bank_bill_crcb_add_pdf(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_063')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.switch_bank_bill_page_size()
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230926-031.pdf')
            # self.click_select_bank('常熟农商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '150'

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230926-031')
    @allure.title('导入银行对账单-农业银行-新增-pdf')
    def test_import_bank_bill_abc_add_pdf(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_064')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.switch_bank_bill_page_size()
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20230925-026.pdf')
            # self.click_select_bank('农业银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '89'

    @allure.tag('【管家】2023-11-17')
    @allure.tag('R20231020-012')
    @allure.tag('R20231009-008')
    @allure.title('导入招商银行对账单报 multiple points')
    def test_import_bank_bill_cmb_multiple_points(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_065')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
            self.close_popup()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        with allure.step('清空银行对账单'):
            if self.get_text_from_bank_bill_total_num() != '0':
                self.switch_bank_bill_page_size()
                self.click_bank_bill_select_all()
                self.click_bank_bill_white_dropdown_buttons('更多')
                self.click_bank_bill_white_dropdown_items('更多', '删除')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_bank_bill_buttons('导入')
            self.click_bank_bill_import_type_by_value(0)
            self.choose_file_to_select_file(
                fr'{get_project_path()}/template/accounting/smart_bookkeeping/R20231020-012.pdf')
            # self.click_select_bank('招商银行')
            self.click_select_subject('银行存款')
            self.click_import_bank_bill_radio('0')
            self.click_import_bank_bill_conform_button()
            self.click_accounting_focus_table_buttons('导入')
            assert '导入成功' in self.get_all_floating_tip()
            assert self.get_text_from_bank_bill_total_num() == '17'

    @pytest.mark.api_accounting_smart_bookkeeping_bank_bill_pdf_parse
    @allure.title('加密pdf导入')
    def test_bank_bill_import_encrypted_pdf(self):
        db = ConnectDB()
        link_id = db.query_all_id_with_password()
        result_list = []
        expected_result = []
        for _ in link_id:
            expected_result.append(db.query_expected_data_by_id(_))
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_066')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '银行对账单')
            self.switch_to_bank_bill_frame()
        with allure.step('过滤银行对账单'):
            self.clear_date()
            self.click_refresh()
        for i, _ in enumerate(link_id):
            with allure.step('获取pdf文件列表'):
                pdf_link = db.query_link_by_id(_)
            with allure.step('获取pdf文件'):
                PageApiDownload.page_api_download(pdf_link)
                filename = pdf_link.split('/')[-1]
                password = db.query_bank_pdf_password(_)
            with allure.step('清空银行对账单'):
                if self.get_text_from_bank_bill_total_num() != '0':
                    self.switch_bank_bill_page_size()
                    self.click_bank_bill_select_all()
                    self.click_bank_bill_white_dropdown_buttons('更多')
                    self.click_bank_bill_white_dropdown_items('更多', '删除')
                    assert '删除成功' in self.get_all_floating_tip()
            with allure.step('导入'):
                self.click_bank_bill_buttons('导入')
                self.click_bank_bill_import_type_by_value(0)
                self.choose_file_to_select_file(
                    fr'{get_project_path()}/download_tmp/{filename}')
                self.click_select_subject('银行存款')
                self.click_import_bank_bill_radio('0')
                self.click_import_bank_bill_conform_button()
                self.type_to_bank_bill_password_input(password)
                self.click_bank_bill_password_conform_button()
                try:
                    result_list.append(expected_result[i] == self.get_text_from_bank_bill_import_result())
                    self.click_accounting_focus_table_buttons('导入')
                    assert '导入成功' in self.get_all_floating_tip()
                except NoSuchElementException:
                    result_list.append(False)
        with allure.step('结果比对'):
            if not all(result_list):
                fail_list = []
                for i, _ in enumerate(result_list):
                    if not _:
                        fail_list.append(link_id[i])
                raise Exception(f'文件id: {fail_list} 解析失败')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_smart_bookkeeping
@pytest.mark.accounting_smart_bookkeeping_income_invoice
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('进项票')
class TestIncomeInvoice(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    IncomeInvoicePage,
    AccountingCommonPage,
    LookupVoucherPage,
    CustomerPage,
    SettingsInvoiceVoucherTemplatePage
):
    @allure.tag('【管家】12月项目')
    @allure.tag('R20231122-030')
    @allure.title('进项发票发票来源中移除智能取票')
    def test_income_remove_item(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多'):
            self.click_income_invoice_more_button()
            self.click_income_invoice_filters_input_source()
            assert self.is_income_invoice_filters_input_drop_down_items_present('云取票')
            assert not self.is_income_invoice_filters_input_drop_down_items_present('智能取票')

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230807-026')
    @allure.title('导出发票的票据类型为空')
    def test_export_file_empty_invoice_type_in(self):
        company = GetYamlData().get_company('proj_R20230807-026')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
            self.clear_date()
            self.income_invoice_input_select_drop_down_item('记账状态', '全部')
            self.click_refresh()
        with allure.step('导出列表'):
            self.click_income_invoice_white_dropdown_button('更多', '导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\R20230807-026-in-2.xls',
                             f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('下载导入模板')
    def test_verify_download_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('下载导入模板'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.click_income_invoice_download_standard_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            check_excel_diff(f'{get_project_path()}\\template\\accounting\\smart_bookkeeping\\进项发票标准模板.xlsx',
                             f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @pytest.mark.p1
    @allure.title('列表指定凭证模板')
    def test_specified_voucher_template_by_list(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('列表指定凭证模板'):
            self.specified_voucher_template_by_list('88880011',
                                                    random_choice_in_list(VOUCHER_TEMPLATE))
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('列表生成凭证-非明细科目')
    def test_generate_voucher_by_list_empty_goods(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('列表生成凭证'):
            self.generate_voucher_by_list('88880012')
            assert '对应系统商品为空，请先匹配系统商品或生成系统商品' in self.get_all_floating_tip()

    # @pytest.mark.p1
    @allure.title('列表生成凭证')
    def test_generate_voucher_by_list(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('88880013'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('88880013')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('列表指定凭证模板'):
            self.specified_voucher_template_by_list('88880013', VOUCHER_TEMPLATE[0])
            assert '指定成功' in self.get_all_floating_tip()
        with allure.step('列表生成凭证'):
            self.generate_voucher_by_list('88880013')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('88880013')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('菜单指定凭证模板-单张')
    def test_specified_voucher_template_by_menu(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('菜单指定凭证模板'):
            self.click_list_checkbox('88880014')
            self.specified_voucher_template_by_menu(random_choice_in_list(VOUCHER_TEMPLATE))
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('菜单指定凭证模板-多张')
    def test_specified_multiple_voucher_template_by_menu(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('同步凭证模板'):
            with allure.step('点击会计菜单'):
                self.click_accounting_data_menu('设置', '票据凭证模版')
                self.switch_to_settings_invoice_voucher_template_frame()
            with allure.step('同步最新模板'):
                self.click_settings_invoice_voucher_template_buttons('同步最新模板')
                self.click_settings_invoice_voucher_template_sync_radio(1)
                self.click_settings_invoice_voucher_template_sync_save_button()
                assert '保存成功' in self.get_all_floating_tip()
                self.switch_default_frame()
                self.close_top_tabs('票据凭证模版')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('菜单指定凭证模板'):
            invoice_list = ['88880022', '88880024']
            self.click_multiple_list_checkbox(invoice_list)
            self.specified_voucher_template_by_menu(random_choice_in_list(VOUCHER_TEMPLATE))
            assert '指定成功' in self.get_all_floating_tip()

    @allure.title('菜单指定凭证模板-未勾选')
    def test_specified_voucher_template_by_menu_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('菜单指定凭证模板'):
            self.click_income_invoice_buttons('指定凭证模板')
            assert '请选择需要指定项' in self.get_all_floating_tip()

    @allure.title('清除指定凭证模板-单张')
    def test_clear_specified_voucher_template_by_menu(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('清除指定凭证模板'):
            self.click_list_checkbox('88880015')
            self.clear_voucher_template_by_menu()
            assert '清除成功，共清除1条记录' in self.get_all_floating_tip()

    @allure.title('清除指定凭证模板-多张')
    def test_clear_specified_multiple_voucher_template_by_menu(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('菜单指定凭证模板'):
            invoice_list = ['88880025', '88880026']
            self.click_multiple_list_checkbox(invoice_list)
            self.clear_voucher_template_by_menu()
            assert '清除成功，共清除2条记录' in self.get_all_floating_tip()

    @allure.title('匹配系统商品-未勾选')
    def test_match_system_goods_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('匹配系统商品'):
            self.click_dropdown_button(1)
            self.uncheck_system_goods_dropdown_item()
            self.click_income_invoice_buttons('匹配系统商品')
            assert '请选择匹配项' in self.get_all_floating_tip()

    @allure.title('匹配系统商品-无需匹配')
    def test_match_system_goods_unnecessary(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('匹配系统商品'):
            self.click_dropdown_button(1)
            self.check_system_goods_dropdown_item()
            self.click_income_invoice_buttons('匹配系统商品')
            assert '无需匹配系统商品' in self.get_all_floating_tip()
            self.click_dropdown_button(1)
            self.uncheck_system_goods_dropdown_item()

    @allure.title('更多-保存')
    def test_more_save(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-保存'):
            self.click_income_invoice_white_dropdown_button('更多', '保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('更多-获取商品及对方-未勾选')
    def test_more_get_goods_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-获取商品及对方'):
            self.click_income_invoice_white_dropdown_button('更多', '获取商品及对方')
            assert '请选择获取项' in self.get_all_floating_tip()

    @allure.title('更多-标记已认证-未勾选')
    def test_more_mark_certified_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记已认证'):
            self.click_income_invoice_white_dropdown_button('更多', '标记已认证')
            assert '请选择发票记录' in self.get_all_floating_tip()

    @allure.title('更多-标记已认证')
    def test_more_mark_certified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记已认证'):
            self.click_list_checkbox('88880016')
            self.click_income_invoice_white_dropdown_button('更多', '标记已认证')
            assert self.is_certified_message_visible('4224.43')
            self.click_conform_certified_buttons()
            assert '标记已认证成功' in self.get_all_floating_tip()

    @allure.title('更多-标记已认证-多张')
    def test_more_multiple_mark_certified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记已认证'):
            invoice_list = ['88880018', '88880019']
            self.click_multiple_list_checkbox(invoice_list)
            self.click_income_invoice_white_dropdown_button('更多', '标记已认证')
            assert self.is_certified_message_visible('8448.86')
            self.click_conform_certified_buttons()
            assert '标记已认证成功' in self.get_all_floating_tip()

    @allure.title('更多-标记未认证-未勾选')
    def test_more_mark_not_certified_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记未认证'):
            self.click_income_invoice_white_dropdown_button('更多', '标记未认证')
            assert '请选择发票记录' in self.get_all_floating_tip()

    @allure.title('更多-标记未认证')
    def test_more_mark_not_certified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记已认证'):
            self.click_list_checkbox('88880017')
            self.click_income_invoice_white_dropdown_button('更多', '标记未认证')
            assert self.is_certified_message_visible('4224.43')
            self.click_conform_certified_buttons()
            assert '标记未认证成功' in self.get_all_floating_tip()

    @allure.title('更多-标记未认证-多张')
    def test_more_multiple_mark_not_certified(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记未认证'):
            invoice_list = ['88880020', '88880021']
            self.click_multiple_list_checkbox(invoice_list)
            self.click_income_invoice_white_dropdown_button('更多', '标记未认证')
            assert self.is_certified_message_visible('8448.86')
            self.click_conform_certified_buttons()
            assert '标记未认证成功' in self.get_all_floating_tip()

    @allure.title('更多-删除-未勾选')
    def test_delete_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('更多-标记未认证'):
            self.click_income_invoice_white_dropdown_button('更多', '删除')
            assert '请选择删除项' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-未勾选')
    def test_generate_voucher_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('按单生成凭证'):
            self.click_income_invoice_buttons('按单生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-已存在凭证')
    def test_generate_voucher_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('按单生成凭证'):
            self.query_account_status('全部')
            self.click_list_checkbox('88880027')
            self.click_income_invoice_buttons('按单生成凭证')
            assert '该记录已生成凭证' in self.get_all_floating_tip()

    @allure.title('凭证联查')
    def test_voucher_link(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('单据过滤'):
            self.query_account_status('全部')
            self.click_list_link_to_voucher_details('88880027')
        with allure.step('联查凭证'):
            self.switch_to_default_content()
            self.switch_to_voucher_detail_frame()
            assert self.is_voucher_entry_visible('88880027')

    @allure.title('按单生成凭证-单张')
    def test_generate_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            if self.is_voucher_exist('88880028'):
                with allure.step('删除凭证'):
                    self.click_list_voucher_checkbox('88880028')
                    self.click_voucher_buttons('删除')
                    self.click_voucher_list_conform_delete_buttons('确定')
                    assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('按单生成凭证'):
            self.query_account_status('全部')
            self.click_list_checkbox('88880028')
            self.click_income_invoice_buttons('按单生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox('88880028')
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-多张')
    def test_generate_multiple_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880029', '88880030']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('按单生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880029', '88880030']
            self.click_multiple_list_checkbox(invoice_list)
            self.click_income_invoice_buttons('按单生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(['88880029', '88880030'])
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未勾选')
    def test_generate_voucher_summary_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-已存在凭证')
    def test_generate_voucher_summary_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            self.click_list_checkbox('88880027')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '该记录已生成凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同票据类型生成一张凭证')
    def test_generate_voucher_summary_single_same_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880031']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880031']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同票据类型生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同票据类型生成一张凭证')
    def test_generate_voucher_summary_multiple_same_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880032', '88880033', '88880034']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880032', '88880033', '88880034']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同票据类型生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同票据类型相同对方生成一张凭证')
    def test_generate_voucher_summary_single_same_type_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880035']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880035']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同票据类型相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同票据类型相同对方生成一张凭证')
    def test_generate_voucher_summary_multiple_same_type_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880037', '88880038', '88880036']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880037', '88880038', '88880036']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同票据类型相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同日期生成一张凭证')
    def test_generate_voucher_summary_single_same_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880039']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880039']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期生成一张凭证')
    def test_generate_voucher_summary_multiple_same_date(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880040', '88880041', '88880042']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880040', '88880041', '88880042']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同日期相同票据类型生成一张凭证')
    def test_generate_voucher_summary_single_same_date_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880043']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880043']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期相同票据类型生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期相同票据类型生成一张凭证')
    def test_generate_voucher_summary_multiple_same_date_type(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880044', '88880045', '88880046']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880044', '88880045', '88880046']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期相同票据类型生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成3张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除3张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同日期相同对方生成一张凭证')
    def test_generate_voucher_summary_single_same_date_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880047']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880047']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同日期相同对方生成一张凭证')
    def test_generate_voucher_summary_multiple_same_date_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880048', '88880049', '88880050']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880048', '88880049', '88880050']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同日期相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成3张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除3张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-相同对方生成一张凭证')
    def test_generate_voucher_summary_single_same_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880051']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880051']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-相同对方生成一张凭证')
    def test_generate_voucher_summary_multiple_same_counterparties(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880052', '88880053', '88880054']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880052', '88880053', '88880054']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成2张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除2张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-单张-全部汇总生成一张凭证')
    def test_generate_voucher_summary_single_all_in_one(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880055']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880055']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('相同对方生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-多张-全部汇总生成一张凭证')
    def test_generate_voucher_summary_multiple_all_in_one(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = ['88880056', '88880057']
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('汇总生成凭证'):
            self.query_account_status('全部')
            invoice_list = ['88880056', '88880057']
            self.click_multiple_list_checkbox(invoice_list)
            self.set_generate_voucher_summary_setting('全部汇总生成一张凭证')
            self.click_income_invoice_buttons('汇总生成凭证')
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_multiple_voucher_checkbox(invoice_list)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('导入-一般纳税人显示认证清单')
    def test_verify_normal_taxpayer_radio(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('检查认证清单选项'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            assert self.is_type_radio_visible('2')

    @allure.title('导入-认证清单-流程指引')
    def test_verify_normal_taxpayer_image(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('检查认证清单图片'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('2')
            self.click_import_type_img_button()
            assert self.is_import_img_visible()
            self.click_import_type_img_close_button()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230531-009')
    @allure.title('导入-认证清单-流程指引-2')
    def test_verify_normal_taxpayer_image_2(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('检查认证清单图片'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('2')
            self.click_import_type_img_button_2()
            assert self.is_import_img_visible()
            self.click_import_type_img_close_button()

    @allure.title('导入-认证清单-错误文件')
    def test_import_normal_taxpayer_list_error(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('2')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入-错误.xlsx'
            )
            self.click_income_invoice_import_button()
            assert '导入失败，非认证清单文件，请按照导出路径导出认证清单' in self.get_all_floating_tip()

    @allure.title('导入-认证清单')
    def test_import_normal_taxpayer_list(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('检查数据是否存在'):
            invoice_list = ['49597493', '22152000000000065670']
            for _ in invoice_list:
                if self.is_checkbox_exist(_):
                    with allure.step('删除数据'):
                        self.click_list_checkbox(_)
                        self.click_income_invoice_white_dropdown_button('更多', '删除')
                        assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('2')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入.xlsx')
            self.click_income_invoice_import_button()
            self.close_import_result()
            self.click_refresh()
        with allure.step('数据还原'):
            invoice_list = ['49597493', '22152000000000065670']
            self.click_multiple_list_checkbox(invoice_list)
            self.click_income_invoice_white_dropdown_button('更多', '删除')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230721-012')
    @allure.title('导入发票无法获取商品明细')
    def test_import_invoice_cant_get_details(self):
        company = GetYamlData().get_company('proj_R20230721-012')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('过滤数据'):
            self.clear_date()
        with allure.step('检查数据是否存在'):
            invoice_list = ['15674862']
            for _ in invoice_list:
                if self.is_checkbox_exist(_):
                    with allure.step('删除数据'):
                        self.click_list_checkbox(_)
                        self.click_income_invoice_white_dropdown_button('更多', '删除')
                        assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230721-012.xlsx')
            self.click_income_invoice_import_button()
        #     self.close_import_result()
        #     self.click_refresh()
        # with allure.step('数据还原'):
        #     self.click_multiple_list_checkbox(invoice_list)
        #     self.click_income_invoice_white_dropdown_button('更多', '删除')
        #     assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入-小规模纳税人不显示认证清单')
    def test_verify_small_taxpayer_radio(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_009')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('检查认证清单选项'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            assert not self.is_type_radio_visible('2')

    @allure.title('导入-按进项票模板导入-未选择文件-新增导入')
    def test_import_template_unselect_file_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('0')
            self.click_income_invoice_import_button()
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.title('导入-按进项票模板导入-未指定参数-新增导入')
    def test_import_template_unselect_parameter_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('0')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入.xlsx')
            self.click_income_invoice_import_button()
            assert '参数不能为空' in self.get_all_floating_tip()

    @allure.title('导入-按进项票模板导入-未选择文件-覆盖导入')
    def test_import_template_unselect_file_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('1')
            self.click_income_invoice_import_button()
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.title('导入-按进项票模板导入-未指定参数-覆盖导入')
    def test_import_template_unselect_parameter_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入.xlsx')
            self.click_income_invoice_import_button()
            assert '参数不能为空' in self.get_all_floating_tip()

    @allure.title('导入-按进项票模板导入-指定错误参数-新增导入')
    def test_import_template_wrong_parameter_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('0')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入.xlsx')
            self.select_import_param('进项:航信:XML')
            self.click_income_invoice_import_button()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.title('导入-按进项票模板导入-指定错误参数-覆盖导入')
    def test_import_template_wrong_parameter_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('0')
            self.click_import_method_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项票-认证清单导入.xlsx')
            self.select_import_param('进项:航信:XML')
            self.click_income_invoice_import_button()
            assert '格式和模板类型不一致,请核实' in self.get_all_floating_tip()

    @allure.title('导入-按标准模板导入-未选择文件-新增导入')
    def test_import_standard_template_unselect_file_add(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.click_import_method_radio('0')
            self.click_income_invoice_import_button()
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.title('导入-按标准模板导入-未选择文件-覆盖导入')
    def test_import_standard_template_unselect_file_new(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.click_import_method_radio('1')
            self.click_income_invoice_import_button()
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-09-28')
    @allure.tag('R20230830-032')
    @allure.title('标准模板导入进项发票-商品名称过长')
    def test_import_standard_template_product_details_too_long(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20230830-032.xlsx'
            )
            self.click_import_method_radio('1')
            self.click_income_invoice_import_button()
            assert '导入失败，导入文件1行, 商品名称列过长, 请检查!' in self.get_all_floating_tip()

    @allure.tag('【管家】12月项目')
    @allure.tag('R20231115-057')
    @allure.title('标准模板导入全电发票增加税额校验')
    def test_import_standard_template_add_tax_value(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_010')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\R20231115-057.xlsx'
            )
            self.click_import_method_radio('1')
            self.click_income_invoice_import_button()
            assert '导入的全电票【税额】列未设置，请检查发票导入文件或模板' in self.get_all_floating_tip()

    @allure.tag('R20230706-009')
    @allure.title('导入-按标准模板导入-对方名称发生变化')
    def test_import_standard_template_name_change(self):
        company_name = '湖南广林电子有限公司湖北分公司'
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('检查客户是否存在'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
            self.search_customer(company_name)
            if self.is_element_visible(self.customer_table_checkbox(company_name)):
                self.click_customer_table_checkbox(company_name)
                self.click_dropdown_buttons('更多', '删除')
                self.click_delete_customer_button('删除')
                assert '删除客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')

        with allure.step('创建客户'):
            self.click_manager_menu('代账服务', '服务管理')
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(company_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2023')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('6')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('小企业会计准则（2013年版）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert company_name == self.get_company_name()

        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('导入'):
            self.click_income_invoice_white_dropdown_button('智能采集', '导入')
            self.click_import_type_radio('1')
            self.send_filepath_to_input(
                rf'{get_project_path()}\template\accounting\smart_bookkeeping\进项发票标准模板-R20230706-009.xlsx')
            self.click_income_invoice_import_button()
            self.click_close_get_invoice_details_button()
            self.click_refresh()
            assert '湖南广林电子有限公司' == self.get_text_from_list_specified_company_name('05358432')

            self.driver.close()
            self.switch_to_window(ori_window)
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230805-007')
    @allure.title('进项发票生成不了凭证')
    def test_income_invoice_cant_generate_voucher(self):
        company = GetYamlData().get_company('proj_R20230805-007')
        invoice_num = '17402822'
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('检查凭证是否存在'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            voucher_list = [invoice_num]
            for _ in voucher_list:
                if self.is_voucher_exist(_):
                    with allure.step('删除凭证'):
                        self.click_list_voucher_checkbox(_)
                        self.click_voucher_buttons('删除')
                        self.click_voucher_list_conform_delete_buttons('确定')
                        assert '共删除1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
            self.close_top_tabs('查凭证')
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '进项票')
            self.switch_to_bill_income_frame()
        with allure.step('列表生成凭证'):
            self.generate_voucher_by_list(invoice_num)
            assert '生成凭证成功，共生成1张凭证' in self.get_all_floating_tip()
            self.switch_default_frame()
        with allure.step('打开查凭证菜单'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
        with allure.step('检查生成结果'):
            self.click_list_voucher_checkbox(invoice_num)
        with allure.step('删除凭证'):
            self.click_voucher_buttons('删除')
            self.click_voucher_list_conform_delete_buttons('确定')
            assert '共删除1张凭证' in self.get_all_floating_tip()

    # @allure.tag('【管家】2023-12-18')
    # @allure.tag('R20231108-041')
    # @allure.title('分录行超过2万自动切换10条/页')
    # def test_income_invoice_cant_generate_voucher(self):
    #     company = GetYamlData().get_company('proj_R20231103-045')
    #     with allure.step('登录'):
    #         self.login(company=company)
    #     with allure.step('点击会计菜单'):
    #         self.click_accounting_menu('智能记账', '进项票')
    #         self.switch_to_bill_income_frame()
    #         self.wait(5)
    #     with allure.step('过滤日期'):
    #         self.clear_date()
    #         self.refresh()
    #         self.wait(5)
    #     with allure.step('切换每页行数'):
    #         self.change_page_size('100条/页')
    #         self.wait(3)
    #         assert '发票分录超过2万行，自动切换至10条/页' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_smart_bookkeeping
@pytest.mark.accounting_smart_bookkeeping_cost
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('费用票')
class TestCostInvoice(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    CostInvoicePage
):
    @allure.title('保存费用票-无改动')
    def test_save_cost_invoice_no_change(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('保存'):
            self.click_cost_invoice_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('删除费用票-未勾选')
    def test_delete_cost_invoice_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('删除'):
            self.click_cost_invoice_buttons('删除')
            assert '请选择删除项' in self.get_all_floating_tip()

    @allure.title('指定凭证模板-未勾选')
    def test_specified_cost_invoice_voucher_template_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('指定凭证模板'):
            self.click_cost_invoice_buttons('指定凭证模板')
            assert '请选择需要指定项' in self.get_all_floating_tip()

    @allure.title('指定凭证模板-未保存')
    def test_specified_cost_invoice_voucher_template_unsaved(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('编辑发票行'):
            self.type_to_cost_invoice_table_input_by_line_num('1', '对方', 'test')
        with allure.step('指定凭证模板'):
            self.click_cost_invoice_buttons('指定凭证模板')
            assert '请先保存数据' in self.get_all_floating_tip()

    @allure.title('按单生成凭证-未勾选')
    def test_cost_invoice_voucher_generate_single_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('按单生成凭证'):
            self.click_cost_invoice_buttons('按单生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    @allure.title('汇总生成凭证-未勾选')
    def test_cost_invoice_voucher_generate_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('汇总生成凭证'):
            self.click_cost_invoice_buttons('汇总生成凭证')
            assert '请选择需要生成项' in self.get_all_floating_tip()

    @allure.title('列表生成凭证-无信息')
    def test_cost_invoice_voucher_generate_in_table_untyped(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('列表生成凭证'):
            self.click_cost_invoice_table_operate_buttons_by_line_num('1', '生成凭证')
            assert '无需生成凭证' in self.get_all_floating_tip()

    @allure.title('列表生成凭证-未保存')
    def test_cost_invoice_voucher_generate_in_table_unsaved(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('编辑发票行'):
            self.type_to_cost_invoice_table_input_by_line_num('1', '对方', 'test')
            self.type_to_cost_invoice_table_input_by_line_num('1', '金额', '3')
            self.type_to_cost_invoice_table_input_by_line_num('1', '税额', '1')
            self.type_to_cost_invoice_table_input_by_line_num('1', '备注', 'test')
        with allure.step('列表生成凭证'):
            self.click_cost_invoice_table_operate_buttons_by_line_num('1', '生成凭证')
            assert '请先保存数据' in self.get_all_floating_tip()

    @allure.title('列表录入金额税额自动计算价税合计')
    def test_cost_invoice_type_amount_to_table_cal_total(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('编辑发票行'):
            self.type_to_cost_invoice_table_input_by_line_num('1', '金额', '3')
            self.type_to_cost_invoice_table_input_by_line_num('1', '税额', '1')
            self.type_to_cost_invoice_table_input_by_line_num('1', '备注', 'test')
            assert '4' == self.get_text_from_cost_invoice_table_input_by_line_num('1', '价税合计')

    @allure.title('列表录入价税合计和税额自动计算金额')
    def test_cost_invoice_type_amount_to_table_cal_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('智能记账', '费用票')
            self.switch_to_cost_invoice_page()
        with allure.step('编辑发票行'):
            self.type_to_cost_invoice_table_input_by_line_num('1', '税额', '1')
            self.type_to_cost_invoice_table_input_by_line_num('1', '价税合计', '3')
            self.type_to_cost_invoice_table_input_by_line_num('1', '备注', 'test')
            assert '2' == self.get_text_from_cost_invoice_table_input_by_line_num('1', '金额')
