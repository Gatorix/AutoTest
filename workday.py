import datetime

import requests
from chinese_calendar import is_workday

# 日期/4的余数    0 =陈敏  1=李慧棉 2=欧青青 3=林欢欢
# 日期/3的余数    0 =黄德昌 1=胜红普  2=盛佰顺   ；
# 转换器提单  日期/2 0=何林蒲  1=欧杰；
# 日期/2 0=黄全  1=黄林
# 日期/3的余数    0=刘颖 1=林茉微 2=曹圣    转换器提单=吕小昆

PM = ['陈敏', '李慧棉', '林欢欢']
RD = ['黄德昌', '胜红普', '盛佰顺', '周建成', '彭锦洋']
RD_T = ['何林蒲', '欧杰']
RD_F = ['黄全', '黄林']
QA = ['刘颖', '林茉微']

if __name__ == '__main__':

    today = datetime.datetime.now().day

    today_pm = PM[today % len(PM)]
    today_rd = RD[today % len(RD)]
    today_rd_t = RD_T[today % len(RD_T)]
    today_rd_f = RD_F[today % len(RD_F)]
    today_qa = QA[today % len(QA)]

    if is_workday(datetime.datetime.now().date()):
        # 自动化测试小组
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=3b7984b7e91b467ba0912503125f93cc'

        # 会计交流群
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=1a14311dc0114555803e88ac82a9bdb5'

        # 管家会计全国第一
        url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=8499063b73d041c0a11cdd89bddf64f3'

        data = {
            'content': '@all 今日在线会计轮值负责人：'
                       f'\n产品：@{today_pm}'
                       f'\n后端开发：@{today_rd}'
                       f'\n前端开发：@{today_rd_f}'
                       f'\n转换器开发：@{today_rd_t}'
                       f'\n测试：@{today_qa}'
        }
        requests.post(url, json=data)
