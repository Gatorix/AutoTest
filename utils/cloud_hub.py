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

    url = ''

    url_fb = ''

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
                   '\n测试报告地址：http://',
        'notifyParams': [
            {
                "type": "mobiles",
                "values": [

                ]
            }
        ]
    }
    requests.post(url, json=data)

    if os.environ["test_model"] == '仅执行PDF解析用例':
        requests.post(url_fb, json=data)

# if __name__ == '__main__':
#     send_results()
