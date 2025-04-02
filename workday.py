import datetime

import requests
from chinese_calendar import is_workday

if __name__ == '__main__':

    today = datetime.datetime.now().day

    today_pm = PM[today % len(PM)]
    today_rd = RD[today % len(RD)]
    today_rd_t = RD_T[today % len(RD_T)]
    today_rd_f = RD_F[today % len(RD_F)]
    today_qa = QA[today % len(QA)]

    if is_workday(datetime.datetime.now().date()):

        url = ""
        data = {
            'content': '@all 今日在线会计轮值负责人：'
                       f'\n产品：@{today_pm}'
                       f'\n后端开发：@{today_rd}'
                       f'\n前端开发：@{today_rd_f}'
                       f'\n转换器开发：@{today_rd_t}'
                       f'\n测试：@{today_qa}'
        }
        requests.post(url, json=data)
