import allure
import pytest

from config.config import EXTREME_TIMEOUT
from base.base_requests import RequestsClient
from page.api.accounting.page_api_download import PageApiDownload
from utils.db_utils import ConnectDB
from utils.file_utils import get_project_path
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_smart_bookkeeping
@pytest.mark.api_accounting_smart_bookkeeping_bank_bill
@pytest.mark.api_accounting_smart_bookkeeping_bank_bill_pdf_parse
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('银行对账单')
class TestApiBankBill(PageApiDownload):
    db = ConnectDB()
    db.query_all_pdf_links()
    bank_name_kv = {
        'abc': '农业银行',
        'abc-js': '农业银行江苏分行',
        'boc': '中国银行',
        'ccb': '建设银行',
        'cebbank': '光大银行',
        'cmb': '招商银行',
        'comm': '交通银行',
        'crbank': '华润银行',
        'cscb': '长沙银行',
        'csrcbank': '常熟农商银行',
        'ecitic': '中信银行',
        'hubeibank': '湖北银行',
        'icbc': '工商银行',
        'pingan': '平安银行',
        'spdb': '浦发银行',
        'zjtlcb': '泰隆银行',
        'psbc': '邮政储蓄银行',
        'cgb': '广发银行',
        'bod': '东莞银行',
        'hbc': '徽商银行',
    }

    @allure.title('PDF银行对账单导入')
    @pytest.mark.parametrize('link_id,name,link', db.query_all_pdf_links())
    def test_all_bank_case(self, link_id, name, link):
        db = ConnectDB()
        if db.is_password_exist_by_id(link_id):
            return

        company = GetYamlData().get_company('api_company_accounting_bank_001')
        bank_name = self.bank_name_kv.get(name)

        expected_result = db.query_expected_data_by_id(link_id)

        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('获取银行id'):
            params = {
                "m": "selectList"
            }

            response = req.get('gl/bank', params=params)

            for _ in response.json().get('data')['items']:
                if bank_name == _.get('name'):
                    bank_item_id = _.get('itemID')

        with allure.step('上传文件'):
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }

            self.page_api_download(link)

            filename = link.split('/')[-1]

            file = {
                'file': (filename,
                         open(f'{get_project_path()}/download_tmp/{filename}', 'rb'),
                         'pdf')
            }

            params = {
                "m": "upload",
                "bankItemId": 701,
                "bankName": bank_name,
                "cover": "1",
                "accNumber": "1002",
                "type": "1"
            }

            response = req.post('gl/bank', headers=headers, params=params, files=file, timeout=EXTREME_TIMEOUT)

            if response.json()['status'] != 200:
                raise Exception(response.json()['msg'])

        with allure.step('结果比对'):
            assert expected_result == (
                str(response.json()["data"]["items"][0]["importCount"]),
                str(response.json()["data"]["items"][0]["totalIncome"]),
                str(response.json()["data"]["items"][0]["totalExpend"])
            )
