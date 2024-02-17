## Product Management API

This README provides an overview of the code provided for a Django-based Product Management API. The code includes serializers, views, signals, models, and URL mappings for handling product-related operations.

### Code Explanation

#### `serializers.py`
- This file defines a serializer class named `ProductSerializer` using Django Rest Framework.
- The serializer specifies the model to be serialized (`Product`) and the fields to include in the serialization.

#### `views.py`
- The `product_list` function handles both GET and POST requests for the `/products/` endpoint.
  - For GET requests, it retrieves all products from the database, serializes them using `ProductSerializer`, and returns the data as JSON.
  - For POST requests, it parses the incoming JSON data, validates it using the serializer, saves the new product, and returns the serialized product data if successful.
- The `products_dummy` function returns a dummy list of products as JSON. This is used for testing purposes.

#### `signals.py`
- This file defines a signal handler function `update_created_at`.
- This function is triggered whenever a new `Product` instance is saved.
- It updates the `created_at` field of the product to the current datetime.

#### `models.py`
- Defines the `Product` model with fields for `title`, `description`, `price`, and `created_at`.

#### `urls.py`
- Maps URL patterns to the corresponding view functions.
- Defines endpoints for accessing product data (`/products/`) and dummy product data (`/products_dummy/`).

### Using Postman

1. **GET Request**: 
   - Open Postman and enter the URL for listing products: `http://localhost:8000/products/`.
   - Select the HTTP method as GET and click Send.
   - Postman will display the list of products retrieved from the API.

2. **POST Request**:
   - Set up a POST request in Postman with the URL `http://localhost:8000/products/`.
   - In the Body tab, select raw and JSON format.
   - Enter the product data in JSON format (e.g., `{ "title": "New Product", "description": "Description of the new product", "price": 25.99 }`).
   - Click Send to execute the POST request.
   - Postman will display the response with the newly created product data if successful.

### Note
- Before using Postman, ensure that the Django development server is running (`python manage.py runserver`).
- Adjust the URL (`http://localhost:8000/`) according to your local development server configuration.