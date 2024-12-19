Library Management System

This project is a Flask-based Library Management System that provides CRUD (Create, Read, Update, Delete) operations for managing books and members. It includes authentication for secure access to API endpoints.

(A) How to Run the Project

Prerequisites

1. Python 3.8+: 

2. Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install Dependencies: Install required Python packages.

pip install flask

Running the Project

1. Navigate to the Project Directory:

cd <path_to_project>/Library Management System

2. Set Flask Environment Variables (Optional):

$env:FLASK_APP = "app.py"      # For PowerShell
export FLASK_APP=app.py        # For Linux/Mac

3. Run the Application:

python app.py

The server will start on http://127.0.0.1:5000.

Testing Endpoints

1. Use Postman or any other API testing tool to interact with the endpoints.

Books API: http://127.0.0.1:5000/books

Members API: http://127.0.0.1:5000/members

(B) Design Choices Made

1. Blueprints for Modularization:

Used Flask Blueprints to separate logic for books and members into different modules (book_routes and member_routes).

Keeps the project structure modular and scalable.

2. Authentication:

Implemented token-based authentication using the Authorization header to secure POST, PUT, and DELETE endpoints.

3. Utility Functions:

Added a paginate utility function to handle pagination for large datasets.

4. Data Representation:

Used Python lists (books, members) in models.py to mimic a database for simplicity. This can be replaced with an actual database in the future.

5. RESTful API Design:

Followed REST principles to design endpoints for better usability and scalability.

(C) Limitations

1. No Persistent Storage: Data is not stored persistently and will reset when the server restarts.

2. No Frontend: The project only provides backend APIs and requires tools like Postman for testing.

3. Limited Authentication: Uses a single static token instead of robust user management.
