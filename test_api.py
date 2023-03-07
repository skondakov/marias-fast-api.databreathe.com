""" Maria's Web Service Unit Tests (Databreathe Backend Coding Challange)

 The unit testing of the API app for Maria's Web Service

"""

from fastapi.testclient import TestClient
from api import app
import re

# This is the test client object that will test the app
client = TestClient(app)


def test_ping() -> None:
    """ Test the ping endpoint """

    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "response": "pong"
    }

def test_get_customers_birthday() -> None:
    """ Test get customers birthdays endpoint """

    response = client.get("/customers/birthday")

    # Check for a valid response code
    assert response.status_code == 200

    # Convert the response to JSON and store in a variable for more assertions
    response_json = response.json()

    # Check if the main data key is available
    assert "customers" in response_json

    # If there is any data available, check for all keys availability, data types and values
    for customer in response_json["customers"]:

        assert "customer_id" in customer
        assert isinstance(customer["customer_id"], int)
        assert customer["customer_id"] > 0

        assert "customer_first_name" in customer
        assert isinstance(customer["customer_first_name"], str)
        assert len(customer["customer_first_name"]) > 0

def test_get_top_selling_products() -> None:
    """ Test get top selling products endpoint """

    # First do some tests with empty data
    response = client.get("/products/top-selling-products/2018")

    # Check for a valid response code
    assert response.status_code == 200

    # Convert the response to JSON and store in a variable for more assertions
    response_json = response.json()

    # Check if the main data key is available
    assert "products" in response_json
    assert len(response_json["products"]) == 0

    # Then tets with a year that we know we have data for
    response = client.get("/products/top-selling-products/2019")

    # Check for a valid response code
    assert response.status_code == 200

    # Convert the response to JSON and store in a variable for more assertions
    response_json = response.json()

    # Check if the main data key is available
    assert "products" in response_json
    assert len(response_json["products"]) > 0

    # If there is any data available, check for all keys availability, data types and values
    for product in response_json["products"]:

        assert "total_sales" in product
        assert isinstance(product["total_sales"], int)
        assert product["total_sales"] > 0

        assert "product_name" in product
        assert isinstance(product["product_name"], str)
        assert len(product["product_name"]) > 0

def test_get_last_order_per_customer() -> None:
    """ Test get last order per custoemr endpoint """

    response = client.get("/customers/last-order-per-customer")

    # Check for a valid response code
    assert response.status_code == 200

    # Convert the response to JSON and store in a variable for more assertions
    response_json = response.json()

    # Check if the main data key is available and if there are custoemrs available
    assert "customers" in response_json
    assert len(response_json["customers"]) > 0

    # If there is any data available, check for all keys availability, data types and values
    for customer in response_json["customers"]:

        assert "customer_id" in customer
        assert isinstance(customer["customer_id"], int)
        assert customer["customer_id"] > 0

        assert "customer_email" in customer
        assert isinstance(customer["customer_email"], str)
        assert len(customer["customer_email"]) > 0

        assert "last_order_date" in customer
        assert isinstance(customer["last_order_date"], str)
        assert re.search("^[1,2][0-9]{3}-[0,1][1-9]-[0,1,2,3][0-9]$", customer["last_order_date"])