import mysql.connector
import configparser
import os

def create_db_connection():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
    config.read(config_path)
    
    db_host = config['database']['DB_HOST']
    db_name = config['database']['DB_NAME']
    db_user = config['database']['DB_USER']
    db_password = config['database']['DB_PASSWORD']
    
    try:
        connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

