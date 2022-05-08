from pickle import TRUE
import mariadb
import sys

class connection():
    def __init__(self):
        '''
            Initialiser for connector
            will return the cursor object but unlikely thats 
            what you actually want
        '''
        try:
            conn = mariadb.connect(
                user="realestate",
                password="realestatepass",
                host="localhost",
                port=3306,
                database="realestate"

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
        self.cursor = conn.cursor(dictionary=True)
        self.conn = conn

    def dict_select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_select(self, sql):
        self.cursor.execute(sql)

    def insert_suburb(self, suburb):
        sql = "INSERT INTO realestate.SUBURB (SUBURB_NAME) VALUES ('" + suburb + "')"
        print(sql)
        self.cursor.execute(sql,suburb)
        self.conn.commit()


    def get_houses(self):
        sql =   '''
                    SELECT * FROM HOUSES
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

