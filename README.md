# FastAPI Learning Project

Welcome to my FastAPI learning project! This repository contains a simple RESTful API for managing products, created as part of my journey to learn FastAPI.

## Project Overview

This application serves as a backend for a product management system. It demonstrates the core concepts of FastAPI, including:

-   **Routing**: defining endpoints for different HTTP methods.
-   **Pydantic Models**: Data validation and serialization.
-   **SQLAlchemy ORM**: Interacting with a PostgreSQL database.
-   **CRUD Operations**: Create, Read, Update, and Delete functionalities.

## Tech Stack

-   **Language**: Python 3.9+
-   **Framework**: FastAPI
-   **Database**: PostgreSQL
-   **ORM**: SQLAlchemy
-   **Server**: Uvicorn

## Project Structure

-   `main.py`: The entry point of the application, containing the API routes and configuration.
-   `database.py`: Handles the database connection and session creation.
-   `database_models.py`: Defines the SQLAlchemy database models.
-   `models.py`: Defines the Pydantic models for request/response schemas.

## Setup and Installation

### Prerequisites

-   Python installed on your machine.
-   PostgreSQL installed and running.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd FASTAPI_TUTE
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv myenv
    # Windows
    myenv\Scripts\activate
    # macOS/Linux
    source myenv/bin/activate
    ```

3.  **Install dependencies:**
    You can install the required packages using pip:
    ```bash
    pip install fastapi uvicorn sqlalchemy psycopg2-binary
    ```

4.  **Database Configuration:**
    Ensure you have a PostgreSQL database created.
    Update the `db_url` in `database.py` with your database credentials if necessary:
    ```python
    db_url="postgresql://<username>:<password>@localhost:5432/<database_name>"
    ```

## Running the Application

To start the server, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

FastAPI creates automatic interactive documentation. Once the server is running, you can access:

-   **Swagger UI**: `http://127.0.0.1:8000/docs` - Test the API endpoints directly from your browser.
-   **ReDoc**: `http://127.0.0.1:8000/redoc` - Alternative API documentation.

### Endpoints

-   `GET /products/`: Retrieve all products.
-   `GET /products/{product_id}`: Retrieve a specific product by ID.
-   `POST /products/`: Create a new product.
-   `PUT /products/{product_id}`: Update an existing product.
-   `DELETE /products/{product_id}`: Delete a product.

## Future Improvements

-   Add authentication (JWT).
-   Add more complex database relationships.
-   Implement unit tests.

---

*This project is for educational purposes.*
