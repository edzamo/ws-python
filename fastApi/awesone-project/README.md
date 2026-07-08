# Awesome FastAPI Project: A Step-by-Step Guide

Welcome! This guide explains how this project was built, step by step. It's designed for developers, especially those coming from a Java background, to quickly understand the key concepts of building a modern web API with Python and FastAPI.

## Core Technologies

- **FastAPI**: The web framework used to build the API. It's known for high performance and its use of modern Python features.
- **SQLModel**: A library for interacting with SQL databases. It combines Pydantic and SQLAlchemy, making it easy to have a single data model for both API validation and database interaction.
  - *(Java Analogy: Think of SQLModel as combining JPA/Hibernate for database mapping and Jackson/Gson for JSON serialization into one powerful tool.)*
- **Uvicorn**: The ASGI server that runs our FastAPI application.
  - *(Java Analogy: This is like an embedded application server such as Tomcat or Jetty.)*

---

## How to Run This Project

1.  **Set up a virtual environment**: Follow the instructions in `VENV_SETUP_PUBLIC.md`.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

---

## Step 1: Defining the Data Models (`model/payments.py`)

The first step in any data-driven application is to define the shape of our data. In this project, we use `SQLModel` to define our `Customer`.

### Key Concepts:

1.  **Base Model (`CustomerProfile`)**: We created a base `CustomerProfile` class that holds the common fields for a customer (`name`, `email`, etc.). This acts as a reusable template.

2.  **Database Model (`CustomerAccount`)**: This class inherits from `CustomerProfile` and adds `table=True` to tell SQLModel that this class maps to a database table. We also add an `id` field which is the primary key.

    ```python
    class CustomerAccount(CustomerProfile, table=True):
        id: int | None = Field(default=None, primary_key=True)
    ```
    - *(Java Analogy: This is like creating a JPA `@Entity` class that will be mapped to a database table.)*

3.  **Request Model (`CustomerRegistrationRequest`)**: This class also inherits from `CustomerProfile`. We use it specifically for the request body of our "create customer" endpoint. This allows us to separate the data we expect from a client from our database representation if needed.
    - *(Java Analogy: This is equivalent to a Data Transfer Object (DTO) used in a `@RequestBody` in Spring.)*

---

## Step 2: Setting Up the Database (`dataBase.py`)

Once we have our models, we need to configure the connection to our database.

### Key Concepts:

1.  **Database Engine**: We create a database "engine" which manages the connection pool to our database. Here, we use a simple SQLite file-based database. The `echo=True` argument is useful for debugging as it prints all the SQL statements that are executed.

    ```python
    engine = create_engine(sqlite_url, echo=True)
    ```

2.  **Lifespan Function (`create_db_and_tables`)**: FastAPI has a `lifespan` event that runs code on startup and shutdown. We use the startup event to create our database tables based on our SQLModel metadata.

    ```python
    def create_db_and_tables(app: FastAPI):
        SQLModel.metadata.create_all(engine) # Runs on startup
        yield # The application runs here
        # Code here would run on shutdown
    ```

3.  **Session Management (`get_session` and `SessionDep`)**: To interact with the database, we need a `Session`. We create a function `get_session` that yields a session and automatically closes it. We then use FastAPI's Dependency Injection system to make it available in our endpoints.

    ```python
    def get_session():
        with Session(engine) as session:
            yield session

    SessionDep = Annotated[Session, Depends(get_session)]
    ```
    - *(Java Analogy: `SessionDep` is like using `@Autowired` to inject an `EntityManager` or a database context into your service or controller.)*

---

## Step 3: Creating the API Endpoints (`main.py`)

This is where we define the API routes and connect everything together.

### Key Concepts:

1.  **FastAPI Instance**: We create the main `app` object and connect our database `lifespan` function to it.

    ```python
    app = FastAPI(lifespan=create_db_and_tables)
    ```

2.  **Decorators (`@app.post`, `@app.get`, etc.)**: These decorators are used to associate a function with an API route and HTTP method.
    - *(Java Analogy: This is identical to using `@PostMapping`, `@GetMapping`, etc., in Spring Boot.)*

3.  **Create Endpoint (`POST /customer`)**:
    - We declare the request body type as `customer: CustomerRegistrationRequest`. FastAPI automatically validates the incoming JSON against this model.
    - We inject the database session using `session: SessionDep`.
    - We convert the request model to our database model (`CustomerAccount.model_validate(customer)`), add it to the session, commit it, and refresh it to get the new ID from the database.

    ```python
    @app.post("/customer", response_model=CustomerAccount)
    async def create_customer(customer: CustomerRegistrationRequest, session: SessionDep):
        db_customer = CustomerAccount.model_validate(customer)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
        return db_customer
    ```

4.  **Read Endpoint (`GET /customer/{customer_id}`)**:
    - We get the `customer_id` from the URL path.
    - We use `session.get(CustomerAccount, customer_id)` to fetch the user.
    - **Crucially**, we check if the customer was found. If not, we raise an `HTTPException` to return a proper `404 Not Found` error.

    ```python
    @app.get("/customer/{customer_id}", response_model=CustomerAccount)
    async def get_customer_by_id(customer_id: int, session: SessionDep):
        customer = session.get(CustomerAccount, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer
    ```

5.  **Update Endpoint (`PATCH /customer/{customer_id}`)**:
    - We use `PATCH` for **partial updates**. This means the client only needs to send the fields they want to change.
    - `customer.model_dump(exclude_unset=True)` creates a dictionary containing *only* the fields that were sent in the request.
    - `db_customer.sqlmodel_update(...)` is a powerful SQLModel helper that applies this partial update to the existing database object.

    ```python
    @app.patch("/customer/{customer_id}", response_model=CustomerAccount)
    async def update_customer(customer_id: int, customer: CustomerProfile, session: SessionDep):
        # ... (get customer)
        customer_data = customer.model_dump(exclude_unset=True)
        db_customer.sqlmodel_update(customer_data)
        # ... (commit and return)
    ```

6.  **Replace Endpoint (`PUT /customer/{customer_id}`)**:
    - We use `PUT` for **full replacement**. The client is expected to send the complete object.
    - We use `customer.model_dump()` without `exclude_unset=True`. This means any fields the client omits will be set to `null` in the database, effectively replacing the entire record.

7.  **Delete Endpoint (`DELETE /customer/{customer_id}`)**:
    - After fetching the customer, we simply call `session.delete(customer)` and `session.commit()` to remove it from the database.

I hope this guide is helpful for your learning journey! Let me know if you have more questions.
