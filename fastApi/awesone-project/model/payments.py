from pydantic import BaseModel # the library used for data validation and settings management using Python type annotations
from sqlmodel import Field, SQLModel


class CustomerProfile(SQLModel):
    """
    Represents the core profile data for a customer.

    This model is used as a base for both API requests (CustomerRegistrationRequest)
    and the database model (CustomerAccount). To create a customer in the database,
    you would create an instance of `CustomerAccount` using this data and save it
    to the database session.
    """
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str= Field(default=None)
    age: int = Field(default=None)


class CustomerRegistrationRequest(CustomerProfile):
    pass


class CustomerAccount(CustomerProfile, table=True):
    id: int | None= Field(default=None, primary_key=True)




class PaymentTransaction(BaseModel):
    id: int
    amount: float
    currency: str
    description: str | None
    customer_id: int


class BillingInvoice(BaseModel):
    id: int
    customer: CustomerAccount
    transactions: list[PaymentTransaction]
    total: int

    @property
    def total_amount(self):
        return sum(transaction.amount for transaction in self.transactions)