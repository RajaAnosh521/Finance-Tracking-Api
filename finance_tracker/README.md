Finance Tracker API:

Finance Tracker API helps you maintain financial control by tracking your expenses, income, and crypto holdings. It is built with Django and Django Rest Framework (DRF) and provides a robust, RESTful interface along with JWT-based user authentication.

API Documentation:

Explore API Documentation:

http://127.0.0.1:8001/?format=openapi

Base URL:

http://127.0.0.1:8001/api/api

Note: All endpoints are prefixed with api/.

Features:

JWT Authentication:

Secure endpoints with login, logout, and registration.

Category Management:

Create, read, update, and delete financial categories.

Transaction Management:

Track income and expenses with CRUD operations.

Swagger/OpenAPI Documentation:

Interactive documentation for easy exploration of API endpoints.

Endpoints:

Authentication (user_auth):

Register a new user:
POST /api/user_auth/register/
Endpoint Name: user_auth_register_create

User Login (JWT token):
POST /api/user_auth/login/
Endpoint Name: user_auth_login_create

User Logout:
POST /api/user_auth/logout/
Endpoint Name: user_auth_logout_create

Categories (tracker)
List all categories:
GET /api/tracker/category/
Endpoint Name: tracker_category_list

Create a new category:
POST /api/tracker/category/
Endpoint Name: tracker_category_create

Retrieve a specific category:
GET /api/tracker/category/{id}/
Endpoint Name: tracker_category_read

Update a specific category:
PUT /api/tracker/category/{id}/
Endpoint Name: tracker_category_update

Partial update a specific category:
PATCH /api/tracker/category/{id}/
Endpoint Name: tracker_category_partial_update

Delete a specific category:
DELETE /api/tracker/category/{id}/
Endpoint Name: tracker_category_delete

Transactions (tracker)
List all transactions:
GET /api/tracker/transaction/
Endpoint Name: tracker_transaction_list

Create a new transaction:
POST /api/tracker/transaction/
Endpoint Name: tracker_transaction_create

Retrieve a specific transaction:
GET /api/tracker/transaction/{id}/
Endpoint Name: tracker_transaction_read

Update a specific transaction:
PUT /api/tracker/transaction/{id}/
Endpoint Name: tracker_transaction_update

Partial update a specific transaction:
PATCH /api/tracker/transaction/{id}/
Endpoint Name: tracker_transaction_partial_update

Delete a specific transaction:
DELETE /api/tracker/transaction/{id}/
Endpoint Name: tracker_transaction_delete

Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/RajaAnosh521/Personal-Finance-Tracking-Api.git
cd finance-tracker
2. Create a Virtual Environment and Install Dependencies
bash
Copy
Edit
python -m venv .venv
pip install -r requirements.txt
3. Run Migrations
bash
Copy
Edit
py manage.py makemigrations
py manage.py migrate
4. Run the API Server
bash
Copy
Edit
py manage.py runserver 8001
5. Access the API Documentation
Open your browser and navigate to:
http://127.0.0.1:8001/?format=openapi
You can also explore the Swagger UI for interactive API testing.

Additional Information
Terms of Service:
Refer to the API documentation or contact the developer for details.
Contact the Developer:
[Insert Contact Information]
License:
BSD License
