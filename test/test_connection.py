import pyodbc

def test_connections(db_connection):
    # db_connection is now expected to be a pyodbc connection object
    assert db_connection is not None, "Database connection object should not be None"
    try:
        cursor = db_connection.cursor()
        assert cursor is not None, "Cursor object should not be None"
        print(f"Successfully connected to the SQL Server database and created a cursor.")
        # Optional: A simple query to ensure the connection is truly working
        cursor.execute("SELECT 1")
        row = cursor.fetchone()
        assert row[0] == 1, "Test query did not return expected result"
        print("Test query SELECT 1 executed successfully.")
        cursor.close()
    except pyodbc.Error as e:
        assert False, f"pyodbc.Error occurred: {e}"


# def test_query_test_table_ann(db_cursor):
#     # This test assumes a specific table 'test_table_ann' which may not exist
#     # in the AdventureWorks database. Commenting out for now.
#     query = "SELECT * FROM test_table_ann"
#     db_cursor.execute(query)
#     results = db_cursor.fetchall()
    
#     # Print the results
#     for row in results:
#         print(row)
    
#     # Include any assertions here
#     assert len(results) >= 0  # Example assertion
