import datetime

from utils.db_utils import ConnectDB
import requests

if __name__ == '__main__':
    db = ConnectDB()
    details = db.get_yesterday_update_info()

    if details:
        # 自动化测试小组
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=3b7984b7e91b467ba0912503125f93cc'

        # 会计交流群
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=1a14311dc0114555803e88ac82a9bdb5'

        # 管家会计全国第一
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=8499063b73d041c0a11cdd89bddf64f3'

        # 账无忧识别服务问题反馈群
        # url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=0c50a2bc8b6c4f0780ce935193e99d00'

        # 账无忧代账平台研发支持
        url = 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=e4ea74eebf374cb0bf8487e039c830f7'

        data = {
            'content': f'【银行对账单PDF识别服务】{datetime.date.today().strftime("%Y-%m-%d")}更新：\n{details[0][0]}',
        }

        requests.post(url, json=data)
