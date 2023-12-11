from ast import Try
from database_connection import MariaDBDatabase

if __name__ == '__main__':
    print('Running')

    try: 
        db = MariaDBDatabase()
        print(f"Starting the connection...\nStatus: {db.conn.is_connected()}")
    except ConnectionError as err:
        raise f"Error during the connection. Message: {err}"
