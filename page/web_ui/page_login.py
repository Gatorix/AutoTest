from base.base_login import LoginBase
from base.base_case import BaseTestCase

from utils.yml import GetYamlData
from utils.file_utils import get_env

from base.base_requests import RequestsClient


class LoginPage(LoginBase, BaseTestCase):
    def input_login_value(self, input_placeholder, input_value, login_tab):
        """
        登录页面输入手机号或密码
        @param login_tab:
        @param input_placeholder: 输入框占位符
        @param input_value: 具体的手机号或密码
        @return:
        """
        input_xpath = self.login_input(input_placeholder, login_tab)
        self.type(input_xpath, input_value)

    def click_login_button(self, login_tab):
        """
        点击登录按钮
        @return:
        """
        button_xpath = self.login_button(login_tab)
        self.click(button_xpath)

    def is_login_fail(self):
        return self.is_element_visible(self.login_fail_area())

    # def is_still_in_login_page(self):
    #     return self.is_element_visible(self.login_button())

    def click_switch_version_button(self):
        self.click(self.switch_version_button())

    def get_text_from_switch_version_button(self):
        return self.get_text(self.switch_version_button())

    def login(self, env=get_env(), company=None, specific_user=None):
        """
        接口登录
        @param env: 测试环境
        @param company: 账套名称，带此参数调用直接进入会计，不带此参数进入管家
        @param specific_user: 指定用户登录
        @return:
        """
        if env == 'old':
            self.__old_version_login()
        else:
            yml = GetYamlData()

            if company:
                req_client = RequestsClient(company=company, specific_user=specific_user)
                self.get(req_client.get_acct_url())
            else:
                req_client = RequestsClient(company=company, specific_user=specific_user)
                self.get(yml.get_url(get_env()))
                cookies = {"domain": ".kdzwy.com",
                           "httpOnly": False,
                           "name": "accttoken",
                           "path": "/guanjia",
                           "sameSite": "Lax",
                           "secure": False,
                           "value": req_client.get_cookies().get('accttoken')}
                self.driver.add_cookie(cookies)
                self.get(f'{yml.get_url(get_env())}guanjia')

    def normal_login(self):
        self.__old_version_login(False)

    def __old_version_login(self, switch_to_old=True):
        yml_data = GetYamlData()
        env = get_env()

        if env == 'mmain':
            self.get('https://mgj.kdzwy.com/')
        elif env == 'pmain':
            self.get('https://pgj.kdzwy.com/')
        else:
            self.get('https://gj.kdzwy.com/')

        if switch_to_old:
            username, password = yml_data.get_login_info('old')
            if env == 'pmain':
                raise Exception('预发环境不支持1.0版本')

            self.click(self.v6_login_tab('金蝶账无忧V1.0登录'))
            self.__login_process(username, password, login_tab='金蝶账无忧V1.0登录')

        else:
            username, password = yml_data.get_login_info(env)
            self.__login_process(username, password)

    def __login_process(self, username, password, login_tab='金蝶账无忧V6.0登录'):
        self.input_login_value('手机号', username, login_tab)
        self.input_login_value('密码', password, login_tab)
        self.click_login_button(login_tab)
