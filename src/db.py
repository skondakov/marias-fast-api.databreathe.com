""" DB Access Wrapper

 This module holds the DB Access wrapper. This wrapper is used to access the App's database

"""

import os
import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection, MySQLConnection, CMySQLConnection
from dotenv import load_dotenv
from src.logger import logger
from typing import Union

def db() -> Union[PooledMySQLConnection, MySQLConnection, CMySQLConnection]:
    """ Opens a new connection to the database and returns it. Logs an error in case of issues"""

    # Load environment variables <
    load_dotenv()

    # Read config values from the env variables #
    db_config = {
        'user': os.getenv('MARIAS_FAST_API_DB_USER'),
        'password': os.getenv('MARIAS_FAST_API_DB_USER_PASSWORD'),
        'host': os.getenv('MARIAS_FAST_API_DB_HOST'),
        'port': os.getenv('MARIAS_FAST_API_DB_PORT'),
        'database': os.getenv('MARIAS_FAST_API_DB_NAME'),
        'raise_on_warnings': True
    }

    # Attempt to open a new connection to the database <
    try:
        db = mysql.connector.connect(**db_config)
    except Exception as e:
      logger.error(f"Failed to connecto to MariaDB with exception: {e}")
    else:
        logger.debug('Database connection created successfully')

    return db