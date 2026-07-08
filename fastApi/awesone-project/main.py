import zoneinfo

from fastapi import FastAPI
from datetime import datetime
from model.payments import BillingInvoice, CustomerAccount, CustomerProfile, CustomerRegistrationRequest, PaymentTransaction


app= FastAPI()

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
async def create_customer(customer: CustomerRegistrationRequest):
    return {"message": f"Customer {customer.name} created successfully", "customer": customer.dict()}

@app.post("/transaction")
async def create_transaction(transaction: PaymentTransaction):
    return {"message": f"Transaction of {transaction.amount} {transaction.currency} created successfully", "transaction": transaction.dict()}

@app.post("/invoice")
async def create_invoice(invoice: BillingInvoice):
    return {"message": f"Invoice for customer {invoice.customer.name} created successfully", "invoice": invoice.dict()} 
