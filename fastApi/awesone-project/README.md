# Awesome FastAPI Project: Guía de Aprendizaje y Referencia Técnica

¡Bienvenido! Esta guía explica los conceptos clave de este proyecto, diseñada para desarrolladores (especialmente aquellos con experiencia en Java/Spring) que deseen dominar la creación de APIs modernas con Python. Úsala como material de estudio y referencia para entrevistas técnicas.

## Tecnologías Principales

- **FastAPI**: El framework web para construir la API. Destaca por su alto rendimiento, su sistema de inyección de dependencias y el uso de características modernas de Python.
- **SQLModel**: Una librería para interactuar con bases de datos SQL. Combina Pydantic (para validación de datos) y SQLAlchemy (para el ORM), permitiendo un único modelo de datos para la API y la base de datos.
  - *(**Analogía con Java**: Piensa en SQLModel como la fusión de **JPA/Hibernate** para el mapeo de base de datos y **Jackson/Gson** para la serialización/validación de DTOs, todo en una sola clase.)*
- **Uvicorn**: El servidor ASGI que ejecuta nuestra aplicación FastAPI.
  - *(**Analogía con Java**: Es el equivalente a un servidor de aplicaciones embebido como **Tomcat** o **Jetty** en Spring Boot.)*

---

## Guía de Conceptos Fundamentales

### 1. Modelado de Datos (`model/payments.py`)

El primer paso es definir la forma de nuestros datos. SQLModel nos permite hacerlo de una manera declarativa y potente.

#### Conceptos Clave:
1.  **Modelo de Base de Datos (`table=True`)**: Cualquier clase que herede de `SQLModel` y tenga `table=True` se convertirá en una tabla de base de datos.
    ```python
    class Customer(CustomerBase, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
    ```
    - **Punto Clave**: Esto es análogo a una clase anotada con `@Entity` en JPA.

2.  **Campos y Columnas (`Field`)**: `Field` se usa para configurar las propiedades de una columna, como claves primarias (`primary_key`), claves foráneas (`foreign_key`), índices (`index=True`) y restricciones (`unique=True`).

3.  **Separación de Modelos (DTOs)**: Es una buena práctica separar la representación de la base de datos de la representación de la API.
    - `CustomerBase`: Contiene campos comunes (un DTO base).
    - `Customer`: El modelo de la tabla (`@Entity`).
    - `CustomerCreate`: El modelo para el cuerpo de la petición (`@RequestBody` DTO).

4.  **Tipos de Campo con Validación (Pydantic)**: SQLModel hereda la potente validación de Pydantic. Puedes usar tipos especiales que validan el formato de los datos automáticamente.
    ```python
    # En la clase CustomerBase
    email: EmailStr = Field(unique=True, index=True)
    ```
    - **Punto Clave**: `EmailStr` no es solo un `str`. Es un tipo especial que Pydantic usa para garantizar que el valor recibido sea una dirección de correo electrónico válida. Si no lo es, se genera un error de validación automáticamente. Otros tipos útiles incluyen `HttpUrl` para URLs, `PositiveInt` para enteros positivos, etc. Esto te ahorra escribir código de validación manual.

5.  **Validación Personalizada con `@field_validator`**: A veces, la validación va más allá del formato y requiere lógica de negocio. Para esto, usamos el decorador `@field_validator`.
    ```python
    # En la clase CustomerBase
    age: Optional[int] = Field(default=None)

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 18:
            raise ValueError("Customer must be at least 18 years old")
        return value
    ```
    - **Punto Clave**: Este validador se ejecuta después de que Pydantic haya verificado que `age` es un entero. Nuestra lógica personalizada comprueba si el valor es menor de 18.
    - Si la condición no se cumple, lanzamos un `ValueError`. FastAPI y Pydantic capturarán este error y lo convertirán automáticamente en una respuesta `HTTP 422 Unprocessable Entity` con un mensaje claro, protegiendo tu lógica de negocio.
    - **Otros Validadores**: Pydantic también ofrece `@model_validator` para validaciones que involucran múltiples campos a la vez (por ejemplo, "si el campo A es 'X', entonces el campo B no puede ser nulo").


---

### 2. Modelado Avanzado de Datos y Relaciones

Entender cómo modelar relaciones es fundamental. SQLModel, al estar basado en SQLAlchemy, ofrece una forma poderosa y declarativa de definir estas relaciones.

*(**Analogía con Java**: Esta sección es el equivalente a aprender a usar las anotaciones `@OneToMany`, `@ManyToOne`, `@ManyToMany` y `@OneToOne` en JPA/Hibernate.)*

#### Relación Uno-a-Muchos (One-to-Many) / Muchos-a-Uno (Many-to-One)

Un `Customer` tiene muchas `Transaction`s. Una `Transaction` pertenece a un `Customer`.

1.  **El lado "Uno" (Customer)**: Se declara una lista de los objetos del lado "Muchos".
    ```python
    # En la clase Customer
    transactions: List["Transaction"] = Relationship(back_populates="customer")
    ```
    - `Relationship`: Define el vínculo. **No crea una columna en la base de datos**.
    - `back_populates="customer"`: Esencial. Le dice a SQLModel que este campo está vinculado al atributo `customer` en la clase `Transaction`.

2.  **El lado "Muchos" (Transaction)**: Se declara la clave foránea y el objeto del lado "Uno".
    ```python
    # En la clase Transaction
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    customer: Optional["Customer"] = Relationship(back_populates="transactions")
    ```
    - `customer_id`: Esta es la **columna real** que se crea en la tabla `transaction`.
    - `customer`: Este es el atributo de navegación para acceder al objeto `Customer` relacionado.

#### Relación Muchos-a-Muchos (Many-to-Many)

Un `Customer` puede tener muchos `Plan`s, y un `Plan` puede tener muchos `Customer`s. Esto requiere una **tabla de enlace** (o tabla de asociación).

1.  **Crear la Tabla de Enlace (`CustomerPlan`)**: Se crea un modelo que contiene las claves foráneas de las dos tablas que se van a relacionar.
    ```python
    class CustomerPlan(SQLModel, table=True):
        plan_id: int = Field(foreign_key="plan.id", primary_key=True)
        customer_id: int = Field(foreign_key="customer.id", primary_key=True)
    ```
    - **Punto Clave**: Esta tabla solo contiene las claves. Su clave primaria es la combinación de ambas claves foráneas.

2.  **Configurar las Relaciones**: Ambos modelos (`Customer` y `Plan`) deben apuntar a la tabla de enlace.
    ```python
    # En la clase Customer
    plans: List["Plan"] = Relationship(back_populates="customers", link_model=CustomerPlan)

    # En la clase Plan
    customers: List["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)
    ```
    - `link_model=CustomerPlan`: Este es el argumento clave. Le dice a SQLModel que use `CustomerPlan` para gestionar esta relación.

#### Relación Uno-a-Uno (One-to-One)

Imaginemos que un `Customer` tiene un único `CustomerProfile` con datos adicionales.

1.  **El lado "Principal" (Customer)**: La relación se declara como un objeto, no una lista.
    ```python
    # En una hipotética clase Customer
    # profile: "CustomerProfile" = Relationship(back_populates="customer")
    ```

2.  **El lado "Dependiente" (CustomerProfile)**: La clave foránea debe tener una restricción `unique`.
    ```python
    # En una hipotética clase CustomerProfile
    # customer_id: int = Field(foreign_key="customer.id", unique=True)
    # customer: "Customer" = Relationship(back_populates="profile")
    ```
    - `unique=True` en la clave foránea es lo que garantiza a nivel de base de datos que la relación sea uno-a-uno.

---

### 3. Configuración de la Base de Datos (`dataBase.py`)

#### Conceptos Clave:

1.  **Motor de Base de Datos (`create_engine`)**: Crea el gestor de conexiones a nuestra base de datos. `echo=True` es tu mejor amigo durante el desarrollo, ya que imprime todas las sentencias SQL que se ejecutan.

2.  **Gestor de Ciclo de Vida (`lifespan`)**: En `main.py`, usamos un `lifespan` para ejecutar código al iniciar y apagar la aplicación. Lo usamos para llamar a `create_db_and_tables()`, que crea las tablas de la base de datos al arrancar.

3.  **Gestión de Sesiones e Inyección de Dependencias**: Para interactuar con la base de datos, necesitamos una `Session`.
    ```python
    # Función generadora para obtener una sesión
    def get_session():
        with Session(engine) as session:
            yield session
    
    # Tipo anotado para la inyección de dependencias
    SessionDep = Annotated[Session, Depends(get_session)]
    ```
    - **Punto Clave**: `SessionDep` es el equivalente a usar `@Autowired` para inyectar un `EntityManager` o un `DbContext` en un servicio o controlador en Java/.NET. FastAPI se encarga de llamar a `get_session`, pasar la sesión al endpoint y cerrarla al final.

---

### 4. Creación de Endpoints (`app/router/customers.py`)

Aquí es donde definimos las rutas de la API y conectamos todo.

#### Conceptos Clave:

1.  **`APIRouter`**: Permite agrupar endpoints relacionados en módulos separados, manteniendo `main.py` limpio. Luego se incluyen en la app principal con `app.include_router()`.

2.  **Decoradores (`@router.post`, `@router.get`)**: Asocian una función con una ruta de la API y un método HTTP.
    - **Punto Clave**: Idéntico a `@PostMapping`, `@GetMapping` en Spring Boot.

3.  **Endpoint de Creación (`POST /customer`)**:
    - **Validación del Cuerpo**: `customer: CustomerRegistrationRequest` le dice a FastAPI que valide el JSON entrante contra este modelo. Si no coincide, devuelve un error 422 automáticamente.
    - **Inyección de Dependencias**: `session: SessionDep` le pide a FastAPI una sesión de base de datos.
    - **Lógica**: Se convierte el DTO a un modelo de entidad (`Customer.model_validate`), se añade a la sesión, se guarda (`commit`) y se refresca para obtener el ID.
    ```python
    @router.post("/customer", response_model=Customer)
    async def create_customer(customer: CustomerRegistrationRequest, session: SessionDep):
        db_customer = Customer.model_validate(customer)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
        return db_customer
    ```

4.  **Endpoint de Lectura (`GET /customer/{customer_id}`)**:
    - **Parámetro de Ruta**: `{customer_id}` se captura como un argumento de la función.
    - **Búsqueda Eficiente**: `session.get(Customer, customer_id)` es la forma más rápida de buscar por clave primaria.
    - **Manejo de Errores**: Es crucial comprobar si el objeto existe y lanzar una `HTTPException` con un código 404 si no se encuentra.
    ```python
    @router.get("/customer/{customer_id}", response_model=Customer)
    async def get_customer_by_id(customer_id: int, session: SessionDep):
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer
    ```

5.  **Endpoint de Actualización Parcial (`PATCH /customer/{customer_id}`)**:
    - **Punto Clave**: `customer.model_dump(exclude_unset=True)` es una de las características más potentes. Crea un diccionario que contiene *únicamente* los campos que el cliente envió en la petición.
    - `db_customer.sqlmodel_update(...)` aplica esta actualización parcial al objeto existente de la base de datos de forma segura.