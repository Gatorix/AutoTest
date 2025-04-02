import time

import allure
import pytest

from base.base_case import BaseTestCase
from base.base_requests import RequestsClient
from page.api.accounting.page_api_voucher import PageApiVoucher
from utils.file_utils import get_project_path, get_env
from utils.yml import GetYamlData


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_smart_bookkeeping
@pytest.mark.api_accounting_smart_bookkeeping_bank_bill
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('银行对账单')
class TestApiBankBill(PageApiVoucher, BaseTestCase):
    @allure.title('银行对账单导入-pdf')
    def test_api_bank_bill_import_pdf(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_001')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('获取银行id'):
            params = {
                "m": "selectList"
            }
            response = req.get('gl/bank', params=params)
            for _ in response.json().get('data')['items']:
                if '招商银行' == _.get('name'):
                    bank_item_id = _.get('itemID')

        with allure.step('上传文件'):
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }
            file = {
                'file': ('招行对账单-02.pdf',
                         open(f'{get_project_path()}/template/accounting/smart_bookkeeping/招行对账单-02.pdf', 'rb'),
                         'pdf')
            }

            params = {
                "m": "upload",
                "bankItemId": bank_item_id,
                "bankName": "招商银行",
                "cover": "1",
                "accNumber": "1002",
                "type": "1"
            }
            response = req.post('gl/bank', headers=headers, params=params, files=file)

            assert response.json()["data"]["items"][0]["totalIncome"] == '399,850.98'
            assert response.json()["data"]["items"][0]["totalExpend"] == '531,223.42'
            assert response.elapsed.total_seconds() < 10

    @allure.title('银行对账单导入-xls')
    def test_api_bank_bill_import_xls(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_002')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('获取银行id'):
            params = {
                "m": "selectList"
            }
            response = req.get('gl/bank', params=params)
            for _ in response.json().get('data')['items']:
                if '标准导入' == _.get('name'):
                    bank_item_id = _.get('itemID')

        with allure.step('上传文件'):
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }
            file = {
                'file': ('api_test_bank_bill_import.xlsx',
                         open(
                             f'{get_project_path()}/template/accounting/smart_bookkeeping/api_test_bank_bill_import.xlsx',
                             'rb'),
                         'xlsx')
            }
            params = {
                "m": "upload",
                "bankItemId": bank_item_id,
                "bankName": "标准导入",
                "cover": "1",
                "accNumber": "1002",
                "type": "0"
            }
            response = req.post('gl/bank', headers=headers, params=params, files=file)

            assert response.json()["data"]["items"][0]["totalIncome"] == '2,040,000.00'
            assert response.elapsed.total_seconds() < 1

    @allure.title('银行对账单生成凭证')
    def test_api_bank_bill_gen_voucher(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_003')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)
        with allure.step('生成凭证'):
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }
            params = {
                "m": "genVoucher",
                "sure": "0",
                "voucherType": "2"
            }
            data = {
                "ids": "732194370938903,732194491508761,732194542230310,732194564114899,732194590599994,732194571550644,732194661932055,732194628905093,732194650667115,732194648630223,732194715772988,732194727282374,732194729949700,732194871271805,732194896538468,732194807403872,732194927021871,732194942886681,732194986746009,732195129442674,732195105547255,732195147642920,732195230469546,732195262253520,732195267896891,732195289463467,732195327922306,732195308371386,732195318450952,732195478571015,732195464281364,732195488166076,732195462878228,732195522067024,732195557168176,732195589422081,732195506439155,732195687102433,732195646750301,732195683150203,732195603321848,732195701338405,732195788588431,732195712708864,732195726569618,732195828196592,732195866523777,732195834863519,732195804427654,732195994687064,732195951869173,732195975943532,732195992271570,732196014255432,732196001562011,732196010826015,732196108845082,732196108402206,732196181375435,732196199517714,732196247300270,732196241215988,732196284497048,732196341520218,732196357890866,732196356095223,732196348411182,732196403049784,732196437550667,732196483797993,732196478138431,732196551537184,732196548967037,732196653840738,732196740148224,732196785352311,732196800985139,732196873947937,732196898961530,732196988962502,732196945015904,732196963257960,732197046123796,732197012585590,732197013437153,732197067719241,732197115765468,732197110233591,732197170784684,732197211796469,732197218006311,732197342927169,732197313006309,732197313990695,732197381702320,732197401305978,732197425466608,732197404188890,732197597864114,732197514012839,732197561370519,732197601901471"
            }
            response = req.post('bs/bankcopy', headers=headers, params=params, data=data)

            voucher_id = response.json()["data"]["success"][0]["voucherId"]

        with allure.step('删除凭证'):
            self.del_voucher(req, voucher_id)

        assert response.elapsed.total_seconds() < 4


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_smart_bookkeeping
@pytest.mark.api_accounting_smart_bookkeeping_income_invoice
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('进项票')
class TestApiIncomeInvoice(PageApiVoucher, BaseTestCase):
    @allure.title('获取进项票商品明细')
    def test_api_income_invoice_get_product_details(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_004')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('获取发票id'):
            params = {
                "m": "query",
                "taxType": "1",
                "startPeriod": "",
                "endPeriod": "",
                "tally": "1",
                "status": "正常",
                "sourceType": "",
                "isRelation": "",
                "accountRuleId": "",
                "orderField": "FCREATEDATE",
                "orderDirection": "asc",
                "name": "",
                "fpType": "0",
                "grType": "0",
                "dkType": "0",
                "businessItemId": "",
                "settlementItemId": "",
                "orderType": "",
                "goodsName": "",
                "taxRate": "",
                "from_rzrq": "",
                "to_rzrq": "",
                "from_taxPeriod": "",
                "to_taxPeriod": "",
                "voucherFromPeriod": "",
                "voucherToPeriod": "",
                "rzstatus": "",
                "code": "",
                "remark": "",
                "amount_condition": "全部",
                "nd": "1698732722198",
                "signedStatus": "",
                "page": "1",
                "limit": "100"
            }
            response = req.get('bs/skfp', params=params)

            for _ in response.json()['data']['items']:
                if _.get('code') == '00935183':
                    invoice_id = _.get('id')

        with allure.step('获取商品明细'):
            headers = {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": f"https://{get_env()}.kdzwy.com:34/intelligenceAccount/incomeInvoice.jsp",
            }
            params = {
                "m": "synchronizegoods",
                "type": "1",
                "contact": "0"
            }
            data = {
                "ids": invoice_id
            }
            response = req.post('bs/skfp', headers=headers, params=params, data=data)
            lot = response.json()['data']['lot']

        with allure.step('获取查询结果'):
            params = {
                "m": "synchronizeprogress",
                "lot": lot
            }
            t1 = 0.0
            for _ in range(10):
                t0 = time.time()
                res = req.post('bs/skfp', headers=headers, params=params)
                if res.json().get('data')['successCount'] == 1:
                    t1 = time.time()
                    break
                time.sleep(1)

            assert t1 - t0 < 0.3

    @allure.title('导入进项发票')
    def test_api_income_invoice_import(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_005')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('上传进项文件'):
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
            }

            files = {
                'file': ('进项发票标准模板-api-test.xlsx',
                         open(
                             f'{get_project_path()}/template/accounting/smart_bookkeeping/进项发票标准模板-api-test.xlsx',
                             'rb'),
                         'xlsx')
            }

            params = {
                "m": "upload",
                "taxType": "1",
                "newfile": "进项发票标准模板-api-test",
                "method": "1",
                "cover": "1",
                "type": "",
                "name": ""
            }
            response = req.post('bs/skfp', headers=headers, params=params, files=files)

            assert response.elapsed.total_seconds() < 3

    @allure.title('进项发票生成凭证')
    def test_api_income_invoice_gen_voucher(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_006')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('生成凭证'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/intelligenceAccount/incomeInvoice.jsp",
            }
            params = {
                "m": "genVoucher",
                "taxType": "1",
                "sure": "0",
                "voucherType": "2"
            }
            data = {
                "ids": "738354700953688,738354702940666,738354704472594,738354705597758,738354707552715,738354709896724,738354711912813,738354714655249,738354717367739,738354719743547,738354721743760,738354724259274,738354727899692,738354730802941,738354732220108,738354734098715,738354736199176,738354738270534,738354740898931,738354742499051,738354743757758,738354745923369,738354747952721,738354750903998,738354753006677,738354756839832,738354758992616,738354762312089,738354765324969,738354769124987,738354772248500,738354775553749,738354779285374,738354782958450,738354784892871,738354787561132,738354790655982,738354793383766,738354795138617,738354799127845,738354801594495,738354803949694,738354806055610,738354808452377,738354811115139,738354813981723,738354816819377,738354818142143,738354821885903,738354824877705,738354827401188,738354829647476,738354831027865,738354833190310,738354835196350,738354836968479,738354838330024,738354840640655,738354842868179,738354843845376,738354845959731,738354847918840,738354849439787,738354850392044,738354852837943,738354854647538,738354856446915,738354858773817,738354860825117,738354863498493,738354865319683,738354868123492,738354870571790,738354872816246,738354875249697,738354877327172,738354879553536,738354881406414,738354883582990,738354885446904,738354886353666,738354888284696,738354890921656,738354892125010,738354894571496,738354895457323,738354897566789,738354899025858,738354901873843,738354902101619,738354904202722,738354907824269,738354909465345,738354912643071,738354919561503,738354922249193,738354927338156,738354931088448,738354933792389"
            }
            response = req.post('bs/skfp', headers=headers, params=params, data=data)

            voucher_id = response.json()["data"]["success"][0]["voucherId"]

        with allure.step('删除凭证'):
            self.del_voucher(req, voucher_id)

        assert response.elapsed.total_seconds() < 10


@pytest.mark.api
@pytest.mark.api_accounting
@pytest.mark.api_accounting_smart_bookkeeping
@pytest.mark.api_accounting_smart_bookkeeping_outcome_invoice
@allure.epic('会计')
@allure.feature('智能记账')
@allure.story('销项票')
class TestApiOutcomeInvoice(PageApiVoucher, BaseTestCase):
    @allure.title('导入销项发票')
    def test_api_outcome_invoice_get_product_details(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_007')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('上传文件'):
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
            }
            files = {
                'file': ('销项发票标准模板-api-test.xlsx',
                         open(
                             f'{get_project_path()}/template/accounting/smart_bookkeeping/销项发票标准模板-api-test.xlsx',
                             'rb'),
                         'xlsx')
            }
            params = {
                "m": "upload",
                "taxType": "0",
                "newfile": "销项发票标准模板-api-test.xlsx",
                "method": "1",
                "cover": "1",
                "type": "",
                "name": ""
            }

            response = req.post('bs/skfp', headers=headers, params=params, files=files)

            assert response.elapsed.total_seconds() < 3.0

    @allure.title('销项发票生成凭证')
    def test_api_outcome_invoice_gen_voucher(self):
        company = GetYamlData().get_company('api_company_accounting_smart_bookkeeping_008')
        with allure.step('创建连接'):
            req = RequestsClient(company=company)

        with allure.step('生成凭证'):
            headers = {
                "Referer": f"https://{get_env()}.kdzwy.com:34/intelligenceAccount/taxInvoice.jsp",
            }
            params = {
                "m": "genVoucher",
                "taxType": "0",
                "sure": "0",
                "voucherType": "2"
            }
            data = {
                "ids": "744647202394141,744647207523606,744647214755821,744647219821209,744647224909733,744647228659390,744647234636292,744647239788226,744647245828522,744647250096709,744647255141745,744647259047654,744647264120839,744647272073293,744647283378599,744647291111630,744647297168259,744647302029183,744647309774076,744647315837966,744647320167788,744647325941140,744647331775793,744647337196478,744647344807146,744647349006522,744647356800214,744647368926816,744647374048335,744647379702993,744647384500293,744647392753854,744647403955897,744647408396138,744647416247891,744647423499630,744647431667941,744647437587827,744647443664299,744647452568836,744647458871807,744647465336362,744647470868202,744647475183379,744647480379952,744647485362992,744647490183456,744647495377572,744647499682695,744647504403843,744647205566440,744647209578898,744647217337420,744647221315760,744647226551556,744647231355015,744647237586159,744647241260898,744647247592110,744647252986067,744647257383616,744647262148539,744647268519856,744647275419113,744647287019490,744647294046954,744647300211212,744647305582113,744647312082963,744647318846767,744647323263192,744647328442523,744647334196646,744647341954419,744647346993523,744647353416399,744647360335312,744647372210513,744647377673779,744647382689535,744647387348408,744647397392804,744647406576441,744647411006461,744647419617232,744647427643641,744647434782076,744647440934340,744647449588360,744647455482492,744647462724664,744647467567470,744647473736155,744647478465371,744647482665076,744647488553137,744647493424076,744647497520776,744647502144847,744647506731051"
            }
            response = req.post('bs/skfp', headers=headers, params=params, data=data)
            voucher_id = response.json()["data"]["success"][0]["voucherId"]

        with allure.step('删除凭证'):
            self.del_voucher(req, voucher_id)

        assert response.elapsed.total_seconds() < 8
