import os
import shutil
import time

from config.config import DEFAULT_TEST_BROWSER, DEFAULT_TEST_ENV, LARGE_TIMEOUT

EXECUTE_WORKSPACE_PATH = 'C:/Users/kddadmin/Jenkins/workspace/autotest'


def get_project_path(project_name='autotest'):
    """
    获取项目绝对路径
    :return:
    """
    file_path = os.path.dirname(__file__)
    if 'SendReport' in file_path:
        return file_path[:file_path.find('SendReport') + len('SendReport')]
    else:
        return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_env():
    env_kv = {
        '生产环境_main': 'main',
        '生产环境_vip0': 'vip0',
        '生产环境_vip1': 'vip1',
        '生产环境_vip2': 'vip2',
        '生产环境_vip3': 'vip3',
        '生产环境_vip4': 'vip4',
        '生产环境_vip5': 'vip5',
        '生产环境_vip6': 'vip6',
        '生产环境_gzmain': 'gzmain',
        '生产环境_gzvip1': 'gzvip1',
        '生产环境_gzvip0': 'gzvip0',
        '预发布环境': 'pmain',
        '模拟环境': 'mmain',
        '灰度环境': 'gray'
    }

    try:
        return env_kv.get(os.environ['test_env'])
    except KeyError:
        return DEFAULT_TEST_ENV


def get_browser_type():
    try:
        return os.environ['browser']
    except KeyError:
        return DEFAULT_TEST_BROWSER


def del_files(path=f'{get_project_path()}/download_tmp'):
    del_list = os.listdir(path)
    for f in del_list:
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def is_dir_empty(folder_path):
    if not os.listdir(folder_path):
        return True
    else:
        return False


def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        raise Exception('文件不存在！')


def get_all_file_path(file_path):
    filelist = os.listdir(file_path)
    company_list = []
    filename_list = []
    file_path_list = []
    for file in filelist:
        # 输出指定后缀类型的文件
        # if(item.endswith('.jpg')):
        company_list.append(file[:-27])
        filename_list.append(file)
        file_path_list.append(rf'E:\autotest\backup\{file}')
    if len(filename_list) == len(file_path_list):
        return company_list, filename_list, file_path_list


def pre_clear_allure_dir(allure_dir, timeout=LARGE_TIMEOUT):
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    for _ in range(int(timeout * 10)):
        try:
            shutil.rmtree(allure_dir)
            os.mkdir(allure_dir)
            return
        except Exception:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)


def get_all_xml_file_path(file_path):
    filelist = os.listdir(file_path)
    company_list = []
    filename_list = []
    file_path_list = []
    for r_file in filelist:
        if r_file.split('.')[-1] == 'xml':
            company_list.append(r_file.split('.')[0])
            filename_list.append(r_file)
            file_path_list.append(rf'{file_path}/{r_file}')
    if len(filename_list) == len(file_path_list):
        return company_list, filename_list, file_path_list
