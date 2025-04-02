import datetime
import sqlite3
import time

from utils.file_utils import get_project_path


class ConnectDB:
    def __init__(self, db_path=rf'{get_project_path()}\db\zwy_files.db'):
        self.__cur = sqlite3.connect(db_path).cursor()

    def query_link_by_id(self, link_id):
        res = self.__cur.execute(
            f'SELECT Links from AccountingBankFiles abf WHERE ID = {link_id} AND is_skip ISNULL')
        return res.fetchall()[0][0]

    def query_bank_pdf_password(self, link_id):
        res = self.__cur.execute(
            f'SELECT password from AccountingBankFiles abf WHERE ID = {link_id} AND is_skip ISNULL')
        return res.fetchall()[0][0]

    def query_all_pdf_links(self):
        res = self.__cur.execute(
            f'SELECT ID, name, Links from AccountingBankFiles WHERE is_skip ISNULL'
        )
        return res.fetchall()

    def query_all_id_with_password(self):
        res = self.__cur.execute(
            'SELECT ID from AccountingBankFiles WHERE is_skip ISNULL and Password IS NOT NULL'
        )
        result = []
        for _ in res.fetchall():
            result.append(_[0])
        return result

    def query_expected_data_by_id(self, link_id):
        res = self.__cur.execute(
            f'SELECT Expected_Total_Line, Expected_Income, Expected_Expenditures from AccountingBankFiles WHERE ID = {link_id}'
        )
        return res.fetchall()[0]

    def is_password_exist_by_id(self, link_id):
        res = self.__cur.execute(
            f'select password from AccountingBankFiles abf where id={link_id}'
        )
        return res.fetchall()[0][0] is not None

    def execute_sql(self, sql):
        res = self.__cur.execute(sql)
        return res.fetchall()

    def get_yesterday_update_info(self):
        time_array = datetime.datetime.strptime(
            str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")),
            "%Y-%m-%d"
        )
        timestamp = int(time.mktime(time_array.timetuple()) * 1000.0 + time_array.microsecond / 1000.0)

        res = self.__cur.execute(f'SELECT info from BankNotices bn where createDate = {timestamp + 28800000};')
        return res.fetchall()


# if __name__ == '__main__':
#     db = ConnectDB()
#     i = db.get_yesterday_update_info()
#     print(i)
