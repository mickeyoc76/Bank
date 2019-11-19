#Test connection and get DB version
import sqlite3

try:
    sqliteConnection = sqlite3.connect('accounts.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")


#Create Table and columns

import sqlite3

try:
    sqliteConnection = sqlite3.connect('accounts.db')
    sqlite_create_table_query = '''CREATE TABLE customers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                balance INTEGER NOT NULL UNIQUE,
                                transaction_date datetime,
                                type TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")


#Insert Data

try:
    sqliteConnection = sqlite3.connect('accounts.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO `customers`
                          ('name', 'balance', 'transaction_date', 'type') 
                           VALUES 
                          ('Dan','7000','2019-03-19','Checking')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into accounts table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")



    # Get Data

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('accounts.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from customers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1]) 
            #print("balance: ", row[2])
            total = "balance: ", row[2]
            print(total[1])
            print("transaction_date: ", row[3])
            print("type: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()


#Update Data

def updateSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('accounts.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update customers set balance = 70000 where id = 2"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

updateSqliteTable()