import allure
import pytest

from page.manager.page_agency import AgencyAccountPage
from page.manager.page_business import BusinessServicePage
from page.manager.page_contract import ContractPage
from page.manager.page_customer import CustomerPage
from page.manager.page_system import SystemBinPage
from page.page_login import LoginPage
from page.manager.page_home import ManagerHomePage
from page.manager.page_collection import CollectionPage
from page.manager.page_common import ManagerCommonPage

from utils.random_data import random_string_generator


@pytest.mark.manager
@pytest.mark.manager_finance
@pytest.mark.manager_finance_follow_up
@allure.epic('管家')
@allure.feature('财务管理')
@allure.story('收款跟进')
class TestCollection(
    LoginPage,
    ManagerHomePage,
    ManagerCommonPage,
    CollectionPage,
    AgencyAccountPage,
    CustomerPage,
    BusinessServicePage,
    ContractPage,
    SystemBinPage
):

    @allure.title('收款-代账服务')
    def test_normal_collection_and_cancel(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.input_collection_details('本次收款', '300')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('取消收款'):
            self.click_audit_table_button('取消收款')
            self.click_conform_cancel()
            assert "成功" in self.get_tip_text()

    @allure.title('申请流失')
    def test_lost_customer_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('点击申请流失'):
            self.click_normal_button('申请流失')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('停止服务')
    def test_stop_service_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('点击申请流失'):
            self.click_normal_button('停止服务')
            assert '请先选择客户！' in self.get_tip_text()

    @allure.title('收款-工商服务')
    def test_collection_business_service(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class('其它费用', 'bussIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()

    @allure.title('收款-工商服务-未录入收款信息')
    def test_collection_business_service_empty_collection_details(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "您未勾选任何收款项目进行收款，请检查" in self.get_tip_text()

    @allure.title('收款-代账服务-帐本费')
    def test_collection_agency_service_bookkeeping(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_year('2023')
            self.type_to_amount_input_in_table_bookkeeping('500')
            self.type_to_discount_input_in_table_bookkeeping('0.9')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()

    @allure.title('收款-新增并删除收款类型')
    def test_add_and_del_collection_class(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('代账服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @allure.title('收款-新增收款类型-名称为空')
    def test_add_collection_class_empty_name(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('新增自定义收款类别'):
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.click_add_collection_class_buttons('确定')
            assert "名称不能为空" in self.get_tip_text()

    @allure.title('收款-新增收款类型-名称重复')
    def test_add_collection_class_repetitive_name(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('代账服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('代账服务')
            self.click_add_collection_class_buttons('确定')
            assert "费用项目重复" in self.get_tip_text()
            self.click_add_collection_class_buttons('取消')
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @allure.title('收款-代账服务-自定义收款')
    def test_collection_agency_service_customize(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
            self.click_table_button(company_name, '收款')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('代账服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class(new_class_name, 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table(new_class_name, '1', '300')
            self.type_to_collection_discount_input_in_table(new_class_name, '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('取消收款'):
            self.click_audit_table_button('取消收款')
            self.click_conform_cancel()
            assert "成功" in self.get_tip_text()
            self.click_tag_close_button('收款审核')
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @allure.title('收款-工商服务-自定义收款')
    def test_collection_business_service_customize(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('工商服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class(new_class_name, 'bussIcon', '1')
            self.type_to_collection_amount_input_in_table(new_class_name, '1', '300')
            self.type_to_collection_discount_input_in_table(new_class_name, '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('取消收款'):
            self.click_audit_table_button('取消收款')
            self.click_conform_cancel()
            assert "取消成功" in self.get_tip_text()
            self.click_tag_close_button('收款审核')
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @allure.title('收款-多项目收款-工商')
    def test_collection_agency_business_service_multiple(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('工商服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
        with allure.step('填写工商自定义行'):
            self.select_collection_class('其它费用', 'bussIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('增行填写自定义行'):
            self.click_add_line_button()
            self.select_collection_class(new_class_name, 'bussIcon', '2')
            self.type_to_collection_amount_input_in_table(new_class_name, '1', '300')
            self.type_to_collection_discount_input_in_table(new_class_name, '2', '0.8')
        with allure.step('增行删行'):
            self.click_add_line_button()
            self.click_delete_line_button('3')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('取消收款'):
            self.click_audit_table_button('取消收款')
            self.click_conform_cancel()
            assert "取消成功" in self.get_tip_text()
            self.click_tag_close_button('收款审核')
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @allure.title('收款-多项目收款-代账')
    def test_collection_agency_acct_service_multiple(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.select_year('2023')
            self.type_to_amount_input_in_table_bookkeeping('500')
            self.type_to_discount_input_in_table_bookkeeping('0.9')
        with allure.step('新增自定义收款类别'):
            new_class_name = random_string_generator()
            self.click_collection_class('1')
            self.click_add_collection_class_button()
            self.type_to_add_collection_class_input(new_class_name)
            self.select_collection_class_belong_to('代账服务')
            self.click_add_collection_class_buttons('确定')
            assert "新增成功" in self.get_tip_text()
        with allure.step('填写工商自定义行'):
            self.select_collection_class('其它费用', 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('增行填写自定义行'):
            self.click_add_line_button()
            self.select_collection_class(new_class_name, 'acctIcon', '2')
            self.type_to_collection_amount_input_in_table(new_class_name, '1', '300')
            self.type_to_collection_discount_input_in_table(new_class_name, '2', '0.8')
        with allure.step('增行删行'):
            self.click_add_line_button()
            self.click_delete_line_button('4')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('取消收款'):
            self.click_audit_table_button('取消收款')
            self.click_conform_cancel()
            assert "取消成功" in self.get_tip_text()
            self.click_tag_close_button('收款审核')
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('删除自定义收款类别'):
            self.click_collection_class('1')
            self.click_collection_class_operate_button(new_class_name, 'delete')
            self.click_conform_delete_collection_class_buttons('确定')
            assert "删除成功" in self.get_tip_text()

    @pytest.mark.proj
    @allure.tag('【管家】2023-09-07')
    @allure.tag('R20230729-005')
    @allure.title('操作收款后下次收款日期显示不对-查询合同应收金额没过滤已删除合同的应收')
    def test_query_contract_amount_should_remove_already_del_contract_amount(self):
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
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', company_name)
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2023-01\n')
            self.input_bookkeeping_detail('服务结束日期', '2023-12\n')
            self.input_bookkeeping_detail('月服务费', '300\n')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
            self.click_tag_close_button('合同')
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')
        with allure.step('搜索公司'):
            self.search_agency_company(company_name)
        with allure.step('创建账套'):
            ori_window = self.driver.current_window_handle
            self.click_table_button(company_name, '创建账套')
            self.click_ignore_set_tip()
            self.wait(3)
            self.switch_to_newest_window()
            self.wait(2)
        with allure.step('创建账套_填写启用期间'):
            self.input_enable_year('2023')  # 编写启用期间：xxx年xx期，如2022年11期
            self.input_enable_month('01')  # 编写启用期间：xxx年xx期，如2022年11期
            self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
            self.select_accounting_standards('小企业会计准则（2013年版）')
        with allure.step('创建账套_点击开始创建'):
            self.click_create_button('开始创建')  # 后跳转至会计页面
            assert company_name == self.get_company_name()
            self.driver.close()
            self.switch_to_window(ori_window)
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
        with allure.step('选择客户'):
            self.close_ads()
            self.search_customer(company_name)
            self.click_customer_table_checkbox(company_name)
        with allure.step('删除客户'):
            self.click_customer_dropdown_buttons('更多', '删除')
            self.click_delete_customer_button('删除')
            assert '删除客户成功' in self.get_tip_text()
            self.click_tag_close_button('客户')
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '回收站')
        with allure.step('恢复账套'):
            self.click_system_bin_button_in_line_by_company(company_name, '恢复')
            self.click_system_bin_conform_recover_buttons()
            assert '恢复成功' in self.get_tip_text()
            self.click_tag_close_button('回收站')
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '合同')
        with allure.step('点击新增合同按钮'):
            self.click_new_contract()
        with allure.step('输入合同基本信息'):
            self.input_contract_detail('客户名称', f'{company_name}_恢复')
        with allure.step('勾选代账服务'):
            self.check_service_type('代账服务')
        with allure.step('输入代账服务信息'):
            self.input_bookkeeping_detail('服务开始日期', '2023-01\n')
            self.input_bookkeeping_detail('服务结束日期', '2023-12\n')
            self.input_bookkeeping_detail('月服务费', '450\n')
        with allure.step('保存合同'):
            self.click_save_button()
        with allure.step('验证浮动提示'):
            assert '新增合同成功' in self.get_tip_text()
            self.click_tag_close_button('合同')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.type_to_collection_inputs('开始收款时间', '2023-01\n')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('检查下次收款日期'):
            assert '2024.01-2024.12' in self.get_text_from_collection_list_next_period_item_by_company(f'{company_name}_恢复')


@pytest.mark.manager
@pytest.mark.manager_finance
@pytest.mark.manager_finance_audit
@allure.epic('管家')
@allure.feature('财务管理')
@allure.story('收款审核')
class TestCollectionAudit(LoginPage, ManagerHomePage, ManagerCommonPage, CollectionPage, ContractPage,
                          AgencyAccountPage, CustomerPage, BusinessServicePage):

    @allure.title('驳回并删除收款-代账服务')
    def test_overrule_collection_and_delete(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.input_collection_details('本次收款', '300')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert '保存成功' in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('勾选收款记录并驳回'):
            self.collection_select_audit_company(company_name)
            self.click_collection_audit_button('驳回')
            self.input_overrule_text('overrule')
            self.click_overrule_button('确定')
            assert '驳回成功' in self.get_tip_text()

    @allure.title('驳回并删除收款-工商服务')
    def test_overrule_collection_and_delete_business_service(self):
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
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_name)
        with allure.step('点击收款'):
            self.click_table_button(company_name, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class('其它费用', 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert '保存成功' in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_name, '收款记录')
        with allure.step('勾选收款记录并驳回'):
            self.collection_select_audit_company(company_name)
            self.click_collection_audit_button('驳回')
        with allure.step('填写驳回原因并点击确定'):
            self.input_overrule_text('overrule')
            self.click_overrule_button('确定')
            assert '驳回成功' in self.get_tip_text()

    @allure.title('审核并取消审核')
    def test_audit_collection_and_cancel(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class('其它费用', 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert '保存成功' in self.get_tip_text()
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.input_collection_details('本次收款', '300')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_collection, '收款记录')
        with allure.step('勾选收款记录并审核'):
            self.collection_select_audit_company(company_collection)
            self.click_collection_audit_button('审核')
            assert "审核成功" in self.get_tip_text()

    @allure.title('审核并取消审核-工商服务')
    def test_audit_collection_and_cancel_business_service(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class('其它费用', 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert '保存成功' in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_collection, '收款记录')
        with allure.step('勾选收款记录并审核'):
            self.collection_select_audit_company(company_collection)
            self.click_collection_audit_button('审核')
            assert "审核成功" in self.get_tip_text()

    @allure.title('重新收款-完整合同')
    def test_recollect_complete_contract(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.input_collection_details('本次收款', '300')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_collection, '收款记录')
        with allure.step('勾选收款记录并驳回'):
            self.collection_select_audit_company(company_collection)
            self.click_collection_audit_button('驳回')
        with allure.step('填写驳回原因并点击确定'):
            self.input_overrule_text('overrule')
            self.click_overrule_button('确定')
            assert "驳回成功" in self.get_tip_text()
        with allure.step('重新收款'):
            self.click_audit_table_button('重新收款')
            self.click_conform_collect('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()

    @allure.title('重新收款')
    def test_recollect(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_service_month('7')
            self.input_collection_details('本次收款', '300')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_collection, '收款记录')
        with allure.step('勾选收款记录并驳回'):
            self.collection_select_audit_company(company_collection)
            self.click_collection_audit_button('驳回')
        with allure.step('填写驳回原因并点击确定'):
            self.input_overrule_text('overrule')
            self.click_overrule_button('确定')
            assert "驳回成功" in self.get_tip_text()
        with allure.step('重新收款'):
            self.click_audit_table_button('重新收款')
            self.click_conform_collect('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()

    @allure.title('重新收款-工商服务')
    def test_recollect_business_service(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('工商服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_business_service_normal_button('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('工商注册')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.select_collection_class('其它费用', 'acctIcon', '1')
            self.type_to_collection_amount_input_in_table('其它费用', '1', '300')
            self.type_to_collection_discount_input_in_table('其它费用', '2', '0.8')
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()
        with allure.step('点击收款记录'):
            self.click_table_button(company_collection, '收款记录')
        with allure.step('勾选收款记录并驳回'):
            self.collection_select_audit_company(company_collection)
            self.click_collection_audit_button('驳回')
        with allure.step('填写驳回原因并点击确定'):
            self.input_overrule_text('overrule')
            self.click_overrule_button('确定')
            assert "驳回成功" in self.get_tip_text()
        with allure.step('重新收款'):
            self.click_audit_table_button('重新收款')
            self.click_conform_collect('确定收款')
            self.ignore_tips()
            assert "保存成功" in self.get_tip_text()

    @allure.title('收款-跨年收款')
    def test_collection_over_year(self):
        company_collection = random_string_generator()
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('代账服务', '服务管理')  # 一级菜单与二级菜单
        with allure.step('创建客户'):
            self.click_service_button_droplist('更多')
            self.select_service_type_droplist('新增客户')
            self.input_new_customer_name(company_collection)
            self.select_new_customer_type('代理记账')
            self.click_new_customer_button('确定')
            assert '新增客户成功' in self.get_tip_text()
            self.click_tag_close_button('服务管理')
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('搜索公司'):
            self.search_company(company_collection)
        with allure.step('点击收款'):
            self.click_table_button(company_collection, '收款')
        with allure.step('填写收款信息'):
            self.select_collect_type('支付宝')
            self.locate_specific_year('2024')
            self.select_multiple_month(['1', '2', '3'])
            self.locate_specific_year('2023')
            self.select_multiple_month(['10', '11', '12'])
        with allure.step('确定收款'):
            self.click_collection_details_bottom_button('确定收款')
            assert "保存成功" in self.get_tip_text()

    @allure.title('驳回-未勾选')
    def test_overrule_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_audit_button('驳回')
            assert "请先选择客户" in self.get_tip_text()

    @allure.title('取消已打印标识-未勾选')
    def test_cancel_print_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_audit_button('取消已打印标识')
            assert "请先选择客户" in self.get_tip_text()

    @allure.title('取消已打印标识-未勾选')
    def test_cancel_print_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_audit_button('打印收据')
            assert "请先选择打印数据" in self.get_tip_text()

    @allure.title('审核-未勾选')
    def test_audit_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_audit_button('审核')
            assert "请选择待审核的收款记录" in self.get_tip_text()

    @allure.title('取消审核-未勾选')
    def test_audit_unselect(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_audit_button('取消审核')
            assert "请选择待取消审核的收款记录" in self.get_tip_text()


@pytest.mark.manager
@pytest.mark.manager_finance
@pytest.mark.manager_finance_follow_up
@allure.epic('管家')
@allure.feature('财务管理')
@allure.story('收款跟进-导出')
class TestCollectionExport(LoginPage, ManagerHomePage, CollectionPage):

    @allure.title('导出收款跟进列表-代账服务')
    def test_collection_export_followup_list(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('代账服务')
        with allure.step('查询2023年'):
            self.switch_to_year('2023')
        with allure.step('导出代账服务列表'):
            self.click_normal_button('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\collection\\收款跟进_2023年.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')

    @allure.title('导出收款跟进列表-工商服务')
    def test_collection_export_business_followup_list(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款跟进')
        with allure.step('切换业务类型'):
            self.click_switch_biz_type_on_top('工商服务')
        with allure.step('导出收款跟进列表'):
            self.click_normal_button('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\collection\\工商服务收款跟进.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')


@pytest.mark.manager
@pytest.mark.manager_finance
@pytest.mark.manager_finance_audit
@allure.epic('管家')
@allure.feature('财务管理')
@allure.story('收款审核-导出')
class TestCollectionAuditExport(LoginPage, ManagerHomePage, CollectionPage):

    @allure.title('导出收款审核列表')
    def test_collection_export_business_audit_list(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('财务管理', '收款审核')
            self.click_collection_filters('收款日期', '本月')
        with allure.step('导出收款审核列表'):
            self.click_collection_audit_button('导出')
        #     tmp_filename = f'{random_string_generator()}.{get_downloaded_filename().split(".")[1]}'
        #     rename_downloaded_file(tmp_filename)
        # with allure.step('对比excel文件差异'):
        #     assert check_excel_diff(
        #         f'{get_project_path()}\\template\\manager\\collection\\收款审核表.xls',
        #         f'{get_project_path()}\\download_tmp\\{tmp_filename}')
