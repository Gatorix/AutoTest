import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
from utils.yml import GetYamlData

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_fixed_asset
@pytest.mark.api_accounting_fixed_asset_card
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('卡片')
class TestApiFACards(BaseTestCase):
    @allure.title('查询卡片')
    def test_api_query_inventory_summary(self):
        company = GetYamlData().get_company('api_company_accounting_fa_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询卡片'):
            params = {
                "m": "list",
                "_search": "false",
                "nd": "1698386876071",
                "rows": "0",
                "page": "1",
                "sidx": "fnumber",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('faCard', params=params)
                assert response.json().get('data')['totalsize'] == 1000
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_fixed_asset
@pytest.mark.api_accounting_fixed_asset_depreciation_detail
@allure.epic('会计')
@allure.feature('固定资产')
@allure.story('折旧明细表')
class TestApiFADepreciationDetail(BaseTestCase):
    @allure.title('查询折旧明细表')
    def test_api_query_inventory_summary(self):
        company = GetYamlData().get_company('api_company_accounting_fa_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询卡片'):
            params = {
                "m": "depreciationDetailSheet",
                "ypf": "202302",
                "ypt": "202307",
                "dept": "true",
                "_search": "false",
                "nd": "1698388238247",
                "rows": "0",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/fa', params=params)
                assert len(response.json().get('data')['items']) == 1003
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5
