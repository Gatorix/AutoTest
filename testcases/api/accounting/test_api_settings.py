import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_settings
@pytest.mark.api_accounting_settings_currency
@allure.epic('会计')
@allure.feature('设置')
@allure.story('币别')
class TestCurrency(BaseTestCase):
    @allure.title('查询币别')
    def test_api_query_currency(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询币别'):
            params = {
                "m": "findAll"
            }
            result = req.get('bs/currency', params=params)

            assert result.json().get('status') == 200
            assert len(result.json().get('data')['items']) >= 1
            assert result.json().get('data')['items'][0].get('number') == 'RMB'


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_settings
@pytest.mark.api_accounting_settings_subject
@allure.epic('会计')
@allure.feature('设置')
@allure.story('科目')
class TestSubject(BaseTestCase):
    @allure.title('查询科目-顺序')
    def test_api_query_subject_asc(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询币别'):
            params = {
                "m": "queryAccount",
                "classId": "1",
                "_search": "false",
                "nd": "1688104378830",
                "rows": "30000",
                "page": "1",
                "sidx": "",
                "sord": "asc"
            }
            result = req.get('gl/account', params=params)
            assert result.json().get('status') == 200

    @allure.title('查询科目-倒叙')
    def test_api_query_subject_desc(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询币别'):
            params = {
                "m": "queryAccount",
                "classId": "1",
                "_search": "false",
                "nd": "1688104378830",
                "rows": "30000",
                "page": "1",
                "sidx": "",
                "sord": "desc"
            }
            result = req.get('gl/account', params=params)
            assert result.json().get('status') == 200

    @allure.title('查询科目-参数错误')
    def test_api_query_subject_wrong_params(self):
        company = GetYamlData().get_company('api_company_accounting_voucher_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('查询币别'):
            params = {
                # "m": "queryAccount",
                # "classId": "1",
                # "_search": "false",
                # "nd": "1688104378830",
                "rows": "30000",
                "page": "1",
                "sidx": "",
                "sord": "desc"
            }
            result = req.get('gl/account', params=params)

            assert result.json().get('status') == 400
            assert '客户端参数错误' in result.json().get('msg')
