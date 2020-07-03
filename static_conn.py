from typing import Tuple

from pymysql import connect, err as mysql_err
from datetime import datetime, timedelta


class StaticConnect(object):

    def __init__(self, host: Tuple[str, int], user: str, password: str,
                 db_name: str, cert_path: str = None) -> None:
        """Init of StaticConnect

        Arguments:
            host: Database host and port.
            user: User to access database.
            password: Password to access database.
            db_name: Name of database.
            cert_path: Path to cert file.
        """
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db_name = db_name
        self.__cert_path = cert_path
        # self.__cert_path = '/etc/nginx/new_ssl/gd_bundle-g2-g1.crt'
        self.__connection = None

    def _create_connection(self, charset: str = 'utf8'):
        if self.__cert_path is None:
            connection = connect(
                host=self.__host[0], port=self.__host[1], user=self.__user,
                passwd=self.__password, db=self.__db_name, charset=charset)
        else:
            connection = connect(
                host=self.__host[0], port=self.__host[1], user=self.__user,
                passwd=self.__password, db=self.__db_name,
                ssl={'ssl': {'ca': self.__cert_path}}, charset=charset)
        if connection is None or connection.open is False:
            raise Exception("Create Connection error")
        self.__create_ts = datetime.now()
        return connection

    def get_connection(self):
        if (
            self.__connection is None or self.__connection.open is False or
            self.__create_ts is None or
            datetime.now() - self.__create_ts > timedelta(minutes=2)
           ):
            self.__create_ts = datetime.now()
            self.disconnect()
            self.__connection = self._create_connection()
        return self.__connection

    def disconnect(self) -> None:
        if self.__connection is not None:
            print("disconnected")
            try:
                self.__connection.close()
            except mysql_err.InternalError:
                print("connection already closed")
            except Exception as e:
                print(e)

    def reconnect(self) -> None:
        self.disconnect()
        self.__connection = self._create_connection()
        return self.__connection

    def getConnection(self) -> None:
        return self.get_connection()

    def _createConnection(self) -> None:
        return self._create_connection()

    def disconnection(self) -> None:
        return self.disconnect()

    def reconnection(self) -> None:
        return self.reconnect()
