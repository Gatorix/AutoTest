from page.web_ui.page_login import LoginPage


class TestYQYData(LoginPage):
    username = '18622230972'
    password = 'wx941019'
    company_list = ['天津滨海高新区商业秘密保护协会']

    def test_get_yqy_data(self):
        self.get('https://www.17dz.com/home/login.html')
        self.type('//input[@placeholder="请输入手机号码"]', self.username)
        self.type('//input[@placeholder="请输入密码"]', self.password)
        self.click('//button/span[text()="登录"]')

        self.wait_for_element_visible('//div[@id="mg-navigation"]', timeout=20)
        self.wait_for_ready_state_complete()
        if self.is_element_visible(
                '//div[@class="miorManageFront-modal-content"]//span[@class="miorManageFront-modal-close-x"]'):
            self.click('//div[@class="miorManageFront-modal-content"]//span[@class="miorManageFront-modal-close-x"]')
        self.wait(500)
        # for company in self.company_list:
