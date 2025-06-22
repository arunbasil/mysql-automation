import pyodbc
import configparser
import os

def create_db_connection():
    config = configparser.ConfigParser()
    # Assuming config.ini is in the 'config' directory, one level above the 'db' directory
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')

    if not os.path.exists(config_path):
        print(f"Error: Configuration file not found at {config_path}")
        return None

    config.read(config_path)
    
    try:
        db_driver = config['database']['DRIVER']
        db_server = config['database']['SERVER']
        db_name = config['database']['DATABASE']
        db_user = config['database']['UID']
        db_password = config['database']['PWD']
    except KeyError as e:
        print(f"Error: Missing configuration key: {e} in {config_path}")
        return None

    conn_str = (
        f"DRIVER={db_driver};"
        f"SERVER={db_server};"
        f"DATABASE={db_name};"
        f"UID={db_user};"
        f"PWD={db_password};"
        f"TrustServerCertificate=yes;"  # Often needed for local Docker instances
    )
    
    try:
        connection = pyodbc.connect(conn_str)
        return connection
    except pyodbc.Error as e:
        print(f"Error while connecting to SQL Server: {e}")
        # print(f"Connection string used: DRIVER=...;SERVER={db_server};DATABASE={db_name};UID={db_user};PWD=...") # Avoid logging full PWD
        print(f"Connection string used (credentials redacted): DRIVER={{...}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={{...}}")
        return None

