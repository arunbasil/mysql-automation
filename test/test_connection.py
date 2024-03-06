

def test_connections(db_connection):
    # You can use db_connection directly in your test
    cursor = db_connection.cursor()
    if cursor:
        print(f"Connected to the MySQL database: {db_connection.get_server_info()}")


def test_query_test_table_ann(db_cursor):
    query = "SELECT * FROM test_table_ann"
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    
    # Print the results
    for row in results:
        print(row)
    
    # Include any assertions here
    assert len(results) >= 0  # Example assertion
