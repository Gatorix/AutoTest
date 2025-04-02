import os
import time

import requests

from datetime import datetime
from time import strftime, gmtime
from lxml import etree

from utils.date_time_utils import format_seconds

EXECUTE_WORKSPACE_PATH = 'C:/Users/kddadmin/Jenkins/workspace/autotest'


# EXECUTE_WORKSPACE_PATH = 'E:/autotest'


def read_dashboard(dashboard_file=f'{EXECUTE_WORKSPACE_PATH}/dashboard.html'):
    passed: int = 0
    untested: int = 0
    skipped: int = 0
    failed: int = 0
    html_str = None
    total_duration: float = 0

    with open(dashboard_file, 'r', encoding='utf-8') as df:
        lines = df.readlines()
        for line in lines:
            if "name: 'Passed'" in line:
                passed = int(lines[lines.index(line) + 1].split(':')[1].strip().replace(',', ''))
            elif "name: 'Untested'" in line:
                untested = int(lines[lines.index(line) + 1].split(':')[1].strip().replace(',', ''))
            elif "name: 'Skipped'" in line:
                skipped = int(lines[lines.index(line) + 1].split(':')[1].strip().replace(',', ''))
            elif "name: 'Failed'" in line:
                failed = int(lines[lines.index(line) + 1].split(':')[1].strip().replace(',', ''))
            elif '<table' in line:
                html_str = line

    html_element = etree.HTML(html_str)
    td_nodes = html_element.xpath('//tbody//td[3]')
    for _ in td_nodes:
        try:
            total_duration += float(_.text)
        except ValueError:
            pass

    return {
        'total': len(td_nodes),
        'passed': passed,
        'untested': untested,
        'skipped': skipped,
        'failed': failed,
        'duration': total_duration
    }


def read_report(report_file=f'{EXECUTE_WORKSPACE_PATH}/report.html'):
    total: int = 0
    html_str = None
    total_duration: float = 0

    with open(report_file, 'r', encoding='utf-8') as df:
        lines = df.readlines()
        for line in lines:
            if "ran in" in line:
                total = int(line.strip().split(' ')[0].replace('<p>', ''))
                total_duration = float(line.strip().split(' ')[4])
            elif '<p class="filter"' in line:
                html_str = line

    html_element = etree.HTML(html_str)
    passed = html_element.xpath('//span[@class="passed"]')[0].text
    skipped = html_element.xpath('//span[@class="skipped"]')[0].text
    failed = html_element.xpath('//span[@class="failed"]')[0].text
    error = html_element.xpath('//span[@class="error"]')[0].text
    xfailed = html_element.xpath('//span[@class="xfailed"]')[0].text
    xpassed = html_element.xpath('//span[@class="xpassed"]')[0].text
    rerun = html_element.xpath('//span[@class="rerun"]')[0].text

    return {
        'total': total,
        'passed': int(passed.split(' ')[0]),
        'skipped': int(skipped.split(' ')[0]),
        'failed': int(failed.split(' ')[0]),
        'error': int(error.split(' ')[0]),
        'xfailed': int(xfailed.split(' ')[0]),
        'xpassed': int(xpassed.split(' ')[0]),
        'rerun': int(rerun.split(' ')[0]),
        'duration': total_duration
    }


def duration():
    try:
        build_time = os.environ["BUILD_TIMESTAMP"]
    except Exception:
        return None
    build_time_array = time.strptime(build_time, "%Y-%m-%d %H:%M:%S")
    build_timestamp = int(time.mktime(build_time_array))
    return format_seconds(time.time() - build_timestamp).split('.')[0]


def send_results():
    result = read_report()

    # 自动化测试小组
    # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=3b7984b7e91b467ba0912503125f93cc'

    # 测试大群
    # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=817237496cd14c4da582cf61a8a465f5'

    # 管家发版群
    # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=8499063b73d041c0a11cdd89bddf64f3'

    # 自动化结果通知群
    url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=09192e2e2c6d4d568d4519908db85e5f'

    # test
    # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=d59d367fb1614200a4ec9999bf8a8db9'

    # 账无忧识别服务问题反馈群
    url_fb = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=0c50a2bc8b6c4f0780ce935193e99d00'

    if os.environ["test_model"] == '仅执行指定功能' and os.environ["test_feature"]:
        features = f'\n\t指定功能：{os.environ["test_feature"]}'
    else:
        features = ''

    data = {
        'content': '\nUI自动化执行结果：'
                   f'\n执行环境：{os.environ["test_env"]}'
                   f'\n执行项目：{os.environ["test_model"]}'
                   f'{features}'
                   f'\n完成时间：{str(datetime.now()).split(".")[0]}'
                   f'\n执行耗时：{duration()}'
                   f'\n执行用例数：{result.get("total")}'
                   f'\n\t成功用例：{result.get("passed")}'
                   f'\n\t失败用例：{result.get("failed") + result.get("error")}'
                   f'\n\t跳过用例：{result.get("skipped")}'
                   f'\n\t其他状态：{result.get("xfailed") + result.get("xpassed")}'
                   f'\n\t累计重试：{result.get("rerun")}'
                   f'\n成功率：{round(result.get("passed") / result.get("total") * 100, 2)}%'
                   '\n测试报告地址：http://172.20.184.42:8080'
                   '\n\t账号：report / 密码：Kdzwy^%$321'
                   '\n\t点击 autotest -> Allure Report',
        'notifyParams': [
            {
                "type": "mobiles",
                "values": [
                    "13590178916",
                    "13538101172",
                    "13926542714",
                    "13715181123",
                    "15018501281",
                    "16675397962",
                    "13155555467",
                    "13640002145",
                    "15875504850",
                    "18708916965",
                    "17877008801",
                    "15180563630",
                    "15818625503",
                    "13510242127",
                    '18845636132'
                ]
            }
        ]
    }
    requests.post(url, json=data)

    if os.environ["test_model"] == '仅执行PDF解析用例':
        requests.post(url_fb, json=data)

# if __name__ == '__main__':
#     send_results()
