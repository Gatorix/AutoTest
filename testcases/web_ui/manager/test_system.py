import allure
import pytest

from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.manager.page_system import DepartmentAndStaffPage


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_system
@pytest.mark.manager_system_department_staff
@allure.epic('管家')
@allure.feature('系统设置')
@allure.story('部门职员')
class TestDepartmentAndStaff(LoginPage,
                             ManagerCommonPage,
                             ManagerHomePage,
                             DepartmentAndStaffPage):
    @allure.title('交接工作-未勾选')
    def test_transfer_work_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击交接工作'):
            self.click_department_and_staff_normal_button('交接工作')
            assert '请选择一个职员进行工作交接' in self.get_tip_text()

    @allure.title('删除-未勾选')
    def test_delete_staff_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击删除'):
            self.click_department_and_staff_normal_button('删除')
            assert '至少选择一个职员' in self.get_tip_text()

    @allure.title('转部门-未勾选')
    def test_transfer_department_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击转部门'):
            self.click_department_and_staff_normal_button('转部门')
            assert '至少选择一个职员' in self.get_tip_text()

    @allure.title('调整岗位-未勾选')
    def test_adjust_position_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击调整岗位'):
            self.click_department_and_staff_normal_button('调整岗位')
            assert '至少选择一个职员' in self.get_tip_text()

    @allure.title('新增职员-姓名为空')
    def test_create_staff_empty_name(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击新增职员'):
            self.click_department_and_staff_normal_button('新增')
        with allure.step('录入职员信息并保存'):
            self.click_new_stuff_buttons('确定')
            assert '职员名称不能为空' in self.get_tip_text()

    @allure.title('新增职员-手机号为空')
    def test_create_staff_empty_phone(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击新增职员'):
            self.click_department_and_staff_normal_button('新增')
        with allure.step('录入职员信息并保存'):
            self.type_new_stuff_input('姓名', 'test_stuff')
            self.click_new_stuff_buttons('确定')
            assert '登录账号不能为空' in self.get_tip_text()

    @allure.title('新增职员-手机号格式错误')
    def test_create_staff_illegal_phone(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击新增职员'):
            self.click_department_and_staff_normal_button('新增')
        with allure.step('录入职员信息并保存'):
            self.type_new_stuff_input('姓名', 'test_stuff')
            self.type_new_stuff_input('手机号', '135111')
            self.click_new_stuff_buttons('确定')
            assert '手机号码格式不正确' in self.get_tip_text()

    @allure.title('新增职员-已存在')
    def test_create_staff_exist(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击新增职员'):
            self.click_department_and_staff_normal_button('新增')
        with allure.step('录入职员信息并保存'):
            self.type_new_stuff_input('姓名', '杨肖然')
            self.type_new_stuff_input('手机号', '18588260467')
            self.click_new_stuff_buttons('确定')
            assert '用户已存在' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('新增职员并删除')
    def test_create_staff_and_delete(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '部门职员')
        with allure.step('点击新增职员'):
            self.click_department_and_staff_normal_button('新增')
        with allure.step('录入职员信息并保存'):
            self.type_new_stuff_input('姓名', 'test_stuff')
            self.type_new_stuff_input('手机号', '13532325454')
            self.click_new_stuff_buttons('确定')
            self.click_new_stuff_alert()
            assert '新增职员成功' in self.get_tip_text()
        with allure.step('查询职员'):
            self.search_staff('test_stuff')
            self.click_list_checkbox('test_stuff')
        with allure.step('删除职员'):
            self.click_department_and_staff_normal_button('删除')
            self.click_conform_delete_buttons('确定')
            assert '职员删除成功' in self.get_tip_text()
