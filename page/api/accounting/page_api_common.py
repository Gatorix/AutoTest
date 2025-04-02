class PageApiCommon:
    @staticmethod
    def page_api_get_current_period(req):
        url = '/bs/systemprofile'
        params = {
            'm': 'getPeriod'
        }
        response = req.get(url, params=params)
        return str(response.json()['data']['period'])
