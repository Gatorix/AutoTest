import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
from utils.file_utils import get_env
from utils.yml import GetYamlData

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_reports
@pytest.mark.api_accounting_reports_balance_sheet
@allure.epic('会计')
@allure.feature('报表')
@allure.story('资产负债表')
class TestApiBalanceSheet(BaseTestCase):
    @allure.title('资产负债表查询')
    def test_api_query_balance_sheet(self):
        company = GetYamlData().get_company('api_company_accounting_reports_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('资产负债表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/balance-sheets.jsp",
            }
            params = {
                "m": "getReportValue",
                "reporttype": "balance",
                "yearperiod": "202303",
                "_search": "false",
                "nd": "1698291484105",
                "rows": "150",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/report', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.8

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_reports
@pytest.mark.api_accounting_reports_profit_sheet
@allure.epic('会计')
@allure.feature('报表')
@allure.story('利润表')
class TestApiProfitSheet(BaseTestCase):
    @allure.title('利润表查询-月报')
    def test_api_query_profit_sheet_monthly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('利润表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/profit-sheets.jsp",
            }

            params = {
                "m": "getProfiltValue",
                "reporttype": "profit",
                "yearperiod": "202303",
                "type": "1",
                "periodParm": "0",
                "_search": "false",
                "nd": "1698305870555",
                "rows": "150",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/report', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.3

    @allure.title('利润表查询-季报')
    def test_api_query_profit_sheet_quarterly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('利润表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/profit-sheets.jsp",
            }

            params = {
                "m": "getProfiltValue",
                "reporttype": "profit",
                "yearperiod": "202301",
                "type": "2",
                "periodParm": "0",
                "_search": "false",
                "nd": "1698306730749",
                "rows": "150",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/report', headers=headers, params=params)
                assert response.json().get('status') == 200
                response_times.append(response.elapsed.total_seconds())

            assert sum(response_times) / API_CASE_REPEAT_TIME < 0.3

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_reports
@pytest.mark.api_accounting_reports_cash_flow_sheet
@allure.epic('会计')
@allure.feature('报表')
@allure.story('现金流量表')
class TestApiCashFlowSheet(BaseTestCase):
    @allure.title('流量表查询-月报')
    def test_api_query_cash_flow_monthly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('现金流量表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/cash-flow-sheets.jsp",
            }

            params = {
                "m": "getCashReportValue",
                "reporttype": "cashflow",
                "yearperiod": "202303",
                "type": "1",
                "_search": "false",
                "nd": "1698307741160",
                "rows": "150",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/report', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 2

    @allure.title('现金流量表查询-季报')
    def test_api_query_cash_flow_quarterly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('标准现金流量表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/cash-flow-sheets.jsp",
            }

            params = {
                "m": "getCashReportValue",
                "reporttype": "cashflow",
                "yearperiod": "202301",
                "type": "2",
                "_search": "false",
                "nd": "1698307915486",
                "rows": "150",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('report/report', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 3

@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_reports
@pytest.mark.api_accounting_reports_standard_cash_flow_sheet
@allure.epic('会计')
@allure.feature('报表')
@allure.story('标准现金流量表')
class TestApiStandardCashFlowSheet(BaseTestCase):
    @allure.title('标准现金流量表查询-月报')
    def test_api_query_standard_cash_flow_monthly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('标准现金流量表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/standard-cash-flow-sheets.jsp",
            }

            params = {
                "m": "getReportValue",
                "yearperiod": "202303",
                "type": "1"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('cashflow', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.2

    @allure.title('标准现金流量表查询-季报')
    def test_api_query_standard_cash_flow_quarterly(self):
        company = GetYamlData().get_company('api_company_accounting_reports_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('标准现金流量表查询'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/reports/standard-cash-flow-sheets.jsp",
            }

            params = {
                "m": "getReportValue",
                "yearperiod": "202301",
                "type": "2"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('cashflow', headers=headers, params=params)
                assert response.json().get('status') == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5
