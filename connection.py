import pymysql


class Connection:
    def __init__(self):
        try:
            host = 'localhost'
            root = 'root'
            password = 'swzipilwV1'
            database = 'usuario'
            self.cnx = pymysql.connect(host=host,
                                       user=root,
                                       password=password,
                                       database=database)
            self.cursor = self.cnx.cursor()
        except pymysql.connector.Error as exception:
            raise exception
