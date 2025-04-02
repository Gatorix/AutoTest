import logging.config

import yaml
from utils.file_utils import get_project_path


class GetYamlData:
    def __init__(self, file_path=None):
        if not file_path:
            self.file_path = f'{get_project_path()}/config/environment.yml'
        else:
            self.file_path = file_path
        self.data = self.__load_yml()

    # @staticmethod
    # def get_jenkins_proj_path():
    #     try:
    #         with open('D:\\config', 'r', encoding='utf-8') as env_config:
    #             proj_path = env_config.readline()
    #             return proj_path
    #     except FileNotFoundError:
    #         return None

    def __load_yml(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data['data']

    def get_login_info(self, env):
        return (self.data[env].get('username'),
                self.data[env].get('password'))

    def get_specific_login_info(self, env, user):
        return (self.data[env][user].get('username'),
                self.data[env][user].get('password'),
                self.data[env][user].get('group'))

    def get_url(self, env):
        return self.data[env].get('url')

    def get_group(self, env):
        return self.data[env]['group']

    def get_company(self, company) -> str:
        company = self.data['company'].get(company)

        if company:
            return company
        else:
            raise Exception('yml文件中未定义该公司')

    def get_result(self, result):
        return self.data['result'].get(result)


def logger():
    with open(fr"{get_project_path()}/config/logging.yml", "r") as f:
        dict_conf = yaml.safe_load(f)

    logging.config.dictConfig(dict_conf)
    return logging.getLogger()
