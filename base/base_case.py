import os.path
import time

import allure

from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from seleniumbase import BaseCase
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

from utils.file_utils import get_project_path, is_dir_empty, get_browser_type


class BaseTestCase(BaseCase):
    def tearDown(self):
        """This method overrides tearDown() from BaseCase."""
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            with allure.step('添加失败截图'):
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        super().tearDown()

    def get_new_driver(self, *args, **kwargs):
        """This method overrides get_new_driver() from BaseCase."""
        if not os.path.isdir(f'{get_project_path()}\\download_tmp\\{self.test_id}'):
            os.mkdir(f'{get_project_path()}\\download_tmp\\{self.test_id}')

        if get_browser_type() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-3d-apis")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('detach', False)
            options.add_argument('--allow-running-insecure-content')
            options.add_argument("--allow-insecure-localhost")
            options.add_argument("--incognito")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")

            if 'test_api_' in self.test_id:
                options.add_argument("--headless=new")

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 0,
                'download.default_directory': f'{get_project_path()}\\download_tmp\\{self.test_id}'
            }
            options.add_experimental_option("prefs", prefs)

            # driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            driver.delete_all_cookies()

            return driver

        elif get_browser_type() == 'edge':
            edge_options = Options()

            edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # 解决selenium无法访问https的问题
            edge_options.add_argument("--ignore-certificate-errors")
            # 允许忽略localhost上的TLS/SSL错误
            edge_options.add_argument("--allow-insecure-localhost")
            # 设置为无痕模式
            edge_options.add_argument("--incognito")
            edge_options.add_argument('--start-maximized')
            # 设置为无头模式
            # options.add_argument("--headless")
            # 解决卡顿
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")

            prefs = {
                "download.default_directory": f'{get_project_path()}\\download_tmp\\{self.test_id}',
                "download.prompt_for_download": False
            }
            edge_options.add_experimental_option('prefs', prefs)

            # edge_service = Service(EdgeChromiumDriverManager().install())

            driver = webdriver.Edge(options=edge_options)
            driver.delete_all_cookies()

            return driver

        elif get_browser_type() == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--disable-3d-apis")
            firefox_options.add_argument('--ignore-certificate-errors')
            firefox_options.add_argument('--ignore-ssl-errors')
            firefox_options.add_argument('--allow-running-insecure-content')
            firefox_options.add_argument("--allow-insecure-localhost")
            firefox_options.add_argument("--incognito")
            firefox_options.add_argument("--disable-extensions")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-gpu")
            firefox_options.add_argument("--disable-dev-shm-usage")

            if self.headless:
                firefox_options.add_argument("--headless=new")

            firefox_options.set_preference("browser.download.folderList", 2)
            firefox_options.set_preference("browser.download.dir",
                                           f'{get_project_path()}\\download_tmp\\{self.test_id}')
            # firefox_profile.set_preference("browser.helpApps.neverAsk.saveToDisk","binary/octet-stream")

            driver = webdriver.Firefox(options=firefox_options)

            driver.maximize_window()
            driver.delete_all_cookies()

            return driver

        elif get_browser_type() == 'ie':

            driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

            return driver

        elif get_browser_type() == '360':
            pass

        else:
            raise Exception('不支持的浏览器类型')

    def rename_downloaded_file(self, new_name):
        folder_of_download = f'{get_project_path()}/download_tmp/{self.test_id}'

        filename = max(
            [f for f in os.listdir(folder_of_download)],
            key=lambda xa: os.path.getctime(os.path.join(folder_of_download, xa))
        )

        os.rename(
            os.path.join(folder_of_download, filename),
            os.path.join(folder_of_download, new_name)
        )

    def get_downloaded_filename(self, time_to_wait: Optional[int] = 60):
        folder_of_download = f'{get_project_path()}/download_tmp/{self.test_id}'
        time_counter = 0

        try:
            filename = max(
                [f for f in os.listdir(folder_of_download)],
                key=lambda xa: os.path.getctime(os.path.join(folder_of_download, xa))
            )
        except ValueError:
            raise Exception('临时下载目录为空！')

        while '.tmp' in filename or '.crdownload' in filename:
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait:
                raise Exception('Waited too long for file to download')

        return max(
            [f for f in os.listdir(folder_of_download)],
            key=lambda xa: os.path.getctime(os.path.join(folder_of_download, xa))
        )

    def get_element_css_value(self, selector, css_property):
        self.wait_for_ready_state_complete()
        element = self.driver.find_element(By.XPATH, selector)
        return element.value_of_css_property(css_property)

    def get_element_location(self, selector):
        # return {x,y}
        self.wait_for_ready_state_complete()
        element = self.find_element(selector)
        return element.location

    def move_mouse_to_element(self, selector):
        self.wait_for_ready_state_complete()
        element = self.find_element(selector)
        ActionChains(self.driver).move_to_element(element).perform()
