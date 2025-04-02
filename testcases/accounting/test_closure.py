import allure
import pytest

from page.accounting.page_lookup_voucher import LookupVoucherPage
from page.manager.page_agency import AgencyAccountPage
from page.manager.page_common import ManagerCommonPage
from page.manager.page_customer import CustomerPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.accounting.page_home import AccountingHomePage
from page.accounting.page_closure import (ClosurePage,
                                          RequisitionRawMaterialsPage,
                                          ProductionCostsPage,
                                          SellingCostsPage,
                                          FinalInspectionPage)
from page.accounting.page_common import AccountingCommonPage
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_process
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转')
class TestClosure(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    AccountingCommonPage,
    LookupVoucherPage
):
    @allure.title('初始期间反结账')
    def test_reverse_closure_init_period(self):
        company = GetYamlData().get_company('company_accounting_closure_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('反结账'):
            self.click_buttons('反结账')
            assert '启用期间不允许反结账！' in self.get_all_floating_tip()

    @allure.title('测算金额并生成凭证')
    def test_cal_and_gen_closure_voucher(self):
        company = GetYamlData().get_company('company_accounting_closure_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('测算金额'):
            self.click_buttons('测算金额')
            assert '测算结转凭证金额完成' in self.get_all_floating_tip()
        with allure.step('一键生成'):
            self.click_buttons('一键生成')
        with allure.step('检查凭证'):
            self.switch_to_default_content()
            self.click_accounting_menu('查凭证')
        with allure.step('删除凭证'):
            self.click_accounting_menu('查凭证')
            self.switch_to_lookup_voucher_frame()
            for _ in ['计提2月工资', '计提折旧费用', '结转本期损益']:
                self.delete_voucher_by_summary(_)
                assert '共删除1张凭证' in self.get_all_floating_tip()

    @allure.title('结账并反结账')
    def test_closure_and_reverse_closure_no_data(self):
        company = GetYamlData().get_company('company_accounting_closure_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('结账'):
            self.click_buttons('结转到下期')
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_default_content()
            assert '恭喜您，结账到2023年2期成功！' in self.get_all_floating_tip()
        with allure.step('反结账'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
            self.click_buttons('反结账')
            self.click_accounting_focus_table_buttons('确定')
            self.switch_to_default_content()
            assert '恭喜您，反结账成功！' in self.get_all_floating_tip()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_templates
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转模板')
class TestClosureTemplates(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    AccountingCommonPage
):

    @allure.title('新增结转模板')
    def test_new_template(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '100')
            self.type_template_info_single_line('2', 'test', '贷', '1002', '转出期末余额', '100')
        with allure.step('保存模板'):
            self.click_input_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('删除模板'):
            self.click_generate_operate_button(template_name, 'del')
            self.click_input_buttons('是')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增结转模板-增行')
    def test_new_template_add_line(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '100')
            self.type_template_info_single_line('2', 'test', '贷', '1002', '转出期末余额', '100')
        with allure.step('增行'):
            self.click_new_template_operate_span('2', 'add')
            self.type_template_info_single_line('3', 'test', '贷', '151102', '转出期末余额', '100')
            self.click_new_template_amount('3')
            assert '3650' in self.get_new_template_amount('3')

    @allure.title('新增结转模板-删行')
    def test_new_template_del_line(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '100')
            self.type_template_info_single_line('2', 'test', '贷', '1002', '转出期末余额', '100')
        with allure.step('删行'):
            self.click_new_template_operate_span('2', 'del')
            assert not self.is_amount_visible('2')

    @allure.title('新增结转模板-必录项校验-名称')
    def test_new_template_verify_name(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            self.click_input_buttons('保存')
            assert '请输入名称' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-摘要')
    def test_new_template_verify_abstract(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.click_input_buttons('保存')
            assert '分录摘要不能为空！' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-科目-第一行')
    def test_new_template_verify_subject_line_one(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_to_new_template_abstract_input('1', 'test')
            self.click_input_buttons('保存')
            assert '第1行分录：科目不存在' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-科目-第二行')
    def test_new_template_verify_subject_line_two(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_to_new_template_abstract_input('1', 'test')
            self.new_template_select_subject('1', '1002')
            self.click_input_buttons('保存')
            assert '第2行分录：科目不存在' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-金额比例小于100')
    def test_new_template_verify_proportion_below_100(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '')
            self.click_input_buttons('保存')
            assert '转入科目金额比例之和不等于100%' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-金额比例大于100')
    def test_new_template_verify_proportion_over_100(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '122')
            self.click_input_buttons('保存')
            assert '金额比例值必须大于等于0，小于等于100' in self.get_all_floating_tip()

    @allure.title('新增结转模板-必录项校验-仅一行分录')
    def test_new_template_verify_only_one_entry(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('录入模板信息'):
            template_name = random_string_generator()
            self.type_to_new_template_name_input(template_name)
            self.type_template_info_single_line('1', 'test', '借', '1001', '转入', '100')
            self.click_new_template_operate_span('2', 'del')
            self.click_input_buttons('保存')
            assert '分录少于2条' in self.get_all_floating_tip()

    @allure.title('新增结转模板-示例图片')
    def test_new_template_demo_img(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('新增模板'):
            self.click_add_box_button()
        with allure.step('展示示例说明'):
            self.click_new_template_demo_button()
            assert self.is_demo_img_visible()
        with allure.step('关闭示例说明'):
            self.click_new_template_demo_button()
            assert not self.is_demo_img_visible()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_carry_forward
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转-生产领料')
class TestRequisitionRawMaterials(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    RequisitionRawMaterialsPage,
    AccountingCommonPage
):
    @allure.title('预置结转模板生成凭证跳转')
    def test_default_template_generate_voucher_requisition_raw_materials(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('生产领料-生成凭证'):
            self.click_generate_voucher_button('生产领料')
            self.switch_to_default_content()
            self.switch_to_requisition_raw_materials_frame()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_carry_forward
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转-结转生产成本')
class TestProductionCosts(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    ProductionCostsPage,
    AccountingCommonPage
):
    @allure.title('预置结转模板生成凭证跳转')
    def test_default_template_generate_voucher_requisition_raw_materials(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('结转生产成本-生成凭证'):
            self.click_generate_voucher_button('结转生产成本')
            self.switch_to_default_content()
            self.switch_to_production_costs_frame()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_carry_forward
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转-结转销售成本')
class TestSellingCosts(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    SellingCostsPage,
    AccountingCommonPage
):
    @allure.title('预置结转模板生成凭证跳转')
    def test_default_template_generate_voucher_requisition_raw_materials(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('结转销售成本-生成凭证'):
            self.click_generate_voucher_button('结转销售成本')
            self.switch_to_default_content()
            self.switch_to_selling_costs_frame()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_carry_forward
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转-资产折旧')
class TestFixedAssetDepreciation(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    SellingCostsPage,
    AccountingCommonPage
):

    @allure.title('预置结转模板生成凭证跳转')
    def test_default_template_generate_voucher_requisition_raw_materials(self):
        company = GetYamlData().get_company('company_accounting_closure_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('结转销售成本-生成凭证'):
            self.click_generate_voucher_button('结转销售成本')
            self.switch_to_default_content()
            self.switch_to_selling_costs_frame()


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_carry_forward
@allure.epic('会计')
@allure.feature('结账')
@allure.story('结转-计提税金')
class TestProvisionOfTaxes(
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    ClosurePage,
    AccountingCommonPage
):
    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-红字提示')
    def test_provision_of_taxes_small_bus_notice(self):
        company = GetYamlData().get_company('company_accounting_closure_007')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            assert '财税〔2022〕10号' in self.get_text_from_taxes_table_2022_notice()

    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-十万以下-按月')
    def test_provision_of_taxes_small_bus_under_10_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_007')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-十万以下-按季')
    def test_provision_of_taxes_small_bus_under_10_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_007')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-十万以上-按月')
    def test_provision_of_taxes_small_bus_above_10_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_008')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-十万以上-按季')
    def test_provision_of_taxes_small_bus_above_10_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_008')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('小规模计提税金-红字提示')
    def test_provision_of_taxes_small_bus_notice(self):
        company = GetYamlData().get_company('company_accounting_closure_006')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            assert '财税〔2022〕10号' in self.get_text_from_taxes_table_2022_notice()

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-勾选-十万以下-按月')
    def test_provision_of_taxes_normal_bus_check_under_10_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_005')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.check_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-勾选-十万以下-按季')
    def test_provision_of_taxes_normal_bus_check_under_10_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_005')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.check_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-勾选-三十万以上-按月')
    def test_provision_of_taxes_normal_bus_check_above_30_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_006')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.check_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-勾选-三十万以上-按季')
    def test_provision_of_taxes_normal_bus_check_above_30_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_006')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.check_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '50' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '50' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-不勾选-十万以下-按月')
    def test_provision_of_taxes_normal_bus_uncheck_under_10_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_005')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.uncheck_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '0' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-勾选-十万以下-按季')
    def test_provision_of_taxes_normal_bus_uncheck_under_10_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_005')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.uncheck_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '0' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '100' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-不勾选-三十万以上-按月')
    def test_provision_of_taxes_normal_bus_uncheck_above_30_by_month(self):
        company = GetYamlData().get_company('company_accounting_closure_006')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按月计提')
            self.uncheck_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '0' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '0' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '0' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')

    @allure.tag('R20230626-058')
    @allure.title('一般纳税人计提税金-不勾选-三十万以上-按季')
    def test_provision_of_taxes_normal_bus_uncheck_above_30_by_season(self):
        company = GetYamlData().get_company('company_accounting_closure_006')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('计提税金'):
            self.click_generate_operate_button('计提税金', 'setting')
            self.click_accounting_focus_table_input_radio_by_label('按季计提')
            self.uncheck_taxes_table_small_profit_input()
            self.click_accounting_focus_table_buttons('确定')
            assert '设置成功' in self.get_all_floating_tip()
            self.click_generate_operate_button('计提税金', 'setting')
            assert '0' == self.get_text_from_taxes_table_input_value('1', 'reduceTaxRate')
            assert '0' == self.get_text_from_taxes_table_input_value('2', 'reduceTaxRate')
            assert '0' == self.get_text_from_taxes_table_input_value('3', 'reduceTaxRate')


@pytest.mark.accounting
@pytest.mark.accounting_closure
@pytest.mark.accounting_closure_check
@allure.epic('会计')
@allure.feature('结账')
@allure.story('期末检查')
class TestClosureCheck(
    LoginPage,
    AccountingHomePage,
    ClosurePage,
    FinalInspectionPage,
    ManagerCommonPage,
    ManagerHomePage,
    AgencyAccountPage,
    CustomerPage
):
    @allure.title('结账页面重新检测')
    def test_closure_check(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('重新检测')
            self.wait_for_closure_check_button_disappear()
        with allure.step('进入报告'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            assert self.is_report_present()

    @allure.title('进入报告后重新检测')
    def test_closure_check(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            self.click_final_inspection_re_check_button()
            assert self.is_report_present()

    @allure.title('首次检测')
    def test_create_account_set_accounting_standards_for_small_business(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
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
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('小企业会计准则（2013年版）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert company_name == self.get_company_name()
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('立即检测')
            self.wait_for_closure_check_button_disappear()
        with allure.step('进入报告'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            assert self.is_report_present()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(company_name)
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(company_name)

    @allure.title('检测报告计算公式悬停提示框内容对比-资产原值不相符')
    def test_closure_check_report_tips_check_asset_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '资产原值不相符'
            self.click_report_formula_tips_by_label(tips_label)
            assert '1,090,420.89' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '1,090,420.89' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)
            assert '相符' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 4)

    @allure.title('检测报告计算公式悬停提示框内容对比-累计折旧不相符')
    def test_closure_check_report_tips_check_depreciation_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '累计折旧不相符'
            self.click_report_formula_tips_by_label(tips_label)
            assert '463,204.02' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '527,470.43' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '-64,266.41' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)
            assert '请检查是否未生成【计提折旧】凭证' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 4)

    @allure.title('检测报告计算公式悬停提示框内容对比-现金赤字或余额过大提醒')
    def test_closure_check_report_tips_check_cash_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '现金赤字或余额过大提醒'
            self.click_report_icon_tips_by_label(tips_label)
            assert '库存现金余额一般控制的比例是3-5天，最多不能超过15天的现金支付金额。\n' \
                   '如果库存现金余额大于（上月库存现金科目贷方发生额合计/30）*15，则会提示库存现金余额过大' == \
                   self.get_text_from_report_icon_tips_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-库存商品')
    def test_closure_check_report_tips_check_inventory_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '库存商品'
            self.click_report_icon_tips_by_label(tips_label)
            assert '库存商品一般不存在为负数' == \
                   self.get_text_from_report_icon_tips_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-原材料')
    def test_closure_check_report_tips_check_materials_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '原材料'
            self.click_report_icon_tips_by_label(tips_label)
            assert '原材料一般不存在为负数' == \
                   self.get_text_from_report_icon_tips_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-应收账款期末余额')
    def test_closure_check_report_tips_check_accounts_receivable_closing_balance_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '应收账款期末余额'
            self.click_report_formula_tips_by_label(tips_label)
            assert '1131 应收账款期末余额 3,372,243.68  = 3,372,243.68\n利润表本年累计营业收入 = 0.00' \
                   == self.get_text_from_report_formula_tips_p_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-预收账款期末余额')
    def test_closure_check_report_tips_check_closing_balance_of_advance_receivables_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '预收账款期末余额'
            self.click_report_formula_tips_by_label(tips_label)
            assert ' = 0.00\n利润表本年累计营业收入 = 0.00' == self.get_text_from_report_formula_tips_p_value(
                tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-资产负债率')
    def test_closure_check_report_tips_check_gearing_ratio_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '资产负债率'
            self.click_report_icon_tips_by_label(tips_label)
            assert '资产负债率=资产负债表总负债/资产负债表总资产' == \
                   self.get_text_from_report_icon_tips_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-利润率')
    def test_closure_check_report_tips_check_profit_ratio_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '利润率'
            self.click_report_icon_tips_by_label(tips_label)
            assert '本年累计利润率=利润表利润总额本年累计金额/利润表营业收入本年累计金额' == \
                   self.get_text_from_report_icon_tips_value(tips_label)

    @allure.title('检测报告计算公式悬停提示框内容对比-业务招待费')
    def test_closure_check_report_tips_check_business_hospitality_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '业务招待费'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00* 60% = 0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '0.00*5‰ =0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过【营业收入】5‰\n 政策：企业发生的与生产经营活动有关的业务招待费支出，按照发生额的60%扣除，' \
                   '但最高不得超过当年销售（营业）收入的5‰' == self.get_text_from_report_formula_tips_td_value(tips_label,
                                                                                                             2, 3)

    @allure.title('检测报告计算公式悬停提示框内容对比-工会经费')
    def test_closure_check_report_tips_check_union_funding_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '工会经费'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '制造费用_工资(52106.59)+管理费用_工资(23511.57)+营业费用_工资及福利费(0)+生产成本_工资(62580.1)*2% =2,763.97' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过工资总额2%\n 政策：企业拨缴的工会经费，不超过工资薪金总额2%的部分，准予扣除' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)

    @allure.title('检测报告计算公式悬停提示框内容对比-职工福利费')
    def test_closure_check_report_tips_check_employee_welfare_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '职工福利费'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '制造费用_工资(52106.59)+管理费用_工资(23511.57)+营业费用_工资及福利费(0)+生产成本_工资(62580.1)*14% =19,347.76' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过工资总额14%\n 政策：职工福利费支出，不超过工资薪金总额14%的部分，准予扣除' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)

    @allure.title('检测报告计算公式悬停提示框内容对比-职工教育经费')
    def test_closure_check_report_tips_check_funds_for_employee_education_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '职工教育经费'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '制造费用_工资(52106.59)+管理费用_工资(23511.57)+营业费用_工资及福利费(0)+生产成本_工资(62580.1)*8%=11,055.86' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过工资总额8%\n 政策：企业发生的职工教育经费支出，不超过工资薪金总额8%的部分，' \
                   '准予在计算企业所得税应纳税所得额时扣除；超过部分，准予在以后纳税年度结转扣除。' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)

    @allure.title('检测报告计算公式悬停提示框内容对比-广告费和业务宣传费')
    def test_closure_check_report_tips_check_advertising_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '广告费和业务宣传费'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '0.00*15% =0.00' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过营业收入15%\n 政策：企业发生的符合条件的广告费和业务宣传费支出，除国务院财政、税务主管部门另有规定外，' \
                   '不超过当年销售(营业)收入15%的部分，准予扣除;超过部分，准予在以后纳税年度结转扣除。' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)

    @allure.title('检测报告计算公式悬停提示框内容对比-捐赠支出')
    def test_closure_check_report_tips_check_advertising_tips(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('结账')
            self.switch_to_closure_frame()
        with allure.step('开始结账检查'):
            self.click_closure_check_buttons('查看报告')
        with allure.step('重新检测'):
            self.switch_to_default_content()
            self.switch_to_final_inspection_frame()
            tips_label = '捐赠支出'
            self.click_report_formula_tips_by_label(tips_label)
            assert '0.00' == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 1)
            assert '-23,511.57*12% =-2,821.39' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 2)
            assert '未超过利润总额12%\n 政策：企业当年发生以及以前年度结转的公益性捐赠支出，不超过年度利润总额12%的部分，准予扣除。' \
                   == self.get_text_from_report_formula_tips_td_value(tips_label, 2, 3)
