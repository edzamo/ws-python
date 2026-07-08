import zoneinfo

from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from model.payments import BillingInvoice, CustomerAccount, CustomerProfile, CustomerRegistrationRequest, PaymentTransaction
from  dataBase import SessionDep, create_db_and_tables
from sqlmodel import Session, select


app= FastAPI(lifespan= create_db_and_tables)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/date")
async def get_date():
    
    now = datetime.now()
    return {"date": now.strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/time") #this a decorate 
async def get_time():
    from datetime import datetime
    now = datetime.now()
    return {"time": now.strftime("%H:%M:%S")}

timezones = {
    "UTC": "UTC",
    "EST": "America/New_York",
    "CST": "America/Chicago",
    "MST": "America/Denver",
    "CO": "America/Denver",
    "ECT": "America/New_York",
    "PST": "America/Los_Angeles"
    
    }

@app.get("/time-zone/{iso_code}") #when you need receive a parameter in the url you need to use curly braces
async def get_time_by_timezone(iso_code: str):
    try:
        print("Received ISO code:" ,iso_code)  # Debugging statement
        iso = iso_code.strip().upper()  # Remove any leading/trailing whitespace
        timezone = timezones.get(iso)
        tz = zoneinfo.ZoneInfo(timezone) 
        return {"time": datetime.now(tz).strftime("%H:%M:%S")}
    except KeyError:
        return {"error": "Unknown timezone"}
    

@app.post("/customer", response_model=CustomerAccount)
async def create_customer(customer: CustomerRegistrationRequest, session: SessionDep):
    # Create a database model instance from the request data
    db_customer = CustomerAccount.model_validate(customer)
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer

@app.get("/customer/{customer_id}", response_model=CustomerAccount)
async def get_customer_by_id(customer_id: int, session: SessionDep):
    customer = session.get(CustomerAccount, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    return customer

@app.patch("/customer/{customer_id}", response_model=CustomerAccount, status_code=status.HTTP_201_CREATED)
async def update_customer(customer_id: int, customer: CustomerProfile, session: SessionDep):
    db_customer = session.get(CustomerAccount, customer_id)
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    # Get the request data, excluding fields that were not set in the request
    customer_data_dict = customer.model_dump(exclude_unset=True)
    db_customer.sqlmodel_update(customer_data_dict) # Use the built-in SQLModel method for partial updates
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer

@app.put("/customer/{customer_id}", response_model=CustomerAccount)
async def replace_customer(customer_id: int, customer: CustomerProfile, session: SessionDep):
    db_customer = session.get(CustomerAccount, customer_id)
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    # Replace the existing customer data with the new data
    db_customer.sqlmodel_update(customer.model_dump())
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer



@app.delete("/customer/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(CustomerAccount, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    session.delete(customer)
    session.commit()
    return {"message": f"Customer with id {customer_id} deleted successfully"}


@app.get("/customers", response_model=list[CustomerAccount])
async def get_customers(session: SessionDep):
    return session.exec(select(CustomerAccount)).all()
    
   

@app.post("/transaction")
async def create_transaction(transaction: PaymentTransaction):
    return {"message": f"Transaction of {transaction.amount} {transaction.currency} created successfully", "transaction": transaction.dict()}

@app.post("/invoice")
async def create_invoice(invoice: BillingInvoice):
    return {"message": f"Invoice for customer {invoice.customer.name} created successfully", "invoice": invoice.dict()} 
