import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
from page.api.accounting.page_api_close_period import PageApiClosePeriod
from page.api.accounting.page_api_settings import PageApiSettingsVoucherType
from page.api.accounting.page_api_voucher import PageApiVoucher
from utils.file_utils import get_env
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_close_period
@allure.epic('会计')
@allure.feature('结账')
class TestApiClosePeriod(
    PageApiSettingsVoucherType,
    PageApiClosePeriod,
    PageApiVoucher,
    BaseTestCase,
):
    @allure.title('计提折旧')
    def test_api_close_period_depreciation(self):
        company = GetYamlData().get_company('api_company_accounting_fa_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('查询凭证字'):
            default_voucher_type_id = self.settings_voucher_type_query_default_voucher_type(req)

        with allure.step('计提折旧'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/checkout/checkout.jsp"
            }

            params = {
                "m": "closeVoucher"
            }

            data = {
                "paramData": "{\"fixedVchData\":{\"groupId\":" + default_voucher_type_id + ",\"date\":\"2023-02-28\",\"fixedSummary\":\"计提折旧费用\",\"classify\":1,\"way\":0}}"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.post('gl/closeperiod', headers=headers, params=params, data=data)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 5

    @allure.title('结转生产成本')
    def test_api_close_period_production_cost(self):
        company = GetYamlData().get_company('api_company_accounting_closure_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('结转生产成本'):
            params = {
                "m": "generateVcByCb",
                "year": "2019",
                "month": "02",
                "cbAmount": "129847.68",
                "category": "1",
                "key": "Carry_Forward_Generation_Cos"
            }

            data = self.production_cost_data()

            response = req.post('gl/closeperiod', params=params, data=data)

            voucher_id = response.json().get('data')['id']
            assert response.elapsed.total_seconds() < 10

        with allure.step('删除凭证'):
            assert '共删除1张凭证' == self.del_voucher(req, voucher_id)

    @allure.title('结转销售成本')
    def test_api_close_period_selling_cost(self):
        company = GetYamlData().get_company('api_company_accounting_closure_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('结转销售成本'):
            params = {
                "m": "generateVcJz",
                "year": "2019",
                "month": "02",
                "incomeValue%20": "80",
                "incomeCategory": "2",
                "incomeKey": "Income_Carry_Forward_Of_Sales",
                "category": "1"
            }

            data = self.selling_cost_data()

            response = req.post('gl/closeperiod', params=params, data=data)

            voucher_id = response.json().get('data')['id']
            assert response.elapsed.total_seconds() < 5

        with allure.step('删除凭证'):
            assert '共删除1张凭证' == self.del_voucher(req, voucher_id)

    @allure.title('结转损益')
    def test_api_close_period_closure_voucher(self):
        company = GetYamlData().get_company('api_company_accounting_closure_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('结转损益'):
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": f"https://{get_env()}.kdzwy.com:34/checkout/checkout.jsp"
            }
            params = {
                "m": "closeVoucher"
            }
            data = {
                "paramData": "{\"plVchData\":{\"groupId\":645707550507058,\"date\":\"2023-01-31\",\"summary\":\"结转本期损益\",\"classify\":1,\"way\":0,\"paraLrkm\":\"645706068820715\",\"paraTzkm\":\"645706147712591\",\"paraJzkm\":\"645706077750604\"}}"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.post('gl/closeperiod', headers=headers, params=params, data=data)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 1.5
