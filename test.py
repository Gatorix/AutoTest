import datetime
import time

import requests

from page.api.accounting.page_api_download import PageApiDownload
from utils.db_utils import ConnectDB
from utils.file_utils import get_project_path

#
# con = ConnectDB()
# res = con.query_bank_pdf_links('SELECT * FROM AccountingBankFiles')
#
# res = requests.get(
#     'https://ks3-cn-shanghai.ksyun.com/prodzwy/ebook/9400000687555/ca5570f4-e70a-4f7c-99b2-071ddf8087d3.pdf')
#
#
# def get_file():
#     with open(rf'{get_project_path()}\download_tmp\ca5570f4-e70a-4f7c-99b2-071ddf8087d3.pdf', 'wb') as download_file:
#         for bl in res.iter_content(chunk_size=1024):
#             if all([
#                 bl,
#                 '"status":402' not in str(bl),
#                 '502 Bad Gateway' not in str(bl)
#             ]):
#                 download_file.write(bl)
#             else:
#                 raise Exception(f'下载失败: {bl.decode("utf-8")}')
#
#
#
# print(file)

# db = ConnectDB()
# pdf_dict = db.query_bank_pdf_links('')
# id_list = list(pdf_dict.keys())
#
# pad = PageApiDownload()
# for i, v in enumerate(id_list):
#     pad.page_api_download(
#         pdf_dict[v],
#         path=r'E:\autotest\template\accounting\smart_bookkeeping\bank_pdf',
#         specific_filename=f'{v}.pdf'
#     )

# db = ConnectDB()
# pdf_dict = db.query_bank_pdf_links('')

# test_fixture_usage.py

import pytest
from utils.db_utils import ConnectDB


# @pytest.fixture(params=['hello', 'Testing'], autouse=True, ids=['test1', 'test2'], name='test')
# def my_method(request):
#     print(request.param)
#
#
# def test_use_fixtures_01():
#     print('this is the first test')
#
#
# def test_use_fixtures_02():
# #     print('this is the second test')
# db = ConnectDB()
#
#
# @pytest.mark.parametrize('link_id,name,link', db.query_all_pdf_links())
# def test_all_bank_case(link_id, name, link):
#     print(link_id, name, link)

def now_to_date(format_string="%Y-%m-%d"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


if __name__ == '__main__':

    date = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=int(1720396800000) / 1000)
    print(date.strftime('%Y-%m-%d'))

    print(datetime.date.today() + datetime.timedelta(days=-1))

    time_array = datetime.datetime.strptime(
        str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")),
        # str((datetime.date.today()).strftime("%Y-%m-%d")),
        "%Y-%m-%d"
    )
    timestamp = int(time.mktime(time_array.timetuple()) * 1000.0 + time_array.microsecond / 1000.0)

    print(timestamp+28800000)
    print(1720396800000)

    # print('*'*5)
    # specified_time = datetime.datetime(2024, 7, 8, 12, 0, 0)
    # specified_timestamp = specified_time.timestamp()
    # print(specified_timestamp)
    # print(1720396800000-1720368000000)