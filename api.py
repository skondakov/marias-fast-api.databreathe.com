from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.db import db
from src.logger import logger

# Build the base FastAPI app class
app = FastAPI()

@app.get("/ping")
async def ping() -> dict:
    """ To be used to test service availability """

    return {"response": "pong"}

@app.get("/customers/birthday")
async def get_customers_birthday() -> dict:
    """ Retrieves a list of clients that have their birthdays today """

    # Get db instance and build a cursor to perform the SQL query
    db_conn = db()
    cursor = db_conn.cursor()

    logger.debug('Connect to the database and retrieve a cursor')

    # Execute the SQL Query
    try:
        cursor.execute(
            "SELECT id, `name` "
            "FROM customer "
            "WHERE (MONTH(birthdate) = MONTH(NOW())) AND (DAY(birthdate) = DAY(NOW()))"
        )
    except Exception as e:
      logger.error(f"Failed to execute SQL query with error: {e}")

    logger.debug('Execute the database query and start retrieving results')

    # Build the response object
    response = {'customers': []}
    for (id, name) in cursor:
        logger.debug(f'Add response object for customwr with id: {id}')
        response['customers'].append({
            'customer_id': id,
            'customer_first_name': name
        })

    # Close the database cursor to free up resources & connectons
    cursor.close()
    logger.debug('Close the database connection')

    # Return a dict response which will be con verted into a JSON
    return response

@app.get("/products/top-selling-products/{year}")
async def get_top_selling_products(year: int) -> dict:
    """ Retrieves a list of clients that have their birthdays today """

    # Get db instance and build a cursor to perform the SQL query
    db_conn = db()
    cursor = db_conn.cursor()

    logger.debug('Connect to the database and retrieve a cursor')

    query = "SELECT p.`name` AS product_name, SUM(s.quantity) AS total_sales " \
        "FROM sale AS s JOIN product AS p ON s.product_id = p.id " \
        "WHERE YEAR(`date`) = %s " \
        "GROUP BY s.product_id " \
        "ORDER BY total_sales DESC " \
        "LIMIT 10"

    query_params = (year, )

    logger.debug('Build the SQL query and prepare the params')

    # Execute the SQL Query
    # Execute the SQL Query
    try:
        cursor.execute(query, query_params)
    except Exception as e:
      logger.error(f"Failed to execute SQL query with error: {e}")

    logger.debug('Execute the database query and start retrieving results')

    # Build the response object
    response = {'products': []}
    for (product_name, total_sales) in cursor:
        logger.debug(f'Add response object for product "{product_name}"')
        response['products'].append({
            'product_name': product_name,
            'total_sales': total_sales
        })

    # Close the database cursor to free up resources & connectons
    cursor.close()
    logger.debug('Close the database connection')

    # Return a dict response which will be con verted into a JSON
    return response

@app.get("/customers/last-order-per-customer")
async def get_last_order_per_customer() -> dict:
    """ Retrieves a list of all customers with their emails and last order dates """

    # Get db instance and build a cursor to perform the SQL query
    db_conn = db()
    cursor = db_conn.cursor()

    logger.debug('Connect to the database and retrieve a cursor')

    # Execute the SQL Query
    try:
        cursor.execute(
            "SELECT c.id, c.email, MAX(s.`date`) AS last_order_date "
            "FROM customer AS c JOIN sale AS s ON s.customer_id = c.id "
            "GROUP BY c.id"
        )
    except Exception as e:
      logger.error(f"Failed to execute SQL query with error: {e}")

    logger.debug('Execute the database query and start retrieving results')

    # Build the response object
    response = {'customers': []}
    for (id, email, last_order_date) in cursor:
        logger.debug(f'Add response object for customwr with id: {id}')
        response['customers'].append({
            'customer_id': id,
            'customer_email': email,
            'last_order_date': last_order_date
        })

    # Close the database cursor to free up resources & connectons
    cursor.close()
    logger.debug('Close the database connection')

    # Return a dict response which will be con verted into a JSON
    return response
