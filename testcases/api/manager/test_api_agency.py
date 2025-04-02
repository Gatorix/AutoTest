# import allure
# import pytest
#
# from base.base_requests import RequestsClient
#
#
# @pytest.mark.api_manager
# @pytest.mark.api_manager_customer
# @pytest.mark.api_manager_customer_contract
# @allure.epic('管家')
# @allure.feature('客户管理')
# @allure.story('合同')
# class TestAgencyService:
#     @allure.title('获取账套链接')
#     def test_get_acct_set_link(self):
#         with allure.step('创建连接'):
#             req = RequestsClient(company='0807test')
#         with allure.step('获取账套链接'):
#
#             url = "https://gzvip1.kdzwy.com:34/gl/voucher"
#             params = {
#                 "m": "addNew"
#             }
#             data = {
#                 "vchData": "{\"id\":\"576615083278629\",\"groupId\":840331633288129,\"number\":1,\"voucherNo\":\"记-1\",\"attachments\":0,\"date\":\"2023-11-30\",\"year\":\"2023\",\"period\":\"11\",\"yearPeriod\":202311,\"entries\":[{\"explanation\":\"11\",\"accountId\":840331688938247,\"accountNumber\":\"1001\",\"dc\":-1,\"amount\":\"33.00\",\"cur\":\"RMB\",\"rate\":1,\"amountFor\":\"33.00\",\"qtyAux\":false,\"entryId\":1,\"limited\":0},{\"explanation\":\"11\",\"accountId\":840331692207464,\"accountNumber\":\"1012\",\"dc\":1,\"amount\":\"33.00\",\"cur\":\"RMB\",\"rate\":1,\"amountFor\":\"33.00\",\"qtyAux\":false,\"entryId\":2,\"limited\":0}],\"debitTotal\":33,\"creditTotal\":33,\"explanation\":\"11\",\"internalind\":\"\",\"transType\":\"\",\"userName\":\"18565630080\",\"checked\":0,\"checkName\":\"\",\"posted\":0,\"modifyTime\":\"2023-11-30\",\"ownerId\":1,\"checkerId\":1}"
#             }
#             response = requests.post(url, headers=headers, params=params, data=data)
