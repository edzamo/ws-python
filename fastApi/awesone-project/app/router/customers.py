# HTTPException se usa para devolver respuestas de error HTTP estándar.
# status contiene códigos de estado HTTP para mayor legibilidad.
# APIRouter nos permite agrupar endpoints en un módulo separado.
from fastapi import HTTPException, Query, status,APIRouter
# `select` es la función de SQLModel/SQLAlchemy para construir consultas SELECT.
from sqlmodel import select


# Importamos nuestra dependencia de sesión y los modelos necesarios.
from dataBase import SessionDep
from model.payments import Customer, CustomerBase, CustomerPlan, CustomerRegistrationRequest, Plan, StatusEnum

# Creamos una instancia de APIRouter. La incluiremos en la app principal en `main.py`.
router = APIRouter()


# `@router.post` define un endpoint que responde a peticiones HTTP POST.
# `response_model=Customer` le dice a FastAPI que la respuesta debe ser un objeto `Customer`.
# FastAPI filtrará los campos para que coincidan con el modelo `Customer`.
# `tags` agrupa los endpoints en la documentación de la API (Swagger UI).
@router.post("/customer", response_model=Customer, tags=['customer'])
# `customer: CustomerRegistrationRequest` indica que el cuerpo de la petición debe ser un JSON que coincida con este modelo. FastAPI lo valida automáticamente.
# `session: SessionDep` es la inyección de dependencias en acción. FastAPI nos proporciona una sesión de base de datos.
async def create_customer(customer: CustomerRegistrationRequest, session: SessionDep):
    # `model_validate` convierte el modelo de la API (`CustomerRegistrationRequest`) en un modelo de base de datos (`Customer`).
    db_customer = Customer.model_validate(customer)
    # `session.add()` añade el nuevo objeto a la sesión, preparándolo para ser guardado.
    session.add(db_customer)
    # `session.commit()` guarda todos los cambios pendientes en la base de datos.
    session.commit()
    # `session.refresh()` actualiza el objeto `db_customer` con los datos de la base de datos (importante para obtener el ID auto-generado).
    session.refresh(db_customer)
    return db_customer

# `@router.get` define un endpoint para peticiones GET.
# `{customer_id}` es un parámetro de ruta. FastAPI lo pasará como argumento a la función.
@router.get("/customer/{customer_id}", response_model=Customer, tags=['customer'])
async def get_customer_by_id(customer_id: int, session: SessionDep):
    # `session.get()` es la forma más eficiente de obtener un objeto por su clave primaria.
    customer = session.get(Customer, customer_id)
    # Es crucial comprobar si el objeto existe.
    if not customer:
        # Si no existe, devolvemos un error 404 Not Found.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    return customer

# `@router.patch` es para actualizaciones parciales. El cliente solo envía los campos que quiere cambiar.
@router.patch("/customer/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED,tags=['customer'])
async def update_customer(customer_id: int, customer: CustomerBase, session: SessionDep):
    db_customer = session.get(Customer, customer_id)
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    # `model_dump(exclude_unset=True)` crea un diccionario solo con los campos que el cliente envió en el JSON.
    customer_data_dict = customer.model_dump(exclude_unset=True)
    # `sqlmodel_update` aplica inteligentemente los cambios del diccionario al objeto de la base de datos.
    db_customer.sqlmodel_update(customer_data_dict)
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer

# `@router.put` es para reemplazos completos. El cliente debe enviar el objeto completo.
@router.put("/customer/{customer_id}", response_model=Customer, tags=['customer'])
async def replace_customer(customer_id: int, customer: CustomerBase, session: SessionDep):
    db_customer = session.get(Customer, customer_id)
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    # `model_dump()` sin `exclude_unset=True` incluye todos los campos, estableciendo a `None` los que no se envíen.
    db_customer.sqlmodel_update(customer.model_dump())
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer


# `@router.delete` para eliminar un recurso.
@router.delete("/customer/{customer_id}",tags=['customer'])
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {customer_id} not found")
    session.delete(customer)
    session.commit()
    return {"message": f"Customer with id {customer_id} deleted successfully"}


# Endpoint para obtener una lista de todos los clientes.
@router.get("/customers", response_model=list[Customer], tags=['customer'])
async def get_customers(session: SessionDep):
    # `session.exec()` ejecuta una consulta. `select(Customer)` crea una consulta para obtener todos los clientes.
    # `.all()` obtiene todos los resultados como una lista.
    return session.exec(select(Customer)).all()

@router.post("/customer/{customer_id}/plan/{plan_id}", tags=['customer'])
async def add_plan_to_customer(customer_id: int, plan_id: int, session: SessionDep, plan_status: StatusEnum = Query(default=StatusEnum.ACTIVE)):
    customer_db = session.get(Customer, customer_id) # Busca al cliente en la base de datos usando el ID proporcionado en la URL.
    plan_db = session.get(Plan, plan_id) # Busca el plan en la base de datos usando el ID proporcionado en la URL.
 
    if not customer_db or not plan_db: # Comprueba si se encontraron tanto el cliente como el plan.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer or Plan not found") # Si uno de los dos no existe, lanza un error 404.
 
    customer_plan_db = CustomerPlan(plan_id=plan_id, customer_id=customer_id, status=plan_status) # Crea una nueva instancia del modelo de la tabla de enlace (CustomerPlan), asociando el cliente y el plan.
    session.add(customer_plan_db) # Añade el nuevo registro de asociación a la sesión de la base de datos, preparándolo para ser guardado.
    session.commit() # Guarda permanentemente la nueva asociación en la base de datos.
    session.refresh(customer_plan_db) # Actualiza el objeto `customer_plan_db` con los datos recién guardados de la base de datos.
    return customer_plan_db # Devuelve el registro de la tabla de enlace recién creado como respuesta JSON.




@router.get("/customer/{customer_id}/plans", tags=['transaction'])
async def get_subcribe_customer_to_plans(customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    query= (select(CustomerPlan)
            .where(CustomerPlan.customer_id == customer_id)
            .where(CustomerPlan.status == plan_status))
    plans = session.exec(query).all()
    return plans
    
    