# Finance Tracker API

A RESTful API for managing personal finances, built with Django and Django Rest Framework (DRF). The API supports user authentication (JWT), CRUD operations for categories and transactions, and is documented using Swagger.

## Note: 
   " That all the endpoints are prefixed by api/ "

## Features
- **JWT Authentication**: Secure login, logout, and token refresh.
- **Category Management**: Create, read, update, and delete financial categories.
- **Transaction Management**: Track income and expenses with categories.
- **Swagger Documentation**: Easy-to-use API reference.

## Endpoints

### Authentication
- `POST /user_auth/register/`: Register a new user.
- `POST /user_auth/login/`: Obtain a JWT token.
- `POST /user_auth/logout/`: Logout and invalidate the token.

### Categories
- `GET /main_app/category/`: List all categories.
- `POST /main_app/category/`: Create a new category.
- `PUT /main_app/category/<id>/`: Update an existing category.
- `DELETE /main_app/category/<id>/`: Delete a category.

### Transactions
- `GET /main_app/transaction/`: List all transactions.
- `POST /main_app/transaction/`: Create a new transaction.
- `PUT /main_app/transaction/<id>/`: Update an existing transaction.
- `DELETE /main_app/transaction/<id>/`: Delete a transaction.

## Setup Instructions
## Clone the repository:  
   
      git clone https://github.com/RajaAnosh521/Personal-Finance-Tracking-Api.git
      cd finance-tracker

##. Create Virtual Environment and install all libraries:

      python -m venv .venv
      pip install -r requirements.txt

## Run all Migrations:
   
      py manage.py makemigrations
      py manage.py migrate

## Run the API:
   
      py manage.py runserver
   
### Documentation
      http://127.0.0.1:8000/api/docs/