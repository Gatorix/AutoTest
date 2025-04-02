import datetime

from utils.db_utils import ConnectDB
import requests

if __name__ == '__main__':
    db = ConnectDB()
    details = db.get_yesterday_update_info()

    if details:

        url = ""

        data = {
            'content': f'【银行对账单PDF识别服务】{datetime.date.today().strftime("%Y-%m-%d")}更新：\n{details[0][0]}',
        }

        requests.post(url, json=data)
