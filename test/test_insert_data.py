
# products = [
#     (1, "Mountain Bike Pro", 1200, 800, 1, "2024-01-01", None, 1),
#     (2, "Road Bike Elite", 1500, 1000, 1, "2024-01-01", None, 1),
#     (3, "Hybrid Bike Classic", 1100, 700, 1, "2024-01-01", None, 1),
#     (4, "Electric Bike Power", 2200, 1800, 1, "2024-01-01", None, 1),
#     (5, "Kids Bike Fun", 300, 200, 1, "2024-01-01", None, 1),
#     (6, "BMX Bike Stunt", 450, 300, 1, "2024-01-01", None, 1),
#     (7, "Touring Bike Journey", 1300, 900, 1, "2024-01-01", None, 1),
#     (8, "Folding Bike Compact", 800, 600, 1, "2024-01-01", None, 1),
#     (9, "Cruiser Bike Relax", 500, 350, 1, "2024-01-01", None, 1),
#     (10, "Cargo Bike Load", 1400, 1000, 1, "2024-01-01", None, 1),
#     (11, "Speed Bike Flash", 1600, 1200, 1, "2024-01-01", None, 1),
#     (12, "City Bike Commute", 850, 650, 1, "2024-01-01", None, 1),
#     (13, "Off-Road Bike Adventure", 1800, 1400, 1, "2024-01-01", None, 1),
#     (14, "Racing Bike Sprint", 1900, 1500, 1, "2024-01-01", None, 1),
#     (15, "Tourist Bike Explorer", 1000, 750, 1, "2024-01-01", None, 1),
# ]



# def test_create_and_insert_customers(db_cursor, db_connection):
#     # Create table
#     create_table_query = """CREATE TABLE IF NOT EXISTS products_base (
#     product_id INT PRIMARY KEY,
#     product_name VARCHAR(255),
#     retail_price DECIMAL(10, 2),
#     wholesale_price DECIMAL(10, 2),
#     is_current TINYINT,
#     effective_date DATE,
#     end_date DATE,
#     version INT);"""
#     db_cursor.execute(create_table_query)

#     # Insert customer data
#     insert_query = """
#     INSERT INTO products_base (product_id, product_name, retail_price, wholesale_price, is_current, effective_date, end_date, version)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#     """
#     db_cursor.executemany(insert_query, products)

#     # Commit the changes using the connection object
#     db_connection.commit()

