# This script holds the DB access module <

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_config = {
  'user': os.getenv('MARIAS_FAST_API_DB_USER'),
  'password': os.getenv('MARIAS_FAST_API_DB_USER_PASSWORD'),
  'host': os.getenv('MARIAS_FAST_API_DB_HOST'),
  'port': os.getenv('MARIAS_FAST_API_DB_PORT'),
  'database': os.getenv('MARIAS_FAST_API_DB_NAME'),
  'raise_on_warnings': True
}


def db():
    return mysql.connector.connect(**db_config)