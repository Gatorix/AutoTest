import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_inventory
@pytest.mark.api_accounting_inventory_manage
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货管理')
class TestApiInventoryManage(BaseTestCase):
    @allure.title('查询存货列表')
    def test_api_query_inventory(self):
        company = GetYamlData().get_company('api_company_accounting_inventory_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询存货汇总表'):
            params = {
                "m": "findItem",
                "itemClassId": "4",
                "_search": "false",
                "nd": "1698376051844",
                "rows": "100",
                "page": "1",
                "sidx": "",
                "sord": "asc",
                "skey": ""
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.post('bs/item', params=params)
                assert response.json().get('data')['records'] == 2969
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.15


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_inventory
@pytest.mark.api_accounting_inventory_summary
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货汇总表')
class TestApiInventorySummary(BaseTestCase):
    @allure.title('查询存货汇总表')
    def test_api_query_inventory_summary(self):
        company = GetYamlData().get_company('api_company_accounting_inventory_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询存货汇总表'):
            header = {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            params = {
                "m": "querySummary"
            }

            data = {
                "id": "",
                "bperiod": "201801",
                "eperiod": "201902",
                "isAll": "true",
                "isMon": "false",
                "isShowNumber": "true",
                "_search": "false",
                "rows": "10000",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.post('ims/report', headers=header, params=params, data=data)
                assert response.json().get('data')['totalsize'] == 2969
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 1


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_inventory
@pytest.mark.api_accounting_inventory_detail
@allure.epic('会计')
@allure.feature('存货')
@allure.story('存货明细表')
class TestApiInventoryDetail(BaseTestCase):
    @allure.title('查询存货明细表')
    def test_api_query_inventory_details(self):
        company = GetYamlData().get_company('api_company_accounting_inventory_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询存货明细表'):
            params = {
                "m": "queryDetail",
                "id": "690500670119310",
                "bperiod": "201902",
                "eperiod": "201902",
                "isShowPriceAndNumber": "1",
                "_search": "false",
                "nd": "1698376838790",
                "rows": "5000",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }
            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.post('ims/report', params=params)
                assert response.json().get('data')['totalsize'] == 3023
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5
