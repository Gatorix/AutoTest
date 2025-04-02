import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from config.config import API_CASE_REPEAT_TIME
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_subsidiary_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('明细账')
class TestApiSubsidiaryLedger(BaseTestCase):
    @allure.title('明细账查询')
    def test_api_query_subsidiary_ledger(self):
        company = GetYamlData().get_company('api_company_accounting_books_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('明细账查询'):
            params = {
                "m": "queryDetail",
                "fromPeriod": "201610",
                "toPeriod": "202303",
                "fromAccountId": "",
                "toAccountId": "",
                "fromLevel": "",
                "toLevel": "",
                "explanation": "",
                "includeItem": "1",
                "invSummaryMx": "0",
                "detail": "0",
                "currency": "RMB",
                "accountId": "274880187846604",
                "oppositeAccount": "0",
                "balance": "1",
                "happen": "1",
                "rhj": "0",
                "happenTotal": "1",
                "accountNum": "1122",
                "number": "1122"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/general', params=params)
                assert response.json().get('data')['totalsize'] == 960
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 1


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_general_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('总账')
class TestApiGeneralLedger(BaseTestCase):
    @allure.title('总账查询')
    def test_api_query_amount_ledger(self):
        company = GetYamlData().get_company('api_company_accounting_books_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('总账查询'):
            params = {
                "m": "queryTotal",
                "fromPeriod": "202301",
                "toPeriod": "202308",
                "reportitem": "",
                "fromAccountId": "",
                "toAccountId": "",
                "fromLevel": "",
                "toLevel": "",
                "includeItem": "1",
                "currency": "RMB",
                "balabceAndCreditOrDebit": "0",
                "onlyBalance": "0",
                "notBnhe": "0",
                "_search": "false",
                "nd": "1698223721951",
                "rows": "10000",
                "page": "1",
                "sidx": "number",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/general', params=params)
                assert response.json().get('records') == 159
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.8


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_voucher_summary
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('凭证汇总表')
class TestApiVoucherSummary(BaseTestCase):
    @allure.title('凭证汇总表查询')
    def test_api_query_voucher_summary(self):
        company = GetYamlData().get_company('api_company_accounting_books_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('凭证汇总表查询'):
            params = {
                "fromDate": "2016-08-01",
                "toDate": "2023-08-31",
                "fromLevel": "1",
                "toLevel": "8",
                "_search": "false",
                "nd": "1698224448460",
                "rows": "10000",
                "page": "1",
                "sidx": "FNUMBER",
                "sord": "asc",
                "groupId": "",
                "fromNum": "",
                "toNum": ""
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('voucher/total/query', params=params)
                assert response.json().get('data')['voucherTotal'] == 1281
                assert response.json().get('data')['voucherAttchTotal'] == 440
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.8


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_balance_sheet
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('科目余额表')
class TestApiBalanceSheet(BaseTestCase):
    @allure.title('科目余额表查询')
    def test_api_query_balance_sheet(self):
        company = GetYamlData().get_company('api_company_accounting_books_004')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('科目余额表查询'):
            params = {
                "m": "query",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "fromAccountId": "",
                "toAccountId": "",
                "fromLevel": "1",
                "toLevel": "9",
                "includeItem": "1",
                "currency": "RMB",
                "balance": "1",
                "happen": "1",
                "currentYearBalance": "1",
                "accountType": "0",
                "isDetailAccount": "1",
                "_search": "false",
                "nd": "1698228655261",
                "rows": "10000",
                "page": "1",
                "sidx": "number",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/balanceReport', params=params)
                assert response.json().get('records') == 216
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.3


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_quantity_amount_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('数量金额明细账')
class TestApiQuantityAmountLedger(BaseTestCase):
    @allure.title('数量金额明细账查询')
    def test_api_query_quantity_amount_ledger(self):
        company = GetYamlData().get_company('api_company_accounting_books_005')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('数量金额明细账查询'):
            params = {
                "m": "queryDetail",
                "_search": "false",
                "nd": "1698287495950",
                "rows": "20000",
                "page": "1",
                "sidx": "date",
                "sord": "asc",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "accountNum": "1405",
                "accountId": "32793023701928",
                "includeItem": "1",
                "amountPlaces": "2",
                "pricePlaces": "2",
                "fromAccountId": "",
                "toAccountId": "",
                "fromLevel": "",
                "toLevel": "",
                "detail": "0",
                "assistentAccount": "0",
                "balance": "1",
                "happen": "1",
                "happenTotal": "1"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/generalqty', params=params)
                assert response.json().get('data')['total'] == 348
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.8


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_quantity_amount_general_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('数量金额总账')
class TestApiQuantityAmountGeneralLedger(BaseTestCase):
    @allure.title('数量金额总账查询')
    def test_api_query_quantity_amount_general_ledger(self):
        company = GetYamlData().get_company('api_company_accounting_books_006')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('数量金额总账查询'):
            params = {
                "m": "queryTotal",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "includeItem": "1",
                "amountPlaces": "2",
                "pricePlaces": "2",
                "_search": "false",
                "nd": "1698288486848",
                "rows": "0",
                "page": "1",
                "sidx": "code",
                "sord": "asc",
                "fromAccountId": "",
                "toAccountId": "",
                "fromLevel": "",
                "toLevel": "",
                "assistentAccount": "0",
                "balance": "1",
                "happen": "1"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/generalqty', params=params)
                assert response.json().get('data')['totalsize'] == 33
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.3


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_multi_column_ledger
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('多栏账')
class TestApiMultiColumnLedger(BaseTestCase):
    @allure.title('多栏账查询')
    def test_api_query_multi_column_ledger(self):
        company = GetYamlData().get_company('api_company_accounting_books_007')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('多栏账查询'):
            params = {
                "m": "getStore",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "showChild": "false",
                "showDetail": "false",
                "includeItem": "true",
                "showDetailBal": "true",
                "currency": "RMB",
                "itemClass": "1",
                "itemId": "0",
                "accountId": "274880187846604",
                "accountName": "应收账款",
                "happen": "1",
                "_search": "false",
                "nd": "1698288770095",
                "rows": "20000",
                "page": "1",
                "sidx": "date",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('multicolaccount', params=params)
                assert len(response.json().get('data')['items']) == 1067
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 1


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_accounting_balance
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('核算项目余额表')
class TestApiAccountingBalance(BaseTestCase):
    @allure.title('核算项目余额表查询')
    def test_api_query_accounting_balance(self):
        company = GetYamlData().get_company('api_company_accounting_books_008')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('核算项目余额表查询'):
            params = {
                "m": "query",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "AccountId": "",
                "auxiliaryId": "",
                "fromLevel": "",
                "auxiliaryType": "1",
                "toLevel": "",
                "includeItem": "0",
                "currency": "RMB",
                "balanceZero": "0",
                "balanceAndDebit": "0",
                "_search": "false",
                "nd": "1698290320736",
                "rows": "10000",
                "page": "1",
                "sidx": "number",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/balanceItemReport', params=params)
                assert response.json().get('records') == 63
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_books
@pytest.mark.api_accounting_books_accounting_detail
@allure.epic('会计')
@allure.feature('账簿')
@allure.story('核算项目明细账')
class TestApiAccountingDetail(BaseTestCase):
    @allure.title('核算项目明细账查询')
    def test_api_query_accounting_balance(self):
        company = GetYamlData().get_company('api_company_accounting_books_009')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('核算项目明细账查询'):
            params = {
                "m": "queryDetailItem",
                "fromPeriod": "201610",
                "toPeriod": "202308",
                "AccountId": "",
                "auxiliaryId": "",
                "fromLevel": "",
                "auxiliaryType": "1",
                "toLevel": "",
                "includeItem": "0",
                "currency": "RMB",
                "assBalance": "0",
                "assBalanceDebit": "0",
                "happenTotal": "1",
                "accountId": "943794734230006",
                "accountNum": "0009",
                "number": "0009",
                "parentId": "0",
                "_search": "false",
                "nd": "1698290571993",
                "rows": "500",
                "page": "1",
                "sidx": "date",
                "sord": "asc"
            }

            avg_response_times = []

            for _ in range(API_CASE_REPEAT_TIME):
                response = req.get('gl/general', params=params)
                assert response.json().get('data')['totalsize'] == 200
                avg_response_times.append(response.elapsed.total_seconds())

            assert sum(avg_response_times) / API_CASE_REPEAT_TIME < 0.5
