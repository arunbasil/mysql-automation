def test_compare_products_data(db_cursor):
    # get data from products
    db_cursor.execute("SELECT * FROM products")
    products_data = set(db_cursor.fetchall())

    # get data from products_base
    db_cursor.execute("SELECT * FROM products_base")
    products_base_data = set(db_cursor.fetchall())

    # Find differences
    differences = products_data.symmetric_difference(products_base_data)

    # Print differences
    if differences:
        print("Differences found:")
        for diff in differences:
            print(diff)
    else:
            print("No differences found")

    # Assert that there are no differences
    assert not differences, "Data in products and products_base tables are different"