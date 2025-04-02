class LoginBase:
    @staticmethod
    def login_input(placeholder, login_tab):
        """
        登录页面手机号和密码的输入框
        @param login_tab:
        @param placeholder: 手机号或密码
        @return:
        """
        tab_kv = {
            '金蝶账无忧V6.0登录': 'v6Wrap',
            '金蝶账无忧V1.0登录': 'v1Wrap',
            '金蝶账无忧企业查账登录': 'customerLoginWrap'
        }
        return f'//div[@id="{tab_kv.get(login_tab)}"]//input[contains(@placeholder,"{placeholder}") and contains(@id,"log")]'

    @staticmethod
    def login_button(login_tab):
        """
        登录页面的登录按钮
        @return:
        """
        tab_kv = {
            '金蝶账无忧V6.0登录': 'sub-btn',
            '金蝶账无忧V1.0登录': 'sub-btn-v1',
            '金蝶账无忧企业查账登录': 'sub-btn-cus'
        }
        return f'//*[@id="{tab_kv.get(login_tab)}"]'

    @staticmethod
    def login_fail_area():
        return '//*[contains(text(),"登录信息已失效")]|//*[contains(text(),"账号已离职")]'

    @staticmethod
    def switch_version_button():
        return '//div[@class="head_top"]/div[@class="fws"]//a'

    @staticmethod
    def v6_login_tab(tab):
        return f'//div[@class="login-form"]//div[@data-tabname="{tab}"]'
