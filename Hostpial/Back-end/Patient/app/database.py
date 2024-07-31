# import snowflake.connector
# from contextlib import contextmanager

# # Remplacez ces valeurs par vos informations de connexion Snowflake
# USER = 'MOMATH92'
# PASSWORD = 'Rassoulle92'
# ACCOUNT = 'mtjxohy-wp28902'
# DATABASE = 'DATARCW'
# SCHEMA = 'PATIENTS'

# @contextmanager
# def get_snowflake_connection():
#     conn = snowflake.connector.connect(
#         user=USER,
#         password=PASSWORD,
#         account=ACCOUNT,
#         database=DATABASE,
#         schema=SCHEMA
#     )
#     try:
#         yield conn
#     finally:
#         conn.close()
import snowflake.connector
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = snowflake.connector.connect(
        user='MOMATH92',
        password='Rassoulle92',  # Remplacez par votre mot de passe
        account='mtjxohy-wp28902',
        warehouse='Databases',
        database='DATARCW',
        schema='PATIENTS'
    )
    try:
        yield conn
    finally:
        conn.close()

