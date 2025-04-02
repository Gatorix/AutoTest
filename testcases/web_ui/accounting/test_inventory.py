import allure
import pytest

from page.web_ui.accounting.page_voucher import VoucherDetailPage
from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.page_login import LoginPage
from page.web_ui.accounting.page_home import AccountingHomePage
from page.web_ui.accounting.page_inventory import (InventorySettingPage,
                                                   InventoryManagePage,
                                                   InventoryOutboundEntryPage,
                                                   InventoryWarehousingEntryPage,
                                                   InventoryNewEntryPage,
                                                   InventoryDetailPage,
                                                   InventorySummaryPage)
from page.web_ui.accounting.page_common import AccountingCommonPage
from utils.excel_utils import check_excel_diff
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.yml import GetYamlData


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_setting
@allure.epic('会计')
@allure.feature('存货')
@allure.story('基础设置')
class TestInventorySetting(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventorySettingPage
):
    @allure.title('导入库存初始数据-未选择文件')
    def test_import_init_inventory_unselected(self):
        company = GetYamlData().get_company('company_accounting_inventory_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导入文件'):
            self.click_inventory_setting_buttons('导入')
            self.click_inventory_setting_buttons('导入B')
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.title('导入库存初始数据')
    def test_import_init_inventory(self):
        company = GetYamlData().get_company('company_accounting_inventory_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导入文件'):
            self.click_inventory_setting_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/库存初始数据导入模板-001.xlsx')
            self.click_inventory_setting_buttons('导入B')
            assert '导入成功' in self.get_all_floating_tip()

    @allure.title('导入库存初始数据')
    def test_import_init_inventory(self):
        company = GetYamlData().get_company('company_accounting_inventory_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导入文件'):
            self.click_inventory_setting_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/common/错误文件类型.zip')
            self.click_inventory_setting_buttons('导入B')
            assert '只能上传*.xls、*.xlsx、*.xml文件！' in self.get_all_floating_tip()

    @allure.title('导入库存初始数据')
    def test_import_init_inventory(self):
        company = GetYamlData().get_company('company_accounting_inventory_001')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导入文件'):
            self.click_inventory_setting_buttons('导入')
            self.click_inventory_setting_buttons('导入B')
            assert '请添加附件' in self.get_all_floating_tip()

    @allure.title('修改初始数量')
    def test_modify_init_quantity(self):
        company = GetYamlData().get_company('company_accounting_inventory_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('修改数量'):
            ori_quantity = self.get_init_quantity_input_by_num('CH001')
            self.set_init_quantity_input_by_num('CH001', str(int(ori_quantity) + 1))
            self.click_inventory_setting_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()

    @allure.title('修改初始金额')
    def test_modify_init_amount(self):
        company = GetYamlData().get_company('company_accounting_inventory_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('修改数量'):
            ori_quantity = self.get_init_amount_input_by_num('CH002')
            self.set_init_amount_input_by_num('CH002', str(int(ori_quantity) + 1))
            self.click_inventory_setting_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_manage
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货管理')
class TestInventoryManage(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventoryManagePage
):

    @allure.title('新增并删除存货类别-表格行')
    def test_add_and_delete_inventory_class_inline(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('新增存货类别'):
            new_type = 'test-001'
            self.click_inventory_manage_buttons('新增')
            self.add_inventory_type_default(new_type)
            self.click_input_buttons('保存')
            assert '存货保存成功' in self.get_all_floating_tip()
        with allure.step('表格行删除存货类别'):
            self.click_input_buttons('关闭')
            self.click_in_line_buttons_by_id(new_type, '删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @pytest.mark.p1
    @allure.title('新增并删除存货类别-勾选删除')
    def test_add_and_delete_inventory_class_button(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('新增存货类别'):
            new_type = 'test-002'
            self.click_inventory_manage_buttons('新增')
            self.add_inventory_type_default(new_type)
            self.click_input_buttons('保存')
            assert '存货保存成功' in self.get_all_floating_tip()
        with allure.step('勾选删除存货类别'):
            self.click_input_buttons('关闭')
            self.click_in_line_checkbox_by_id(new_type)
            self.click_inventory_manage_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('修改存货类别')
    def test_modify_inventory_class(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('修改存货类别'):
            self.click_in_line_buttons_by_id('CH010', '编辑')
            self.click_input_buttons('确定')
            assert '存货保存成功' in self.get_all_floating_tip()

    @allure.title('新增存货类别-编码包含下划线')
    def test_add_inventory_class_contains_underline(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('新增存货类别'):
            new_type = random_string_generator()
            self.click_inventory_manage_buttons('新增')
            self.add_inventory_type_default(new_type)
            self.click_input_buttons('保存')
            assert '存货保存失败！编码不允许存在下划线，请重新输入！' in self.get_all_floating_tip()

    @allure.title('新增存货类别-必录校验-编码')
    def test_add_inventory_class_verify_id(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('新增存货类别'):
            self.click_inventory_manage_buttons('新增')
            self.click_input_buttons('保存')
            assert '编码不能为空' in self.get_verify_text('编码')

    @allure.title('新增存货类别-必录校验-名称')
    def test_add_inventory_class_verify_name(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('新增存货类别'):
            new_type = random_string_generator()
            self.click_inventory_manage_buttons('新增')
            self.type_to_add_inventory_type_inputs('编码', new_type)
            self.click_input_buttons('保存')
            assert '名称不能为空' in self.get_verify_text('名称')

    @allure.title('导入')
    def test_inventory_class_import(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('导入存货类别'):
            self.click_inventory_manage_buttons('导入')
            self.click_inventory_manage_buttons('下一步')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/存货类型导入-001.xls')
            self.click_inventory_manage_buttons('导入')
            assert '1' in self.get_import_success_result()
            self.click_buttons_text('返回存货列表')
        with allure.step('删除存货类别'):
            self.click_in_line_checkbox_by_id('test-import')
            self.click_inventory_manage_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入-未选择文件')
    def test_inventory_class_import_unselect_file(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('导入存货类别'):
            self.click_inventory_manage_buttons('导入')
            self.click_inventory_manage_buttons('下一步')
            self.click_inventory_manage_buttons('导入')
            assert '请选择要上传的文件' in self.get_all_floating_tip()

    @allure.title('导入-错误文件类型')
    def test_inventory_class_import_error_file_type(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('导入存货类别'):
            self.click_inventory_manage_buttons('导入')
            self.click_inventory_manage_buttons('下一步')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/common/错误文件类型.zip')
            assert '只能上传*.xls、*.xlsx、*.xml文件' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-12-18')
    @allure.tag('R20231108-019')
    @allure.title('存货管理-系统存货列表显示不完整')
    def test_inv_list_display_incomplete(self):
        company = GetYamlData().get_company('proj_R20231108-019')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('进入系统商品页'):
            self.click_inventory_manage_buttons('发票商品对应系统存货')
            self.wait(1)
            assert self.is_line_visible('CH00026')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_warehousing_entry
@allure.epic('会计')
@allure.feature('存货')
@allure.story('入库单')
class TestInventoryWarehousingEntry(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventoryWarehousingEntryPage,
    InventoryNewEntryPage
):

    @allure.title('复制-未勾选')
    def test_copy_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('复制入库单'):
            self.click_inventory_warehousing_entry_buttons('复制')
            assert '请选择要复制的单据' in self.get_all_floating_tip()

    @allure.title('删除-未勾选')
    def test_delete_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('删除入库单'):
            self.click_inventory_warehousing_entry_buttons('删除')
            assert '请选择要删除的数据' in self.get_all_floating_tip()

    @allure.title('更改单据类型-未勾选')
    def test_change_bill_type_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('删除入库单'):
            self.click_inventory_warehousing_entry_buttons('更改单据类型')
            assert '请选择需要指定单据类型的数据' in self.get_all_floating_tip()

    @allure.title('新增产品入库单-未录入')
    def test_new_product_warehousing_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增材料入库单-未录入')
    def test_new_material_warehousing_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增材料入库单'):
            self.click_inventory_warehousing_entry_buttons('材料入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增周转材料入库单-未录入')
    def test_new_turnover_material_warehousing_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增周转材料入库单'):
            self.click_inventory_warehousing_entry_buttons('周转材料入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增产品入库单')
    def test_new_turnover_material_warehousing_entry(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            bill_number = self.get_table_head_inputs_value('单据编号')
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('删除数据'):
            self.switch_to_default_content()
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
            self.click_list_bill_type(bill_number)
            self.click_inventory_warehousing_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增并复制产品入库单')
    def test_copy_turnover_material_warehousing_entry(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            bill_number = self.get_table_head_inputs_value('单据编号')
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('复制产品入库单'):
            self.click_inventory_new_entry_buttons('复制')
            assert '复制成功，请保存数据！' in self.get_all_floating_tip()
            bill_number_copy = self.get_table_head_inputs_value('单据编号')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('删除数据'):
            self.switch_to_default_content()
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
            self.click_list_checkbox_by_bill_number(bill_number)
            self.click_list_checkbox_by_bill_number(bill_number_copy)
            self.click_inventory_warehousing_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增产品入库单-必录校验-存货编码')
    def test_new_turnover_material_warehousing_entry_verify_id(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '请选择存货编码' in self.get_all_floating_tip()

    @allure.title('新增产品入库单-必录校验-数量')
    def test_new_turnover_material_warehousing_entry_verify_qty(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('存货编码', 'CH001')
            self.click_inventory_new_entry_buttons('保存')
            assert '请输入数量' in self.get_all_floating_tip()

    @allure.title('新增产品入库单-单价计算校验')
    def test_new_turnover_material_warehousing_entry_verify_unit_price(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('新增产品入库单'):
            self.click_inventory_warehousing_entry_buttons('产品入库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '6.33')
            self.type_to_table_cells('金额', '22.12')
            assert '3.49447077' == self.get_table_cells_value('单价')

    @allure.title('更改单据类型-材料入库单')
    def test_warehousing_entry_type_material(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'RKD2023010002'
            bill_type = '材料入库单'
            self.click_list_bill_type(bill)
            self.click_inventory_warehousing_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_warehousing_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('更改单据类型-产品入库单')
    def test_warehousing_entry_type_product(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'RKD2023010001'
            bill_type = '产品入库单'
            self.click_list_bill_type(bill)
            self.click_inventory_warehousing_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_warehousing_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('更改单据类型-周转材料入库单')
    def test_warehousing_entry_type_turnover_material(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'RKD2023010003'
            bill_type = '周转材料入库单'
            self.click_list_bill_type(bill)
            self.click_inventory_warehousing_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_warehousing_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('导入入库单-新增导入')
    def test_warehousing_entry_import_add(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            bill = 'RKD2020020001'
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/入库单导入-001.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()
        with allure.step('删除单据'):
            self.click_inventory_warehousing_entry_buttons('刷新')
            self.click_list_checkbox_by_bill_number(bill)
            self.click_inventory_warehousing_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入入库单-新增导入-已存在')
    def test_warehousing_entry_import_add_exist(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/入库单导入-003.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '导入成功,共导入0张,跳过1张' in self.get_all_floating_tip()

    @allure.title('导入入库单-覆盖导入')
    def test_warehousing_entry_import_new(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            bill = 'RKD2020020002'
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/入库单导入-002.xlsx')
            self.click_import_type_radio('1')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()
        with allure.step('删除单据'):
            self.click_inventory_warehousing_entry_buttons('刷新')
            self.click_list_checkbox_by_bill_number(bill)
            self.click_inventory_warehousing_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入入库单-覆盖导入-已存在')
    def test_warehousing_entry_import_new_exist(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/入库单导入-004.xlsx')
            self.click_import_type_radio('1')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()

    @allure.title('导入入库单-新增导入-编码错误')
    def test_warehousing_entry_import_add_error_class(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/入库单导入-005.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '导入失败，文件5行存货编码不存在' in self.get_all_floating_tip()

    @allure.title('导入入库单-文件类型错误')
    def test_warehousing_entry_import_error_file(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('导入'):
            self.click_inventory_warehousing_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/common/错误文件类型.zip')
            self.click_inventory_warehousing_entry_buttons('导入B')
            assert '只能上传*.xls、*.xlsx、*.xml文件！' in self.get_all_floating_tip()

    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230815-039')
    @allure.title('按凭证生成入库单没有往来单位，凭证是有供应商的')
    def test_generate_warehousing_entry_by_voucher_empty_supplier_R20230815_039(self):
        company = GetYamlData().get_company('proj_R20230815-039')
        bill = 'RKD2023060001'
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('删除入库单'):
            if self.is_element_visible(self.list_checkbox_by_bill_number(bill)):
                self.click_inventory_warehousing_entry_buttons('刷新')
                self.click_list_checkbox_by_bill_number(bill)
                self.click_inventory_warehousing_entry_buttons('删除')
                self.click_input_buttons('确定')
                assert '删除成功' in self.get_all_floating_tip()
        with allure.step('自动生成入库单'):
            self.click_inventory_warehousing_entry_buttons('自动生成入库单')
            self.click_auto_gen_bill_by_type_radio('按凭证自动生成入库单')
            self.click_auto_gen_bill_step_span('下一步')
            self.click_auto_gen_bill_step_span('下一步')
            assert '生成成功,共生成1条记录！' in self.get_all_floating_tip()
            assert '北京勤十诚文化传媒有限公司' == self.get_text_from_warehousing_entry_table_customer_td_by_bill_num(
                bill)

    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230728-047')
    @allure.title('入库单有根据凭证生成，但是没有往来单位，也无法手动选择往来单位，科目挂的往来核算的辅助核算')
    def test_generate_warehousing_entry_by_voucher_empty_supplier_R20230728_047(self):
        company = GetYamlData().get_company('proj_R20230728-047')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('自动生成入库单'):
            self.click_inventory_warehousing_entry_buttons('自动生成入库单')
            self.click_auto_gen_bill_by_type_radio('按凭证自动生成入库单')
            self.click_auto_gen_bill_step_span('下一步')
            self.click_auto_gen_bill_step_span('下一步')
            assert '生成成功,共生成3条记录！' in self.get_all_floating_tip()
            assert '往来单位1' == self.get_text_from_warehousing_entry_table_customer_td_by_voucher_num('记-1')
            assert '往来1' == self.get_text_from_warehousing_entry_table_customer_td_by_voucher_num('记-2')
        with allure.step('删除入库单'):
            self.click_inventory_warehousing_entry_buttons('刷新')
            self.click_warehousing_entry_select_all()
            self.click_inventory_warehousing_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_outbound_entry
@allure.epic('会计')
@allure.feature('存货')
@allure.story('出库单')
class TestInventoryOutboundEntry(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventoryOutboundEntryPage,
    InventoryNewEntryPage
):

    @allure.title('复制-未勾选')
    def test_copy_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('复制出库单'):
            self.click_inventory_outbound_entry_buttons('复制')
            assert '请选择要复制的单据' in self.get_all_floating_tip()

    @allure.title('删除-未勾选')
    def test_delete_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('删除出库单'):
            self.click_inventory_outbound_entry_buttons('删除')
            assert '请选择要删除的数据' in self.get_all_floating_tip()

    @allure.title('更改单据类型-未勾选')
    def test_change_bill_type_unselect(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('删除出库单'):
            self.click_inventory_outbound_entry_buttons('更改单据类型')
            assert '请选择需要指定单据类型的数据' in self.get_all_floating_tip()

    @allure.title('新增产品出库单-未录入')
    def test_new_product_outbound_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增材料出库单-未录入')
    def test_new_material_outbound_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增材料出库单'):
            self.click_inventory_outbound_entry_buttons('材料出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增周转材料出库单-未录入')
    def test_new_turnover_material_outbound_entry_empty(self):
        company = GetYamlData().get_company('company_accounting_inventory_003')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增周转材料出库单'):
            self.click_inventory_outbound_entry_buttons('周转材料出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.click_inventory_new_entry_buttons('保存')
            assert '请录入数据' in self.get_all_floating_tip()

    @allure.title('新增产品出库单')
    def test_new_turnover_material_outbound_entry(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            bill_number = self.get_table_head_inputs_value('单据编号')
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('删除数据'):
            self.switch_to_default_content()
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
            self.click_list_bill_type(bill_number)
            self.click_inventory_outbound_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增并复制产品出库单')
    def test_copy_turnover_material_outbound_entry(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            bill_number = self.get_table_head_inputs_value('单据编号')
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('复制产品出库单'):
            self.click_inventory_new_entry_buttons('复制')
            assert '复制成功，请保存数据！' in self.get_all_floating_tip()
            bill_number_copy = self.get_table_head_inputs_value('单据编号')
            self.click_inventory_new_entry_buttons('保存')
            assert '保存成功' in self.get_all_floating_tip()
        with allure.step('删除数据'):
            self.switch_to_default_content()
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
            self.click_list_bill_type(bill_number)
            self.click_inventory_outbound_entry_buttons('删除')
            self.click_input_buttons('确定')
            self.click_list_bill_type(bill_number_copy)
            self.click_inventory_outbound_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('新增产品出库单-必录校验-存货编码')
    def test_new_turnover_material_outbound_entry_verify_id(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('数量', '2')
            self.type_to_table_cells('金额', '50')
            self.click_inventory_new_entry_buttons('保存')
            assert '请选择存货编码' in self.get_all_floating_tip()

    @allure.title('新增产品出库单-必录校验-数量')
    def test_new_turnover_material_outbound_entry_verify_qty(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('存货编码', 'CH001')
            self.click_inventory_new_entry_buttons('保存')
            assert '请输入数量' in self.get_all_floating_tip()

    @allure.title('新增产品出库单-单价计算校验')
    def test_new_turnover_material_outbound_entry_verify_unit_price(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('新增产品出库单'):
            self.click_inventory_outbound_entry_buttons('产品出库单')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            self.type_to_table_cells('存货编码', 'CH001')
            self.type_to_table_cells('数量', '6.33')
            self.type_to_table_cells('金额', '22.12')
            assert '3.49447077' == self.get_table_cells_value('单价')

    @allure.title('更改单据类型-材料出库单')
    def test_outbound_entry_type_material(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'CKD2023010002'
            bill_type = '材料出库单'
            self.click_list_bill_type(bill)
            self.click_inventory_outbound_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_outbound_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('更改单据类型-产品出库单')
    def test_outbound_entry_type_product(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'CKD2023010001'
            bill_type = '产品出库单'
            self.click_list_bill_type(bill)
            self.click_inventory_outbound_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_outbound_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('更改单据类型-周转材料出库单')
    def test_outbound_entry_type_turnover_material(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('更改单据类型'):
            bill = 'CKD2023010003'
            bill_type = '周转材料出库单'
            self.click_list_bill_type(bill)
            self.click_inventory_outbound_entry_buttons('更改单据类型')
            self.change_bill_type(bill_type)
            self.click_inventory_outbound_entry_buttons('确定')
            assert '更改单据类型成功' in self.get_all_floating_tip()
            assert bill_type == self.get_list_bill_type(bill)

    @allure.title('导入出库单-新增导入')
    def test_outbound_entry_import_add(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            bill = 'CKD2020020001'
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/出库单导入-001.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()
        with allure.step('删除单据'):
            self.click_inventory_outbound_entry_buttons('刷新')
            self.click_list_checkbox_by_bill_number(bill)
            self.click_inventory_outbound_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入出库单-新增导入-已存在')
    def test_outbound_entry_import_add_exist(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/出库单导入-003.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '导入成功,共导入0张,跳过1张' in self.get_all_floating_tip()

    @allure.title('导入出库单-覆盖导入')
    def test_outbound_entry_import_new(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            bill = 'CKD2020020002'
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/出库单导入-002.xlsx')
            self.click_import_type_radio('1')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()
        with allure.step('删除单据'):
            self.click_inventory_outbound_entry_buttons('刷新')
            self.click_list_checkbox_by_bill_number(bill)
            self.click_inventory_outbound_entry_buttons('删除')
            self.click_input_buttons('确定')
            assert '删除成功' in self.get_all_floating_tip()

    @allure.title('导入出库单-覆盖导入-已存在')
    def test_outbound_entry_import_new_exist(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/出库单导入-004.xlsx')
            self.click_import_type_radio('1')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '导入成功,共导入1张' in self.get_all_floating_tip()

    @allure.title('导入出库单-新增导入-编码错误')
    def test_outbound_entry_import_add_error_class(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/accounting/inventory/出库单导入-005.xlsx')
            self.click_import_type_radio('0')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '导入失败，文件5行存货编码不存在' in self.get_all_floating_tip()

    @allure.title('导入出库单-文件类型错误')
    def test_outbound_entry_import_error_file(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '出库单')
            self.switch_to_outbound_entry_frame()
        with allure.step('导入'):
            self.click_inventory_outbound_entry_buttons('导入')
            self.send_filepath_to_input(
                f'{get_project_path()}/template/common/错误文件类型.zip')
            self.click_inventory_outbound_entry_buttons('导入B')
            assert '只能上传*.xls、*.xlsx、*.xml文件！' in self.get_all_floating_tip()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_summary
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货汇总表')
class TestInventorySummary(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventorySummaryPage,
    InventoryDetailPage
):

    @allure.title('联查存货明细')
    def test_link_to_inventory_detail(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('联查存货明细'):
            self.click_inventory_detail_link('CH00011')
            self.switch_to_default_content()
            self.switch_to_inventory_detail_frame()
            assert 'CH00011' in self.get_inventory_class()

    @allure.tag('【管家】2023-11-17')
    @allure.tag('R20231011-070')
    @allure.title('存货汇总表分页')
    def test_split_page(self):
        company = GetYamlData().get_company('proj_R20231011-070')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-10', '2023-10')
            self.click_inventory_summary_buttons('刷新')
            self.wait_for_loading_finish()
        with allure.step('检查当前页行数'):
            assert 502 == self.get_total_num_grid_table_tr()


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_detail
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货收发明细表')
class TestInventoryDetail(
    VoucherDetailPage,
    AgencyAccountPage,
    ManagerCommonPage,
    LoginPage,
    ManagerHomePage,
    AccountingHomePage,
    AccountingCommonPage,
    InventoryDetailPage,
    InventoryNewEntryPage
):

    @allure.title('未选择存货查询')
    def test_query_inventory_detail_unselected(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.type_to_inventory('')
            self.click_inventory_detail_buttons('刷新')
            assert '请先选择存货！' in self.get_all_floating_tip()

    @allure.title('联查单据')
    def test_query_inventory_link_to_bill(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.select_inventory('CH00011 铜覆铝  KG')
            self.click_inventory_detail_buttons('刷新')
        with allure.step('联查单据'):
            self.click_bill_link('RKD2023030006')
            self.switch_to_default_content()
            self.switch_to_new_entry_frame()
            assert 'RKD2023030006' == self.get_table_head_inputs_value('单据编号')

    @allure.title('联查凭证')
    def test_query_inventory_link_to_voucher(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.select_inventory('002 AS2003上盖   PCS')
            self.click_inventory_detail_buttons('刷新')
        with allure.step('联查凭证'):
            self.click_voucher_link('RKD2023030003')
            self.switch_to_default_content()
            self.switch_to_voucher_detail_frame()
            assert 'AS2003上盖AS2003上盖' in self.get_voucher_summary('1')


@pytest.mark.ui
@pytest.mark.accounting
@pytest.mark.accounting_inventory
@pytest.mark.accounting_inventory_export
@allure.epic('会计')
@allure.feature('存货')
@allure.story('导出')
class TestInventoryExport(
    LoginPage,
    AgencyAccountPage,
    ManagerCommonPage,
    ManagerHomePage,
    AccountingHomePage,
    InventorySettingPage,
    InventoryManagePage,
    InventoryWarehousingEntryPage,
    InventorySummaryPage,
    InventoryDetailPage
):

    @allure.title('导出库存初始模板')
    def test_inventory_export_init_inventory_template(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导出模板'):
            self.click_inventory_setting_buttons('导入')
            self.click_download_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/库存初始数据导入模板.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出库存初始列表')
    def test_inventory_export_init_inventory(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '基础设置')
            self.switch_to_inventory_setting_frame()
        with allure.step('进入库存初始数据'):
            self.click_inventory_setting_buttons('库存初始数据')
        with allure.step('导出模板'):
            self.click_inventory_setting_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/库存初始数量-002.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('下载导入模板')
    def test_inventory_import_template(self):
        company = GetYamlData().get_company('company_accounting_inventory_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('下载导入模板'):
            self.click_inventory_manage_buttons('导入')
            self.inventory_manage_click_download_template()
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/存货类型导入模板.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货类型列表')
    def test_inventory_class_export(self):
        company = GetYamlData().get_company('company_accounting_inventory_002')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货管理')
            self.switch_to_inventory_manage_frame()
        with allure.step('下载导入模板'):
            self.click_inventory_manage_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/存货类型导出-001.xls',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('入库单导入模板')
    def test_import_warehousing_entry_template(self):
        company = GetYamlData().get_company('company_accounting_inventory_004')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '入库单')
            self.switch_to_warehousing_entry_frame()
        with allure.step('下载导入模板'):
            self.click_inventory_warehousing_entry_buttons('导入')
            self.click_text_buttons('下载库存单据导入模板')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/库存单据导入模板.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货汇总表-默认')
    def test_inventory_summary_default(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509210022全部@存货收发汇总表#202301至202303.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货汇总表-按月汇总')
    def test_inventory_summary_by_month(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_checkbox('按月汇总')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205719全部@存货收发汇总表#202301至202303.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货汇总表-显示全部')
    def test_inventory_summary_display_all(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_checkbox('显示全部')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205828全部@存货收发汇总表#202301至202303.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货汇总表-显示金额')
    def test_inventory_summary_display_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_checkbox('显示金额')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205832全部@存货收发汇总表#202301至202303.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货汇总表-勾选全部')
    def test_inventory_summary_check_all(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货汇总表')
            self.switch_to_inventory_summary_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_checkbox('按月汇总')
            self.click_checkbox('显示全部')
            self.click_checkbox('显示金额')
            self.click_inventory_summary_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_summary_buttons('导出')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205637全部@存货收发汇总表#202301至202303.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货收发明细表-导出单个')
    def test_inventory_detail_export_present(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.select_inventory('CH00011 铜覆铝  KG')
            self.click_inventory_detail_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_detail_buttons('导出当前存货')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205528存货收发明细表.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货收发明细表-导出单个-显示金额')
    def test_inventory_detail_export_present_display_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.select_inventory('CH00011 铜覆铝  KG')
            self.click_detail_checkbox()
            self.click_inventory_detail_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_detail_buttons('导出当前存货')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/inventory/20240509205503存货收发明细表#202301至202303.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货收发明细表-导出全部')
    def test_inventory_detail_export_all(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_inventory_detail_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_detail_buttons('导出全部存货')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(f'{get_project_path()}/template/accounting/inventory/20240509205003存货收发明细表.xlsx',
                                    f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出存货收发明细表-导出全部-显示金额')
    def test_inventory_detail_export_all_display_amount(self):
        company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
        with allure.step('登录'):
            self.login(company=company)
        with allure.step('点击会计菜单'):
            self.click_accounting_menu('库存', '存货收发明细表')
            self.switch_to_inventory_detail_frame()
        with allure.step('输入过滤条件'):
            self.select_period('2023-01', '2023-03')
            self.click_detail_checkbox()
            self.click_inventory_detail_buttons('刷新')
        with allure.step('导出并比对excel文件'):
            self.click_inventory_detail_buttons('导出全部存货')
            tmp_filename = f'{random_string_generator()}.{self.get_downloaded_filename().split(".")[1]}'
            self.rename_downloaded_file(tmp_filename)
        with allure.step('对比excel文件差异'):
            assert check_excel_diff(
                f'{get_project_path()}/template/accounting/inventory/20240509205238存货收发明细表#202301至202303.xlsx',
                f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
