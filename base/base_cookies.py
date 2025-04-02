import json

import requests

from config import config
from utils.file_utils import get_env
from utils.yml import GetYamlData

yml = GetYamlData()


class RequestsClient:
    def __init__(
            self,
            env=get_env(),
            username=yml.get_login_info(get_env())[0],
            password=yml.get_login_info(get_env())[1],
            group=None,
            company=None
    ):
        self._env = env
        self._username = username
        self._password = password
        self._group = group
        self._company = company

        self._gj_domain = f"http://{self._env}.kdzwy.com/guanjia/"
        self._kj_domain = f"https://{self._env}.kdzwy.com:34/"
        self._cookies = None
        self._self_node = None
        self._company_id = None

        get_acct_token_result = self.__get_acct_token()
        if get_acct_token_result.get('is_success'):
            self._cookies = get_acct_token_result.get('msg')
        else:
            raise Exception(get_acct_token_result.get('msg'))

        if self._group:
            get_all_group_info_result = self.__get_all_group_info()
            if get_all_group_info_result.get('is_success'):
                group_data = get_all_group_info_result.get('msg')
            else:
                raise Exception(get_all_group_info_result.get('msg'))

            group_info_dict = self.__get_specific_group_eid(group_data)

            get_specific_group_token_result = self.__get_specific_group_token(group_info_dict)
            if get_specific_group_token_result.get('is_success'):
                self._cookies = get_specific_group_token_result.get('msg')
            else:
                raise Exception(get_specific_group_token_result.get('msg'))

        if self._company:
            get_node_id_result = self.__get_node_id()
            if get_node_id_result.get('is_success'):
                self._self_node = get_node_id_result.get('msg')
            else:
                raise Exception(get_node_id_result.get('msg'))

            get_company_id_result = self.__get_company_id()
            if get_company_id_result.get('is_success'):
                self._company_id = get_company_id_result.get('msg')
            else:
                raise Exception(get_company_id_result.get('msg'))

    def __get_acct_token(self):
        auth_url = f"{self._gj_domain}user/auth"
        auth_data = {'username': f'{self._username}',
                     'password': f'{self._password}'}
        try:
            auth_response = requests.post(auth_url, data=auth_data, timeout=config.LARGE_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            return {'is_success': False, 'msg': '获取token超时'}
        except requests.exceptions.ProxyError as p:
            return {'is_success': False, 'msg': f'获取token失败:{p}'}

        if auth_response.json().get('code') != 200:
            return {'is_success': False, 'msg': auth_response.json().get('msg')}
        else:
            res_json = json.loads(auth_response.text)
            acct_token = {'accttoken': res_json.get('data')['access_token']}
            return {'is_success': True, 'msg': acct_token}

    def __get_all_group_info(self):
        get_all_url = f"{self._gj_domain}companys/getAll"
        try:
            response = requests.get(get_all_url, cookies=self._cookies, verify=True,
                                    timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            return {'is_success': False, 'msg': '获取圈子信息超时'}

        res_json_group_data = response.json().get('data')
        if len(res_json_group_data):
            return {'is_success': True, 'msg': res_json_group_data}
        else:
            return {'is_success': False, 'msg': '圈子列表为空'}

    def __get_specific_group_eid(self, group_data):
        group_info_dict = {}
        for _ in group_data:
            if _.get('name') == self._group:
                group_info_dict['accCompanyId'] = _.get('accCompanyId')
                group_info_dict['eid'] = _.get('eid')
        if group_info_dict:
            return group_info_dict
        else:
            raise Exception(f'未查询到该圈子：{self._group}')

    def __get_specific_group_token(self, group_info_dict):
        switch_group_url = f"{self._gj_domain}companys/{group_info_dict.get('accCompanyId')}" \
                           f"/switch/{self._env}/{group_info_dict.get('eid')}"
        try:
            switch_group_response = requests.get(switch_group_url, cookies=self._cookies, verify=True,
                                                 timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            return {'is_success': False, 'msg': '获取圈子token超时'}

        new_acct_token_raw = switch_group_response.request.headers.get('Cookie').split(';')
        # new_acct_token_raw.remove(new_acct_token_raw[0])
        new_acct_token = {}
        for _ in new_acct_token_raw:
            new_acct_token[_.split('=')[0]] = _.split('=')[1]

        return {'is_success': True, 'msg': new_acct_token}

    def __get_node_id(self):
        self_node_url = f"{self._gj_domain}acctflow/selfnode"
        try:
            self_node_response = requests.get(self_node_url, cookies=self._cookies, verify=True,
                                              timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            return {'is_success': False, 'msg': '获取node_id超时'}

        self_node_res_json = self_node_response.json().get('data')
        if self_node_res_json:
            node_id = ''
            for _ in self_node_res_json:
                if _.get('nodeName') == '服务管理':
                    node_id = _.get('id')
            return {'is_success': True, 'msg': node_id}
        else:
            return {'is_success': False, 'msg': '获取node_id失败'}

    def __get_company_id(self):
        get_company_id_url = f"{self._gj_domain}acctflow/nodecustomer"
        get_company_id_params = {
            "nodeId": self._self_node,
            "page": "1",
            "limit": "1",
            "orderProperty": "acctCreateDate",
            "orderDirection": "desc",
            "fromDate": "",
            "toDate": "",
            "taxType": "",
            "taxCycle": "",
            "dispatchRole": "",
            "acctType": "",
            "valuate": "",
            "followUpStartTime": "",
            "followUpEndTime": "",
            "followUpType": "1",
            "followUp": "",
            "customerSource": "",
            "condition": "",
            "condition1": "",
            "condition2": "",
            "nodeType": "",
            "nodeValue": "",
            "tagId": "",
            "name": self._company,
            "dispatchStartTime": "",
            "dispatchEndTime": "",
            "operator": "",
            "acctPeriod": "",
            "noFollowUpOperator": "",
            "noFollowUpDays": "",
            "followUpTypeNew": "",
            "positionType": "0",
            "dispatchName": ""
        }
        try:
            get_company_id_response = requests.get(get_company_id_url, cookies=self._cookies,
                                                   params=get_company_id_params, verify=True,
                                                   timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            return {'is_success': False, 'msg': "获取company_id超时"}

        res_json = get_company_id_response.json().get('data')

        if len(res_json['items']) == 0:
            return {'is_success': False, 'msg': '未查询到该公司'}
        elif res_json['items'][0].get('companyName') != self._company:
            return {'is_success': False, 'msg': '未查询到该公司'}
        else:
            company_id = str(res_json['items'][0]['companyId'])
            return {'is_success': True, 'msg': company_id}

    def get_cookies(self):
        return self._cookies

    def get_acct_url(self):
        acct_url = f"{self._gj_domain}customer/accounturl"

        acct_params = {
            "companyId": self._company_id
        }
        try:
            acct_response = requests.get(acct_url, cookies=self._cookies, params=acct_params, verify=True,
                                         timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            raise Exception(f"获取{self._company}会计url超时")

        return acct_response.json().get('data')


# if __name__ == '__main__':
#     req = RequestsClient(company='test_api_003')
#     print(req.get_cookies())
