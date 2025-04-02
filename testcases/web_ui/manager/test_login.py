import allure
import pytest

from page.web_ui.page_login import LoginPage
from page.web_ui.manager.page_home import ManagerHomePage


@pytest.mark.ui
@pytest.mark.manager
@pytest.mark.manager_login
@allure.epic('管家')
@allure.feature('登录')
@allure.story('登录')
class TestLogin(LoginPage, ManagerHomePage):
    @pytest.mark.p1
    @allure.title('普通登录成功-6.0')
    def test_normal_login(self):
        with allure.step('登录'):
            self.normal_login()
            self.close_popup()
            assert self.is_avatar_visible()
