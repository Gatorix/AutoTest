import allure
import pytest

from page.web_ui.manager.page_agency import AgencyAccountPage, ReceiveInvoiceRecordPage, ReceiveInvoicePage, \
    BookkeepingPage, GatherInvoicePage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_customer import CustomerPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.page_login import LoginPage

from utils.random_data import random_string_generator
from utils.file_utils import get_project_path


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_agency
@pytest.mark.manager_agency_service
@allure.epic('管家')
@allure.feature('代账服务')
@allure.story('服务管理')
class TestAgency(LoginPage,
                 ManagerCommonPage,
                 ManagerHomePage,
                 AgencyAccountPage,
                 ReceiveInvoiceRecordPage,
                 CustomerPage):

    @allure.title('人员派工-报税员')
    def test_person_dispatch_tax(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        with allure.step('选择报税员'):
            self.dispatch_select_style('报税员')
            self.dispatch_search_name('请输入人员', '报税01')
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('人员派工-记账员')
    def test_person_dispatch_bookkeeping(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        with allure.step('选择记账员'):
            self.dispatch_select_style('记账员')
            self.dispatch_search_name('请输入人员', '记账01')
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()

    @allure.title('人员派工-开票员')
    def test_person_dispatch_invoice(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        with allure.step('选择开票员'):
            self.dispatch_select_style('开票员')
            self.dispatch_search_name('请输入人员', '开票01')
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('人员派工-客户经理')
    def test_person_dispatch_manager(self):
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
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        with allure.step('选择客户经理'):
            self.dispatch_select_style('客户经理')
            self.dispatch_search_name('请输入人员', '经理01')
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()

    @allure.title('人员派工-未勾选')
    def test_person_dispatch_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('点击派工'):
            self.click_service_button('派工')
            assert '请先选择客户' in self.get_tip_text()

    @allure.title('审税金-未勾选')
    def test_audit_tax_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('点击审税金'):
            self.click_service_button('审税金')
            assert '请先选择客户' in self.get_tip_text()

    @allure.title('停止服务-未勾选')
    def test_stop_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('点击停止服务'):
            self.click_service_button('停止服务')
            assert '请先选择客户' in self.get_tip_text()

    @allure.title('反审税金-未勾选')
    def test_anti_moderation_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('更多-反审税金'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('反审税金')
            assert '请先选择客户' in self.get_tip_text()

    @allure.title('添加服务-未勾选')
    def test_add_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('更多-添加服务'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('添加服务')
            assert '请先选择一个客户' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('添加客户并删除')
    def test_add_customer_and_delete(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('更多-新增客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
        with allure.step('录入客户信息'):
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')  # 一级菜单与二级菜单
            self.close_ads()
        with allure.step('选择客户'):
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('打开派工查询')
    def test_query_dispatch(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('更多-派工查询'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('派工查询')
        with allure.step('检查页签'):
            self.click_tag_close_button('派工查询')

    @allure.title('打开查合同')
    def test_query_dispatch(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('更多-查合同'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('查合同')
        with allure.step('检查页签'):
            self.click_tag_close_button('查看合同')

    @pytest.mark.p1
    @allure.title('打开收票记录')
    def test_query_dispatch(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('更多-收票记录'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('收票记录')
        with allure.step('检查页签'):
            self.click_tag_close_button('收票记录')

    @allure.title('删除账套-未勾选')
    def test_delete_accounting_set_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单一级菜单与二级菜单
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('删除账套')
            assert '请先选择客户' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('部门派工')
    def test_department_dispatch(self):
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
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        # 弹出派工弹框
        with allure.step('选择部门'):
            self.click_dispatch_button('部门')  # 默认是人员派工，需手动选择部门派工
        # with allure.step('部门-派工-搜索部门名字'):
        #     self.dispatch_search_name('请输入部门', '财务部')
        # with allure.step('点击添加按钮'):
        #     self.dispatch_add_name('添加')
        # with allure.step('点击确定'):
        #     self.click_page_popups_bottom_button('确 定', '派工')
        #     assert '派工成功！' in self.get_tip_text()

    @allure.title('部门派工-已存在')
    def test_dispatch_dep_exist(self):
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
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('点击派工'):
            self.click_service_button('派工')
        with allure.step('选择部门'):
            self.click_dispatch_button('部门')  # 默认是人员派工，需手动选择部门派工
        # with allure.step('部门-派工-搜索部门名字'):
        #     self.dispatch_search_name('请输入部门', '财务部')
        # with allure.step('点击添加按钮'):
        #     self.dispatch_add_name('添加')
        # with allure.step('点击确定'):
        #     self.click_page_popups_bottom_button('确 定', '派工')
        #     assert '派工成功！' in self.get_tip_text()
        #     self.click_page_popups_bottom_button('取 消', '派工')
        # with allure.step('勾选某行'):
        #     self.select_audit_company(company_name)
        # with allure.step('点击派工'):
        #     self.click_service_button('派工')
        # with allure.step('选择部门'):
        #     self.click_dispatch_button('部门')  # 默认是人员派工，需手动选择部门派工
        # with allure.step('部门-派工-搜索部门名字'):
        #     self.dispatch_search_name('请输入部门', '财务部')
        # with allure.step('点击添加按钮'):
        #     self.dispatch_add_name('添加')
        # with allure.step('点击确定'):
        #     self.click_page_popups_bottom_button('确 定', '派工')
        #     assert self.is_tip_visible()

    # @allure.title('部门派工-转派工-已存在')
    # def test_dep_dispatch_transfer_exist(self):
    #     company_name = random_string_generator()
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu('代账服务', '服务管理')
    #     with allure.step('创建客户'):
    #         self.click_service_button_droplist('更多')
    #         self.select_service_type_droplist('新增客户')
    #         self.input_new_customer_name(company_name)
    #         self.select_new_customer_type('代理记账')
    #         self.click_new_customer_button('确定')
    #         assert '新增客户成功' in self.get_tip_text()
    #     with allure.step('搜索公司'):
    #         self.search_company(company_name)
    #     with allure.step('勾选某行'):
    #         self.select_audit_company(company_name)
    #     with allure.step('点击派工'):
    #         self.click_service_button('派工')
    #     with allure.step('选择部门'):
    #         self.click_dispatch_button('部门')  # 默认是人员派工，需手动选择部门派工
    #     with allure.step('部门-派工-搜索部门名字'):
    #         self.dispatch_search_name('请输入部门', '财务部')
    #     with allure.step('点击添加按钮'):
    #         self.dispatch_add_name('添加')
    #     with allure.step('点击确定'):
    #         self.click_page_popups_bottom_button('确 定', '派工')
    #         assert '派工成功！' in self.get_tip_text()
    #     with allure.step('点击派工查询标签页'):
    #         self.click_dispatch_or_query_button('派工查询')
    #     with allure.step('转派工'):
    #         self.click_dispatch_change_button('财务部', '转派工')
    #         self.click_dispatch_department_select_button()
    #         self.click_dispatch_staff_select_button('财务部')  # 根据老部门定位新职员，默认选择第一个
    #         self.click_dispatch_ok_button('确定')
    #         assert '客户已存在财务部部门的派工，请选择其它职员或部门' in self.get_tip_text()

    # @allure.title('部门派工-转派工人员-已存在')
    # def test_dispatch_transfer_stuff_exist(self):
    #     company_name = random_string_generator()
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu('代账服务', '服务管理')
    #     with allure.step('创建客户'):
    #         self.click_service_button_droplist('更多')
    #         self.select_service_type_droplist('新增客户')
    #         self.input_new_customer_name(company_name)
    #         self.select_new_customer_type('代理记账')
    #         self.click_new_customer_button('确定')
    #         assert '新增客户成功' in self.get_tip_text()
    #     with allure.step('搜索公司'):
    #         self.search_company(company_name)
    #     with allure.step('勾选某行'):
    #         self.select_audit_company(company_name)
    #     with allure.step('点击派工'):
    #         self.click_service_button('派工')
    #         self.dispatch_search_name('请输入人员', '财务01')
    #     with allure.step('点击添加按钮'):
    #         self.dispatch_add_name('添加')
    #     with allure.step('检查是否需要授权'):
    #         self.click_add_tips_button('继续')
    #     with allure.step('点击确定'):
    #         self.click_service_details_bottom_button('确 定')
    #         assert '派工成功！' in self.get_tip_text()
    #     with allure.step('点击派工查询标签页'):
    #         self.click_dispatch_or_query_button('派工查询')  # 可输入派工or派工查询
    #     # 找到外勤部所在的行，先后点击【转派工】与【删除】按钮
    #     with allure.step('转派工'):
    #         self.click_dispatch_change_button('财务部', '转派工')
    #         self.click_dispatch_department_select_button('财务部')
    #         self.click_dispatch_staff_select_button('财务01')  # 根据老部门定位新职员，默认选择第一个
    #         self.click_dispatch_ok_button('确定')  # 根据老部门定位确定或取消按钮
    #         assert '已存在财务01职员且角色为客户经理(代账)岗位的派工，请选择其它职员或部门' in self.get_tip_text()

    # @allure.title('部门派工-转派工')
    # def test_dispatch_transfer(self):
    #     company_name = random_string_generator()
    #     with allure.step('登录'):
    #         self.login()
    #         self.close_popup()
    #     with allure.step('点击菜单'):
    #         self.click_manager_menu('代账服务', '服务管理')
    #     with allure.step('创建客户'):
    #         self.click_service_button_droplist('更多')
    #         self.select_service_type_droplist('新增客户')
    #         self.input_new_customer_name(company_name)
    #         self.select_new_customer_type('代理记账')
    #         self.click_new_customer_button('确定')
    #         assert '新增客户成功' in self.get_tip_text()
    #     with allure.step('搜索公司'):
    #         self.search_company(company_name)
    #     with allure.step('勾选某行'):
    #         self.select_audit_company(company_name)
    #     with allure.step('点击派工'):
    #         self.click_service_button('派工')
    #     # 弹出派工弹框
    #     with allure.step('选择部门'):
    #         self.click_dispatch_button('部门')  # 默认是人员派工，需手动选择部门派工
    #     with allure.step('部门-派工-搜索部门名字'):
    #         self.dispatch_search_name('请输入部门', '财务部')
    #     with allure.step('点击添加按钮'):
    #         self.dispatch_add_name('添加')
    #     with allure.step('点击确定'):
    #         self.click_page_popups_bottom_button('确 定', '派工')
    #         assert '派工成功！' in self.get_tip_text()
    #     # 弹出派工弹框
    #     with allure.step('点击派工查询标签页'):
    #         self.click_dispatch_or_query_button('派工查询')  # 可输入派工or派工查询
    #     # 找到外勤部所在的行，先后点击【转派工】与【删除】按钮
    #     with allure.step('转派工'):
    #         self.click_dispatch_change_button('财务部', '转派工')  # 财务部所在行的转派工按钮（上一个用例中选了财务部）
    #         # 点击转派工后，选择xx部门xx职员
    #         self.click_dispatch_department_select_button()  # 根据老部门定位新部门，默认选择第一个
    #         # 选择XX职员（默认选择第一职员）
    #         self.click_dispatch_staff_select_button('行政01')  # 根据老部门定位新职员，默认选择第一个
    #         self.click_dispatch_ok_button('确定')  # 根据老部门定位确定或取消按钮
    #         assert '转派工成功！' in self.get_tip_text()
    #         self.wait(1.5)
    #     with allure.step('删除派工'):
    #         self.click_dispatch_change_button('行政部', '删除')  # 财务部所在行的删除按钮
    #         assert '删除成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('报税_审税金与反审税金')
    def test_audit_tax_anti_audit(self):
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
            self.input_tax_info(['增值税（一般纳税人）', '个人所得税', '印花税'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('填写税金'):
            self.click_table_button(company_name, '填写税金')
            self.select_service_month('报税期间', '1')  # 报税期间选择月份
            for _ in range(3):
                self.input_taxes_details(f'{_ + 1}', '300')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '填写税金')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
            self.select_audit_company(company_name)
        with allure.step('点击审税金'):
            self.click_service_button('审税金')
        with allure.step('选择税金'):
            self.select_audit_taxes('审税金')  # 选择第一行账期的税金
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '审税金')  # 审税金页面的确定按钮
            assert '审核成功！' in self.get_tip_text()
        with allure.step('还原账号数据'):
            self.select_audit_company(company_name)  # 勾选某行
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('反审税金')  # 从下拉框里选择”反审税金“
        with allure.step('反审'):
            self.select_audit_taxes('反审税金')  # 选择第一行账期的税金
            self.click_page_popups_bottom_button('确 定', '反审税金')  # 反审税金页面的确定按钮
            assert '反审成功！' in self.get_tip_text()

    @allure.title('报税-未审核')
    def test_audit_tax_not_audit(self):
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
            self.input_tax_info(['增值税（一般纳税人）', '个人所得税', '印花税'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击填写税金'):
            self.click_table_button(company_name, '填写税金')
        # 跳转至填写税金弹框
        with allure.step('填写税金'):
            self.select_service_month('报税期间', '1')  # 报税期间选择月份
            for _ in range(3):
                self.input_taxes_details(f'{_ + 1}', '300')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '填写税金')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
        with allure.step('报税'):
            self.click_page_popups_bottom_button('确 定', '报税')
            assert '请审核税金' in self.get_tip_text()

    @allure.title('报税-未上传图片')
    def test_audit_tax_empty_picture(self):
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
            self.input_tax_info(['增值税（一般纳税人）', '个人所得税', '印花税'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击填写税金'):
            self.click_table_button(company_name, '填写税金')
        # 跳转至填写税金弹框
        with allure.step('填写税金'):
            self.select_service_month('报税期间', '1')  # 报税期间选择月份
            for _ in range(3):
                self.input_taxes_details(f'{_ + 1}', '300')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '填写税金')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('点击审税金'):
            self.click_service_button('审税金')
        # 弹出审税金弹框
        with allure.step('选择税金'):
            self.select_audit_taxes('审税金')  # 选择第一行账期的税金
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '审税金')  # 审税金页面的确定按钮
            assert '审核成功！' in self.get_tip_text()
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
        with allure.step('报税'):
            self.click_page_popups_bottom_button('确 定', '报税')
            assert '请上传图片' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('报税')
    def test_audit_tax(self):
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
            self.input_tax_info(['增值税（一般纳税人）', '个人所得税', '印花税'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击填写税金'):
            self.click_table_button(company_name, '填写税金')
        # 跳转至填写税金弹框
        with allure.step('填写税金'):
            self.select_service_month('报税期间', '1')  # 报税期间选择月份
            for _ in range(3):
                self.input_taxes_details(f'{_ + 1}', '300')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '填写税金')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('点击审税金'):
            self.click_service_button('审税金')
        # 弹出审税金弹框
        with allure.step('选择税金'):
            self.select_audit_taxes('审税金')  # 选择第一行账期的税金
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '审税金')  # 审税金页面的确定按钮
            assert '审核成功！' in self.get_tip_text()
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
        with allure.step('上传图片'):
            self.upload_tax_picture(f'{get_project_path()}/template/common/Snipaste.png')
        with allure.step('报税'):
            self.click_page_popups_bottom_button('确 定', '报税')
            assert '保存成功' in self.get_tip_text()

    @allure.title('填写税金并重新报税')
    def test_tax_declaration(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.input_tax_info(['增值税（一般纳税人）'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击填写税金'):
            self.click_table_button(company_name, '填写税金')
        with allure.step('填写税金'):
            self.select_service_month('报税期间', '1')  # 报税期间选择月份
            self.input_taxes_details('1', '300')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '填写税金')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
        with allure.step('重新报税'):
            self.click_page_popups_bottom_button('重新报税', '报税')
        with allure.step('弹框确认'):
            self.click_conform_button('确定')
            assert '保存成功！' in self.get_tip_text()

    @allure.title('服务设定')
    def test_setting_services(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击服务设定'):
            self.click_table_button(company_name, '服务设定')
        with allure.step('确定'):
            self.click_page_popups_bottom_button('确 定', '服务设定')
            assert '保存成功！' in self.get_tip_text()

    @allure.title('报税_不需报税与重新报税')
    def test_tax_redeclaration(self):
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
            self.input_tax_info(['增值税（一般纳税人）'])
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
        with allure.step('不需报税'):
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
            self.click_page_popups_bottom_button('不需报税', '报税')
        with allure.step('弹框确认'):
            self.click_conform_button('确定')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('点击报税按钮'):
            self.click_table_button(company_name, '报税')
        with allure.step('重新报税'):
            self.select_service_month('报税账期', '1')  # 报税期间选择1月
            self.click_page_popups_bottom_button('重新报税', '报税')
        with allure.step('弹框确认'):
            self.click_conform_button('确定')
            assert '保存成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('收票-首次收票并删除收票记录')
    def test_receive_invoice(self):
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
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_begin_month('十一月')
            self.select_service_month('收票期间', '10')
            self.input_receipt_details('收入发票', '1', '1')
            self.input_receipt_details('收入发票', '100', '2')
            self.input_receipt_details('收入发票', '10', '3')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('点击收票记录按钮'):
            self.select_audit_company(company_name)
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('收票记录')
        with allure.step('删除收票记录'):
            self.click_operate_button_in_table_by_company(company_name, '删除')
            self.click_conform_delete_buttons('确定')
            assert '删除成功' in self.get_tip_text()

    @allure.title('收票-重复收票')
    def test_receive_invoice_twice(self):
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
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_begin_month('十一月')
            self.select_service_month('收票期间', '10')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '保存成功！' in self.get_tip_text()
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_service_month('收票期间', '10')
            self.input_receipt_details('收入发票', '1', '1')
            self.input_receipt_details('收入发票', '100', '2')
            self.input_receipt_details('收入发票', '10', '3')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '保存成功！' in self.get_tip_text()

    @allure.title('收票-首次收票-未选择开始期间')
    def test_receive_invoice_empty_period(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
        with allure.step('录入客户信息'):
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_service_month('收票期间', '10')
            self.input_receipt_details('收入发票', '1', '1')
            self.input_receipt_details('收入发票', '100', '2')
            self.input_receipt_details('收入发票', '10', '3')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '请选择开始期间' in self.get_tip_text()

    @allure.title('收票-首次收票-未选择账期')
    def test_receive_invoice_empty_acct_period(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
        with allure.step('录入客户信息'):
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_begin_month('十一月')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '请选择账期' in self.get_tip_text()

    @allure.title('收票-首次收票')
    def test_receive_invoice_empty_record(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
        with allure.step('录入客户信息'):
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收票按钮'):
            self.click_table_button(company_name, '收票')
        with allure.step('录入收票信息'):
            self.select_service_month('收票期间', '10')
            self.input_receipt_details('收入发票', '1', '1')
            self.input_receipt_details('收入发票', '100', '2')
            self.input_receipt_details('收入发票', '10', '3')
            self.select_begin_month('十一月')
            self.click_page_popups_bottom_button('保存', '收票')
            assert '保存成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('添加服务')
    def test_add_service(self):
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
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('更多-添加服务'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('添加服务')  # 从下拉框里选择”添加服务“
        # 弹出添加服务弹框
        with allure.step('选择某一个服务类型'):
            self.select_service('服务类型', '工商变更')
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '添加服务')
            assert '保存成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('停止服务与恢复服务')
    def test_stop_service(self):
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
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        # 停止服务
        with allure.step('停止服务'):
            self.click_service_button('停止服务')
        # 弹出停止服务确认对话框
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '停止服务')
            assert '停止服务成功！' in self.get_tip_text()
        # 恢复服务
        with allure.step('点击”已停止服务“选项卡'):
            self.stop_or_not_services('已停止服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('勾选某行'):
            self.select_audit_company(company_name)
        with allure.step('恢复服务'):
            self.click_service_button('恢复服务')
        # 弹出停止服务确认对话框
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '恢复服务')
            assert '恢复服务成功！' in self.get_tip_text()

    @pytest.mark.p1
    @allure.title('创建账套并删除-小企业会计准则（2013年版）')
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
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(company_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(company_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(company_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(company_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
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

    @allure.title('创建账套并删除-新会计准则（2006年版）')
    def test_create_account_set_new_accounting_standards(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('新会计准则（2006年版）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-新企业会计准则（2019年未执行新金融、新收入和新租赁准则）')
    def test_create_account_set_accounting_standards_for_business_enterprise(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('新企业会计准则（2019年未执行新金融、新收入和新租赁准则）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-新企业会计准则（2019年执行新金融、新收入和新租赁准则）')
    def test_create_account_set_accounting_standards_for_business_enterprise_executed(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('新企业会计准则（2019年执行新金融、新收入和新租赁准则）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-民间非营利组织会计制度')
    def test_create_account_set_accounting_standards_for_non_profit(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('民间非营利组织会计制度')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-农村集体经济组织会计制度(2008年版)')
    def test_create_account_set_accounting_standards_for_village_2008(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('农村集体经济组织会计制度(2008年版)')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-农村集体经济组织会计制度(2024年版)')
    def test_create_account_set_accounting_standards_for_village_2008(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('农村集体经济组织会计制度(2024年版)')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-政府制度会计准则')
    def test_create_account_set_accounting_standards_for_government(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('政府制度会计准则')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-农民专业合作社财务会计制度(2007年版)')
    def test_create_account_set_accounting_standards_for_farmers_professional_cooperatives_2007(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('农民专业合作社财务会计制度(2007年版)')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('创建账套并删除-农民专业合作社财务会计制度(2021年版)')
    def test_create_account_set_accounting_standards_for_farmers_professional_cooperatives_2021(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('检查是否已创建账套'):
            if not self.is_element_visible(self.service_table_line_buttons(account_name, '创建账套')):
                with allure.step('搜索公司'):
                    self.search_company(account_name)
                with allure.step('勾选某行'):
                    self.select_audit_company(account_name)
                with allure.step('更多-删除账套'):
                    self.click_service_button_droplist('更多')  # 点击【更多】下拉框
                    self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
                with allure.step('确认删除'):
                    self.click_page_popups_bottom_button('确 定', '删除账套')
                    assert self.is_delete_success(account_name)
                    self.click_page_popups_bottom_button('取 消', '删除账套')
        with allure.step('点击创建账套按钮'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(account_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2022')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('11')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('农民专业合作社财务会计制度(2021年版)')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert account_name == self.get_company_name()
            self.driver.close()
        with allure.step('搜索公司'):
            self.switch_to_window(ori_window)
            self.search_company(account_name)
        with allure.step('勾选某行'):
            self.select_audit_company(account_name)
        with allure.step('更多-删除账套'):
            self.click_service_button_droplist('更多')  # 点击【更多】下拉框
            self.select_service_type_droplist('删除账套')  # 从下拉框里选择”删除账套“
        with allure.step('点击确定'):
            self.click_page_popups_bottom_button('确 定', '删除账套')
            assert self.is_delete_success(account_name)

    @allure.title('跟进并删除跟进记录')
    def test_followup_and_delete(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('选择跟进类型'):
            self.click_table_button(account_name, '跟进')
            self.select_dropdown_item('跟进记录', '请选择', '续费跟进')
        with allure.step('输入并保存跟进记录'):
            title = '12123'
            self.type_textarea('跟进记录', title)
            self.click_page_popups_bottom_button('保 存', '跟进记录')
            assert '保存跟进记录成功' in self.get_tip_text()
        with allure.step('删除跟进记录'):
            self.click_followup_table_button(title, '删除')
        with allure.step('确认删除'):
            self.click_page_popups_bottom_button('确定删除', '提示')
            assert '删除成功' in self.get_tip_text()

    @allure.title('跟进并删除跟进记录-未录入')
    def test_already_followup_and_delete(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('选择跟进类型'):
            self.click_table_button(account_name, '跟进')
            self.select_dropdown_item('跟进记录', '请选择', '续费跟进')
        with allure.step('输入并保存跟进记录'):
            self.click_page_popups_bottom_button('保 存', '跟进记录')
            assert '请输入跟进记录' in self.get_tip_text()

    @allure.title('跟进记录置顶并取消')
    def test_pin_and_unpin(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('选择跟进类型'):
            self.click_table_button(account_name, '跟进')
            self.select_dropdown_item('跟进记录', '请选择', '续费跟进')
        with allure.step('输入并保存跟进记录'):
            title = '12123'
            self.type_textarea('跟进记录', title)
            self.click_page_popups_bottom_button('保 存', '跟进记录')
            assert '保存跟进记录成功' in self.get_tip_text()
        with allure.step('置顶'):
            self.click_followup_table_button(title, '置顶')
        with allure.step('取消置顶'):
            self.click_followup_table_button(title, '取消')
        with allure.step('删除跟进记录'):
            self.click_followup_table_button(title, '删除')
        with allure.step('确认删除'):
            self.click_page_popups_bottom_button('确定删除', '提示')
            assert '删除成功' in self.get_tip_text()

    @allure.title('收票-保存并标记完成-未选择')
    def test_invoice_save_and_mark_unselected(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('点击收票'):
            self.click_table_button(account_name, '收票')
        with allure.step('直接保存'):
            self.click_page_popups_bottom_button('保存并标记完成', '收票')
            assert '请选择开始期间！' in self.get_tip_text()

    @allure.title('收票-保存-未选择')
    def test_invoice_save_unselected(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('点击收票'):
            self.click_table_button(account_name, '收票')
        with allure.step('直接保存'):
            self.click_page_popups_bottom_button('保存', '收票')
            assert '请选择开始期间！' in self.get_tip_text()

    @allure.title('标记-未选择')
    def test_mark_unselected(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.search_company(account_name)
        with allure.step('点击标记'):
            self.click_table_button(account_name, '标记')
        with allure.step('直接保存'):
            self.click_page_popups_bottom_button('确 定', '标记')
            assert '保存成功' in self.get_tip_text()


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_agency
@pytest.mark.manager_agency_invoice
@allure.epic('管家')
@allure.feature('代账服务')
@allure.story('收票')
class TestReceiveInvoiceRecord(LoginPage,
                               ManagerCommonPage,
                               ManagerHomePage,
                               AgencyAccountPage,
                               ReceiveInvoiceRecordPage,
                               ReceiveInvoicePage,
                               CustomerPage):

    @allure.title('查询收票记录-全部')
    def test_query_record_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('收票')
        with allure.step('过滤人员'):
            self.switch_role('经理01')
        with allure.step('点击按钮'):
            self.click_normal_buttons('收票记录')

    @allure.title('查询派工记录-单客户')
    def test_query_dispatch_single(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('收票')
            self.click_mask_div()
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('点击菜单'):
            self.click_normal_buttons('更多')
            self.click_dropdown_buttons('派工查询')

    @pytest.mark.p1
    @allure.title('查询派工记录-全部')
    def test_query_dispatch_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('收票')
            self.click_mask_div()
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('点击菜单'):
            self.click_normal_buttons('更多')
            self.click_dropdown_buttons('派工查询')
            self.click_normal_buttons('查询')


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_agency
@pytest.mark.manager_agency_bookkeeping
@allure.epic('管家')
@allure.feature('代账服务')
@allure.story('记账')
class TestBookkeeping(LoginPage,
                      ManagerCommonPage,
                      ManagerHomePage,
                      AgencyAccountPage,
                      ReceiveInvoiceRecordPage,
                      ReceiveInvoicePage,
                      BookkeepingPage,
                      CustomerPage):
    @pytest.mark.p1
    @allure.title('标记缺票并取消-银行')
    def test_lark_invoice_mark_bank(self):
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
        with allure.step('切换功能页签'):
            self.click_agency_title('记账')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('标记缺票'):
            self.bookkeeping_search_company(company_name)
            self.click_buttons_in_line_by_company(company_name, '缺票')
            self.click_lark_invoice_mark_inputs_by_label('银行对账单')
            self.lark_invoice_mark_select_month('02')
            self.click_lark_invoice_mark_buttons('确定')
            assert '保存成功' in self.get_tip_text()

    @allure.title('标记缺票并取消-工资')
    def test_lark_invoice_mark_salary(self):
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
        with allure.step('切换功能页签'):
            self.click_agency_title('记账')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('标记缺票'):
            self.bookkeeping_search_company(company_name)
            self.click_buttons_in_line_by_company(company_name, '缺票')
            self.click_lark_invoice_mark_inputs_by_label('工资单')
            self.lark_invoice_mark_select_month('03')
            self.click_lark_invoice_mark_buttons('确定')
            assert '保存成功' in self.get_tip_text()

    @allure.title('标记缺票并取消-社保')
    def test_lark_invoice_mark_social_insurance(self):
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
        with allure.step('切换功能页签'):
            self.click_agency_title('记账')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('标记缺票'):
            self.bookkeeping_search_company(company_name)
            self.click_buttons_in_line_by_company(company_name, '缺票')
            self.click_lark_invoice_mark_inputs_by_label('社保')
            self.lark_invoice_mark_select_month('03')
            self.click_lark_invoice_mark_buttons('确定')
            assert '保存成功' in self.get_tip_text()

    @allure.title('标记缺票并取消-公积金')
    def test_lark_invoice_mark_accumulation_fund(self):
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
        with allure.step('切换功能页签'):
            self.click_agency_title('记账')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('标记缺票'):
            self.bookkeeping_search_company(company_name)
            self.click_buttons_in_line_by_company(company_name, '缺票')
            self.click_lark_invoice_mark_inputs_by_label('公积金')
            self.lark_invoice_mark_select_month('03')
            self.click_lark_invoice_mark_buttons('确定')
            assert '保存成功' in self.get_tip_text()


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_agency
@pytest.mark.manager_agency_service
@allure.epic('管家')
@allure.feature('财务管理')
@allure.story('服务管理-导出')
class TestAgencyServiceExport(LoginPage, ManagerHomePage, AgencyAccountPage, ReceiveInvoicePage):

    @allure.title('导出列表全部数据')
    def test_export_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('导出')
            self.click_export_type_button('按列表全部导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\代账服务-列表导出-全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选数据')
    def test_export_list_selected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('导出')
            self.click_export_type_button('按列表勾选导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\代账服务-列表导出-勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('按照导入模板导出列表全部数据')
    def test_export_list_by_import_template_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('按导入模板导出')
            self.click_export_type_button('按列表全部导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\代账服务-按导入模板导出-全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('按照导入模板导出列表勾选数据')
    def test_export_list_by_import_template_selected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('按导入模板导出')
            self.click_export_type_button('按列表勾选导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\代账服务-按导入模板导出-勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('收票流程导出')
    def test_collection_flow_export(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('收票')
            self.click_mask_div()
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('点击按钮'):
            self.click_normal_buttons('流程导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\客户流程节点表-收票.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('记账流程导出')
    def test_bookkeeping_flow_export(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('记账')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('点击按钮'):
            self.click_normal_buttons('流程导出')
            # tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
            # rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\客户流程节点表-记账.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('报税流程导出')
    def test_tax_flow_export(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换功能页签'):
            self.click_agency_title('报税')
        with allure.step('过滤人员'):
            self.switch_root_role()
        with allure.step('点击按钮'):
            self.click_normal_buttons('流程导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\agency\\客户流程节点表-报税.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_agency
@pytest.mark.manager_agency_service
@allure.epic('管家')
@allure.feature('智能财税')
@allure.story('智能采集')
class TestGatherInvoice(LoginPage, ManagerHomePage, GatherInvoicePage):
    @allure.tag('【管家】12月项目')
    @allure.tag('R20231123-032')
    @allure.title('导出列表全部数据')
    def test_gather_invoice_delete_conform(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('智能财税', '智能采集')
        with allure.step('发票采集'):
            self.switch_to_gather_frame()
            self.click_invoice_tab()
            self.click_in_line_buttons_by_invoice_name('销项:税务数字账户-销项:EXCEL', 'delete')
            assert self.is_conform_box_cancel_buttons_visible()
