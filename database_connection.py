from pickle import NONE
import mariadb as mariadb_connector
import os
from dotenv import load_dotenv

load_dotenv()

class MariaDBDatabase:
    
    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USERNAME")
        self._passwd = os.getenv("PASSWD")
        self._database = os.getenv("DATABASE")
        self.conn = self._connecting()
    
    def _connecting(self):
        return mariadb_connector.connect(
            host=self._host,
            user=self._username,
            password=self._passwd,           
            database=self._database

        )