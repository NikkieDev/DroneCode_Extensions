import mysql.connector

def db_connect(host, username, password, db=None):
    if db is None:
        try:
            database = mysql.connector.connect(host=host, username=username, password=password)
            print("Successfully connected to MySQL without database.")
        except mysql.connector.Error as err:
            print(f"An error occured: {err}")
            
    elif db is not None:
        try:
            database = mysql.connector.connect(host=host, username=username, password=password, database=db)
            print(f"Successfully connected to MySQL at {db}")

        except mysql.connector.Error as err:
            print(f"An error occured: {err}")

    return database

def cursor_create(database_cursor):
    cursor = database_cursor.cursor()

    return cursor

def db_close(database):
    database.close()
    return print("Closed connection to database")

def cursor_close(cursor):
    cursor.close()
    return print("Closed cursor between client and database")


############################
# MADE                     #
# BY                       #
# NikkieDev Software       #
# https://nikkiedev.com    #
############################