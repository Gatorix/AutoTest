class PageApiSettingsVoucherType:
    @staticmethod
    def settings_voucher_type_query_default_voucher_type(req):
        default_voucher_type_id = ''
        voucher_type_url = "gl/generatecode"

        params = {
            "m": "findAll"
        }

        voucher_type_response = req.get(voucher_type_url, params=params)

        for _ in voucher_type_response.json()['data']['items']:
            if _.get('defaultCode'):
                default_voucher_type_id = str(_.get('id'))

        return default_voucher_type_id


class PageApiSettingsSubjects:
    @staticmethod
    def settings_subject_query_specified_subject(req,class_id,num):
        subject_id = ''
        query_acct_url = "gl/account"
        params = {
            "m": "queryAccount",
            "classId": class_id,
            "_search": "false",
            "rows": "30000",
            "page": "1",
            "sidx": "",
            "sord": "asc"
        }
        query_acct_url_response = req.get(query_acct_url, params=params)

        for _ in query_acct_url_response.json()["data"]["items"]:
            if _.get('number') == num:
                subject_id = _.get('id')

        return subject_id
