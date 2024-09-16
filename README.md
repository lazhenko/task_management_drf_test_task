# Task Management API

A Django-based Task Management API with token-based authentication (JWT) and CRUD operations for tasks. The project uses Django REST Framework for API development and `djangorestframework-simplejwt` for JWT authentication.

## Features

- Token-based authentication using JWT
- Task creation, retrieval, updating, and deletion
- Filtering and pagination on task lists
- Unit tests for API methods

## Requirements

- Python 3.9+
- Django 4.0+
- Django REST Framework
- PostgreSQL or SQLite (SQLite is used by default)

## Setup Instructions

### 1. Clone the Repository

Clone the project repository from GitHub (or another source):

    git clone https://github.com/yourusername/task_management_drf_test_task.git
    cd task_management_drf_test_task

### 2. Set Up a Virtual Environment
Create and activate a virtual environment for the project:

# Create a virtual environment (Windows)
    python -m venv venv

# Activate the virtual environment (Windows)
    venv\Scripts\activate

# For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

### 3. Install Dependencies
Install all the project dependencies from the requirements.txt file:

    pip install -r requirements.txt

### 4. Apply Migrations
Apply the migrations to set up the database schema:

    python manage.py migrate

### 5. Create a Superuser (Optional)
Create a superuser account to access the Django Admin interface:

    python manage.py createsuperuser

### 6. Start the Development Server
Start the Django development server:

    python manage.py runserver

The project will be running at http://127.0.0.1:8000/.

### 7. API Endpoints
You can interact with the following API endpoints:

    POST /api/token/ — Obtain JWT token
    POST /api/token/refresh/ — Refresh JWT token
    GET /api/tasks/ — Retrieve a list of tasks (with filtering options)
    POST /api/tasks/ — Create a new task
    GET /api/tasks/{id}/ — Retrieve a task by ID
    PUT /api/tasks/{id}/ — Update a task by ID
    DELETE /api/tasks/{id}/ — Delete a task by ID