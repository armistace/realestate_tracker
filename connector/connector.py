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
        self.cursor.execute(sql, suburb)
        self.conn.commit()

    def insert_ratings(self, rating_type):
        sql = "INSERT INTO realestate.RATING (RATING_TYPE) VALUES ('" + rating_type + "')"
        print(sql)
        self.cursor.execute(sql, rating_type)
        self.conn.commit()

    def insert_houses(self, houses):
        '''
            House is the only insert that expects the form_data
            var passed in its entirety, it will then call the keys 
            individually 
        '''
        insert_string = ""
        for item in houses:
            if item == 'ratings':
                id_query = self.get_id(True, houses[item])
                id = id_query[0]['ID']
                insert_string = insert_string + ',"' + str(id) + '"'
            elif item == 'suburbs':
                id_query = self.get_id(False, houses[item])
                id = id_query[0]['ID']
                insert_string = insert_string + ',"' + str(id) + '"'
            else:
                insert_string = insert_string + ',"' + str(houses[item]) + '"'
        # remove trailing comma
        insert_string=insert_string[1:]
        top_sql =   '''
                    INSERT INTO realestate.HOUSES (
                    OUR_ESTIMATED_PRICE,
                    OWNERS_EXPECTED_PRICE,
                    ACTUAL_SOLD_PRICE,
                    LAST_BOUGHT_PRICE,
                    YEARS_SINCE_LAST_BOUGHT,
                    LISTING_WEB_LINK,
                    BEDROOMS,
                    STUDY,
                    LIVING_AREAS,
                    POOL,
                    LAND_SIZE,
                    RATING_ID,
                    SUBURB_ID
                )
                VALUES (
                '''
        sql = top_sql + insert_string + ")"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()


    def get_houses(self):
        sql =   '''
                    SELECT * FROM HOUSES
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_ratings(self):
        sql =   '''
                    SELECT RATING_TYPE FROM RATING
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_subrubs(self):
        sql =   '''
                    SELECT SUBURB_NAME FROM SUBURB
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_id(self, rating_table_switch, filter):
        if rating_table_switch:
            table = "RATING"
            filter_column = "RATING_TYPE"
        else:
            table = 'SUBURB'
            filter_column = 'SUBURB_NAME'
        sql = 'SELECT ID FROM ' + table + ' WHERE ' + filter_column + ' = "' + filter + '"'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

