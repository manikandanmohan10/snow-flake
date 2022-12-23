#!/usr/bin/env python
import os
import snowflake.connector
from dotenv import load_dotenv
load_dotenv()

# Gets the version
ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT')
    # user = 'Manikandan10',
    # password = 'Softsuave@123',
    # # account = 'NI51874',
    # account = 'hm85009.central-india.azure'
    )

cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()