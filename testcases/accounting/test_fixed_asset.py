import allure
import pytest

from page.manager.page_agency import AgencyAccountPage
from page.manager.page_common import ManagerCommonPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.accounting.page_home import AccountingHomePage
from page.accounting.page_fixed_asset import (FixedAssetClassPage,
                                              FixedAssetCardPage,
                                              FixedAssetAddCardPage,
                                              FixedAssetDepreciationSummaryPage,
                                              FixedAssetDepreciationDetailPage,
                                              FixedAssetModifyCardPage)
from page.accounting.page_common import AccountingCommonPage
from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.accounting
@pytest.mark.accounting_fixed_asset
@pytest.mark.accounting_fixed_asset_class
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('资产类别')
class TestFixedAssetClass(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    FixedAssetClassPage,
    FixedAssetCardPage,
    FixedAssetAddCardPage,
    FixedAssetDepreciationSummaryPage,
    FixedAssetDepreciationDetailPage,
    FixedAssetModifyCardPage,
    AccountingCommonPage
):

    @allure.title('新增并删除类别')
    def test_add_and_delete_class(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
            assert '新增资产类别成功' in self.get_all_floating_tip()
            self.click_add_class_buttons('关闭')
        with allure.step('还原数据'):
            self.click_checkbox_in_line_by_num(num)
            self.click_class_buttons('删除')
            self.click_add_class_buttons('确定')
            assert '资产类别删除成功' in self.get_all_floating_tip()

    @allure.title('新增并删除类别-表格行')
    def test_add_and_delete_class_in_line(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
            assert '新增资产类别成功' in self.get_all_floating_tip()
            self.click_add_class_buttons('关闭')
        with allure.step('还原数据'):
            self.click_buttons_in_line_by_num(num, '删除')
            self.click_add_class_buttons('确定')
            assert '资产类别删除成功' in self.get_all_floating_tip()

    @allure.title('新增类别-字段必录校验-类别编码')
    def test_verify_class_num(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
        with allure.step('字段校验'):
            self.switch_to_add_class_frame()
            assert '不能为空' in self.get_add_class_inputs_errors('类别编码')

    @allure.title('新增类别-字段必录校验-类别编码')
    def test_verify_class_name(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
        with allure.step('字段校验'):
            self.switch_to_add_class_frame()
            assert '不能为空' in self.get_add_class_inputs_errors('类别名称')

    @allure.title('新增类别-字段必录校验-预计使用年限')
    def test_verify_estimated_useful_life(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
        with allure.step('字段校验'):
            self.switch_to_add_class_frame()
            assert '不能为空' in self.get_add_class_inputs_errors('预计使用年限')

    @allure.title('新增类别-字段必录校验-预计净残值率')
    def test_verify_salvage_rate(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = random_string_generator()
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
        with allure.step('字段校验'):
            self.switch_to_add_class_frame()
            assert '不能为空' in self.get_add_class_inputs_errors('预计净残值率')

    @allure.title('新增类别-字段重复校验-类别编码')
    def test_verify_class_number_exist(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('新增资产类别'):
            self.click_class_buttons('新增')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            num = '001'
            self.type_add_class_inputs('类别编码', num)
            self.type_add_class_inputs('类别名称', num)
            self.type_add_class_inputs('预计使用年限', '10')
            self.type_add_class_inputs('预计净残值率', '5')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('保存')
        with allure.step('字段校验'):
            assert '新增资产类别失败！001已存在！' in self.get_all_floating_tip()

    @allure.title('修改类别')
    def test_modify_class(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '资产类别')
            self.switch_to_fixed_asset_class_frame()
        with allure.step('修改资产类别'):
            self.click_buttons_in_line_by_num('002', '修改')
            self.switch_to_add_class_frame()
        with allure.step('录入资产类别信息'):
            self.type_add_class_inputs('类别编码', '002')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_class_frame()
            self.click_add_class_buttons('确定')
        with allure.step('修改校验'):
            assert '修改资产类别成功！' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_fixed_asset
@pytest.mark.accounting_fixed_asset_card
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('卡片')
class TestFixedAssetCard(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    FixedAssetClassPage,
    FixedAssetCardPage,
    FixedAssetAddCardPage,
    FixedAssetDepreciationSummaryPage,
    FixedAssetDepreciationDetailPage,
    FixedAssetModifyCardPage,
    AccountingCommonPage
):

    @allure.title('无卡片数据')
    def test_card_empty(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
            assert '没有卡片数据哦！' in self.get_all_floating_tip()

    @allure.title('删除-未勾选')
    def test_delete_unselected(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('删除卡片'):
            self.click_card_buttons('删除')
            assert '请先选择你想要删除的卡片' in self.get_all_floating_tip()

    @allure.title('新增并删除卡片-新增页面')
    def test_add_and_delete_card_new(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.add_card(num)
            assert '新增卡片成功' in self.get_all_floating_tip()
        with allure.step('删除卡片'):
            self.click_card_buttons('删除')
            self.click_conform_buttons('确定')

    @allure.title('新增并删除卡片-列表删除')
    def test_add_and_delete_card_list(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.add_card(num)
            assert '新增卡片成功' in self.get_all_floating_tip()
        with allure.step('删除卡片'):
            self.switch_to_default_content()
            self.close_tab_by_tab_name('新增卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
            self.click_buttons_in_line_by_num(num, '删除')
            self.click_conform_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增并删除卡片-勾选删除')
    def test_add_and_delete_card_button(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.add_card(num)
            assert '新增卡片成功' in self.get_all_floating_tip()
        with allure.step('删除卡片'):
            self.switch_to_default_content()
            self.close_tab_by_tab_name('新增卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
            self.click_checkbox_in_line_by_num(num)
            self.click_card_buttons('删除')
            self.click_conform_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增卡片-必录项校验-资产编码')
    def test_add_card_verify_asset_number(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            self.click_card_buttons('保存')
            assert '资产编码不能为空' in self.get_all_floating_tip()

    @allure.title('新增卡片-必录项校验-资产名称')
    def test_add_card_verify_asset_name(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.type_add_card_input('资产编码', num)
            self.click_card_buttons('保存')
            assert '资产名称不能为空' in self.get_all_floating_tip()

    @allure.title('新增卡片-必录项校验-资产类别')
    def test_add_card_verify_asset_class(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.type_add_card_input('资产编码', num)
            self.type_add_card_input('资产名称', num)
            self.click_card_buttons('保存')
            assert '资产类别不能为空' in self.get_all_floating_tip()

    @allure.title('新增卡片-必录项校验-使用部门')
    def test_add_card_verify_asset_dep(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.type_add_card_input('资产编码', num)
            self.type_add_card_input('资产名称', num)
            self.type_add_card_input('资产类别', '001_房屋、建筑物')
            self.click_dropdown_list('001_房屋、建筑物')
            self.click_card_buttons('保存')
            assert '使用部门不能为空' in self.get_all_floating_tip()

    @allure.title('新增卡片-必录项校验-原值')
    def test_add_card_verify_asset_value(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.type_add_card_input('资产编码', num)
            self.type_add_card_input('资产名称', num)
            self.type_add_card_input('资产类别', '001_房屋、建筑物')
            self.click_dropdown_list('001_房屋、建筑物')
            self.type_add_card_input('使用部门', '研发部')
            self.click_dropdown_list('研发部')
            self.click_card_buttons('保存')
            assert '原值不能为空' in self.get_all_floating_tip()

    @allure.title('新增后复制卡片')
    def test_add_card_and_copy(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('新增卡片'):
            self.click_card_buttons('新增')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_add_card_frame()
        with allure.step('录入卡片信息'):
            num = random_string_generator()
            self.add_card(num)
            assert '新增卡片成功' in self.get_all_floating_tip()
        with allure.step('复制卡片'):
            self.click_card_buttons('复制')
            self.type_to_copy_card_input('3')
            self.click_conform_buttons('确定')
            assert '卡片复制成功' in self.get_all_floating_tip()
        with allure.step('删除卡片'):
            self.switch_to_default_content()
            self.close_tab_by_tab_name('新增卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
            self.click_all_checkbox_by_same_name(num)
            self.click_card_buttons('删除')
            self.click_conform_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('修改卡片')
    def test_modify_card(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('修改卡片'):
            self.click_buttons_in_line_by_num('test_modify', '修改')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_modify_card_frame()
            self.click_card_buttons('保存')
            assert '修改卡片成功' in self.get_all_floating_tip()

    @allure.title('清理卡片')
    def test_clear_card(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('清理卡片'):
            self.click_buttons_in_line_by_num('test_clear', '修改')
            self.switch_to_default_content()
            self.switch_to_fixed_asset_modify_card_frame()
            self.click_card_buttons('清理')
            assert '卡片清理成功' in self.get_all_floating_tip()
            self.click_card_buttons('清理')
            assert '取消卡片清理成功' in self.get_all_floating_tip()

    @allure.title('导入卡片')
    def test_import_card(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
            self.click_card_buttons('刷新')
        with allure.step('清空数据'):
            if not self.is_list_empty():
                self.click_check_all()
                self.click_card_buttons('删除')
                self.click_conform_buttons('确定')
        with allure.step('导入卡片'):
            self.click_card_buttons('导入')
            self.click_next_step_button()
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/fixed_asset/资产卡片导入模板-001.xls')
            self.click_card_buttons('导入B')
            assert '4' in self.get_import_result()
        with allure.step('删除卡片'):
            self.click_return_to_list()
            self.click_check_all()
            self.click_card_buttons('删除')
            self.click_conform_buttons('确定')
            self.click_card_buttons('刷新')
            assert '没有卡片数据哦' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_fixed_asset
@pytest.mark.accounting_fixed_asset_depreciation_summary
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('折旧汇总表')
class TestFixedAssetDepreciationSummary(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    FixedAssetClassPage,
    FixedAssetCardPage,
    FixedAssetAddCardPage,
    FixedAssetDepreciationSummaryPage,
    FixedAssetDepreciationDetailPage,
    FixedAssetModifyCardPage,
    AccountingCommonPage
):

    @allure.title('折旧汇总表无数据')
    def test_summary_empty(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '折旧汇总表')
            self.switch_to_fixed_asset_depreciation_summary_frame()
            assert '没有数据哦！' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_fixed_asset
@pytest.mark.accounting_fixed_asset_depreciation_detail
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('折旧明细表')
class TestFixedAssetDepreciationDetail(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    FixedAssetClassPage,
    FixedAssetCardPage,
    FixedAssetAddCardPage,
    FixedAssetDepreciationSummaryPage,
    FixedAssetDepreciationDetailPage,
    FixedAssetModifyCardPage,
    AccountingCommonPage
):

    @allure.title('折旧明细表无数据')
    def test_detail_empty(self):
        company = GetYamlData().get_company('company_accounting_fixed_asset_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '折旧明细表')
            self.switch_to_fixed_asset_depreciation_detail_frame()
            assert '没有数据哦！' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_fixed_asset
@pytest.mark.accounting_fixed_asset_export
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('导出')
class TestFixedAssetExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    FixedAssetCardPage,
    FixedAssetDepreciationSummaryPage,
    FixedAssetDepreciationDetailPage
):

    @allure.title('导出卡片')
    def test_export_card(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
        with allure.step('导出卡片'):
            self.click_card_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/fixed_asset/资产卡片列表-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出标准模板')
    def test_export_standard_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '卡片')
            self.switch_to_fixed_asset_card_frame()
        with allure.step('导出标准模板'):
            self.click_card_buttons('导入')
            self.click_standard_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/fixed_asset/资产卡片导入标准模板.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出折旧汇总表')
    def test_export_depreciation_summary(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '折旧汇总表')
            self.switch_to_fixed_asset_depreciation_summary_frame()
        with allure.step('导出折旧汇总表'):
            self.click_card_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/fixed_asset/折旧汇总表-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出折旧明细表')
    def test_export_depreciation_detail(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('资产', '折旧明细表')
            self.switch_to_fixed_asset_depreciation_detail_frame()
        with allure.step('导出折旧明细表'):
            self.click_card_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/fixed_asset/折旧明细表-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
