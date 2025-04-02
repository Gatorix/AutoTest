import allure
import pytest

from page.web_ui.accounting.page_settings import (SettingsSubjectPage,
                                                  SettingsSubAccountPage,
                                                  SettingsCommonPage,
                                                  SettingsSubAccountDetailsPage,
                                                  SettingsInvoiceVoucherTemplatePage,
                                                  SettingsVoucherTypePage,
                                                  SettingsCurrencyPage,
                                                  AdvanceSettingsSystemArgsPage)
from page.web_ui.page_login import LoginPage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_common import AccountingCommonPage
from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path

from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_voucher_type
@allure.epic('会计')
@allure.feature('设置')
@allure.story('凭证字')
class TestSettingsVoucherType(
    SettingsVoucherTypePage,
    SettingsCommonPage,
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage
):
    @pytest.mark.p1
    @allure.title('新增凭证字')
    def test_create_voucher_type(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '凭证字')
            self.switch_to_settings_voucher_type_frame()
        with allure.step('新增凭证字'):
            self.click_settings_voucher_type_add_button()
            test_str = random_string_generator(4, '')
            self.type_to_settings_common_details_focus_table_input_by_label('凭证字', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('打印标题', test_str)
            self.click_settings_common_details_focus_table_radio_by_label('是否默认', 0)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '新增成功' in self.get_all_floating_tip()
        with allure.step('删除凭证字'):
            self.click_settings_common_details_focus_table_buttons('关闭')
            self.click_settings_voucher_type_operate_button_in_line_by_type(test_str, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增并修改凭证字')
    def test_create_and_modify_voucher_type(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '凭证字')
            self.switch_to_settings_voucher_type_frame()
        with allure.step('新增凭证字'):
            self.click_settings_voucher_type_add_button()
            test_str = random_string_generator(4, '')
            self.type_to_settings_common_details_focus_table_input_by_label('凭证字', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('打印标题', test_str)
            self.click_settings_common_details_focus_table_radio_by_label('是否默认', 0)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '新增成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('修改凭证字'):
            test_str_1 = random_string_generator(4, '')
            self.click_settings_voucher_type_operate_button_in_line_by_type(test_str, '编辑')
            self.type_to_settings_common_details_focus_table_input_by_label('凭证字', test_str_1)
            self.type_to_settings_common_details_focus_table_input_by_label('打印标题', test_str_1)
            self.click_settings_common_details_focus_table_radio_by_label('是否默认', 0)
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '修改成功' in self.get_all_floating_tip()
        with allure.step('删除凭证字'):
            self.click_settings_voucher_type_operate_button_in_line_by_type(test_str_1, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增凭证字-名称为空')
    def test_create_voucher_type_empty_name(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '凭证字')
            self.switch_to_settings_voucher_type_frame()
        with allure.step('新增凭证字'):
            self.click_settings_voucher_type_add_button()
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '凭证字不能为空' in self.get_text_from_settings_common_details_focus_table_error_label_by_label(
                '凭证字')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_advance_settings
@pytest.mark.accounting_advance_settings_sys_args
@allure.epic('会计')
@allure.feature('设置')
@allure.story('系统参数')
class TestAdvanceSettingsSystemArgs(
    AdvanceSettingsSystemArgsPage,
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage
):
    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231116-009')
    @allure.title('科目编码示例')
    def test_subject_code_demo(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '系统参数')
            self.click_top_tabs_label('系统参数')
            self.switch_to_sys_args_frame()
        with allure.step('鼠标悬停并校验提示框'):
            self.move_to_sys_args_subject_demo_button()
            assert self.is_element_visible(self.sys_args_subject_demo_box())
            assert '2、表示二级科目，可以添加2位数，比如01-99' in self.get_text_from_sys_args_subject_demo_box()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_subject
@allure.epic('会计')
@allure.feature('设置')
@allure.story('科目')
class TestSettingsSubject(
    SettingsSubjectPage,
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage
):
    @allure.title('小企业会计准则-新增科目-科目编码为空')
    def test_small_business_create_subject_empty_code(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', 'test11')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            self.switch_to_settings_subject_focus_table_iframe()
            assert '科目编码不能为空' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-科目编码错误')
    def test_small_business_create_subject_wrong_code(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '19911')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            self.switch_to_settings_subject_focus_table_iframe()
            assert '科目编码结构为4-2-2-2，请输入正确的编码' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-科目名称为空')
    def test_small_business_create_subject_empty_name(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '1999')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            self.switch_to_settings_subject_focus_table_iframe()
            assert '科目名称不能为空' in self.get_all_floating_tip()

    @pytest.mark.p1
    @allure.title('小企业会计准则-新增科目-资产类')
    def test_small_business_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1997'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-带核算项目')
    def test_small_business_create_subject_with_sub(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1996'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-带数量核算')
    def test_small_business_create_subject_with_amount(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1995'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_options_by_label('数量核算')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-带外币核算-未选择币别')
    def test_small_business_create_subject_with_multiple_currency_empty_currency(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '1994')
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', '1994')
            self.click_settings_subject_focus_table_options_by_label('外币核算')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            self.switch_to_settings_subject_focus_table_iframe()
            assert '请选择至少一种币别' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-带外币核算')
    def test_small_business_create_subject_with_multiple_currency(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1991'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_options_by_label('外币核算')
            self.click_settings_subject_focus_table_options_by_label('人民币')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-现金及现金等价物')
    def test_small_business_create_subject_with_cash(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1993'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_options_by_label('现金及现金等价物')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230707-013')
    @allure.title('小企业会计准则-新增科目-贷方-勾选全部-科目名称包含"+"')
    def test_small_business_create_subject_debit_add_symbol_in_subject_name(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1799'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', f'+{subject_code}')
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('数量核算')
            self.click_settings_subject_focus_table_options_by_label('现金及现金等价物')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
            assert self.get_text_from_settings_subject_name_by_id(subject_code) == f'+{subject_code}'
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-贷方-勾选全部')
    def test_small_business_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1992'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('数量核算')
            self.click_settings_subject_focus_table_options_by_label('现金及现金等价物')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-负债类-二级科目')
    def test_small_business_create_subject_debit_second_level(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '221101'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_operating_buttons_by_id('2211', '增加下级')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('客户')
            self.click_settings_subject_focus_table_options_by_label('供应商')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230707-013')
    @allure.title('新增二级科目-科目名称中包含"+"-首字符')
    def test_subject_name_contains_add_at_start(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '220201'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_operating_buttons_by_id('2202', '增加下级')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '01')
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', f'+{subject_code}')
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('客户')
            self.click_settings_subject_focus_table_options_by_label('供应商')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            assert self.get_text_from_settings_subject_name_by_id(subject_code) == f'+{subject_code}'
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230707-013')
    @allure.title('新增二级科目-科目名称中包含"+"-尾字符')
    def test_subject_name_contains_add_at_end(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '220301'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_operating_buttons_by_id('2203', '增加下级')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '01')
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', f'{subject_code}+')
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('客户')
            self.click_settings_subject_focus_table_options_by_label('供应商')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            assert self.get_text_from_settings_subject_name_by_id(subject_code) == f'{subject_code}+'
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230707-013')
    @allure.title('新增二级科目-科目名称中包含"+"-在中间')
    def test_subject_name_contains_add_in_middle(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '220101'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_operating_buttons_by_id('2201', '增加下级')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', '01')
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', '2201+01')
            self.click_settings_subject_focus_table_radio_by_label('-1')
            self.click_settings_subject_focus_table_options_by_label('辅助核算')
            self.click_settings_subject_focus_table_options_by_label('客户')
            self.click_settings_subject_focus_table_options_by_label('供应商')
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            assert self.get_text_from_settings_subject_name_by_id(subject_code) == '2201+01'
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-权益类')
    def test_small_business_create_subject_interests(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '3199'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-成本类')
    def test_small_business_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '4099'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('小企业会计准则-新增科目-损益类')
    def test_small_business_create_subject_profit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '6099'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('非盈利组织-新增科目-资产类')
    def test_non_profit_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_non_profit_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            subject_code = '1999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_class('资产')
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('非盈利组织-新增科目-负债类')
    def test_non_profit_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_non_profit_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '2999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('非盈利组织-新增科目-净资产类')
    def test_non_profit_create_subject_net_assets(self):
        company_name = GetYamlData().get_company('company_accounting_standards_non_profit_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('净资产')
            subject_code = '3199'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('非盈利组织-新增科目-收入费用类')
    def test_non_profit_create_subject_income_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_non_profit_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('收入费用')
            subject_code = '5999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-资产类')
    def test_government_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '1999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-负债类')
    def test_government_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '2999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-净资产类')
    def test_government_create_subject_net_assets(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('净资产')
            subject_code = '3999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-收入类')
    def test_government_create_subject_income(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('收入')
            subject_code = '4999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-费用类')
    def test_government_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('费用')
            subject_code = '5999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('政府-新增科目-预算类')
    def test_government_create_subject_budget(self):
        company_name = GetYamlData().get_company('company_accounting_standards_government_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('预算')
            subject_code = '9999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('村集体-新增科目-资产类')
    def test_village_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_village_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '199'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('村集体-新增科目-负债类')
    def test_village_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_village_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '299'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('村集体-新增科目-权益类')
    def test_village_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_village_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '399'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('村集体-新增科目-成本类')
    def test_village_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_village_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '499'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('村集体-新增科目-损益类')
    def test_village_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_village_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '599'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-资产类')
    def test_new_2006_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '1999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-负债类')
    def test_new_2006_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '2999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-共同类')
    def test_new_2006_create_subject_common(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('共同')
            subject_code = '3999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-权益类')
    def test_new_2006_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '4999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-成本类')
    def test_new_2006_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '5999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新准则2006-新增科目-损益类')
    def test_new_2006_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2006_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '6999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-资产类')
    def test_new_2019_00_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '1999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-负债类')
    def test_new_2019_00_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '2999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-共同类')
    def test_new_2019_00_create_subject_common(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('共同')
            subject_code = '3999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-权益类')
    def test_new_2019_00_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '4999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-成本类')
    def test_new_2019_00_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '5999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-执行-新增科目-损益类')
    def test_new_2019_00_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_00_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '6999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-资产类')
    def test_new_2019_01_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '1999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-负债类')
    def test_new_2019_01_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '2999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-共同类')
    def test_new_2019_01_create_subject_common(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('共同')
            subject_code = '3999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-权益类')
    def test_new_2019_01_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '4999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-成本类')
    def test_new_2019_01_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '5999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('新企业会计准则-未执行-新增科目-损益类')
    def test_new_2019_01_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_new_2019_01_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '6999'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2007-新增科目-资产类')
    def test_farmer_2007_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2007_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '199'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2007-新增科目-负债类')
    def test_farmer_2007_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2007_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '299'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2007-新增科目-权益类')
    def test_farmer_2007_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2007_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '399'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2007-新增科目-成本类')
    def test_farmer_2007_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2007_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '499'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2007-新增科目-损益类')
    def test_farmer_2007_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2007_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '499'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2021-新增科目-资产类')
    def test_farmer_2021_create_subject_asset(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2021_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('资产')
            subject_code = '199'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2021-新增科目-负债类')
    def test_farmer_2021_create_subject_debit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2021_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('负债')
            subject_code = '299'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2021-新增科目-权益类')
    def test_farmer_2021_create_subject_rights(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2021_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('权益')
            subject_code = '399'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2021-新增科目-成本类')
    def test_farmer_2021_create_subject_costs(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2021_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('成本')
            subject_code = '499'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()

    @allure.title('农专2021-新增科目-损益类')
    def test_farmer_2021_create_subject_profits(self):
        company_name = GetYamlData().get_company('company_accounting_standards_farmer_2021_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '科目')
            self.switch_to_settings_subject_frame()
        with allure.step('检查科目是否存在'):
            self.click_settings_subject_class('损益')
            subject_code = '499'
            if self.is_element_visible(self.settings_subject_operating_buttons_by_id(subject_code, '删除')):
                self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
                self.click_settings_subject_focus_table_buttons('确定')
                assert '操作成功' in self.get_all_floating_tip()
        with allure.step('新增科目'):
            self.click_settings_subject_buttons('新增')
            self.switch_to_settings_subject_focus_table_iframe()
            self.type_to_settings_subject_focus_table_input_by_label('科目编码', subject_code)
            self.type_to_settings_subject_focus_table_input_by_label('科目名称', subject_code)
            self.switch_to_parent_frame()
            self.click_settings_subject_focus_table_buttons('保存')
            assert '操作成功' in self.get_all_floating_tip()
            self.click_settings_subject_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_subject_operating_buttons_by_id(subject_code, '删除')
            self.click_settings_subject_focus_table_buttons('确定')
            assert '操作成功' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_sub_account
@allure.epic('会计')
@allure.feature('设置')
@allure.story('辅助核算')
class TestSettingsSubAccount(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    SettingsSubAccountPage,
    SettingsCommonPage
):
    @allure.title('进入预置辅助核算明细-客户')
    def test_enter_sys_default_sub_details_customer(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('客户')
            assert self.is_top_tab_visible('客户')

    @allure.title('进入预置辅助核算明细-供应商')
    def test_enter_sys_default_sub_details_supplier(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('供应商')
            assert self.is_top_tab_visible('供应商')

    @allure.title('进入预置辅助核算明细-职员')
    def test_enter_sys_default_sub_details_employee(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('职员')
            assert self.is_top_tab_visible('职员')

    @allure.title('进入预置辅助核算明细-项目')
    def test_enter_sys_default_sub_details_project(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('项目')
            assert self.is_top_tab_visible('项目')

    @allure.title('进入预置辅助核算明细-部门')
    def test_enter_sys_default_sub_details_department(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('部门')
            assert self.is_top_tab_visible('部门')

    @allure.title('进入预置辅助核算明细-存货')
    def test_enter_sys_default_sub_details_inventory(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('点击系统预置辅助核算项目'):
            self.click_settings_sub_accounting_types('存货')
            assert self.is_top_tab_visible('存货')

    @allure.title('新增自定义辅助核算项目')
    def test_create_customize_sub_accounting(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        sub_name = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('新增自定义辅助核算项目'):
            self.click_settings_sub_accounting_new_type()
        with allure.step('录入自定义字段'):
            self.type_to_settings_common_details_focus_table_input_by_label('名称', sub_name)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '自定义核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('删除自定义辅助核算项目'):
            self.click_settings_sub_accounting_customize_type_operating_buttons(sub_name, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增自定义辅助核算项目-名称过长')
    def test_create_customize_sub_accounting_name_too_long(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        sub_name = random_string_generator()
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('新增自定义辅助核算项目'):
            self.click_settings_sub_accounting_new_type()
        with allure.step('录入自定义字段'):
            self.type_to_settings_common_details_focus_table_input_by_label('名称', sub_name)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '保存失败！名称长度不能大于20' in self.get_all_floating_tip()

    @allure.title('新增自定义辅助核算项目-重名')
    def test_create_customize_sub_accounting_name_already_exist(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        sub_name = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('新增自定义辅助核算项目'):
            self.click_settings_sub_accounting_new_type()
        with allure.step('录入自定义字段'):
            self.type_to_settings_common_details_focus_table_input_by_label('名称', sub_name)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '自定义核算项目保存成功' in self.get_all_floating_tip()
            self.type_to_settings_common_details_focus_table_input_by_label('名称', sub_name)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '保存失败！名称重复，请重新输入名称' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('删除自定义辅助核算项目'):
            self.wait(2)
            self.click_settings_sub_accounting_customize_type_operating_buttons(sub_name, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增自定义辅助核算项目-修改名称')
    def test_create_customize_sub_accounting_rename(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        sub_name = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('新增自定义辅助核算项目'):
            self.click_settings_sub_accounting_new_type()
        with allure.step('录入自定义字段'):
            self.type_to_settings_common_details_focus_table_input_by_label('名称', sub_name)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '自定义核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('修改自定义辅助核算项目'):
            self.click_settings_sub_accounting_customize_type_operating_buttons(sub_name, '编辑')
            self.type_to_settings_common_details_focus_table_input_by_label('名称', f'{sub_name}123')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '自定义核算项目保存成功' in self.get_all_floating_tip()
        with allure.step('删除自定义辅助核算项目'):
            self.click_settings_sub_accounting_customize_type_operating_buttons(f'{sub_name}123', '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_sub_account_details
@allure.epic('会计')
@allure.feature('设置')
@allure.story('辅助核算明细')
class TestSettingsSubAccountDetails(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    SettingsSubAccountPage,
    SettingsCommonPage,
    SettingsSubAccountDetailsPage
):
    @allure.title('切换辅助核算')
    def test_switch_sub_accounting_class(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            for _ in ['客户', '供应商', '职员', '项目', '部门', '存货']:
                self.switch_to_settings_sub_accounting_details_frame()
                self.click_settings_sub_accounting_details_tab_li(_)
                self.switch_to_default_content()
                assert self.is_top_tab_visible(_)

    @pytest.mark.p1
    @allure.title('客户-新增辅助核算')
    def test_customer_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231115-027')
    @allure.title('辅助核算被使用-财务初始余额')
    def test_occupation_by_init_balance(self):
        company_name = GetYamlData().get_company('proj_R20231115-027')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('删除'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('test4', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '【test4】已经被【财务初始余额】使用了，不可删除！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231115-027')
    @allure.title('辅助核算被使用-凭证')
    def test_occupation_by_voucher(self):
        company_name = GetYamlData().get_company('proj_R20231115-027')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('删除'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('test3', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '【test3】已经被【凭证】使用了，不可删除！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231115-027')
    @allure.title('辅助核算被使用-工资')
    def test_occupation_by_salary(self):
        company_name = GetYamlData().get_company('proj_R20231115-027')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('职员')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('删除'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('emp1', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '【emp1】已经被【工资】使用了，不可删除！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231115-027')
    @allure.title('辅助核算被使用-卡片')
    def test_occupation_by_asset_card(self):
        company_name = GetYamlData().get_company('proj_R20231115-027')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('部门')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('删除'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('dep1', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '【dep1】已经被【卡片】使用了，不可删除！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231115-027')
    @allure.title('辅助核算被使用-库存')
    def test_occupation_by_inventory(self):
        company_name = GetYamlData().get_company('proj_R20231115-027')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('删除'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('test111', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '【test111】已经被【库存】使用了，不可删除！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230928-010')
    @allure.title('客户-新增辅助核算-连续点击保存产生重复数据')
    def test_customer_add_sub_accounting_item_double_click(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-10-26')
    @allure.tag('R20230914-001')
    @allure.title('客户-辅助核算过滤-不区分大小写')
    def test_customer_upper_or_lower_query(self):
        company_name = GetYamlData().get_company('proj_R20230914-001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('查询'):
            self.search_sub_accounting_item('coco')
            assert 4 == self.get_all_settings_sub_accounting_details_line_num()

    @allure.title('客户-新增辅助核算-编码为空')
    def test_customer_add_sub_accounting_item_empty_code(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', '')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '名称不能为空' in self.get_text_from_settings_common_details_focus_table_error_label_by_label('名称')

    @allure.title('客户-新增辅助核算-名称为空')
    def test_customer_add_sub_accounting_item_empty_name(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', '')
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '编码不能为空' in self.get_text_from_settings_common_details_focus_table_error_label_by_label('编码')

    @allure.title('客户-新增辅助核算-按钮删除')
    def test_customer_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_checkbox_in_line_by_code(random_str)
            self.click_settings_sub_accounting_details_buttons('删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('供应商-新增辅助核算')
    def test_supplier_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('供应商')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('职员-新增辅助核算')
    def test_employee_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('职员')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('项目-新增辅助核算')
    def test_project_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('项目')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('部门-新增辅助核算')
    def test_department_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('部门')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('存货-新增辅助核算-编码存在下划线')
    def test_inventory_add_sub_accounting_item_error(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5)
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存失败！编码不允许存在下划线，请重新输入' in self.get_all_floating_tip()

    @allure.title('存货-新增辅助核算')
    def test_inventory_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5, '')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('存货-新增辅助核算-全部字段')
    def test_inventory_add_sub_accounting_item_all(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5, '')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('规格', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('单位', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('自定义-新增辅助核算')
    def test_customize_add_sub_accounting_item(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        random_str = random_string_generator(5, '')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('自定义项目')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('新增'):
            self.click_settings_sub_accounting_details_buttons('新增')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', random_str)
            self.type_to_settings_common_details_focus_table_input_by_label('名称', random_str)
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '核算项目保存成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code(random_str, 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('下载导入模板')
    def test_export_import_template(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_download_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\settings\\核算维度导入模板.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('下载导入模板-存货')
    def test_export_import_template_inventory(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_download_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\settings\\核算维度导入模板-存货.xls',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导入核算维度-普通')
    def test_import_sub_accounting(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('检查数据'):
            if self.is_element_visible(
                    self.settings_sub_accounting_details_checkbox_in_line_by_code('test_fev954')):
                self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('test_fev954', 'del')
                self.click_settings_common_details_focus_table_buttons('确定')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_button_by_name('下一步')
            self.upload_file_to_settings_sub_accounting_details_upload_file_input(
                f'{get_project_path()}/template/accounting/settings/导入核算维度.xls')
            self.click_settings_sub_accounting_details_buttons('导入')
            self.wait(3)
            assert '1' in self.get_text_from_settings_sub_accounting_details_import_result(1)
            self.click_settings_sub_accounting_details_button_by_name('返回客户列表')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('test_fev954', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入核算维度-存货')
    def test_import_sub_accounting_inventory(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('检查数据'):
            if self.is_element_visible(
                    self.settings_sub_accounting_details_checkbox_in_line_by_code('fev95a')):
                self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('fev95a', 'del')
                self.click_settings_common_details_focus_table_buttons('确定')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_button_by_name('下一步')
            self.upload_file_to_settings_sub_accounting_details_upload_file_input(
                f'{get_project_path()}/template/accounting/settings/导入核算维度-存货.xls')
            self.click_settings_sub_accounting_details_buttons('导入')
            self.wait(3)
            assert '1' in self.get_text_from_settings_sub_accounting_details_import_result(1)
            self.click_settings_sub_accounting_details_button_by_name('返回存货列表')
        with allure.step('还原数据'):
            self.click_settings_sub_accounting_details_operate_buttons_in_line_by_code('fev95a', 'del')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入核算维度-普通-文件错误')
    def test_import_sub_accounting_wrong_file(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('客户')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_button_by_name('下一步')
            self.upload_file_to_settings_sub_accounting_details_upload_file_input(
                f'{get_project_path()}/template/accounting/settings/导入核算维度-存货.xls')
            self.click_settings_sub_accounting_details_buttons('导入')
            self.wait(3)
            assert '导入的Excel列数不对，请仔细检查模版' in self.get_text_from_settings_sub_accounting_details_import_result_text()

    @allure.title('导入核算维度-存货-文件错误')
    def test_import_sub_accounting_inventory_wrong_file(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '辅助核算')
            self.switch_to_settings_sub_accounting_frame()
        with allure.step('进入核算项目明细'):
            self.click_settings_sub_accounting_types('存货')
            self.switch_to_default_content()
            self.switch_to_settings_sub_accounting_details_frame()
        with allure.step('导入'):
            self.click_settings_sub_accounting_details_buttons('导入')
            self.click_settings_sub_accounting_details_button_by_name('下一步')
            self.upload_file_to_settings_sub_accounting_details_upload_file_input(
                f'{get_project_path()}/template/accounting/settings/导入核算维度.xls')
            self.click_settings_sub_accounting_details_buttons('导入')
            self.wait(3)
            assert '导入的Excel列数不对，请仔细检查模版' in self.get_text_from_settings_sub_accounting_details_import_result_text()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_currency
@allure.epic('会计')
@allure.feature('设置')
@allure.story('币别')
class TestSettingsCurrency(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    SettingsCurrencyPage,
    SettingsCommonPage
):
    @pytest.mark.p1
    @allure.title('新增币别并删除')
    def test_create_and_delete_currency(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '币别')
            self.switch_to_settings_currency_frame()
        with allure.step('新增币别'):
            test_str = random_string_generator(3, '')
            self.click_settings_currency_add_button()
            self.type_to_settings_common_details_focus_table_input_by_label('编码', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('币别', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('汇率', '1.23233')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '新增成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('删除币别'):
            self.click_settings_currency_operating_buttons_in_line_by_code(test_str, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('编辑币别并删除')
    def test_modify_and_delete_currency(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '币别')
            self.switch_to_settings_currency_frame()
        with allure.step('新增币别'):
            test_str = random_string_generator(3, '')
            self.click_settings_currency_add_button()
            self.type_to_settings_common_details_focus_table_input_by_label('编码', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('币别', test_str)
            self.type_to_settings_common_details_focus_table_input_by_label('汇率', '1.23233')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '新增成功' in self.get_all_floating_tip()
            self.click_settings_common_details_focus_table_buttons('关闭')
        with allure.step('编辑币别'):
            self.click_settings_currency_operating_buttons_in_line_by_code(test_str, '编辑')
            test_str_1 = random_string_generator(3, '')
            self.type_to_settings_common_details_focus_table_input_by_label('编码', test_str_1)
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '修改成功' in self.get_all_floating_tip()
        with allure.step('删除币别'):
            self.click_settings_currency_operating_buttons_in_line_by_code(test_str, '删除')
            self.click_settings_common_details_focus_table_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('币别字段校验-为空')
    def test_currency_input_check_empty(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '币别')
            self.switch_to_settings_currency_frame()
        with allure.step('新增币别'):
            self.click_settings_currency_add_button()
            self.click_settings_common_details_focus_table_buttons('保存')
            for _ in ['编码', '币别', '汇率']:
                assert '不能为空' in self.get_text_from_settings_common_details_focus_table_error_label_by_label(_)

    @allure.title('币别字段校验-编码')
    def test_currency_input_check_code(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '币别')
            self.switch_to_settings_currency_frame()
        with allure.step('新增币别'):
            self.click_settings_currency_add_button()
            self.type_to_settings_common_details_focus_table_input_by_label('编码', '3')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '币别编码只能为三位的英文字母' in self.get_text_from_settings_common_details_focus_table_error_label_by_label(
                '编码')

    @allure.title('币别字段校验-币别')
    def test_currency_input_check_currency(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '币别')
            self.switch_to_settings_currency_frame()
        with allure.step('新增币别'):
            self.click_settings_currency_add_button()
            self.type_to_settings_common_details_focus_table_input_by_label('币别', '3')
            self.click_settings_common_details_focus_table_buttons('保存')
            assert '币别名称只能为字母或汉字' in self.get_text_from_settings_common_details_focus_table_error_label_by_label(
                '币别')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_settings
@pytest.mark.accounting_settings_invoice_voucher_template
@allure.epic('会计')
@allure.feature('设置')
@allure.story('票据凭证模板')
class TestSettingsInvoiceVoucherTemplate(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage,
    SettingsCommonPage,
    SettingsInvoiceVoucherTemplatePage
):
    @pytest.mark.p1
    @allure.title('新增票据凭证模板并删除')
    def test_new_invoice_voucher_template(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('新增票据凭证模板'):
            self.click_settings_invoice_voucher_template_buttons('新增')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('单据名称', '销售增值税发票')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '其他')
            self.type_to_settings_new_invoice_voucher_template_inputs_by_label('摘要内容', 'test')
            for _ in ['单据日期', '往来单位', '发票号码', '发票商品', '规格型号', '备注']:
                self.click_settings_new_invoice_voucher_template_summary_span(_)
            self.fill_one_line_of_voucher_template(1, '借', '1001', '金额')
            self.fill_one_line_of_voucher_template(2, '贷', '1002', '金额')
            # self.click_settings_new_invoice_voucher_template_operating_buttons_in_line(3, '删除')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('新增票据凭证模板-科目缺失')
    def test_new_invoice_voucher_template_empty_subject(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('新增票据凭证模板'):
            self.click_settings_invoice_voucher_template_buttons('新增')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('单据名称', '销售增值税发票')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '其他')
            self.type_to_settings_new_invoice_voucher_template_inputs_by_label('摘要内容', 'test')
            for _ in ['单据日期', '往来单位', '发票号码', '发票商品', '规格型号', '备注']:
                self.click_settings_new_invoice_voucher_template_summary_span(_)
            self.fill_one_line_of_voucher_template(1, '借', '1001', '金额')
            self.fill_one_line_of_voucher_template(2, '贷', None, '金额')
            # self.click_settings_new_invoice_voucher_template_operating_buttons_in_line(3, '删除')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '凭证模板不完整,科目不存在' in self.get_all_floating_tip()

    @allure.title('新增票据凭证模板-结算类型已存在')
    def test_new_invoice_voucher_template_already_exist(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('新增票据凭证模板'):
            self.click_settings_invoice_voucher_template_buttons('新增')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('单据名称', '销售增值税发票')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '现金')
            self.type_to_settings_new_invoice_voucher_template_inputs_by_label('摘要内容', 'test')
            for _ in ['单据日期', '往来单位', '发票号码', '发票商品', '规格型号', '备注']:
                self.click_settings_new_invoice_voucher_template_summary_span(_)
            self.fill_one_line_of_voucher_template(1, '借', '1001', '金额')
            self.fill_one_line_of_voucher_template(2, '贷', '1002', '金额')
            # self.click_settings_new_invoice_voucher_template_operating_buttons_in_line(3, '删除')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '存在相同单据名称+结算方式+业务类型的票据凭证模板' in self.get_all_floating_tip()

    @allure.title('新增票据凭证模板-摘要为空')
    def test_new_invoice_voucher_template_empty_summary(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('新增票据凭证模板'):
            self.click_settings_invoice_voucher_template_buttons('新增')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('单据名称', '销售增值税发票')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '现金')
            self.fill_one_line_of_voucher_template(1, '借', '1001', '金额')
            self.fill_one_line_of_voucher_template(2, '贷', '1002', '金额')
            # self.click_settings_new_invoice_voucher_template_operating_buttons_in_line(3, '删除')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '摘要不能为空' in self.get_all_floating_tip()

    @allure.tag('R20230619-021')
    @allure.tag('【管家】2023-07-27')
    @allure.title('新增票据凭证模板修改业务类型提示金额来源不正确')
    def test_new_invoice_voucher_template_modify_biz_type(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('新增票据凭证模板'):
            self.click_settings_invoice_voucher_template_buttons('新增')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('单据名称', '销售增值税发票')
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '现金')
            self.type_to_settings_new_invoice_voucher_template_inputs_by_label('摘要内容', 'test')
            for _ in ['单据日期', '往来单位', '发票号码', '发票商品', '规格型号', '备注']:
                self.click_settings_new_invoice_voucher_template_summary_span(_)
            self.fill_one_line_of_voucher_template(1, '借', '1001', '金额')
            self.fill_one_line_of_voucher_template(2, '贷', '1002', '金额')
            # self.click_settings_new_invoice_voucher_template_operating_buttons_in_line(3, '删除')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '存在相同单据名称+结算方式+业务类型的票据凭证模板' in self.get_all_floating_tip()
            self.select_settings_new_invoice_voucher_template_inputs_by_label('结算方式', '银行存款')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.tag('R20230619-021')
    @allure.tag('【管家】2023-07-27')
    @allure.title('编辑已存在的票据凭证模板-摘要')
    def test_exist_invoice_template_abs_edit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('摘要编辑按钮'):
            self.click_settings_invoice_voucher_template_buttons_in_line_by_method('往来结算', '编辑摘要')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.tag('R20230619-021')
    @allure.tag('【管家】2023-07-27')
    @allure.title('编辑已存在的票据凭证模板-科目')
    def test_exist_invoice_template_subject_edit(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('摘要编辑按钮'):
            self.click_settings_invoice_voucher_template_buttons_in_line_by_method('往来结算', '编辑模板')
            self.click_settings_new_invoice_voucher_template_buttons_by_id('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.tag('R20231203-008')
    @allure.tag('【管家】2024年01月')
    @allure.title('相同会计制度间复制票据凭证模板')
    def test_copy_template_same_acct(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('复制模板'):
            acct_name = '会计自动化测试-固定资产-001'
            self.click_settings_invoice_voucher_template_buttons('复制至其他账套')
            self.type_to_settings_invoice_voucher_template_acct_search_input(acct_name)
            self.click_settings_invoice_voucher_template_acct_search_result(acct_name)
            self.click_settings_invoice_voucher_template_copy_submit_button()
            assert '复制票据凭证模板成功1个账套！' in self.get_all_floating_tip()

    @allure.tag('R20231203-008')
    @allure.tag('【管家】2024年01月')
    @allure.title('不同会计制度间复制票据凭证模板')
    def test_copy_template_diff_acct(self):
        company_name = GetYamlData().get_company('company_accounting_standards_small_2013_001')
        with allure.step('登录'):
            self.login(company=company_name)
        with allure.step('点击会计菜单'):
            self.click_accounting_data_menu('设置', '票据凭证模版')
            self.switch_to_settings_invoice_voucher_template_frame()
        with allure.step('同步最新模板'):
            self.click_settings_invoice_voucher_template_buttons('同步最新模板')
            self.click_settings_invoice_voucher_template_sync_radio(1)
            self.click_settings_invoice_voucher_template_sync_save_button()
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('复制模板'):
            acct_name = '农民专业合作社财务会计制度(2007年版)_001'
            self.click_settings_invoice_voucher_template_buttons('复制至其他账套')
            self.type_to_settings_invoice_voucher_template_acct_search_input(acct_name)
            self.click_settings_invoice_voucher_template_acct_search_result(acct_name)
            self.click_settings_invoice_voucher_template_copy_submit_button()
            assert '复制票据凭证模板成功0个账套，失败1个账套，失败原因：会计制度不一致！' in self.get_all_floating_tip()
