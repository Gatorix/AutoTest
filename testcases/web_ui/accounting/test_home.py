import allure
import pytest

from page.web_ui.page_login import LoginPage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_common import AccountingCommonPage
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_home
@allure.epic('会计')
@allure.feature('首页')
@allure.story('首页')
class TestHome(
    LoginPage,
    AccountingHomePage,
    AccountingCommonPage
):
    @allure.title('跳转财务报表')
    def test_link_to_balance_sheet(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('跳转报表'):
            for _ in ['资产负债表', '利润表', '现金流量表', '纳税一览表']:
                self.switch_to_home_frame()
                self.click_home_report_link(_)
                self.switch_to_default_content()
                self.close_tab_by_tab_name(_)

    @allure.title('数据测算')
    def test_cal_data(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('数据测算'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
        with allure.step('核对结果'):
            assert self.get_text_from_home_report_cal_result('资产负债表') == '7,135,518.22'
            assert self.get_text_from_home_report_cal_result('利润表') == '-23,511.57'
            assert self.get_text_from_home_report_cal_result('现金流量表') == '1,261,108.55'
            assert self.get_text_from_home_report_cal_result('纳税一览表') == '0.00'

    @allure.title('跳转录凭证')
    def test_link_to_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('跳转录凭证'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('录凭证')
            self.switch_to_default_content()
            self.close_tab_by_tab_name('录凭证')

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230721-032')
    @allure.title('年收入测算-加载图标一直显示')
    def test_year_income_measure_loading_icon(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('切换月份'):
            self.switch_to_home_frame()
            span = '年收入测算'
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-01'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-03'
            assert 'loader dn' == self.get_loading_span_attribute(span)

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230721-032')
    @allure.title('月收入测算-加载图标一直显示')
    def test_month_income_measure_loading_icon(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('切换月份'):
            self.switch_to_home_frame()
            span = '月收入测算'
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-01'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-03'
            assert 'loader dn' == self.get_loading_span_attribute(span)

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230721-032')
    @allure.title('所得税测算-加载图标一直显示')
    def test_tax_measure_loading_icon(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('切换月份'):
            self.switch_to_home_frame()
            span = '所得税测算'
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '-1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-01'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-02'
            assert 'loader dn' == self.get_loading_span_attribute(span)
            self.click_home_measure_div_month_adj_buttons(span, '+1')
            assert self.get_text_from_home_measure_div_month_span(span) == '2023-03'
            assert 'loader dn' == self.get_loading_span_attribute(span)

    @allure.title('年收入测算-设置-确定')
    def test_year_measure_config_conform(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('年收入测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('年收入测算-设置')
            self.click_accounting_focus_table_buttons('确定')
            assert not self.is_element_visible(self.accounting_focus_table_buttons('确定'))

    @allure.title('年收入测算-设置-取消')
    def test_year_measure_config_cancel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('年收入测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('年收入测算-设置')
            self.click_accounting_focus_table_buttons('取消')
            assert not self.is_element_visible(self.accounting_focus_table_buttons('取消'))

    @allure.title('年收入测算-设置-关闭')
    def test_year_measure_config_close(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('年收入测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('年收入测算-设置')
            self.click_accounting_focus_table_close_button()
            assert not self.is_element_visible(self.accounting_focus_table_close_button())

    @allure.title('所得税测算-设置-确定')
    def test_tax_measure_config_conform(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('所得税测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-设置')
            self.click_accounting_focus_table_buttons('确定')
            assert not self.is_element_visible(self.accounting_focus_table_buttons('确定'))

    @allure.title('所得税测算-设置-取消')
    def test_tax_measure_config_cancel(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('所得税测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-设置')
            self.click_accounting_focus_table_buttons('取消')
            assert not self.is_element_visible(self.accounting_focus_table_buttons('取消'))

    @allure.title('所得税测算-设置-关闭')
    def test_tax_measure_config_close(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('所得税测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-设置')
            self.click_accounting_focus_table_close_button()
            assert not self.is_element_visible(self.accounting_focus_table_close_button())

    @allure.title('所得税测算-提示-关闭')
    def test_tax_measure_tips_close(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('所得税测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-提示')
            self.click_accounting_focus_table_close_button()
            assert not self.is_element_visible(self.accounting_focus_table_close_button())

    @allure.title('本期财务指标-刷新')
    def test_financial_indices_refresh(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('所得税测算-设置'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-刷新')
            assert '2,958.00' == self.get_text_from_home_financial_indices_list_item('现金')
            assert '1,258,150.55' == self.get_text_from_home_financial_indices_list_item('银行存款')

    @allure.tag('【管家】2023-08-18')
    @allure.tag('R20230721-032')
    @allure.title('本期财务指标-新增指标点击取消后无法正常退出设置页面')
    def test_financial_indices_refresh(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-管理')
        with allure.step('新增并取消添加项目'):
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            self.click_home_financial_indices_add_new_item()
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('取消')
            self.click_accounting_focus_table_buttons('确定')
            assert not self.is_element_visible(self.accounting_focus_table_buttons('确定'))

    @allure.title('本期财务指标-新增指标并删除')
    def test_financial_indices_refresh(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-管理')
        with allure.step('添加项目'):
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            self.click_home_financial_indices_add_new_item()
            self.type_to_home_financial_indices_input_by_label('项目名称', 'test')
            self.type_to_home_financial_indices_input_by_label('科目', '1301')
            self.click_accounting_subject_drop_down_list_item('1301')
            self.click_home_financial_indices_add_button()
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            assert '新增报表项成功！' in self.get_all_floating_tip()
        with allure.step('删除项目'):
            self.click_home_financial_indices_table_buttons('test', '删除')
            assert '删除成功！' in self.get_all_floating_tip()

    @allure.title('本期财务指标-重复新增')
    def test_financial_indices_create_already_exist(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-管理')
        with allure.step('添加项目'):
            item_name = random_string_generator()
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            self.click_home_financial_indices_add_new_item()
            self.type_to_home_financial_indices_input_by_label('项目名称', item_name)
            self.type_to_home_financial_indices_input_by_label('科目', '1301')
            self.click_accounting_subject_drop_down_list_item('1301')
            self.click_home_financial_indices_add_button()
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            assert '新增报表项成功！' in self.get_all_floating_tip()
        with allure.step('添加项目'):
            self.click_home_financial_indices_add_new_item()
            self.type_to_home_financial_indices_input_by_label('项目名称', item_name)
            self.type_to_home_financial_indices_input_by_label('科目', '1301')
            self.click_accounting_subject_drop_down_list_item('1301')
            self.click_home_financial_indices_add_button()
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            assert f'科目名称[{item_name}]在纳税一览表中已存在，请修改科目名称' in self.get_all_floating_tip()
            self.wait(1)
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('取消')
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
        with allure.step('删除项目'):
            self.click_home_financial_indices_table_buttons(item_name, '删除')
            assert '删除成功！' in self.get_all_floating_tip()

    @allure.title('本期财务指标-新增-未填写科目')
    def test_financial_indices_create_empty_subject(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-管理')
        with allure.step('添加项目'):
            item_name = random_string_generator()
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            self.click_home_financial_indices_add_new_item()
            self.type_to_home_financial_indices_input_by_label('项目名称', item_name)
            self.click_home_financial_indices_add_button()
            assert '请填写科目！' in self.get_all_floating_tip()

    @allure.title('本期财务指标-新增-未填写规则')
    def test_financial_indices_create_empty_rule(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('本期财务指标-管理')
        with allure.step('添加项目'):
            item_name = random_string_generator()
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            self.click_home_financial_indices_add_new_item()
            self.type_to_home_financial_indices_input_by_label('项目名称', item_name)
            self.switch_to_default_content()
            self.switch_to_home_frame()
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_accounting_focus_table_inner_frame('财务状况管理')
            assert '请添加报表规则！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230802-036')
    @allure.title('数据测算后，点击年收入测算、所得税测算配置按钮出现重复弹窗')
    def test_home_page_cal_data_income_tax_popup_repeat(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击本期财务指标-管理'):
            self.switch_to_home_frame()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-设置')
            self.click_accounting_focus_table_close_button()
            self.click_home_blue_buttons('数据测算')
            self.click_home_measure_div_buttons('所得税测算-设置')
            self.click_accounting_focus_table_close_button()
            assert not self.is_element_visible(self.accounting_focus_table_close_button())

    @allure.title('切换账套')
    def test_switch_accounting_set(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        company_0 = GetYamlData().get_company('company_accounting_smart_bookkeeping_046')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('切换账套'):
            self.switch_acct_set(company_0)
            assert '046' in self.get_text_from_my_company_span()

    # @allure.title('切换账套')
    # def test_switch_accounting_set_random_switch_100_times(self):
    #     company_list = []
    #     with allure.step('登录'):
    #         self.login(company=company_list[0])
    #     for i, _ in enumerate(company_list):
    #         with allure.step('切换账套'):
    #             if i == 0 or '恢复' in _:
    #                 continue
    #             self.switch_acct_set(_)
    #             assert _ in self.get_text_from_my_company_span()
    #             self.click_accounting_menu('查凭证')
    #             assert self.is_top_tab_visible('查凭证')
