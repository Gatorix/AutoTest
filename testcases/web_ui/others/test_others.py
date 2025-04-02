import allure
import pytest

from page.web_ui.manager.page_agency import AgencyAccountPage
from page.web_ui.manager.page_common import ManagerCommonPage
from page.web_ui.manager.page_customer import CustomerPage
from page.web_ui.manager.page_home import ManagerHomePage
from page.web_ui.manager.page_system import SystemBinPage
from page.web_ui.page_login import LoginPage

from utils.file_utils import del_files


# @pytest.mark.skip
# @allure.epic('其他')
# @allure.feature('创建账套')
# class TestCreateSet(AgencyAccountPage,
#                     ManagerCommonPage,
#                     LoginPage,
#                     ManagerHomePage,
#                     AccountingHomePage):
#     def test_create_set(self):
#         for _ in company_list:
#             with allure.step('登录'):
#                 self.login()
#             with allure.step('关闭弹窗'):
#                 self.close_popup()
#             with allure.step('点击菜单'):
#                 try:
#                     self.click_manager_menu('代账服务', '服务管理')
#                 except ElementNotVisibleException:
#                     self.wait(1)
#                     self.click_manager_menu('代账服务', '服务管理')
#             with allure.step('搜索公司'):
#                 company = _.replace('\n', '')
#                 self.search_company(company)
#                 self.wait(2)
#                 if self.is_element_visible(self.service_table_line_buttons(company, '创建账套')):
#                     self.click_table_button(company, '创建账套')
#                     self.click_ignore_set_tip()
#                     self.wait(3)
#                     self.switch_to_accounting_window()
#
#                     self.input_enable_year('2023')  # 编写启用期间：xxx年xx期，如2022年11期
#                     self.input_enable_month('1')  # 编写启用期间：xxx年xx期，如2022年11期
#                     self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
#                     self.click_create_button('开始创建')  # 后跳转至会计页面
#                     assert company == self.get_company_name()
#                 else:
#                     continue
#
#     @pytest.mark.skip
#     def test_create_set_1(self):
#         for _ in company_list[::-1]:
#             with allure.step('登录'):
#                 self.login()
#             with allure.step('关闭弹窗'):
#                 self.close_popup()
#             with allure.step('点击菜单'):
#                 try:
#                     self.click_manager_menu('代账服务', '服务管理')
#                 except ElementNotVisibleException:
#                     self.wait(1)
#                     self.click_manager_menu('代账服务', '服务管理')
#             with allure.step('搜索公司'):
#                 company = _.replace('\n', '')
#                 self.search_company(company)
#                 self.wait(2)
#                 if self.is_element_visible(self.service_table_line_buttons(company, '创建账套')):
#                     self.click_table_button(company, '创建账套')
#                     self.click_ignore_set_tip()
#                     self.wait(3)
#                     self.switch_to_accounting_window()
#
#                     self.input_enable_year('2023')  # 编写启用期间：xxx年xx期，如2022年11期
#                     self.input_enable_month('1')  # 编写启用期间：xxx年xx期，如2022年11期
#                     self.select_tax_type('一般纳税人')  # 选择【纳税性质】:一般纳税人、小规模纳税人
#                     self.click_create_button('开始创建')  # 后跳转至会计页面
#                     assert company == self.get_company_name()
#                 else:
#                     continue
#
#
# @pytest.mark.skip
# @allure.epic('其他')
# @allure.feature('切换账套')
# class TestSwitchSet(AgencyAccountPage,
#                     ManagerCommonPage,
#                     LoginPage,
#                     ManagerHomePage,
#                     AccountingHomePage,
#                     AccountingCommonPage):
#     def test_switch_set_1(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         with allure.step('搜索公司'):
#             company = '切换测试101'
#             self.search_company(company)
#         with allure.step('进入账套'):
#             self.click_table_button(company, '进账簿')
#             self.switch_to_accounting_window()
#             for _ in range(len(company_list)):
#                 try:
#                     choice_company = random.choice(company_list).replace('\n', '')
#                     self.switch_acct(choice_company)
#                     assert choice_company == self.get_text_from_my_company_span()
#                 except NoSuchElementException:
#                     print(f'切换到：{choice_company} 失败\n')
#
#     def test_switch_set_2(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         with allure.step('搜索公司'):
#             company = '切换测试101'
#             self.search_company(company)
#         with allure.step('进入账套'):
#             self.click_table_button(company, '进账簿')
#             self.switch_to_accounting_window()
#             for _ in range(len(company_list)):
#                 try:
#                     choice_company = random.choice(company_list).replace('\n', '')
#                     self.switch_acct(choice_company)
#                     assert choice_company == self.get_text_from_my_company_span()
#                 except NoSuchElementException:
#                     print(f'切换到：{choice_company} 失败\n')
#
#     def test_switch_set_3(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         with allure.step('搜索公司'):
#             company = '切换测试101'
#             self.search_company(company)
#         with allure.step('进入账套'):
#             self.click_table_button(company, '进账簿')
#             self.switch_to_accounting_window()
#             for _ in range(len(company_list)):
#                 try:
#                     choice_company = random.choice(company_list).replace('\n', '')
#                     self.switch_acct(choice_company)
#                     assert choice_company == self.get_text_from_my_company_span()
#                 except NoSuchElementException:
#                     print(f'切换到：{choice_company} 失败\n')
#
#     def test_switch_set_4(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         with allure.step('搜索公司'):
#             company = '切换测试101'
#             self.search_company(company)
#         with allure.step('进入账套'):
#             self.click_table_button(company, '进账簿')
#             self.switch_to_accounting_window()
#             for _ in range(len(company_list)):
#                 try:
#                     choice_company = random.choice(company_list).replace('\n', '')
#                     self.switch_acct(choice_company)
#                     assert choice_company == self.get_text_from_my_company_span()
#                 except NoSuchElementException:
#                     print(f'切换到：{choice_company} 失败\n')
#
#
# @pytest.mark.skip
# @allure.epic('其他')
# @allure.feature('备份账套')
# class TestBackupSet(AgencyAccountPage,
#                     ManagerCommonPage,
#                     LoginPage,
#                     ManagerHomePage,
#                     AccountingHomePage,
#                     AccountingCommonPage,
#                     AdvanceSettingsBackupAndRecoverPage):
#     company_list = [
#         '自动化测试_会计制度_农业_001',
#         '自动化测试_会计制度_村集体_001',
#         '自动化测试_会计制度_政府_001',
#         '自动化测试_会计制度_非盈利组织_001',
#         '自动化测试_会计制度_企业准则（未执行）_001',
#         '自动化测试_会计制度_企业准则（执行）_001',
#         '自动化测试_会计制度_新准则_001',
#         '自动化测试_会计制度_农专_001',
#         '自动化测试-管家-代账服务-导出-001',
#         '自动化测试-代账服务-031',
#         '自动化测试-代账服务-030',
#         '自动化测试-代账服务-029',
#         '自动化测试-代账服务-028',
#         '自动化测试-代账服务-027',
#         '自动化测试-代账服务-026',
#         '自动化测试-代账服务-025',
#         '自动化测试-物品-导出-003',
#         '自动化测试-物品-导出-002',
#         '自动化测试-物品-导出-001',
#         '自动化测试-物品-003',
#         '自动化测试-流失-004',
#         '自动化测试-流失-003',
#         '自动化测试-流失-002',
#         '自动化测试-客户-015',
#         '自动化测试-客户-014',
#         '自动化测试-客户-013',
#         '自动化测试-客户-012',
#         '自动化测试-合同-020',
#         '自动化测试-合同-019',
#         '自动化测试-合同-018',
#         '自动化测试-合同-017',
#         '自动化测试-合同-016',
#         '自动化测试-合同-015',
#         '自动化测试-合同-014',
#         '自动化测试-合同-013',
#         '自动化测试-合同-012',
#         '自动化测试-合同-011',
#         '自动化测试-合同-010',
#         '自动化测试-合同-009',
#         '自动化测试-合同-008',
#         '自动化测试-工商年报-012',
#         '自动化测试-工商年报-011',
#         '自动化测试-工商年报-010',
#         '自动化测试-工商年报-009',
#         '自动化测试-工商年报-008',
#         '自动化测试-工商年报-007',
#         '自动化测试-工商年报-006',
#         '自动化测试-工商年报-005',
#         '自动化测试-工商年报-003',
#         '自动化测试-工商年报-001',
#         '自动化测试-工商年报-002',
#         '自动化测试-工商年报-004',
#         '自动化测试-收票-010',
#         '自动化测试-收票-009',
#         '自动化测试-收票-008',
#         '自动化测试-收票-007',
#         '自动化测试-收票-006',
#         '自动化测试-收票-005',
#         '自动化测试-收票-004',
#         '自动化测试-收票-003',
#         '自动化测试-代账服务-024',
#         '自动化测试-代账服务-023',
#         '自动化测试-管家-代账服务-导出-004',
#         '自动化测试-管家-代账服务-导出-003',
#         '自动化测试-管家-代账服务-导出-002',
#         '自动化测试-管家-导出-007',
#         '自动化测试-管家-导出-006',
#         '自动化测试-管家-导出-005',
#         '自动化测试-管家-导出-004',
#         '自动化测试-代账服务-022',
#         '自动化测试-收票-002',
#         '自动化测试-收票-001',
#         '自动化测试-代账服务-021',
#         '自动化测试-代账服务-020',
#         '自动化测试-代账服务-019',
#         '自动化测试-管家-导出-001',
#         '自动化测试-收款-013',
#         '自动化测试-收款-009',
#         '自动化测试-收款-010',
#         '自动化测试-收款-012',
#         '自动化测试-收款-014',
#         '自动化测试-收款-015',
#         '自动化测试-收款-016',
#         '自动化测试-收款-019',
#         '自动化测试-收款-022',
#         '自动化测试-收款-024',
#         '自动化测试-收款-026',
#         '会计自动化测试-设置-005',
#         '会计自动化测试-设置-004',
#         '会计自动化测试-设置-003',
#         '会计自动化测试-设置-002',
#         '会计自动化测试-设置-001',
#         '会计自动化测试-结账-005',
#         '会计自动化测试-结账-004',
#         '会计自动化测试-结账-003',
#         '会计自动化测试-结账-002',
#         '会计自动化测试-结账-001',
#         '会计自动化测试-存货-005',
#         '会计自动化测试-存货-004',
#         '会计自动化测试-存货-003',
#         '会计自动化测试-存货-002',
#         '会计自动化测试-存货-001',
#         '会计自动化测试-固定资产-005',
#         '会计自动化测试-固定资产-004',
#         '会计自动化测试-固定资产-003',
#         '会计自动化测试-固定资产-002',
#         '会计自动化测试-固定资产-001',
#         '会计自动化测试-智能记账-056',
#         '会计自动化测试-智能记账-055',
#         '会计自动化测试-智能记账-054',
#         '会计自动化测试-智能记账-053',
#         '会计自动化测试-智能记账-052',
#         '会计自动化测试-智能记账-051',
#         '会计自动化测试-智能记账-050',
#         '会计自动化测试-智能记账-049',
#         '会计自动化测试-智能记账-048',
#         '会计自动化测试-智能记账-047',
#         '会计自动化测试-智能记账-046',
#         '会计自动化测试-智能记账-045',
#         '会计自动化测试-智能记账-044',
#         '会计自动化测试-智能记账-043',
#         '会计自动化测试-智能记账-042',
#         '会计自动化测试-智能记账-041',
#         '会计自动化测试-智能记账-040',
#         '会计自动化测试-智能记账-039',
#         '会计自动化测试-智能记账-038',
#         '会计自动化测试-智能记账-037',
#         '会计自动化测试-智能记账-036',
#         '会计自动化测试-智能记账-035',
#         '会计自动化测试-智能记账-034',
#         '会计自动化测试-智能记账-033',
#         '会计自动化测试-智能记账-032',
#         '会计自动化测试-智能记账-031',
#         '会计自动化测试-智能记账-030',
#         '会计自动化测试-智能记账-029',
#         '会计自动化测试-智能记账-028',
#         '会计自动化测试-智能记账-027',
#         '会计自动化测试-智能记账-026',
#         '会计自动化测试-智能记账-025',
#         '会计自动化测试-智能记账-024',
#         '会计自动化测试-智能记账-023',
#         '会计自动化测试-智能记账-022',
#         '会计自动化测试-智能记账-021',
#         '会计自动化测试-智能记账-020',
#         '会计自动化测试-智能记账-019',
#         '会计自动化测试-智能记账-018',
#         '会计自动化测试-智能记账-017',
#         '会计自动化测试-智能记账-016',
#         '会计自动化测试-智能记账-015',
#         '会计自动化测试-智能记账-014',
#         '会计自动化测试-智能记账-013',
#         '会计自动化测试-智能记账-012',
#         '会计自动化测试-智能记账-011',
#         '会计自动化测试-智能记账-010',
#         '会计自动化测试-智能记账-009',
#         '会计自动化测试-智能记账-008',
#         '会计自动化测试-智能记账-007',
#         '会计自动化测试-智能记账-005',
#         '会计自动化测试-智能记账-006',
#         '会计自动化测试-智能记账-004',
#         '自动化测试-代账服务-018',
#         '自动化测试-代账服务-017',
#         '自动化测试-代账服务-016',
#         '自动化测试-代账服务-015',
#         '自动化测试-代账服务-014',
#         '自动化测试-代账服务-013',
#         '自动化测试-代账服务-012',
#         '会计自动化测试-智能记账-003',
#         '会计自动化测试-智能记账-002',
#         '会计自动化测试-智能记账-001',
#         '自动化测试-物品-002',
#         '自动化测试-物品-001',
#         '自动化测试-外勤-006',
#         '自动化测试-外勤-005',
#         '自动化测试-外勤-004',
#         '自动化测试-外勤-003',
#         '自动化测试-外勤-002',
#         '自动化测试-外勤-001',
#         '自动化测试-客户-011',
#         '自动化测试-客户-010',
#         '自动化测试-客户-009',
#         '自动化测试-客户-008',
#         '自动化测试-客户-007',
#         '自动化测试-客户-006',
#         '自动化测试-客户-005',
#         '自动化测试-客户-004',
#         '自动化测试-客户-003',
#         '自动化测试-客户-002',
#         '自动化测试-客户-001',
#         '自动化测试-合同-007',
#         '自动化测试-合同-006',
#         '自动化测试-代账服务-011',
#         '自动化测试-代账服务-010',
#         '自动化测试-代账服务-009',
#         '自动化测试-代账服务-008',
#         '自动化测试-代账服务-007',
#         '自动化测试-代账服务-006',
#         '自动化测试-代账服务-005',
#         '自动化测试-代账服务-004',
#         '自动化测试-代账服务-003',
#         '自动化测试-代账服务-002',
#         '自动化测试-代账服务-001',
#         '自动化测试-收款-006',
#         '自动化测试-收款-005',
#         '自动化测试-收款-004',
#         '自动化测试-收款-003',
#         '自动化测试-收款-002',
#         '自动化测试-收款-001',
#         '自动化测试-合同-005',
#         '自动化测试-合同-004',
#         '自动化测试-合同-003',
#         '自动化测试-合同-002',
#         '自动化测试-合同-001']
#
#     def test_backup_files(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         for _ in self.company_list:
#             with allure.step('搜索公司'):
#                 company = _.replace('\n', '')
#                 self.search_company(company)
#                 self.wait(2)
#                 # if self.is_element_visible(self.service_table_line_buttons(company, '创建账套')):
#                 #     self.click_table_button(company, '创建账套')
#                 #     self.click_ignore_set_tip()
#                 #     self.wait(3)
#                 #     self.switch_to_accounting_window()
#
#                 if self.is_element_visible(self.service_table_line_buttons(company, '进账簿')):
#                     self.click_table_button(company, '进账簿')
#                     self.switch_to_newest_window()
#                     self.click_accounting_menu('设置', '备份与恢复')
#                     self.switch_to_backup_frame()
#                     self.click_backup_buttons('开始备份')
#                     self.click_backup_input_buttons('确定')
#                     self.wait_for_backup_finished()
#                     self.click_latest_backup_line_operate_buttons('下载')
#                     self.switch_to_default_content()
#                     self.wait(5)
#                     self.driver.close()
#                     self.switch_to_default_window()
#
#                 else:
#                     continue
#
#
# @pytest.mark.skip
# @allure.epic('其他')
# @allure.feature('恢复账套')
# class TestRecoverSet(AgencyAccountPage,
#                      ManagerCommonPage,
#                      LoginPage,
#                      ManagerHomePage,
#                      AccountingHomePage,
#                      AccountingCommonPage,
#                      CreateSetPage):
#
#     def test_recover(self):
#
#         from test import get_acct_url, headers
#
#         r_company_list, filename_list, file_path_list = get_all_file_path(r"E:\autotest\backup")
#         for x in r_company_list:
#             self.get(get_acct_url(x)['data'])
#             self.save_cookies()
#             if self.is_company_span_visible():
#                 continue
#
#             with open(r'E:\autotest\testcases\others\saved_cookies\cookies.txt') as coo:
#                 cookies_from_file = json.loads(coo.readline())
#                 acct_cookies = {}
#                 for _ in cookies_from_file:
#                     acct_cookies[_.get('name')] = _.get('value')
#
#             file = {
#                 'file': (filename_list[r_company_list.index(x)],
#                          open(file_path_list[r_company_list.index(x)], 'rb'),
#                          'zip')
#             }
#
#             url = "https://mmain.kdzwy.com:34/upload"
#
#             params = {
#                 "endyear": "2023",
#                 "endmonth": "12",
#                 "orderId": "0"
#             }
#
#             response_upload = requests.post(url, headers=headers, cookies=acct_cookies, params=params, files=file,
#                                             verify=True)
#             # print(response_upload.text)
#
#             response_json = json.loads(response_upload.text)
#
#             fid = response_json.get('data')['items'][0]['fid']
#
#             url = "https://mmain.kdzwy.com:34/gl/backup"
#             params = {
#                 "m": "recover"
#             }
#             data = {
#                 "id": fid,
#                 "isStart": "1",
#                 "name": ""
#             }
#             response = requests.post(url, headers=headers, cookies=acct_cookies, params=params, data=data, verify=True)
#
#             print(f'{x}: {response.text}')
#             if '失败' in json.loads(response.text).get('msg'):
#                 count = 0
#                 while count < 5:
#                     r_res = requests.post(url, headers=headers, cookies=acct_cookies, params=params, data=data,
#                                           verify=True)
#                     print(f'{x}: {r_res.text}')
#                     if '失败' not in json.loads(r_res.text).get('msg'):
#                         break
#                     count += 1
#                     self.wait(3)
#
#     def test_recover_set(self):
#         with allure.step('登录'):
#             self.normal_login()
#             self.close_popup()
#         with allure.step('点击菜单'):
#             try:
#                 self.click_manager_menu('代账服务', '服务管理')
#             except ElementNotVisibleException:
#                 self.wait(1)
#                 self.click_manager_menu('代账服务', '服务管理')
#         filename_list, filepath_list = get_all_file_path(r"E:\autotest\backup")
#         for _ in filename_list:
#
#             if '固定资产' in _ or '存货' in _:
#                 continue
#             else:
#                 with allure.step('搜索公司'):
#                     company = _.replace('\n', '')
#                     self.search_company(company)
#                     self.wait(2)
#                     if self.is_element_visible(self.service_table_line_buttons(company, '创建账套')):
#                         self.click_table_button(company, '创建账套')
#                         self.click_ignore_set_tip()
#                         self.wait(3)
#                         self.switch_to_newest_window()
#                         self.click_create_mode_span('导入第三方')
#                         self.click_import_set_type('从备份文件恢复账套')
#                         self.upload_file_to_import_file_inputs('zip', filepath_list[filename_list.index(_)])
#                         self.click_create_button('开始创建')  # 后跳转至会计页面
#                         self.wait(1)
#
#                         if self.is_floating_tip_visible():
#                             # self.wait(4)
#                             # self.click_create_button('开始创建')  # 后跳转至会计页面
#                             self.driver.close()
#                             self.switch_to_default_window()
#                             print(f'{_} 上传失败')
#                             continue
#                         else:
#                             self.wait_for_upload_finish()
#
#                             assert company == self.get_company_name()
#                             self.wait(5)
#                             self.driver.close()
#                             self.switch_to_default_window()
#
#                     else:
#                         continue
# from utils.yml import logger


# class TestAccountFactory(LoginPage, ManagerHomePage, AgencyAccountPage):
#
#     def test_stop_service(self):
#         log = logger()
#         self.login(specific_user='test_account_factory')
#         self.click_manager_menu('代账服务', '服务管理')
#
#         self.click_service_button_droplist('更多')
#         self.select_service_type_droplist('提交外包记录')
#
#         with open(r'C:\Users\kingdee\Desktop\comany_list.txt', 'r', encoding='utf-8') as c_file:
#             company_list = c_file.readlines()
#
#         self.switch_to_frame('//*[@class="osRecord-wraper"]//iframe')
#
#         for idx, company in enumerate(company_list):
#             company = company.replace('\n', '')
#             self.type('//input[@placeholder="搜索客户名称/服务名称/申请人"]', f'{company}\n')
#             services = self.find_visible_elements(
#                 f'//div[@title="{company}"]/parent::td//following-sibling::td[contains(@data-code,"listop")]//span[text()="申请停止"]'
#             )
#
#             if services:
#                 for service in services:
#                     service.click()
#                     self.wait(0.2)
#                     self.click('//div[@title="是否确认停止合作"]//following-sibling::div/a[text()="确定"]')
#                     self.wait(1)
#                     assert '申请停止' == self.get_text(
#                         f'//div[@title="{company}"]/parent::td//following-sibling::td[contains(@data-code,"billstatus")]//span'
#                     )
#
#             self.move_mouse_to_element(f'//span[@title="{company}"]')
#             self.click(f'//span[@title="{company}"]//preceding-sibling::i')
#             log.info(f'[{idx + 1}/{len(company_list)}]: {company} - 终止{len(services)}条记录')


@pytest.mark.cleanup
@allure.epic('其他')
@allure.title('清理测试数据-客户')
class TestClearData(LoginPage, ManagerHomePage, ManagerCommonPage, CustomerPage, SystemBinPage):
    def test_delete_test_customer(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('客户管理', '客户')
            self.close_ads()
        with allure.step('删除客户'):
            self.search_customer('autotest_')
            self.customer_switch_show_num(100)
            total_test_data = int(self.get_text_from_customer_list_total_line().split(' ')[1])
            if total_test_data != 0:
                delete_times = int(total_test_data / 100) if total_test_data % 100 == 0 else int(
                    total_test_data / 100 + 1)
                for _ in range(delete_times):
                    self.click_customer_list_select_all_span()
                    self.click_dropdown_buttons('更多', '删除')
                    self.click_delete_customer_button('删除')
                    assert '删除客户成功' in self.get_tip_text()

    def test_delete_accounting_set(self):
        with allure.step('登录'):
            self.login()
            self.close_popup()
        with allure.step('点击菜单'):
            self.click_manager_menu('系统设置', '回收站')
        with allure.step('删除账套'):
            self.type_to_system_bin_inputs_by_label('客户名称', 'autotest_')
            self.click_system_bin_buttons('查询')
            self.manager_bottom_line_switch_show_num(100)
            total_test_data = int(self.get_text_from_manager_bottom_line_total_line().split(' ')[1])
            if total_test_data != 0:
                delete_times = int(total_test_data / 100) if total_test_data % 100 == 0 else int(
                    total_test_data / 100 + 1)
                for _ in range(delete_times):
                    self.click_system_bin_check_all_span()
                    self.click_system_bin_buttons('彻底删除')
                    self.click_system_bin_conform_delete('确定删除')
                    self.type_to_system_bin_conform_again_input()
                    self.click_system_bin_conform_again_button()
                    self.click_system_bin_conform_delete('取 消')


@pytest.mark.cleanup
@allure.epic('其他')
@allure.title('清理临时下载目录')
class TestClearDownloadFiles:
    def test_clear_download_path(self):
        del_files()
