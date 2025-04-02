import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from page.api.accounting.page_api_voucher import PageApiVoucher
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_salary
@allure.epic('会计')
@allure.feature('工资')
@allure.story('工资')
class TestApiSalary(
    PageApiVoucher,
    BaseTestCase
):
    @allure.title('计提工资')
    def test_api_provision_of_salary(self):
        company = GetYamlData().get_company('api_company_accounting_salary_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('生成计提工资凭证'):
            params = {
                "m": "genVoucher",
                "number": "wage",
                "id": "1",
                "period": "202302"
            }
            response = req.post('ws/wage', params=params)

            voucher_id = response.json().get('data')['id']

        with allure.step('删除凭证'):
            assert '共删除1张凭证' == self.del_voucher(req, voucher_id)

            assert response.json().get('status') == 200
            assert response.elapsed.total_seconds() < 2

    @allure.title('发放工资')
    def test_api_pay_salary(self):
        company = GetYamlData().get_company('api_company_accounting_salary_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('生成发放工资凭证'):
            params = {
                "m": "genVoucher",
                "number": "wage",
                "id": "2",
                "period": "202302"
            }
            response = req.post('ws/wage', params=params)

            voucher_id = response.json().get('data')['id']

        with allure.step('删除凭证'):
            assert '共删除1张凭证' == self.del_voucher(req, voucher_id)

            assert response.json().get('status') == 200
            assert response.elapsed.total_seconds() < 2
