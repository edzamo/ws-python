

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select

from dataBase import SessionDep # Python encontrará esto desde la raíz del proyecto
from model.payments import Customer, Transaction, TransactionCreate


router= APIRouter()



@router.post("/transaction" , tags=['transaction'])
async def create_transaction(transaction: TransactionCreate, session: SessionDep):
    # --- Validación de Lógica de Negocio ---
    transaction_data = transaction.model_dump()  # Convierte el objeto de entrada (TransactionCreate) a un diccionario de Python.
    customer = session.get(Customer, transaction_data.get("customer_id"))  # Busca en la base de datos al cliente usando el 'customer_id' del diccionario.
    if not customer:  # Comprueba si el cliente fue encontrado en la base de datos.
        # Si el cliente no existe, lanza una excepción HTTP 404 (Not Found).
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id {transaction_data.get('customer_id')} not found")
    trasaction_data_db = Transaction.model_validate(transaction_data)  # Valida el diccionario y lo convierte en una instancia del modelo de base de datos 'Transaction'.
    session.add(trasaction_data_db)  # Añade la nueva instancia de transacción a la sesión de la base de datos (la prepara para ser guardada).
    session.commit()  # Guarda permanentemente todos los cambios en la sesión actual en la base de datos.
    session.refresh(trasaction_data_db)  # Actualiza el objeto 'trasaction_data_db' con los datos de la base de datos (por ejemplo, para obtener el nuevo ID).
    return trasaction_data_db  # Devuelve el objeto de la transacción recién creada como respuesta JSON.


@router.get("/transactions", tags=['transaction'])
async def get_transactions(session: SessionDep, offset: int = 0, limit: int = 10):
    # `offset` y `limit` son parámetros de consulta (query parameters) para la paginación.
    # FastAPI los extrae automáticamente de la URL (ej: /transactions?offset=0&limit=20).
    # Construimos una consulta que selecciona todas las transacciones, salta `offset` resultados y limita a `limit`.
    transactions = session.exec(select(Transaction).offset(offset).limit(limit)).all()
    return transactions




@router.get("/transaction/{transaction_id}", tags=['transaction'])
async def get_transaction(transaction_id: int, session: SessionDep):
    # Obtenemos la transacción por su ID.
    transaction = session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return transaction
