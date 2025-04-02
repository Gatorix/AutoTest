import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
@pytest.mark.api
@pytest.mark.api_manager
@pytest.mark.api_manager_customer
@pytest.mark.api_manager_customer_contract
@allure.epic('管家')
@allure.feature('客户管理')
@allure.story('合同')
class TestCustomerManagement(BaseTestCase):
    @allure.title('获取合同列表-多次请求')
    def test_api_get_contract_list_top_50_multiple_times(self):
        with allure.step('创建连接'):
            req = RequestsClient()
        with allure.step('获取合同列表'):
            limit = 50
            params = {
                "page": "1",
                "limit": limit,
                "orderProperty": "contractHeadDate",
                "orderDirection": "desc",
                "nodeValue": "",
                "nodeType": "",
                "noSalesMan": "0"
            }
            avg_response_times = []
            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get("contract/getList", params=params)
                assert limit == len(response.json().get('data')['items'])
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times)/API_CASE_REPEAT_TIME < 1

    @allure.title('获取合同列表-前50条')
    def test_api_get_contract_list_top_50(self):
        with allure.step('创建连接'):
            req = RequestsClient()
        with allure.step('获取合同列表'):
            limit = 50
            params = {
                "page": "1",
                "limit": limit,
                "orderProperty": "contractHeadDate",
                "orderDirection": "desc",
                "nodeValue": "",
                "nodeType": "",
                "noSalesMan": "0"
            }
            response = req.get("contract/getList", params=params)

            assert limit == len(response.json().get('data')['items'])
            # assert response.elapsed.total_seconds() < 0.3

    @allure.title('获取合同列表-查询指定公司名称')
    def test_api_get_contract_list(self):
        with allure.step('创建连接'):
            req = RequestsClient()
        with allure.step('获取合同列表'):
            limit = 1
            company = "接口自动化测试-报表-001"
            params = {
                "page": "1",
                "limit": "10",
                "orderProperty": "contractHeadDate",
                "orderDirection": "desc",
                "name": company,
                "nodeValue": "",
                "nodeType": "",
                "noSalesMan": "0"
            }
            response = req.get("contract/getList", params=params)

            assert limit == len(response.json().get('data')['items'])
            assert company == response.json().get('data')['items'][0].get('customerName')
            assert response.elapsed.total_seconds() < 1
