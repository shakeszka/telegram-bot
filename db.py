import sqlite3
from sqlite3 import Error

def create_connection():
    global connection, cursor
    connection = None

    try:
        connection = sqlite3.connect("test.sqlite")
        print("Connection to SQLite DB successful")

        cursor = connection.cursor()
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_table():
    try:
        # connection.execute("""CREATE TABLE MATERIALS  (
        #     id INTEGER PRIMARY KEY,
        #     name TEXT,
        #     category TEXT,
        #     doc BLOB
        # )""")
        connection.execute("""CREATE TABLE MATERIALS  (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT)""")
    except Error as e:
        #print(f"The error '{e}' occurred")
        print("DB tables are already created. The connection is successful.")

    connection.commit()

def add_to_table(text, category):
    try:
        # cursor.execute(f"INSERT INTO MATERIALS(name, category, file) values('{text}', '{category}')")
        cursor.execute(f"INSERT INTO MATERIALS(name, category) values('{text}', '{category}')")
    except Error as e:
        print(f"The error '{e}' occurred")
    print("Successfully added to the table!")
    connection.commit()

def watch_table(filter):
    if filter == "all":
        try:
            cursor.execute("SELECT * FROM  SAT")
            result = cursor.fetchall()
            return result
        except:
            print("Something happened when watching table")

    elif filter == "sat_verbal":
        try:
            cursor.execute("SELECT * FROM  SAT WHERE category = 'sat_verbal' ")
            result = cursor.fetchall()
            return result
        except:
            print("Something happened when watching table")

    elif filter == "sat_math":
        try:
            cursor.execute("SELECT * FROM  SAT WHERE category = 'sat_math' ")
            result = cursor.fetchall()
            return result
        except:
            print("Something happened when watching table")

    connection.commit()
