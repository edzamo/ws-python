from typing import TYPE_CHECKING, List, Optional
from pydantic import BaseModel,EmailStr, field_validator # Componentes clave de Pydantic
from sqlmodel import  Field, Relationship, SQLModel, Session, select # Componentes clave de SQLModel
from enum import Enum
from dataBase import engine



# Este bloque solo se ejecuta durante el análisis de tipos (por tu IDE),
# pero es ignorado en tiempo de ejecución, evitando errores de importación circular.
if TYPE_CHECKING:
    # Aunque las clases están en el mismo archivo, esto ayuda a algunos analizadores estáticos.
    from .payments import Customer, Plan, Transaction, Invoice


class StatusEnum(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    REFUNDED = "refunded"
    ACTIVE = "active"
    INACTIVE = "inactive"
    CANCELLED = "cancelled"

# --- Tabla de Enlace (Link Table) ---
# Debe definirse ANTES de los modelos que la usan (Customer y Plan)

# Esta es una tabla de asociación para la relación muchos-a-muchos entre Customer y Plan.
class CustomerPlan(SQLModel , table = True):
    # `foreign_key` crea una restricción de clave foránea a la tabla 'plan'.
    # `primary_key=True` indica que este campo es parte de la clave primaria.
    plan_id: int = Field(foreign_key="plan.id", primary_key=True)
    customer_id: int = Field(foreign_key="customer.id", primary_key=True)
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)
# --- Customer Models ---


# Clase base (como un DTO base) que contiene los campos comunes. No es una tabla.
class CustomerBase(SQLModel):
    """
    Represents the core profile data for a customer.
    This is used for API requests and as a base for the database model.
    """

    name: str
    description: Optional[str] = Field(default=None)
    # `unique=True` asegura que no haya dos clientes con el mismo email.
    # `index=True` crea un índice en la base de datos para acelerar las búsquedas por email.
    email: EmailStr = Field(unique=True, index=True)
    age: Optional[int] = Field(default=None)



    @field_validator("mail")
    @classmethod
    def validate_email(cls, value ):
        session = Session(engine)
        query= select(Customer).where(Customer.email == value)
        customer = session.exec(query).first()
        if customer:
            raise ValueError("Email already exists")
    
        return value

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 18:
            raise ValueError("Customer must be at least 18 years old")
        return value


# Este es un modelo para la API (DTO), usado para el cuerpo de la petición de registro.
class CustomerRegistrationRequest(CustomerBase):
    pass


# Este es el modelo de la base de datos. `table=True` le dice a SQLModel que cree una tabla para esta clase.
class Customer(CustomerBase, table=True):
    # `id` es la clave primaria, opcional porque la base de datos la generará.
    id: Optional[int] = Field(default=None, primary_key=True)
    # `Relationship` define la relación con otras tablas. No crea una columna en la tabla `customer`.
    # `back_populates` es el nombre del atributo en el modelo `Transaction` que apunta de vuelta a este. Es crucial para una relación bidireccional.
    transactions: List["Transaction"] = Relationship(back_populates="customer")
    invoices: List["Invoice"] = Relationship(back_populates="customer")
    # `link_model` se usa para relaciones muchos-a-muchos, especificando la tabla de asociación.
    plans: List["Plan"] = Relationship(back_populates="customers", link_model=CustomerPlan)


# --- Transaction Models ---


class TransactionBase(SQLModel):
    amount: int
    currency: str


# Modelo de la tabla 'transaction'.
class Transaction(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Estas son las columnas de clave foránea que realmente existen en la base de datos.
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    invoice_id: Optional[int] = Field(default=None, foreign_key="invoice.id")

    # Relaciones inversas
    # Usamos comillas ("Customer") para evitar errores de importación circular, ya que `Customer` se define arriba.
    customer: Optional["Customer"] = Relationship(back_populates="transactions")
    invoice: Optional["Invoice"] = Relationship(back_populates="transactions")

# DTO para crear una transacción. Exige que se proporcione un `customer_id`.
class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")


# --- Billing Models ---

# --- Invoice Models (NUEVO) ---

class InvoiceBase(SQLModel):
    status: str = Field(default="pending")
    total_amount: float

# Modelo de la tabla 'invoice'.
class Invoice(InvoiceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")

    # Relaciones
    # Una factura pertenece a un cliente.
    customer: "Customer" = Relationship(back_populates="invoices")
    # Una factura puede tener muchas transacciones.
    transactions: List["Transaction"] = Relationship(back_populates="invoice")

# --- DTOs (Data Transfer Objects) ---

class BillingInvoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    # `@property` permite que esto se calcule como un atributo, no como un método.
    @property
    def total_amount(self):
        return sum(transaction.amount for transaction in self.transactions)


## --- Plans Models ---

# Modelo de la tabla 'plan'.
class Plan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None)
    price: float
    # Relación inversa muchos-a-muchos con Customer.
    customers: List["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)
