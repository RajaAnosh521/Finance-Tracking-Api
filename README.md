🌟 Finance Tracker API 🚀

📊 Manage your finances smartly! The Finance Tracker API helps you track expenses, income, and crypto holdings with ease.
Built with Django & Django REST Framework (DRF), it provides a secure, scalable, and efficient financial tracking system with JWT authentication.

📜 API Documentation 📝

🔗 Explore API Documentation: API Docs

🌍 Base URL: http://127.0.0.1:8001/api/api

⚠️ Note: All endpoints are prefixed with api/.

✨ Features 🌟

🔒 JWT Authentication – Secure login, logout, and registration.
📂 Category Management – Create, read, update, and delete financial categories.
💰 Transaction Management – Track income & expenses with CRUD operations.
📑 Swagger/OpenAPI Docs – Interactive API documentation for easy testing.

🚀 Endpoints 🌐

🔐 Authentication (user_auth)

✅ Register a new user:
POST /api/user_auth/register/
🔹 Endpoint: user_auth_register_create

✅ User Login (JWT Token):
POST /api/user_auth/login/
🔹 Endpoint: user_auth_login_create

✅ User Logout:
POST /api/user_auth/logout/
🔹 Endpoint: user_auth_logout_create

📂 Categories (tracker)

📋 List all categories:
GET /api/tracker/category/
🔹 Endpoint: tracker_category_list

➕ Create a new category:
POST /api/tracker/category/
🔹 Endpoint: tracker_category_create

🔍 Retrieve a specific category:
GET /api/tracker/category/{id}/
🔹 Endpoint: tracker_category_read

✏️ Update a category:
PUT /api/tracker/category/{id}/
🔹 Endpoint: tracker_category_update

🛠 Partially update a category:
PATCH /api/tracker/category/{id}/
🔹 Endpoint: tracker_category_partial_update

🗑 Delete a category:
DELETE /api/tracker/category/{id}/
🔹 Endpoint: tracker_category_delete

💰 Transactions (tracker)

📊 List all transactions:
GET /api/tracker/transaction/
🔹 Endpoint: tracker_transaction_list

➕ Create a new transaction:
POST /api/tracker/transaction/
🔹 Endpoint: tracker_transaction_create

🔍 Retrieve a transaction:
GET /api/tracker/transaction/{id}/
🔹 Endpoint: tracker_transaction_read

✏️ Update a transaction:
PUT /api/tracker/transaction/{id}/
🔹 Endpoint: tracker_transaction_update

🛠 Partially update a transaction:
PATCH /api/tracker/transaction/{id}/
🔹 Endpoint: tracker_transaction_partial_update

🗑 Delete a transaction:
DELETE /api/tracker/transaction/{id}/
🔹 Endpoint: tracker_transaction_delete

⚙️ Setup Instructions 🛠
📥 1. Clone the Repository

    git clone https://github.com/RajaAnosh521/Finance-Tracking-Api.git
    cd finance-tracker

🏗 2. Create a Virtual Environment & Install Dependencies

    python -m venv .venv
    pip install -r requirements.txt

🛠 3. Run Migrations

    py manage.py makemigrations
    py manage.py migrate

🚀 4. Run the API Server

    py manage.py runserver 8001

📑 5. Access the API Documentation

Open your browser and go to:
   
   🔗 API Documentation

📢 Additional Information 🛡

📜 Terms of Service: Refer to the API documentation or contact the developer.
📧 Contact the Developer: ✉️ rajaanosh521@gmail.com
🛡 License: BSD License