import allure
import pytest

from page.manager.page_agency import AgencyAccountPage
from page.manager.page_collection import CollectionPage
from page.manager.page_contract import ContractPage
from page.manager.page_customer import CustomerPage
from page.manager.page_report import RenewalAnalysisPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.manager.page_common import ManagerCommonPage
from page.manager.page_business import BusinessServicePage, BusinessReportPage

from utils.random_data import random_string_generator


@pytest.mark.manager
@pytest.mark.manager_business
@pytest.mark.manager_business_manage
@allure.epic('管家')
@allure.feature('工商服务')
@allure.story('服务管理')
class TestBusinessService(
    LoginPage,
    ManagerCommonPage,
    ManagerHomePage,
    AgencyAccountPage,
    CustomerPage,
    BusinessServicePage,
    ContractPage,
    CollectionPage,
    RenewalAnalysisPage
):
    @allure.title('开始服务-未勾选')
    def test_start_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击开始服务'):
            self.click_business_service_normal_button('开始服务')
            assert '至少选择一个公司' in self.get_tip_text()

    @allure.title('派工-未勾选')
    def test_dispatch_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击派工'):
            self.click_business_service_normal_button('派工')
            assert '至少选择一个公司' in self.get_tip_text()

    @allure.title('添加服务-未勾选')
    def test_add_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击派工'):
            self.click_business_service_normal_button('添加服务')
            assert '请选择一个服务' in self.get_tip_text()

    @allure.title('停止服务-未勾选')
    def test_stop_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击派工'):
            self.click_business_service_normal_button('更多', '停止服务')
            self.click_conform_stop_service()
            assert '至少选择一项要停止的服务' in self.get_tip_text()

    @allure.title('收齐资料-未开始服务')
    def test_collect_file_not_started_service(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.business_service_search_company(company_name)
        with allure.step('点击表格按钮'):
            self.click_buttons_in_line_by_company(company_name, '未收齐')
        with allure.step('录入资料详情'):
            labels = ['委托代理人的身份证件复印件', '公司名称预先核准申请书', '公司设立登记申请书']
            self.collect_files('资料已收齐', labels, random_string_generator())
            assert '还未确认开始服务，请先确认！' in self.get_tip_text()

    @allure.title('保存资料-未开始服务')
    def test_collected_file_not_started_service(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.business_service_search_company(company_name)
        with allure.step('点击表格按钮'):
            self.click_buttons_in_line_by_company(company_name, '未收齐')
        with allure.step('录入资料详情'):
            labels = ['委托代理人的身份证件复印件', '公司名称预先核准申请书', '公司设立登记申请书']
            self.collect_files('保 存', labels, random_string_generator())
            assert '还未确认开始服务，请先确认！' in self.get_tip_text()

    @allure.title('开始服务-单个公司')
    def test_start_service_single(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.business_service_search_company(company_name)
        with allure.step('点击表格按钮'):
            self.click_buttons_in_line_by_company(company_name, '开始服务')
            assert '开始服务成功' in self.get_tip_text()
        with allure.step('恢复初始状态'):
            self.click_buttons_in_line_by_company(company_name, '上一步')
            self.click_conform_tips_on_top_buttons('确定')
            assert '恢复初始状态' in self.get_tip_text()

    @allure.title('开始服务-多个公司')
    def test_start_service_multiple(self):
        company_name_1 = random_string_generator()
        company_name_2 = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name_1)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name_2)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('勾选行'):
            self.check_checkbox_in_line_by_company([company_name_1, company_name_2])
        with allure.step('点击按钮'):
            self.click_business_service_normal_button('开始服务')
            assert '开始服务成功' in self.get_tip_text()

    @allure.title('新增公司-空名称')
    def test_add_new_company_empty(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击按钮'):
            self.click_business_service_normal_button('新增客户')
            self.new_customer('')
            assert '客户名称、服务类型和合同编号均不能为空' in self.get_tip_text()

    @allure.title('新增公司-已存在')
    def test_add_new_company_exist(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert self.is_customer_exist_tip_visible()

    @allure.title('新增公司')
    def test_add_new_company(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('点击按钮'):
            self.click_business_service_normal_button('新增客户')
            self.new_customer(company_name)
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()

    @allure.title('人员派工-客户经理')
    def test_person_dispatch_manager(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.business_service_search_company(account_name)
        with allure.step('勾选某行'):
            self.check_checkbox_in_line_by_company(account_name)
        with allure.step('点击派工'):
            self.click_business_service_normal_button('派工')
        with allure.step('选择客户经理'):
            self.dispatch_select_style('客户经理')
        with allure.step('人员-派工-搜索名字'):
            self.dispatch_search_name('请输入人员', '经理01')
        with allure.step('点击添加按钮'):
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()
        with allure.step('还原账号数据'):
            self.click_dispatch_or_query_button('派工查询')  # 输入派工or派工查询，进入到派工查询页面
            self.click_dispatch_change_button('经理01', '删除')  # 点报税员角色所在行的【删除】按钮
            assert '删除成功！' in self.get_tip_text()

    @allure.title('人员派工-经办人')
    def test_person_dispatch_agency(self):
        account_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(account_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('搜索公司'):
            self.business_service_search_company(account_name)
        with allure.step('勾选某行'):
            self.check_checkbox_in_line_by_company(account_name)
        with allure.step('点击派工'):
            self.click_business_service_normal_button('派工')
        # 弹出派工弹框
        with allure.step('选择客户经理'):
            self.dispatch_select_style('经办人')
        with allure.step('人员-派工-搜索名字'):
            self.dispatch_search_name('请输入人员', '经办01')
        with allure.step('点击添加按钮'):
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()
        with allure.step('还原账号数据'):
            self.click_dispatch_or_query_button('派工查询')  # 输入派工or派工查询，进入到派工查询页面
            self.click_dispatch_change_button('经办01', '删除')  # 点报税员角色所在行的【删除】按钮
            assert '删除成功！' in self.get_tip_text()

    @allure.title('查询派工记录-单客户')
    def test_query_dispatch_single(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('更多', '派工查询')

    @allure.title('查询派工记录-全部')
    def test_query_dispatch_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('更多', '派工查询')
            self.click_business_service_normal_button('查询')

    @allure.title('停止服务并恢复')
    def test_stop_service_recover(self):
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
        with allure.step('过滤公司'):
            self.business_service_search_company(company_name)
            self.check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('更多', '停止服务')
            self.click_conform_stop_service()
            assert '停止服务成功' in self.get_tip_text()
        with allure.step('切换已停止服务'):
            self.click_stop_service_buttons('已停止服务')
        with allure.step('过滤公司'):
            self.business_service_search_company(company_name)
            self.check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('恢复服务')
            self.click_conform_recover_service_buttons('确定')
            assert '恢复服务成功' in self.get_tip_text()

    @allure.title('恢复服务-未勾选')
    def test_recover_service_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('切换已停止服务'):
            self.click_stop_service_buttons('已停止服务')
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('恢复服务')
            assert '至少选择一项要恢复的服务' in self.get_tip_text()

    @pytest.mark.proj
    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230810-032')
    @allure.title('将客户的代账服务停止，工商服务查询不到派工记录')
    def test_stop_agency_service_biz_service_cant_query_dispatch_record(self):
        contract_id = random_string_generator()
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_name)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2023-01\n')
            self.input_bookkeeping_detail('服务结束日期', '2023-12\n')
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
            self.click_tag_close_button('合同')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('勾选某行'):
            self.check_checkbox_in_line_by_company(company_name)
        with allure.step('点击派工'):
            self.click_business_service_normal_button('派工')
        with allure.step('选择客户经理'):
            self.dispatch_select_style('客户经理')
        with allure.step('人员-派工-搜索名字'):
            self.dispatch_search_name('请输入人员', '经理01')
        with allure.step('点击添加按钮'):
            self.dispatch_add_name('添加')
        with allure.step('检查是否需要授权'):
            self.click_add_tips_button('继续')
        with allure.step('点击确定'):
            self.click_service_details_bottom_button('确 定')
            assert '派工成功！' in self.get_tip_text()
            self.click_service_details_bottom_button('取 消')
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('勾选某行'):
            self.check_checkbox_in_line_by_company(company_name)
        with allure.step('点击派工'):
            self.click_business_service_normal_button('派工')
            self.click_dispatch_or_query_button('派工查询')
            assert self.get_line_num_from_dispatch_record_table() != 0


    @allure.title('查看工商应收明细')
    def test_business_payment_analysis(self):
        contract_id = random_string_generator()
        company_name = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_name)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_name)
            self.input_contract_detail('合同编号', contract_id)
        with allure.step('勾选工商服务服务'):
            self.check_service_type('工商服务')
        with allure.step('点击合同类型的下拉菜单'):
            self.click_spacial_dropdown_button()
            self.click_spacial_dropdown_drop_button()
            self.type_to_contract_business_service_table_amount_input_by_line(1, '3000')
            self.click_spacial_dropdown_button(2)
            self.click_spacial_dropdown_drop_button('工商变更')
            self.type_to_contract_business_service_table_amount_input_by_line(2, '4000')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
            self.click_tag_close_button('合同')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.type_to_collection_amount_input_in_table('工商注册', '1', '1000')
            self.type_to_collection_amount_input_in_table('工商变更', '1', '1500')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('勾选收款记录并审核'):
            self.collection_select_audit_company(company_name)
            self.click_collection_audit_button('审核')
            assert "审核成功" in self.get_tip_text()
            self.click_tag_close_button('收款跟进')
        with allure.step('点击菜单'):
            self.click_manager_menu('报表中心', '续费分析')
            self.renewal_analysis_click_report_type_div('工商应收明细')



@pytest.mark.manager
@pytest.mark.manager_business
@pytest.mark.manager_business_report
@allure.epic('管家')
@allure.feature('工商服务')
@allure.story('工商年报')
class TestBusinessReport(
    LoginPage,
    ManagerCommonPage,
    ManagerHomePage,
    AgencyAccountPage,
    CustomerPage,
    BusinessServicePage,
    BusinessReportPage
):

    @allure.title('确认已申报-未勾选')
    def test_conform_report_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('确认已申报')
            assert '请至少选择一项进行操作' in self.get_tip_text()

    @allure.title('设置年报方式-未勾选')
    def test_report_setting_unselected(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('设置年报方式')
            assert '请至少选择一项进行操作' in self.get_tip_text()

    @allure.title('确认已申报-单家公司')
    def test_conform_report_single(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_search_company(company_name)
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('确认已申报')
            assert '确认申报成功' in self.get_tip_text()
        with allure.step('还原数据'):
            self.report_click_buttons_in_line_by_company(company_name, '取消已申报')
            assert '已成功取消申报' in self.get_tip_text()

    @allure.title('确认已申报-单家公司-列表')
    def test_conform_report_single_by_list(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_search_company(company_name)
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.report_click_buttons_in_line_by_company(company_name, '确认已申报')
            self.click_conform_already_report_button()
            assert '确认申报成功' in self.get_tip_text()
        with allure.step('还原数据'):
            self.report_click_buttons_in_line_by_company(company_name, '取消已申报')
            assert '已成功取消申报' in self.get_tip_text()

    @allure.title('确认已申报-多家公司')
    def test_conform_report_multiple(self):
        company_name_1 = random_string_generator()
        company_name_2 = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name_1)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_name_2)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_check_checkbox_in_line_by_company([company_name_1, company_name_2])
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('确认已申报')
            self.click_conform_report_buttons('确定')
        with allure.step('还原数据'):
            for _ in [company_name_1, company_name_2]:
                self.report_click_buttons_in_line_by_company(_, '取消已申报')
                assert '已成功取消申报' in self.get_tip_text()

    @allure.title('确认已申报-重复确认')
    def test_conform_report_exist(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('确认已申报'):
            self.report_click_buttons_in_line_by_company(company_name, '确认已申报')
            self.click_conform_already_report_button()
            assert '确认申报成功' in self.get_tip_text()
            self.business_report_check_checkbox_in_line_by_company(company_name)
            self.click_business_service_normal_button('确认已申报')
            assert '当前所选客户已申报（或无需申报），无需再次确认申报' in self.get_tip_text()

    @allure.title('设置年报方式-单公司')
    def test_report_setting_single(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('设置年报方式'):
            self.click_business_service_normal_button('设置年报方式')
            report_type = '固定年报'
            self.click_report_type_radio(report_type)
            self.click_report_setting_buttons('确定')
            assert report_type in self.get_report_type_div_text(company_name)
        with allure.step('还原数据'):
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.click_business_service_normal_button('设置年报方式')
            report_type_roll = '滚动年报'
            self.click_report_type_radio(report_type_roll)
            self.click_report_setting_buttons('确定')
            assert report_type_roll in self.get_report_type_div_text(company_name)

    @allure.title('设置年报方式-单公司-列表')
    def test_report_setting_single_list(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('设置年报方式'):
            self.report_click_buttons_in_line_by_company(company_name, '设置年报方式')
            report_type = '固定年报'
            self.click_report_type_radio(report_type)
            self.click_report_setting_buttons('确定')
            assert report_type in self.get_report_type_div_text(company_name)
        with allure.step('还原数据'):
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('点击菜单'):
            self.report_click_buttons_in_line_by_company(company_name, '设置年报方式')
            report_type_roll = '滚动年报'
            self.click_report_type_radio(report_type_roll)
            self.click_report_setting_buttons('确定')
            assert report_type_roll in self.get_report_type_div_text(company_name)

    @allure.title('跟进-无跟进记录')
    def test_followup_empty(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('过滤公司'):
            self.business_report_check_checkbox_in_line_by_company(company_name)
        with allure.step('跟进'):
            self.report_click_buttons_in_line_by_company(company_name, '跟进')
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


@pytest.mark.manager
@pytest.mark.manager_business
@pytest.mark.manager_business_manage
@allure.epic('管家')
@allure.feature('工商服务')
@allure.story('服务管理-导出')
class TestBusinessServiceExport(LoginPage, ManagerHomePage, BusinessServicePage, AgencyAccountPage):

    @allure.title('导出列表全部数据')
    def test_export_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_business_service_normal_button('更多', '导出')
            self.click_export_type_button('按列表全部导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商服务-列表-全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选数据')
    def test_export_list_checked(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_business_service_normal_button('更多', '导出')
            self.click_export_type_button('按列表勾选导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商服务-列表-勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('按导入模板导出-导出列表全部数据')
    def test_export_list_all_by_import_template(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_business_service_normal_button('更多', '按导入模板导出')
            self.click_export_type_button('按列表全部导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商服务-按导入模板导出-列表-全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('按导入模板导出-导出列表勾选数据')
    def test_export_list_checked_by_import_template(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')
        with allure.step('更多-导出'):
            self.click_business_service_normal_button('更多', '按导入模板导出')
            self.click_export_type_button('按列表勾选导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商服务-按导入模板导出-列表-勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.manager
@pytest.mark.manager_business
@pytest.mark.manager_business_report
@allure.epic('管家')
@allure.feature('工商服务')
@allure.story('工商年报-导出')
class TestBusinessReportExport(LoginPage, ManagerHomePage, BusinessServicePage, BusinessReportPage, AgencyAccountPage):

    @allure.title('导出列表全部数据')
    def test_export_list_all(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('导出'):
            self.click_normal_button('导出')
            self.click_export_type_button('按列表全部导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商年报情况导出-列表全部.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出列表勾选数据')
    def test_export_list_checked(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '工商年报')
        with allure.step('设置过滤条件'):
            self.unselect_if_selected_filter_item('申报截止日期', '本月')
            self.unselect_if_selected_filter_item('申报状态', '待申报')
        with allure.step('导出'):
            self.click_normal_button('导出')
            self.click_export_type_button('按列表勾选导出')
            self.click_export_buttons('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\business\\工商年报情况导出-列表勾选.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')
