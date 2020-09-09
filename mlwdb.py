# encoding: utf-8
from typing import Tuple
from json import dumps, loads
from datetime import datetime
from pymysql.err import OperationalError

from static_conn import StaticConnect

import config

static_connection = StaticConnect(
        (config.database_url, 3306), config.database_account, config.database_password, config.database_db, None)

# static_connection = StaticConnect(
#         (config.database_url, 3306), config.database_account, config.database_password, config.database_db, 2)

class databs:
    def __init__(self):
        self.__db_name = config.database_db
        self.static_connection = static_connection
        self.connection = self.static_connection.get_connection()

    def converter(self, obj):
        if isinstance(obj, datetime):
            return str(obj).replace('-', '/')

    def fatch(self, sql, params=None):
        return self.fetch(sql=sql, params=params)

    def fetch(self, sql, params=None):
        try:
            with self.connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(sql, params)
                else:
                    cursor.execute(sql)
                return cursor.fetchall()
        except OperationalError as oe:
            self.connection = self.static_connection.reconnect()
            raise oe

    def commit(self, sql, params=None, retry=0):
        try:
            with self.connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(sql, params)
                else:
                    cursor.execute(sql)
                self.connection.commit()
                return cursor.lastrowid
        except OperationalError as oe:
            self.connection = self.static_connection.reconnect()
            raise oe

    def commit_and_return_affected_rows(self, sql, params=None, retry=0):
        try:
            with self.connection.cursor() as cursor:
                if params is not None:
                    return cursor.execute(sql, params)
                else:
                    return cursor.execute(sql)
        except OperationalError as oe:
            self.connection = self.static_connection.reconnect()
            raise oe

    def type_switch(self, argument):
        return {
            'int': 'text',
            'varchar': 'text',
            'timestamp': 'combodate'
        }.get(argument, argument)

    def tableInfo(self, tableName):
        # look old one and do it
        return self.table_info(table_name=tableName)

    def table_info(self, table_name):
        query_cmd = (
            "SELECT COLUMN_NAME, IS_NULLABLE, DATA_TYPE,"
            "CHARACTER_MAXIMUM_LENGTH , COLUMN_COMMENT "
            "FROM information_schema.columns "
            "WHERE table_name = %s AND TABLE_SCHEMA = %s"
        )
        results = self.fetch(sql=query_cmd,
                             params=[table_name, self.__db_name])
        for row in results:
            row[2] = self.type_switch(argument=row[2])
            if row[0] == 'ann_cate_id' or row[0] == 'enable':
                row[2] = 'select'
            if row[3] > 20:
                row[2] = 'textarea'
        return results

    def tableFetch(self, tableName):
        return self.table_fetch(table_name=tableName)

    def table_fetch(self, table_name):
        return self.fetch(sql="SELECT * FROM `%s` LIMIT 30", params=[table_name])
