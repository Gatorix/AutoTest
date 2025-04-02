import json
import logging.config

import requests
import yaml

from config import config
from utils.file_utils import get_env, get_project_path
from utils.random_data import shorten_response_text
from utils.yml import GetYamlData

yml = GetYamlData()

with open(f"{get_project_path()}/config/logging.yml", "r") as f:
    dict_conf = yaml.safe_load(f)

logging.config.dictConfig(dict_conf)
root = logging.getLogger()


class RequestsClient:
    def __init__(
            self,
            env=get_env(),
            username=yml.get_login_info(get_env())[0],
            password=yml.get_login_info(get_env())[1],
            group=yml.get_group(get_env()),
            company=None,
            specific_user=None
    ):
        self._env = env
        self._username = username
        self._password = password
        self._group = group
        if specific_user:
            self._username, self._password, self._group = yml.get_specific_login_info(self._env, specific_user)
        self._company = company

        self._gj_domain = f"https://{self._env}.kdzwy.com/guanjia/"
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

            get_acct_cookies_result = self.__get_acct_cookies()
            if get_acct_cookies_result.get('is_success'):
                self._cookies = get_acct_cookies_result.get('msg')
            else:
                raise Exception(get_acct_cookies_result.get('msg'))

    def __get_acct_token(self):
        auth_url = f"{self._gj_domain}user/auth"
        auth_data = {'username': f'{self._username}',
                     'password': f'{self._password}'}
        try:
            root.info('Login - 开始获取acct_token')
            auth_response = requests.post(auth_url, data=auth_data, timeout=config.LARGE_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error('Login - 获取acct_token超时')
            return {'is_success': False, 'msg': '获取token超时'}
        except requests.exceptions.ProxyError as p:
            root.error(f'Login - 获取acct_token失败:{shorten_response_text(str(p))}')
            return {'is_success': False, 'msg': f'获取token失败:{shorten_response_text(str(p))}'}

        if auth_response.json().get('code') != 200:
            root.error(f'Login - 获取acct_token失败: {shorten_response_text(auth_response.json().get("msg"))}')
            return {'is_success': False, 'msg': auth_response.json().get('msg')}
        else:
            res_json = json.loads(auth_response.text)
            acct_token = {'accttoken': res_json.get('data')['access_token']}
            root.info(f"Login - 获取acct_token成功: {shorten_response_text(str(acct_token))}")
            return {'is_success': True, 'msg': acct_token}

    def __get_all_group_info(self):
        get_all_url = f"{self._gj_domain}companys/getAll"
        try:
            root.info('Login - 开始获取圈子信息')
            response = requests.get(get_all_url, cookies=self._cookies, verify=True, timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error(f"Login - 获取圈子信息超时")
            return {'is_success': False, 'msg': '获取圈子信息超时'}

        res_json_group_data = response.json().get('data')
        if len(res_json_group_data):
            root.info(f"Login - 获取圈子信息成功: {shorten_response_text(str(res_json_group_data))}")
            return {'is_success': True, 'msg': res_json_group_data}
        else:
            root.error(f"Login - 圈子列表为空")
            return {'is_success': False, 'msg': '圈子列表为空'}

    def __get_specific_group_eid(self, group_data):
        root.info('Login - 解析圈子信息')
        group_info_dict = {}
        for _ in group_data:
            if _.get('name') == self._group:
                group_info_dict['accCompanyId'] = _.get('accCompanyId')
                group_info_dict['eid'] = _.get('eid')
        if group_info_dict:
            root.info(f'Login - 解析圈子信息完成: {shorten_response_text(str(group_info_dict))}')
            return group_info_dict
        else:
            root.error(f'Login - 未查询到该圈子: {self._group}')
            raise Exception(f'未查询到该圈子: {self._group}')

    def __get_specific_group_token(self, group_info_dict):
        switch_group_url = f"{self._gj_domain}companys/{group_info_dict.get('accCompanyId')}" \
                           f"/switch/{self._env}/{group_info_dict.get('eid')}"
        try:
            root.info('Login - 根据圈子eid切换圈子, 并获取新token')
            switch_group_response = requests.get(switch_group_url, cookies=self._cookies, verify=True,
                                                 timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error('Login - 切换圈子超时')
            return {'is_success': False, 'msg': '获取圈子token超时'}

        new_acct_token_raw = switch_group_response.request.headers.get('Cookie').split(';')
        # new_acct_token_raw.remove(new_acct_token_raw[0])
        new_acct_token = {}
        for _ in new_acct_token_raw:
            new_acct_token[_.split('=')[0]] = _.split('=')[1]

        root.info(f'Login - 指定圈子token获取成功: {shorten_response_text(str(new_acct_token))}')
        return {'is_success': True, 'msg': new_acct_token}

    def __get_node_id(self):
        self_node_url = f"{self._gj_domain}acctflow/selfnode"
        try:
            root.info(f'Login - 获取node_id')
            self_node_response = requests.get(self_node_url, cookies=self._cookies, verify=True,
                                              timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error(f'Login - 获取node_id超时')
            return {'is_success': False, 'msg': '获取node_id超时'}

        self_node_res_json = self_node_response.json().get('data')
        if self_node_res_json:
            node_id = ''
            for _ in self_node_res_json:
                if _.get('nodeName') == '服务管理':
                    node_id = _.get('id')
            root.info(f'Login - 获取node_id成功: {node_id}')
            return {'is_success': True, 'msg': node_id}
        else:
            root.error(f'Login - 获取node_id失败: {shorten_response_text(str(self_node_response.json()))}')
            return {'is_success': False, 'msg': '获取node_id失败'}

    def __get_company_id(self):
        get_company_id_url = f"{self._gj_domain}acctflow/nodecustomer"
        get_company_id_params = {
            "nodeId": self._self_node,
            "page": "1",
            "limit": "1000",
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
            root.info(f'Login - 获取[{self._company}]company_id')
            get_company_id_response = requests.get(get_company_id_url, cookies=self._cookies,
                                                   params=get_company_id_params, verify=True,
                                                   timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error(f'Login - 获取company_id超时')
            return {'is_success': False, 'msg': "获取company_id超时"}

        res_json = get_company_id_response.json().get('data')

        if len(res_json['items']) == 1 and res_json['items'][0].get('companyName') == self._company:
            company_id = str(res_json['items'][0]['companyId'])
            root.info(f'Login - 获取[{self._company}]company_id成功: {company_id}')
            return {'is_success': True, 'msg': company_id}

        elif len(res_json['items']) > 1:
            for _ in res_json['items']:
                if _.get('companyName') == self._company:
                    company_id = str(_['companyId'])
                    root.info(f'Login - 获取[{self._company}]company_id成功: {company_id}')
                    return {'is_success': True, 'msg': company_id}

        else:
            root.error(f'Login - 获取[{self._company}]company_id失败: 未查询到该公司')
            return {'is_success': False, 'msg': '未查询到该公司'}

    def __get_acct_cookies(self):
        acct_url = f"{self._gj_domain}customer/accounturl"

        acct_params = {
            "companyId": self._company_id
        }
        root.info(f'Login - 获取[{self._company}]acct_cookies')
        try:
            acct_response = requests.get(acct_url, cookies=self._cookies, params=acct_params, verify=True,
                                         timeout=config.NORMAL_TIMEOUT)
        except requests.exceptions.ReadTimeout:
            root.error(f'Login - 获取[{self._company}]会计url超时')
            return {'is_success': False, 'msg': f"获取[{self._company}]acct_cookies超时"}
        try:
            acct_url_res = requests.get(acct_response.json().get('data'))
        except Exception as s:
            root.error(f'Login - 获取[{self._company}]acct_cookies失败: {s}')
            raise Exception(s)
        acct_cookies_raw = (acct_url_res.request.headers.get('Cookie')).split(';')
        acct_cookies = {}

        for _ in acct_cookies_raw:
            acct_cookies[_.split('=')[0]] = _.split('=')[1]
        root.info(f'Login - 获取[{self._company}]acct_cookies成功: {acct_cookies}')
        return {'is_success': True, 'msg': {**acct_cookies, **self._cookies}}

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

    def post(self, path: str, **kwargs):
        if self._company:
            url = f'{self._kj_domain}{path}'
        else:
            url = f'{self._gj_domain}{path}'

        header = {"Content-Type": "application/json;charset=UTF-8"}
        headers = kwargs.get("headers", header)
        jsons = kwargs.get('json', {})
        params = kwargs.get("params", {})
        data = kwargs.get("data", "")
        files = kwargs.get("files", {})
        stream = kwargs.get("stream", False)
        cookies = kwargs.get("cookies", self._cookies)
        timeout = kwargs.get("timeout", config.NORMAL_TIMEOUT)

        try:
            root.info(f'POST请求: {url}')
            response = requests.post(
                url,
                headers=headers,
                cookies=cookies,
                data=data,
                json=jsons,
                params=params,
                files=files,
                stream=stream,
                timeout=timeout,
                verify=True
            )

            post_params = {
                'headers': headers,
                'cookies': cookies,
                'data': data,
                'jsons': jsons,
                'params': params,
                'files': files,
                'stream': stream
            }

            for _ in post_params.keys():
                root.info(f'POST请求参数 - {_}: {post_params.get(_)}') if post_params.get(_) else None

            root.info(f'POST请求结束, 返回状态: {response.status_code}')
            root.info(f'POST请求结束, 接口响应时间: {response.elapsed.total_seconds()}')
            result = f'{shorten_response_text(response.text)}'
            root.info(f'POST请求结束, 返回结果: {result}')

            return response

        except requests.exceptions.ReadTimeout as r:
            root.error(f'POST请求超时: {r}')
            raise Exception(r)

        except Exception as e:
            root.error(f'POST请求发生异常: {e}')
            raise Exception(e)

    def get(self, path, **kwargs):
        if self._company:
            url = f'{self._kj_domain}{path}'
        else:
            url = f'{self._gj_domain}{path}'

        header = {"Content-Type": "application/json;charset=UTF-8"}
        headers = kwargs.get("headers", header)
        jsons = kwargs.get('json', {})
        params = kwargs.get("params", {})
        data = kwargs.get("data", "")
        files = kwargs.get("files", {})
        stream = kwargs.get("stream", False)
        cookies = kwargs.get("cookies", self._cookies)
        timeout = kwargs.get("timeout", config.NORMAL_TIMEOUT)

        try:
            root.info(f'GET请求: {url}')
            response = requests.get(
                url,
                headers=headers,
                cookies=cookies,
                data=data,
                json=jsons,
                params=params,
                files=files,
                stream=stream,
                timeout=timeout,
                verify=True
            )

            get_params = {
                'headers': headers,
                'cookies': cookies,
                'data': data,
                'jsons': jsons,
                'params': params,
                'files': files,
                'stream': stream
            }

            for _ in get_params.keys():
                root.info(f'GET请求参数 - {_}: {get_params.get(_)}') if get_params.get(_) else None

            root.info(f'GET请求结束, 返回状态: {response.status_code}')
            root.info(f'GET请求结束, 接口响应时间: {response.elapsed.total_seconds()}')
            result = f'{shorten_response_text(response.text)}'
            root.info(f'GET请求结束, 返回结果: {result}')

            return response

        except requests.exceptions.ReadTimeout as r:
            root.error(f'GET请求超时: {r}')
            raise Exception(r)

        except Exception as e:
            root.error(f'GET请求发生异常: {e}')
            raise Exception(e)

    def delete(self, path, **kwargs):
        pass

    def head(self):
        pass

    def patch(self):
        pass

    def put(self):
        pass
