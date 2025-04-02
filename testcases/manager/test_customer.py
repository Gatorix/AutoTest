import allure
import pytest

from page.manager.page_agency import AgencyAccountPage
from page.manager.page_business import BusinessServicePage
from page.manager.page_contract import ContractExpirePage, ContractPage, ContractInvoicePage, ContractChangeRecordPage
from page.manager.page_items import ItemsPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.manager.page_customer import CustomerPage, LostManagePage
from page.manager.page_common import ManagerCommonPage

from utils.date_time_utils import get_today
from utils.random_data import random_string_generator
from utils.file_utils import get_project_path


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_manage
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('客户')
class TestCustomer(LoginPage, ManagerHomePage, ManagerCommonPage, CustomerPage, AgencyAccountPage):

    @allure.title('查看外勤')
    def test_click_field(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
        with allure.step('查看外勤'):
            self.click_table_buttons(company_name, '查看外勤')
        with allure.step('检查页签'):
            assert self.is_top_label_appear('外勤任务')

    @allure.title('查看合同')
    def test_click_contract(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
        with allure.step('查看合同'):
            self.click_table_buttons(company_name, '查看合同')
        with allure.step('检查页签'):
            assert self.is_top_label_appear('合同')

    @allure.title('新增并删除客户-代理记账')
    def test_create_and_delete_customer_bookkeeping(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.input_contract_details('2023-01', '2023-12')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('新增并删除客户-工商注册')
    def test_create_and_delete_customer_login(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.input_contract_details('2023-01', '2023-12')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('新增并删除客户-工商变更')
    def test_create_and_delete_customer_change(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商变更')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('新增并删除客户-工商注销')
    def test_create_and_delete_customer_logout(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注销')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('申请流失-未勾选')
    def test_lost_customer_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('点击申请流失'):
            self.close_ads()
            self.click_normal_button('申请流失')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('申请流失-未输入停止时间')
    def test_lost_customer_date_empty(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('点击申请流失'):
            self.close_ads()
            self.click_normal_button('申请流失')
        with allure.step('直接确定'):
            self.click_customer_area_label_button('流失申请', '确 定')
            assert '请选择预计服务停止时间' in self.get_tip_text()

    @allure.title('申请流失-未输入流失分类')
    def test_lost_customer_type_empty(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('点击申请流失'):
            self.close_ads()
            self.click_normal_button('申请流失')
        with allure.step('输入流失时间'):
            self.click_customer_area_label_input_date('流失申请', '选择日期', get_today())
        with allure.step('直接确定'):
            self.click_customer_area_label_button('流失申请', '确 定')
            assert '请选择流失分类' in self.get_tip_text()

    @allure.title('申请流失-未输入流失原因')
    def test_lost_customer_reason_empty(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('点击申请流失'):
            self.click_normal_button('申请流失')
        with allure.step('输入流失时间'):
            self.click_customer_area_label_input_date('流失申请', '选择日期', get_today())
        with allure.step('输入流失分类'):
            self.click_customer_area_label_input_reason('流失申请', '请选择', '禁签客户',
                                                        '客户经营范围属禁签范围')
        with allure.step('直接确定'):
            self.click_customer_area_label_button('流失申请', '确 定')
            assert '请输入流失原因' in self.get_tip_text()

    @allure.title('申请流失并删除')
    def test_lost_customer_and_recover_delete(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.click_new_customer_button('确定')
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('点击申请流失'):
            self.close_ads()
            self.click_normal_button('申请流失')
        with allure.step('输入流失时间'):
            self.click_customer_area_label_input_date('流失申请', '选择日期', get_today())
        with allure.step('输入流失分类'):
            self.click_customer_area_label_input_reason('流失申请', '请选择', '禁签客户',
                                                        '客户经营范围属禁签范围')
        with allure.step('输入流失原因'):
            self.type_customer_area_label_textarea('流失申请', 'test')
        with allure.step('点击确定'):
            self.click_customer_area_label_button('流失申请', '确 定')
            assert '保存成功' in self.get_tip_text()
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户' in self.get_tip_text()

    @allure.title('授权看账-未勾选')
    def test_grant_permission_uncheck(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('点击授权看账'):
            self.close_ads()
            self.click_normal_button('授权客户看账')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('删除客户')
    def test_delete_customer(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('删除客户'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '删除')
            assert '请至少选择一个客户进行删除' in self.get_tip_text()

    @allure.title('合并客户-未选择')
    def test_marge_customer_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('合并客户'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '合并客户')
            assert '请选择相关记录！' in self.get_tip_text()

    @allure.title('合并客户-未选择合并后客户')
    def test_marge_customer_empty_customer(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('合并客户'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '合并客户')
            self.click_merge_customer_area_buttons('确定')
            assert '请选择合并后的客户！' in self.get_tip_text()

    @allure.title('合并客户-单客户')
    def test_marge_customer_single(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('合并客户'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '合并客户')
            self.merge_customer(company_name)
            self.click_merge_customer_area_buttons('确定')
            assert '合并客户须至少为两个' in self.get_tip_text()

    @allure.title('合并客户')
    def test_merge_customer(self):
        company_name_1 = random_string_generator()
        company_name_2 = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name_1)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name_2)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer('test_')
            self.click_customer_table_checkbox(company_name_1)
            self.click_customer_table_checkbox(company_name_2)
        with allure.step('合并客户'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '合并客户')
            self.merge_customer(company_name_1)
            self.click_merge_customer_area_buttons('确定')
            assert '合并客户成功' in self.get_tip_text()
        with allure.step('删除客户'):
            self.search_customer('test_')
            self.click_customer_table_checkbox(company_name_1)
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('修改客户')
    def test_modify_customer(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('编辑客户信息'):
            self.click_customer_in_line(company_name)
            self.type_to_modify_customer_inputs_by_label('统一信用代码', random_string_generator())
            self.click_modify_customer_conform_button()
            assert '修改客户成功' in self.get_tip_text()

    @allure.title('添加标记')
    def test_mark_customer(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
        with allure.step('添加标记'):
            self.click_table_buttons(company_name, '添加标记')
            self.click_mark_conform()
            assert '保存成功' in self.get_tip_text()

    @allure.title('跟进并删除记录')
    def test_followup_and_delete_record(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
        with allure.step('跟进'):
            self.click_table_buttons(company_name, '跟进')
            self.input_follow_up('test')
            self.click_follow_up_button('保存')
            assert '保存跟进记录成功' in self.get_tip_text()
        with allure.step('删除跟进记录'):
            self.click_delete_followup_record('test')
            self.click_conform_delete_followup_record()
            assert '删除成功' in self.get_tip_text()

    @allure.title('跟进-无跟进内容')
    def test_followup_empty(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
        with allure.step('跟进'):
            self.click_table_buttons(company_name, '跟进')
            self.click_follow_up_button('保存')
            assert '请输入跟进记录' in self.get_tip_text()
            self.click_close_followup()

    @allure.title('新增客户-客户已存在')
    def test_new_customer_exist(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.click_new_customer_button('确定')
            assert self.is_customer_exist()

    @allure.title('授权看账-无内容')
    def test_grant_permission_empty(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('授权客户看账'):
            self.click_normal_button('授权客户看账')
            self.click_grant_permission_buttons('确定')
            assert '看账账号' in self.get_tip_text()
            self.click_close_grant_permission()

    @allure.title('标记税控盘-勾选')
    def test_mark_tax_box_checked(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.click_new_customer_button('确定')
        with allure.step('搜索客户'):
            self.search_customer(company_name)
        with allure.step('标记税控盘'):
            self.click_customer_table_checkbox(company_name)
            self.click_dropdown_buttons('更多', '标记税控盘')
            self.click_tax_box_buttons('确定')
            assert '标记税控盘成功' in self.get_tip_text()
        with allure.step('选择客户'):
            self.search_customer(company_name)
        with allure.step('删除客户'):
            self.click_customer_table_checkbox(company_name)
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')

    @allure.title('标记税控盘-未勾选')
    def test_mark_tax_box_uncheck(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('标记税控盘'):
            self.close_ads()
            self.click_dropdown_buttons('更多', '标记税控盘')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('分配客户经理-未勾选')
    def test_customer_manager_uncheck(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
        with allure.step('分配客户经理'):
            self.click_dropdown_buttons('更多', '分配客户经理')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('分配客户经理-未指定')
    def test_customer_manager_unselect(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('分配客户经理'):
            self.click_dropdown_buttons('更多', '分配客户经理')
            self.click_customer_manager_buttons('确定')
            assert '请先添加派工人员！' in self.get_tip_text()
            self.click_close_customer_manager()

    @allure.title('分配客户经理')
    def test_customer_manager(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('分配客户经理'):
            self.click_dropdown_buttons('更多', '分配客户经理')
            self.click_add_dispatch_button_by_name('经理01')
            self.click_customer_manager_buttons('确定')
            # self.click_re_dispatch_customer_manager_alert_buttons('确定')
            assert '分配客户经理成功' in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_lost_manage
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('流失管理')
class TestLostManage(LoginPage, ManagerHomePage, ManagerCommonPage, CustomerPage, LostManagePage):

    @allure.title('流失恢复-未勾选')
    def test_customer_lose_management_recover_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '流失管理')
        with allure.step('点击流失恢复'):
            self.click_lost_manage_buttons('流失恢复')
        assert '请先选择客户！' in self.get_tip_text()

    @allure.title('审核-未勾选')
    def test_customer_lose_management_audit_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '流失管理')
        with allure.step('点击流失恢复'):
            self.click_lost_manage_buttons('审核')
        assert '请选择一条数据' in self.get_tip_text()

    @allure.title('导出')
    def test_customer_lose_management_export(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '流失管理')
        with allure.step('点击导出'):
            self.click_lost_manage_buttons('导出')

    @allure.title('申请流失并恢复')
    def test_lost_customer_and_recover(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.click_new_customer_button('确定')
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('点击申请流失'):
            self.close_ads()
            self.click_normal_button('申请流失')
        with allure.step('输入流失时间'):
            self.click_customer_area_label_input_date('流失申请', '选择日期', get_today())
        with allure.step('输入流失分类'):
            self.click_customer_area_label_input_reason('流失申请', '请选择', '禁签客户',
                                                        '客户经营范围属禁签范围')
        with allure.step('输入流失原因'):
            self.type_customer_area_label_textarea('流失申请', 'test')
        with allure.step('点击确定'):
            self.click_customer_area_label_button('流失申请', '确 定')
            assert '保存成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('流失恢复'):
            self.click_manager_menu('客户管理', '流失管理')
            self.lost_manage_search_company(company_name)
            self.click_buttons_in_line_by_company_name(company_name, '审核')
            self.click_conform_lost_area_buttons('审核流失', '确定')
            assert '审核成功' in self.get_tip_text()
            self.click_checkbox_in_line_by_company_name(company_name)
            self.click_lost_manage_buttons('流失恢复')
            self.click_conform_lost_area_buttons('流失恢复提示', '确定')
            assert '恢复成功' in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_manage
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('客户-导出')
class TestCustomerExport(LoginPage, ManagerHomePage, ContractExpirePage, CustomerPage):

    @allure.title('导出列表全部')
    def test_export_customer_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
        with allure.step('导出'):
            self.click_dropdown_buttons('更多', '导出')
            self.export('按列表全部导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\customer\\客户资料表-列表全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选')
    def test_export_customer_list_checked(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
        with allure.step('导出'):
            self.click_dropdown_buttons('更多', '导出')
            self.export('按列表勾选导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\customer\\客户资料表-列表勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_lost_manage
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('流失管理-导出')
class TestLostManageExport(LoginPage, ManagerHomePage, ContractExpirePage, LostManagePage):

    @allure.title('导出列表全部')
    def test_export_expired_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '流失管理')
        with allure.step('导出'):
            self.click_lost_manage_buttons('导出')
            self.export('按列表全部导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\customer\\流失管理-列表全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选')
    def test_export_expired_list_checked(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '流失管理')
        with allure.step('导出'):
            self.click_lost_manage_buttons('导出')
            self.export('按列表勾选导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\customer\\流失管理-列表勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_contract
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('合同')
class TestContract(LoginPage,
                   ManagerCommonPage,
                   ManagerHomePage,
                   ContractPage,
                   ContractInvoicePage,
                   ContractChangeRecordPage,
                   AgencyAccountPage,
                   CustomerPage,
                   BusinessServicePage):

    @allure.title('合同新增-代账服务-已存在')
    def test_new_contract_proxy_exist(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2022-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2022-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '合同编号已存在' in self.get_tip_text()

    @allure.title('合同新增-代账服务')
    def test_new_contract_proxy(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2023-11')
            self.input_bookkeeping_detail('服务结束日期', '2023-11')
        with allure.step('保存合同'):
            self.click_save_button()
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('输入合同编号'):
            self.input_normal_detail('客户编号', contract_id)
        with allure.step('搜索合同编号'):
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击删除'):
            self.click_delete_contract_button()
        with allure.step('确认删除'):
            self.click_confirm_delete_button()
            assert '删除合同成功' in self.get_tip_text()

    @allure.title('合同新增-工商服务-已存在')
    def test_new_contract_ic_exist(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选工商服务服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
        with allure.step('点击下拉菜单的工商注册'):
            self.click_spacial_dropdown_drop_button()
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选工商服务服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
        with allure.step('点击下拉菜单的工商注册'):
            self.click_spacial_dropdown_drop_button()
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '合同编号已存在' in self.get_tip_text()

    @allure.title('合同新增-工商服务')
    def test_new_contract_ic(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选工商服务服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
        with allure.step('点击下拉菜单的工商注册'):
            self.click_spacial_dropdown_drop_button()
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('输入合同编号'):
            self.input_normal_detail('客户编号', contract_id)
        with allure.step('搜索合同编号'):
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击删除'):
            self.click_delete_contract_button()
        with allure.step('确认删除'):
            self.click_confirm_delete_button()
            assert '删除合同成功' in self.get_tip_text()

    @allure.title('合同审核与反审核')
    def test_audit_contract(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选工商服务服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
        with allure.step('点击下拉菜单的工商注册'):
            self.click_spacial_dropdown_drop_button()
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
        with allure.step('保存合同'):
            self.click_save_button()
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('输入合同编号'):
            self.input_normal_detail('客户编号', contract_id)
        with allure.step('搜索合同编号'):
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击反审核'):
            self.click_return_contract_check_button('反审核')
            assert '反审核成功' in self.get_tip_text()

    @allure.title('合同导出')
    def test_export_contract(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('更多-导出'):
            self.click_contract_more_button()
            self.click_contract_derive_button()
            self.click_derive_button()
        # with allure.step('处理临时文件'):
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel差异'):
        #     if get_env() == 'prod':
        #         check_excel_diff(f'{get_project_path()}\\template\\manager\\contract\\合同列表-autotest-001.xls',
        #                          f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
        #     elif get_env() == 'mock':
        #         check_excel_diff(f'{get_project_path()}\\template\\manager\\contract\\合同列表-autotest-002.xls',
        #                          f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('调整续费类型-未勾选')
    def test_adj_type_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('更多-调整续费类型'):
            self.click_dropdown_buttons('更多', '调整续费类型')
            assert '请选择需要调整续费类型的合同' in self.get_tip_text()

    @allure.title('调整续费类型')
    def test_adj_type_unselected(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('过滤合同'):
            self.search_contract(company_contract)
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('更多-调整续费类型'):
            self.click_dropdown_buttons('更多', '调整续费类型')
            self.adj_type('续签')
            assert '调整成功' in self.get_tip_text()
            assert '续签' == self.get_text_from_contract_type_in_line_by_company_name(company_contract)

    @allure.title('修改合同')
    def test_modify_contract(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
            self.search_contract(company_contract)
        with allure.step('补充合同信息'):
            self.click_contract_id_by_company_name(company_contract)
            self.click_modify_contract_buttons('编辑')
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
            self.type_modify_contract_service_total_amount(1, 500)
            self.click_modify_contract_buttons('保存')
            assert '修改成功' in self.get_tip_text()

    @allure.title('编辑页面审核合同')
    def test_modify_contract_audit(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
            self.search_contract(company_contract)
        with allure.step('补充合同信息'):
            self.click_contract_id_by_company_name(company_contract)
            self.click_modify_contract_buttons('审核')
            assert '审核成功' in self.get_tip_text()
            self.click_modify_contract_buttons('反审核')
            assert '反审核成功' in self.get_tip_text()
            self.click_modify_contract_buttons('关闭')

    @allure.title('合同续签')
    def test_renew_contract(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('输入合同编号'):
            self.input_normal_detail('客户编号', company_contract)
        with allure.step('搜索合同编号'):
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('点击续签'):
            self.click_continue_contract_button('续签')
        with allure.step('勾选代账服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
        with allure.step('点击下拉菜单的工商注册'):
            self.click_spacial_dropdown_drop_button()
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
        with allure.step('保存合同'):
            self.click_save_button()
            assert '合同服务续签成功' in self.get_tip_text()

    @allure.title('合同续签-未勾选')
    def test_renew_contract_unselected(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('输入合同编号'):
            self.input_normal_detail('客户编号', company_contract)
        with allure.step('搜索合同编号'):
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('点击续签'):
            self.click_continue_contract_button('续签')
        with allure.step('保存合同'):
            self.click_save_button()
            assert '请勾选服务' in self.get_tip_text()

    @allure.title('合同变更-提前终止-未勾选')
    def test_change_contract_end_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            assert '请选择需要变更的合同' in self.get_tip_text()

    @allure.title('合同变更-提前终止-未审核')
    def test_termination_of_the_contract_unaudited(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            assert '未审核合同无法进行变更操作' in self.get_tip_text()

    @allure.title('合同变更-提前终止-服务期限不完整')
    def test_termination_of_the_contract_information_incomplete(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            assert '代账服务期限不完整无法进行变更' in self.get_tip_text()

    @allure.title('合同变更-提前终止-未录入原因')
    def test_termination_of_the_contract_empty_reason(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2023-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', contract_id)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            self.termination_contract('服务终止日期', '四月')
            assert '请填写变更原因' in self.get_tip_text()

    @allure.title('合同变更-提前终止-终止期间不在服务期内')
    def test_termination_of_the_contract_beyond_service(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2022-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', contract_id)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            self.termination_contract('服务终止日期', '四月')
            assert '终止月份不在合同期间内' in self.get_tip_text()

    @allure.title('合同变更-提前终止-未录入终止期间')
    def test_termination_of_the_contract_empty_period(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2022-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', contract_id)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            self.click_area_buttons('提前终止', '确定')
            assert '请选择终止月份' in self.get_tip_text()

    @allure.title('合同变更-提前终止')
    def test_termination_of_the_contract(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', contract_id)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(contract_id)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-提前终止'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('提前终止')
            self.termination_contract('服务终止日期', '四月', 'test_reason')
            assert '变更成功' in self.get_tip_text()

    @allure.title('查看合同变更记录')
    def test_view_change_record(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
            self.search_contract(company_contract)
        with allure.step('补充合同信息'):
            self.click_contract_id_by_company_name(company_contract)
            self.click_modify_contract_buttons('编辑')
            self.input_start_and_end_date_to_table_line('2023-01', '2023-12')
            self.type_modify_contract_service_total_amount(1, 500)
            self.click_modify_contract_buttons('保存')
            assert '修改成功' in self.get_tip_text()
            self.click_modify_contract_buttons('关闭')
        with allure.step('查看变更记录'):
            self.click_button_in_table_by_company_name(company_contract, '变更记录')
            assert self.is_record_list_change_type_visible()

    @allure.title('合同变更-收款变更-未勾选')
    def test_change_collection_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            assert '请选择需要变更的合同' in self.get_tip_text()

    @allure.title('合同变更-收款变更-未审核')
    def test_change_collection_contract_unaudited(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            assert '未审核合同无法进行变更操作' in self.get_tip_text()

    @allure.title('合同变更-收款变更-服务期限不完整')
    def test_change_collection_contract_information_incomplete(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            assert '代账服务期限不完整无法进行变更' in self.get_tip_text()

    @allure.title('合同变更-收款变更-未录入期间')
    def test_change_collection_contract_empty_period(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            self.click_area_buttons('收款变更', '下一步')
            assert '请选择终止月份' in self.get_tip_text()

    @allure.title('合同变更-收款变更-未录入原因')
    def test_change_collection_contract_empty_reason(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            self.change_collection('服务终止日期', '四月')
            assert '请填写变更原因' in self.get_tip_text()

    @allure.title('合同变更-收款变更')
    def test_change_collection_contract(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-收款变更'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('收款变更')
            self.change_collection('服务终止日期', '三月', 'test_reason')
            self.click_area_buttons('收款变更', '下一步')
            self.click_area_buttons('收款变更', '关闭')

    @allure.title('合同变更-变更业务员-未勾选')
    def test_change_stuff_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击合同变更-变更业务员'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('变更业务员')
            assert '请至少选择一项进行操作' in self.get_tip_text()

    @allure.title('合同变更-变更业务员-未审核')
    def test_change_person_contract_unaudited(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-变更业务员'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('变更业务员')
            assert '未审核合同无法进行变更操作' in self.get_tip_text()

    @allure.title('合同变更-变更业务员')
    def test_change_person_contract(self):
        contract_id = random_string_generator()
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_contract)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2022-11')
            self.input_bookkeeping_detail('服务结束日期', '2028-11')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
        with allure.step('搜索合同'):
            self.input_normal_detail('客户编号', company_contract)
            self.click_contract_num_search_button('客户编号')
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击审核'):
            self.click_contract_check_button()
            assert '审核成功' in self.get_tip_text()
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('点击合同变更-变更业务员'):
            self.click_normal_button('合同变更')
            self.click_normal_dropdown_items('变更业务员')
            self.change_person('记账01')
            assert '变更成功' in self.get_tip_text()

    @allure.title('审核-未勾选')
    def test_audit_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击审核按钮'):
            self.click_normal_button('审核')
            assert '请至少选择一个合同进行批量审核' in self.get_tip_text()

    @allure.title('删除-未勾选')
    def test_delete_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击删除按钮'):
            self.click_normal_button('删除')
            assert '请在左侧选中要删除的行，再进行删除操作' in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_invoice
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('合同发票')
class TestContractInvoice(LoginPage,
                          ManagerCommonPage,
                          ManagerHomePage,
                          ContractPage,
                          ContractInvoicePage,
                          ContractChangeRecordPage,
                          AgencyAccountPage,
                          CustomerPage,
                          BusinessServicePage):
    @allure.title('发票申请-未勾选')
    def test_replay_invoice_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('更多-发票申请'):
            self.click_dropdown_buttons('更多', '发票申请')
            assert '请至少选择一项进行操作' in self.get_tip_text()

    @allure.title('发票申请-金额为零')
    def test_replay_invoice_zero(self):
        company_contract = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_contract)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('过滤合同'):
            self.search_contract(company_contract)
        with allure.step('勾选合同'):
            self.check_contract_inputbox(company_contract)
        with allure.step('更多-发票申请'):
            self.click_dropdown_buttons('更多', '发票申请')
            self.type_to_apply_invoice_area_inputs_by_label('客户名称', company_contract)
            self.type_to_apply_invoice_area_inputs_by_label('公司税号', '91440300000000')
            self.click_apply_invoice_area_button()
            assert '当前合同的已审核收款金额为0或已完全开票，故本次申请开票总额为0，无需开票，请检查' in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_change_record
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('服务到期明细')
class TestContractChangeRecord(LoginPage,
                               ManagerCommonPage,
                               ManagerHomePage,
                               ContractPage,
                               ContractExpirePage):

    @allure.title('申请流失-未勾选')
    def test_lost_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '服务到期明细')
        with allure.step('点击菜单'):
            self.click_normal_buttons('申请流失')
            assert '请选择申请流失的客户' in self.get_tip_text()

    @allure.title('查询到期明细')
    def test_query_expired_contract(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '服务到期明细')
        with allure.step('输入过滤条件'):
            self.click_filter_item_by_label('合同到期月', '本月')


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_change_record
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('服务到期明细-导出')
class TestContractChangeRecordExport(LoginPage, ManagerHomePage, ContractExpirePage):

    @allure.title('导出列表全部')
    def test_export_expired_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '服务到期明细')
        with allure.step('输入过滤条件'):
            self.click_filter_item_by_label('合同到期月', '本月')
        with allure.step('导出'):
            self.click_normal_buttons('导出')
            self.export('按列表全部导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\contract\\合同续签明细-列表全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选')
    def test_export_expired_list_checked(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '服务到期明细')
        with allure.step('输入过滤条件'):
            self.click_filter_item_by_label('合同到期月', '本月')
        with allure.step('导出'):
            self.click_normal_buttons('导出')
            self.export('按列表勾选导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\contract\\合同续签明细-列表勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_items
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('客户物品管理')
class TestItems(LoginPage, ManagerCommonPage, ManagerHomePage, ItemsPage, CustomerPage):

    @allure.title('接收并归还物品')
    def test_receive_and_return_items(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_head_details('请输入客户', company_name)
            self.click_company_list(company_name)
            self.input_item_details('开户许可证')
            self.submit_items()
            self.close_items()
        with allure.step('搜索客户'):
            self.click_tag_refresh_button('客户物品管理')
            self.search_company('客户名称', company_name)
        with allure.step('勾选并进入归还物品'):
            self.check_items(company_name)
            self.click_dropdown_button('外部交接', '归还客户')
            self.close_ads()
            self.submit_items()
            self.close_items()

    @allure.title('接收物品-未输入物品')
    def test_receive_items_empty_item(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_head_details('请输入客户', company_name)
            self.click_company_list(company_name)
            self.submit_items()
            assert '入库商品缺失' in self.get_tip_text()

    @allure.title('接收物品-未输入公司')
    def test_receive_item_empty_company(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_item_details('开户许可证')
            self.submit_items()
            assert '请填写客户名称' in self.get_tip_text()

    @allure.title('内部转交')
    def test_trans_and_delete_record(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_head_details('请输入客户', company_name)
            self.click_company_list(company_name)
            self.input_item_details('开户许可证')
            self.submit_items()
            self.close_items()
        with allure.step('搜索客户'):
            self.search_company('客户名称', company_name)
        with allure.step('勾选并点击内部移交'):
            self.check_items(company_name)
            self.click_normal_button('内部移交')
        with allure.step('选择接收人并关闭'):
            self.select_person('财务01')
            self.submit_items()
            self.close_items()
        with allure.step('删除交接记录'):
            self.click_transfer_record_button(company_name)
            self.click_transfer_record_list_button('删除')
            self.click_transfer_record_conform_delete()
            assert '单据删除成功' in self.get_tip_text()

    @allure.title('内部转交-未勾选')
    def test_trans_item_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('勾选并点击内部移交'):
            self.click_normal_button('内部移交')
            assert '请选择物品进行交接' in self.get_tip_text()

    @allure.title('编辑物品备注-未勾选')
    def test_modify_memo_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('编辑物品备注'):
            self.click_normal_button('更多', '编辑物品备注')
            assert '请至少勾选一项' in self.get_tip_text()

    @allure.title('编辑物品备注')
    def test_modify_memo(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_head_details('请输入客户', company_name)
            self.click_company_list(company_name)
            self.input_item_details('开户许可证')
            self.submit_items()
            self.close_items()
        with allure.step('搜索客户'):
            self.search_company('客户名称', company_name)
        with allure.step('编辑物品备注'):
            self.check_items(company_name)
            self.click_normal_button('更多', '编辑物品备注')
            self.modify_memo_or_location('编辑物品备注', '编辑物品备注')
            assert '修改成功' in self.get_tip_text()
        with allure.step('还原物品备注'):
            self.check_items(company_name)
            self.click_normal_button('更多', '编辑物品备注')
            self.modify_memo_or_location('编辑物品备注')
            assert '修改成功' in self.get_tip_text()

    @allure.title('编辑存放位置-未勾选')
    def test_modify_location_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('编辑存放位置'):
            self.click_normal_button('更多', '编辑存放位置')
            assert '请至少勾选一项' in self.get_tip_text()

    @allure.title('编辑存放位置')
    def test_modify_location(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('新增客户'):
            self.close_ads()
            self.click_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('点击收到入库'):
            self.click_dropdown_button('外部交接', '收到入库')
        with allure.step('填写入库信息并提交'):
            self.input_head_details('请输入客户', company_name)
            self.click_company_list(company_name)
            self.input_item_details('开户许可证')
            self.submit_items()
            self.close_items()
        with allure.step('搜索客户'):
            self.search_company('客户名称', company_name)
        with allure.step('编辑存放位置'):
            self.check_items(company_name)
            self.click_normal_button('更多', '编辑存放位置')
            self.modify_memo_or_location('编辑存放位置', '编辑存放位置')
            assert '修改成功' in self.get_tip_text()
        with allure.step('还原存放位置'):
            self.check_items(company_name)
            self.click_normal_button('更多', '编辑存放位置')
            self.modify_memo_or_location('编辑存放位置')
            assert '修改成功' in self.get_tip_text()

    #
    # @allure.title('导入客户物品')
    # def test_upload_file(self):
    #     company_name = GetYamlData().get_company('company_items_003')
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu('客户管理', '客户物品管理')
    #     with allure.step('导入客户物品'):
    #         self.click_normal_button('导入客户物品')
    #         self.upload_file(f'{get_project_path()}\\template\\manager\\item\\客户物品清单模板-正常.xlsx')
    #         assert '导入成功' in self.get_tip_text()
    #     with allure.step('勾选并进入归还物品'):
    #         self.check_items(company_name)
    #         self.click_dropdown_button('外部交接', '归还客户')
    #         self.close_ads()
    #         self.submit_items()
    #         self.close_items()

    @allure.title('导入客户物品-客户不存在')
    def test_upload_file_customer_not_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('导入客户物品'):
            self.click_normal_button('导入客户物品')
            self.upload_file(
                f'{get_project_path()}/template/manager/item/客户物品清单模板-客户不存在.xlsx')
            assert '客户名称不在系统客户中' in self.get_tip_text()

    @allure.title('导入客户物品-物品不存在')
    def test_upload_file_item_not_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('导入客户物品'):
            self.click_normal_button('导入客户物品')
            self.upload_file(
                f'{get_project_path()}\\template\\manager\\item\\客户物品清单模板-物品不存在.xlsx')
            assert '物品名称不在系统物品中' in self.get_tip_text()

    @allure.title('导入客户物品-人员不存在')
    def test_upload_file_person_not_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('导入客户物品'):
            self.click_normal_button('导入客户物品')
            self.upload_file(
                f'{get_project_path()}\\template\\manager\\item\\客户物品清单模板-人员不存在.xlsx')
            assert '持有人名称和对应的手机号码不在系统职工中' in self.get_tip_text()

    @allure.title('导入客户物品-手机号不存在')
    def test_upload_file_phone_not_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('导入客户物品'):
            self.click_normal_button('导入客户物品')
            self.upload_file(
                f'{get_project_path()}\\template\\manager\\item\\客户物品清单模板-手机号不存在.xlsx')
            assert '持有人名称和对应的手机号码不在系统职工中' in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_customer
@pytest.mark.manager_customer_items
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('客户物品管理-导出')
class TestItemExport(LoginPage, ManagerHomePage, ItemsPage):
    @allure.title('下载导入模板')
    def test_download_template(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('下载导入模板'):
            self.click_normal_button('导入客户物品')
            self.click_download_template()
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     check_excel_diff(f'{get_project_path()}\\template\\manager\\item\\客户物品清单模板-autotest-001.xlsx',
        #                      f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')

    @allure.title('导出物品列表')
    def test_export(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户物品管理')
        with allure.step('导出物品列表'):
            self.click_normal_button('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     check_excel_diff(f'{get_project_path()}\\template\\manager\\item\\物品库存明细.xls',
        #                      f'{get_project_path()}\\download_tmp\\{self.test_id}\\{tmp_filename}')
