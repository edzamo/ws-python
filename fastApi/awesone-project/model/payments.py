from pydantic import BaseModel # the library used for data validation and settings management using Python type annotations


class CustomerProfile(BaseModel):
    name: str
    description: str | None
    email: str
    age: int


class CustomerRegistrationRequest(CustomerProfile):
    pass


class CustomerAccount(CustomerProfile):
    id: int | None


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