import allure
import pytest

from page.web_ui.manager.page_customer import CustomerPage
from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.manager.page_field import FieldPage
from page.web_ui.manager.page_common import ManagerCommonPage
from utils.random_data import random_string_generator


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_field
@allure.epic('管家')
@allure.feature('外勤管理')
@allure.story('外勤任务')
class TestField(LoginPage, ManagerHomePage, ManagerCommonPage, FieldPage, CustomerPage):
    @allure.title('新增任务类型-已存在')
    def test_new_task_type_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击任务类型'):
            self.click_home_button('任务类型')
        with allure.step('输入任务类型'):
            self.input_task_type('其他')
        with allure.step('点击新增类型按钮'):
            self.click_new_task_button()
            assert '当前名称已存在,请重新输入' in self.get_tip_text()

    @allure.title('新增任务类型为空')
    def test_new_task_type_empty(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击任务类型'):
            self.click_home_button('任务类型')
        with allure.step('输入任务类型'):
            self.input_task_type('')
        with allure.step('点击新增类型按钮'):
            self.click_new_task_button()
            assert '不能新增空类型!' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('修改任务类型')
    def test_modify_task_type(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击任务类型'):
            self.click_home_button('任务类型')
        with allure.step('修改任务类型'):
            self.click_task_operate_button('left', 'edit', '1')
            self.click_task_operate_button('left', 'input', '1', text='')
            self.click_task_operate_button('left', 'edit', '1')
            assert '成功' in self.get_tip_text()

    @allure.title('删除任务类型-无法删除')
    def test_delete_task_type_not_available(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击任务类型'):
            self.click_home_button('任务类型')
        with allure.step('删除任务类型'):
            self.click_task_operate_button('left', 'delete', '1')
            assert '当前类型已经使用过,无法删除' in self.get_tip_text()

    @allure.title('分配-未勾选')
    def test_dispatch_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('分配')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('完成-未勾选')
    def test_finish_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('完成')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('取消任务-未勾选')
    def test_cancel_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('取消任务')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('关闭任务-未勾选')
    def test_close_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('关闭任务')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('激活任务-未勾选')
    def test_active_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('激活任务')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('删除任务-未勾选')
    def test_delete_task_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击按钮'):
            self.click_home_button('删除')
            assert '请选择一行' in self.get_tip_text()

    @allure.title('新增任务-未输入客户')
    def test_new_task_empty_customer(self):
        task_id = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '请选择客户、任务类型和任务内容！' in self.get_tip_text()

    @allure.title('新增任务-未输入任务类型')
    def test_new_task_empty_task_type(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            # self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '请选择客户、任务类型和任务内容！' in self.get_tip_text()

    @allure.title('新增任务-未输入任务内容')
    def test_new_task_empty_task_details(self):
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '请选择客户、任务类型和任务内容！' in self.get_tip_text()

    @allure.title('分配任务-未选择部门')
    def test_dispatch_task_empty_department(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('分配任务'):
            self.click_home_button('分配')
            self.distribution_task_click_buttons('确定')
            assert '请选择部门和职员' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('新增并删除任务')
    def test_new_task_and_delete(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('删除任务'):
            self.click_home_button('删除')
            assert '删除任务成功！' in self.get_tip_text()

    @allure.title('取消任务-未输入原因')
    def test_cancel_task_empty_reason(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击取消任务'):
            self.click_home_button('取消任务')
        with allure.step('输入取消原因'):
            self.cancel_task_click_button('确定')
            assert '请填写原因' in self.get_tip_text()

    @allure.title('关闭任务-未输入原因')
    def test_close_task_empty_reason(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击取消任务'):
            self.click_home_button('关闭任务')
        with allure.step('输入取消原因'):
            self.close_task_click_button('确定')
            assert '请填写关闭任务原因' in self.get_tip_text()

    @allure.title('激活任务-进行中')
    def test_activate_task_running(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击激活任务'):
            self.click_home_button('激活任务')
            assert '不能选择进行中任务进行激活' in self.get_tip_text()

    @allure.title('激活任务-完成')
    def test_activate_task_finished(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('过滤任务状态'):
            self.click_filed_head_filter('完成状态', '进行中')
        with allure.step('搜索任务'):
            self.search_task_by_task_detail(task_id)
            self.click_checkbox_in_table(task_id)
        with allure.step('点击完成任务'):
            self.click_home_button('完成')
            self.finish_task_click_button('确定')
            assert '完成提单成功' in self.get_tip_text()
        with allure.step('过滤任务状态'):
            self.click_filed_head_filter('完成状态', '已完成')
        with allure.step('搜索任务'):
            self.search_task_by_task_detail(task_id)
            self.click_checkbox_in_table(task_id)
        with allure.step('点击激活任务'):
            self.click_home_button('激活任务')
            assert '激活任务成功' in self.get_tip_text()

    @allure.title('激活任务-取消')
    def test_activate_task_canceled(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('过滤任务状态'):
            self.click_filed_head_filter('完成状态', '进行中')
        with allure.step('搜索任务'):
            self.search_task_by_task_detail(task_id)
            self.click_checkbox_in_table(task_id)
        with allure.step('点击取消任务'):
            self.click_home_button('取消任务')
            self.cancel_task_input('取消任务')
            self.cancel_task_click_button('确定')
            assert '取消提单成功！' in self.get_tip_text()

    @allure.title('激活任务-关闭')
    def test_activate_task_closed(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('过滤任务状态'):
            self.click_filed_head_filter('完成状态', '进行中')
        with allure.step('搜索任务'):
            self.search_task_by_task_detail(task_id)
            self.click_checkbox_in_table(task_id)
        with allure.step('点击关闭任务'):
            self.click_home_button('关闭任务')
            self.close_task_input('关闭任务')
            self.close_task_click_button('确定')
            assert '关闭任务成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('分配并取消任务')
    def test_new_task_and_distribution(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('分配任务'):
            self.click_home_button('分配')
            self.distribution_task_select_org_and_employee('财务部', '财务01')
            self.distribution_task_click_buttons('确定')
            assert '分配任务成功！' in self.get_tip_text()
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击取消任务'):
            self.click_home_button('取消任务')
        with allure.step('输入取消原因'):
            self.cancel_task_input('取消任务')
            self.cancel_task_click_button('确定')
            assert '取消提单成功！' in self.get_tip_text()

    @allure.title('新增并关闭任务')
    def test_new_task_and_close(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击关闭任务'):
            self.click_home_button('关闭任务')
        with allure.step('输入关闭原因'):
            self.close_task_input('关闭任务')
        with allure.step('确定关闭'):
            self.close_task_click_button('确定')
            assert '关闭任务成功！' in self.get_tip_text()

    @allure.title('新增并完成任务')
    def test_new_task_and_finish(self):
        company_name = random_string_generator()
        task_id = random_string_generator()
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('点击新增任务'):
            self.click_home_button('新增任务')
        with allure.step('输入任务信息'):
            self.new_task_customer(company_name)
            self.new_task_type('代开发票')
            self.new_task_input_details(task_id)
        with allure.step('新增任务页面点击确定按钮'):
            self.new_task_click_button('确定')
            assert '新增任务成功！' in self.get_tip_text()
        with allure.step('搜索刚创建的任务'):
            self.search_task_by_task_detail(task_id)
        with allure.step('勾选列表中的任务'):
            self.click_checkbox_in_table(task_id)
        with allure.step('点击完成任务'):
            self.click_home_button('完成')
        with allure.step('输入完成备注'):
            self.finish_task_input('完成任务')
        with allure.step('确定完成'):
            self.finish_task_click_button('确定')
            assert '完成提单成功！' in self.get_tip_text()

    @allure.title('新增并导出任务')
    def test_new_task_and_export(self):
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
            self.click_manager_menu('外勤管理', '外勤任务')
        with allure.step('搜索任务'):
            self.search_task_by_task_detail(company_name)
        with allure.step('点击导出'):
            self.click_home_button('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     if get_env() == 'prod':
        #         check_excel_diff(f'{get_project_path()}\\template\\manager\\field\\外勤列表-autotest-001.xls',
        #                          f'{get_project_path()}\\download_tmp\\{self.test_id}{tmp_filename}')
        #     elif get_env() == 'mock':
        #         check_excel_diff(f'{get_project_path()}\\template\\manager\\field\\外勤列表-autotest-002.xls',
        #                          f'{get_project_path()}\\download_tmp\\{self.test_id}{tmp_filename}')
