import db.connection as connection
from mysql.connector import Error
import datetime

def insert_data(connection, id, datetime, name):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO test_table_ann (id, datetime, name) VALUES (%s, %s, %s)"
        data_to_insert = (id, datetime, name)
        cursor.execute(insert_query, data_to_insert)
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error while inserting data: {e}")
    finally:
        if cursor:
            cursor.close()


def query_data(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as e:
        print(f"Error while querying data: {e}")
        return None
    finally:
        cursor.close()


    select_query = "SELECT column1, column2 FROM my_table"
    records = query_data(connection, select_query)
    if records:
        for row in records:
            print(f"column1: {row[0]}, column2: {row[1]}")

    connection.close()