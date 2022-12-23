import os
from dotenv import load_dotenv 
import snowflake.connector

load_dotenv()


conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DB_NAME'),
    schema=os.getenv('SNOWFLAKE_SCHEMA_NAME'),
    session_parameters={
        'QUERY_TAG': 'snow-test',
    }
)

conn.cursor().execute("ALTER SESSION SET QUERY_TAG = 'snow-test'")

# Creating the database 
# Link - https://docs.snowflake.com/en/user-guide/python-connector-example.html#creating-a-database-schema-and-warehouse
conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
conn.cursor().execute("USE DATABASE testdb_mg")
conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")

# Using the database
# Link - https://docs.snowflake.com/en/user-guide/python-connector-example.html#using-the-database-schema-and-warehouse
conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
conn.cursor().execute("USE DATABASE testdb_mg")
conn.cursor().execute("USE SCHEMA testdb_mg.testschema_mg")

