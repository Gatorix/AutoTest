class PageApiVoucher:
    @staticmethod
    def voucher_data(*args):
        return {
            "vchData": "{\"id\":\"0\","
                       "\"groupId\":%s,"
                       "\"number\":24,\"voucherNo\":\"记-24\","
                       "\"attachments\":0,\"date\":\"%s\","
                       "\"year\":\"%s\",\"period\":\"%s\",\"yearPeriod\":%s,"
                       "\"entries\":[%s],"
                       "\"debitTotal\":%s,\"creditTotal\":%s,\"explanation\":\"api_test\","
                       "\"internalind\":\"\",\"transType\":\"\",\"userName\":\"18565630080\","
                       "\"checked\":0,\"checkName\":\"\",\"posted\":0,"
                       "\"modifyTime\":\"2023-11-30\",\"ownerId\":1,\"checkerId\":1}" % args
        }

    @staticmethod
    def voucher_data_entries(*args):
        return "{\"explanation\":\"api_test\",\"accountId\":%s,\"accountNumber\":\"%s\",""\"dc\":%s,\"amount\":\"%s\",\"cur\":\"RMB\",\"rate\":1,\"amountFor\":\"%s\",""\"qtyAux\":false,\"entryId\":1,\"limited\":0}," % args

    @staticmethod
    def del_voucher(req, voucher_id):
        params = {
            "m": "deleteById"
        }

        data = {
            "del": voucher_id,
        }

        headers = {"Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8'}

        response = req.post("gl/voucher", headers=headers, params=params, data=data)

        return response.json()['data']['msg']
