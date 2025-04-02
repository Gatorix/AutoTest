import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from page.api.accounting.page_api_common import PageApiCommon
from page.api.accounting.page_api_settings import PageApiSettingsVoucherType, PageApiSettingsSubjects
from page.api.accounting.page_api_voucher import PageApiVoucher
from utils.file_utils import get_project_path
from utils.random_data import random_string_generator
from utils.excel_utils import check_excel_diff
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_voucher
@allure.epic('会计')
@allure.feature('录凭证')
@allure.story('录凭证')
class TestApiVoucher(
    PageApiCommon,
    PageApiVoucher,
    PageApiSettingsVoucherType,
    PageApiSettingsSubjects,
    BaseTestCase
):
    @allure.title('创建凭证-100*2')
    def test_api_add_voucher_2_entries_100_times(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('查询凭证字'):
            default_voucher_type_id = self.settings_voucher_type_query_default_voucher_type(req)

        with allure.step('查询科目'):
            subj_id_1121 = self.settings_subject_query_specified_subject(req, '1', '1121')
            subj_id_1131 = self.settings_subject_query_specified_subject(req, '1', '1131')

        with allure.step('查询当前期间'):
            current_period = self.page_api_get_current_period(req)
            year = current_period[:4]
            period = current_period[-2:]
            date = f'{year}-{period}-01'

        with allure.step('创建凭证'):
            url = "gl/voucher"
            params = {
                "m": "addNew"
            }

            entries_d = self.voucher_data_entries(subj_id_1121, '1121', '1', '88.00', '88.00')
            entries_c = self.voucher_data_entries(subj_id_1131, '1131', '0', '88.00', '88.00')
            entries = ''.join([entries_c, entries_d])

            data = self.voucher_data(default_voucher_type_id,
                                     date, year, period, current_period,
                                     entries,
                                     '88.00', '88.00')

            headers = {"Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8'}

            voucher_id_list = []

            avg_response_times = []

            for _ in range(100):
                response = req.post(url, headers=headers, params=params, data=data)

                avg_response_times.append(response.elapsed.total_seconds())

                voucher_id = response.json()['data']['id']

                voucher_id_list.append(voucher_id)

            assert sum(avg_response_times) / 100 < 0.15

        with allure.step('删除凭证'):

            avg_response_times_del = []

            for _ in voucher_id_list:
                url = "gl/voucher"

                params = {
                    "m": "deleteById"
                }

                data = {
                    "del": _,
                }

                response = req.post(url, headers=headers, params=params, data=data)

                avg_response_times_del.append(response.elapsed.total_seconds())

                assert '共删除1张凭证' == response.json()['data']['msg']

            assert sum(avg_response_times_del) / 100 < 0.3

    @allure.title('创建凭证-1*100')
    def test_api_add_voucher_100_entries_5_times(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('查询凭证字'):
            default_voucher_type_id = self.settings_voucher_type_query_default_voucher_type(req)

        with allure.step('查询科目'):
            subj_id_1121 = self.settings_subject_query_specified_subject(req, '1', '1121')
            subj_id_1131 = self.settings_subject_query_specified_subject(req, '1', '1131')

        with allure.step('查询当前期间'):
            current_period = self.page_api_get_current_period(req)
            year = current_period[:4]
            period = current_period[-2:]
            date = f'{year}-{period}-01'

        with allure.step('创建凭证'):
            url = "gl/voucher"
            params = {
                "m": "addNew"
            }

            entries_d = self.voucher_data_entries(subj_id_1121, '1121', '1', '88.00', '88.00') * 50
            entries_c = self.voucher_data_entries(subj_id_1131, '1131', '0', '88.00', '88.00') * 50
            entries = ''.join([entries_c, entries_d])

            data = self.voucher_data(default_voucher_type_id,
                                     date, year, period, current_period,
                                     entries,
                                     '4400.00', '4400.00')

            headers = {"Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8'}

            voucher_id_list = []

            avg_response_times = []

            for _ in range(5):
                response = req.post(url, headers=headers, params=params, data=data)

                avg_response_times.append(response.elapsed.total_seconds())

                voucher_id = response.json()['data']['id']

                voucher_id_list.append(voucher_id)

            assert sum(avg_response_times) / 100 < 0.5

        with allure.step('删除凭证'):
            avg_response_times_del = []

            for _ in voucher_id_list:
                url = "gl/voucher"

                params = {
                    "m": "deleteById"
                }

                data = {
                    "del": _,
                }

                response = req.post(url, headers=headers, params=params, data=data)

                avg_response_times_del.append(response.elapsed.total_seconds())

                assert '共删除1张凭证' == response.json()['data']['msg']

            assert sum(avg_response_times_del) / 100 < 0.12


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_lookup_voucher
@allure.epic('会计')
@allure.feature('查凭证')
@allure.story('查凭证')
class TestApiLookUpVoucher(BaseTestCase):
    # @allure.title('凭证查询')
    # def test_api_lookup_voucher(self):
    #     company = GetYamlData().get_company('api_company_accounting_voucher_001')
    #     with allure.step('创建连接'):
    #         req = RequestsClient(company=company)
    #
    #     with allure.step('查询凭证'):
    #         params = {
    #             "m": "findList",
    #             "fromPeriod": "201610",
    #             "toPeriod": "202303",
    #             "_search": "false",
    #             "nd": "1698218213640",
    #             "rows": "100",
    #             "page": "1",
    #             "sidx": "date",
    #             "sord": "asc"
    #         }
    #
    #         response = req.get('gl/voucher', params=params)
    #         print(response.json())


    @allure.title('下载凭证导入模板')
    def test_api_download_voucher_import_template(self):
        company = GetYamlData().get_company('company_accounting_voucher_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('下载凭证导入模板'):
            url = "gl/voucher"

            headers = {
                "Content-Type": 'application/x-msdownload;charset=utf-8'
            }

            params = {
                'm': 'printTemplate'
            }

            response = req.get(url, headers=headers, params=params)

            temp_file = f'{get_project_path()}\\download_tmp\\{self.test_id}\\{random_string_generator()}.xls'

            with open(temp_file, 'wb') as download_file:
                for bl in response.iter_content(chunk_size=1024):
                    if all([
                        bl,
                        '"status":402' not in str(bl),
                        '502 Bad Gateway' not in str(bl)
                    ]):
                        download_file.write(bl)
                    else:
                        return {'is_success': False, 'msg': f'下载备份失败: {bl.decode("utf-8")}'}

        with allure.step('比对excel文件'):
            assert check_excel_diff(
                f'{get_project_path()}\\template\\accounting\\voucher\\凭证导入模板.xls',
                temp_file
            )

#     @allure.title('凭证打印')
#     def test_api_print_voucher(self):
#         company = GetYamlData().get_company('company_accounting_smart_bookkeeping_050')
#         with allure.step('创建连接'):
#             req = RequestsClient(company=company)
#
#         with allure.step('查询凭证'):
#             url = "gl/voucher"
#
#             headers = {
#                 "Content-Type": "application/x-www-form-urlencoded",
#             }
#
#             params = {
#                 "m": "printExport"
#             }
#
#             data = {
#                 "dataField": "date%#mark%#summary%#subject%#debit%#credit%#people%#auditor",
#                 "columnTitle": "%%E6%%97%%A5%%E6%%9C%%9F%#%%E5%%87%%AD%%E8%%AF%%81%%E5%%AD%%97%%E5%%8F%%B7%#%%E6%%91%%98%%E8%%A6%%81%#%%E7%%A7%%91%%E7%%9B%%AE%#%%E5%%80%%9F%%E6%%96%%B9%%E9%%87%%91%%E9%%A2%%9D%#%%E8%%B4%%B7%%E6%%96%%B9%%E9%%87%%91%%E9%%A2%%9D%#%%E5%%88%%B6%%E5%%8D%%95%%E4%%BA%%BA%#%%E5%%AE%%A1%%E6%%A0%%B8%%E4%%BA%%BA",
#                 "sheetName": "%%E5%%87%%AD%%E8%%AF%%81%%E5%%88%%97%%E8%%A1%%A8%#2023%%E5%%B9%%B4%%E7%%AC%%AC3%%E6%%9C%%9F",
#                 "sidx": "date",
#                 "sord": "asc",
#                 "op": "2",
#                 "showParams": "%%5Bobject%%20Object%%5D",
#                 "voucherIds": "642871682467922",
#                 "marginLeft": "0",
#                 "marginTop": "200",
#                 "eachPageVou": "2",
#                 "pagePrint": "1",
#                 "js_disPrintMaker": "0",
#                 "showVoucherNo": "0",
#                 "showNoAmount": "0",
#                 "showZDR": "0",
#                 "showRemark": "0",
#                 "js_printAttachments": "0",
#                 "js_printCover": "0",
#                 "isSummary": "0",
#                 "level": "1",
#                 "dcSummary": "0",
#                 "notShowZero": "0",
#                 "showSameItem": "0",
#                 "showPrintDate": "0",
#                 "showPage": "0",
#                 "showNoCountAndAmount": "0",
#                 "showNoCount": "0",
#                 "invSummary": "0",
#                 "printDate": "2024-02-02",
#                 "showQtyPrice": "0",
#                 "showCur": "0",
#                 "attachmentList": "0",
#                 "invoiceList": "0",
#                 "elecInvoiceList": "0",
#                 "paperInvoiceList": "0",
#                 "voucherAttachment": "0",
#                 "bankreceiptList": "0",
#                 "pageSize": "",
#                 "pageDirection": "x",
#                 "pageRotationNumber": "-90",
#                 "onlyPrintMostDetailedItem": "0",
#                 "pageZWY": "0",
#                 "fontSize": "9"
#             }
#             response = req.post(url, headers=headers, params=params, data=data)
#
# with open(rf'C:\Users\kingdee\Desktop\test\{random_string_generator()}.pdf', 'wb') as download_file:
#     for bl in response.iter_content(chunk_size=1024):
#         if all([
#             bl,
#             '"status":402' not in str(bl),
#             '502 Bad Gateway' not in str(bl)
#         ]):
#             download_file.write(bl)
#         else:
#             return {'is_success': False, 'msg': f'下载备份失败: {bl.decode("utf-8")}'}
