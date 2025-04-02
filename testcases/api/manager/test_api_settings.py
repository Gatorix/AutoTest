import json

import allure
import pytest

from base.base_requests import RequestsClient


@allure.epic('管家')
@allure.feature('创建UI自动化预置数据')
@pytest.mark.pre_data
class TestCreatePreData:
    @allure.title('创建部门和用户')
    def test_create_dep_and_staff(self):
        user_list = {'记账01': '记账员',
                     '报税01': '报税员',
                     '经办01': '经办人',
                     '经理01': '客户经理(代账)',
                     '开票01': '开票员'}

        sub_dep_user_list = {'财务01': '客户经理(代账)',
                             '行政01': '客户经理(代账)'}

        with allure.step('创建连接'):
            req = RequestsClient()
        with allure.step('查询部门'):
            staff_tree_url = "department/addStaffTree"
            params = {
                "isStaffTree": "1",
                "enable": "1"
            }
            staff_tree_response = req.get(staff_tree_url, params=params)
            root_department_id = staff_tree_response.json().get('data')[0].get('id')

        with allure.step('查询岗位'):
            position_url = "position"
            params = {
                "page": "1",
                "limit": "50"
            }
            position_response = req.get(position_url, params=params)
            current_env_position = {}
            for _ in position_response.json().get('data').get('items'):
                current_env_position[_.get('positionName')] = _.get('positionId')

        with allure.step('创建用户'):
            for index, _ in enumerate(user_list.keys()):
                create_user_url = "staff"
                create_user_data = {
                    "username": f"{_}",
                    "loginphone": f'136{index}666888{index}',
                    "gender": "0",
                    "birthDate": "2023-09-14",
                    "email": "",
                    "phone": "",
                    "qq": "",
                    "address": "",
                    "sysrole": [],
                    "departmentId": int(root_department_id),
                    "positionList": [
                        {
                            "positionId": int(current_env_position.get(user_list.get(_)))
                        }
                    ],
                    "dataList": [],
                    "powerChangedLog": "$新增岗位：、$"
                }
                data = json.dumps(create_user_data, separators=(',', ':'))
                response = req.post(create_user_url, data=data)

                print(response.json())

        with allure.step('创建二级部门'):
            create_dep_url = "department"
            departments = ['财务部', '行政部']
            for _ in departments:
                data = {
                    "departmentId": root_department_id,
                    "departmentName": _
                }
                data = json.dumps(data, separators=(',', ':'))
                response = req.post(create_dep_url, data=data)
                print(response.json())

        with allure.step('创建二级部门职员'):
            with allure.step('查询部门'):
                staff_tree_url = "department/addStaffTree"
                params = {
                    "isStaffTree": "1",
                    "enable": "1"
                }
                staff_tree_response = req.get(staff_tree_url, params=params)
                dep_id_kv = {}
                for _ in staff_tree_response.json().get('data')[0].get('children'):
                    dep_id_kv[_.get('label')] = _.get('departmentId')

            with allure.step('创建职员'):
                for index, _ in enumerate(sub_dep_user_list.keys()):
                    create_user_url = "staff"
                    create_user_data = {
                        "username": f"{_}",
                        "loginphone": f'136{index}666777{index}',
                        "gender": "0",
                        "birthDate": "2023-09-14",
                        "email": "",
                        "phone": "",
                        "qq": "",
                        "address": "",
                        "sysrole": [],
                        "departmentId": int(dep_id_kv.get(f'{_[:2]}部')),
                        "positionList": [
                            {
                                "positionId": int(current_env_position.get(sub_dep_user_list.get(_)))
                            }
                        ],
                        "dataList": [],
                        "powerChangedLog": "$新增岗位：、$"
                    }
                    data = json.dumps(create_user_data, separators=(',', ':'))
                    response = req.post(create_user_url, data=data)
                    print(response.json())
