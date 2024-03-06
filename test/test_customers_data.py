

def test_compare_customers_data(db_cursor):
    # Fetch data from customers
    db_cursor.execute("SELECT * FROM customer")
    customers_data = set(db_cursor.fetchall())

    # Fetch data from customers_base
    db_cursor.execute("SELECT * FROM customer_base")
    customers_base_data = set(db_cursor.fetchall())

    # Find differences
    differences = customers_data.symmetric_difference(customers_base_data)

    # Print differences
    if differences:
        print("Differences found:")
        for diff in differences:
            print(diff)

    # Assert that there are no differences
    assert not differences, "Data in customers and customers_base tables are different"
