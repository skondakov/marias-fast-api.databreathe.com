# This script holds the DB access module <

import os
import mysql.connector
from dotenv import load_dotenv
from src.logger import logger

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


def db():

    try:
        db = mysql.connector.connect(**db_config)
    except Exception as e:
      logger.error(f"Failed to connecto to MariaDB with exception: {e}")

    return db