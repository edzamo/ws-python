# typing.Annotated se usa para añadir metadatos a los tipos, clave para la inyección de dependencias de FastAPI.
from typing import Annotated

# Depends es la función de FastAPI que gestiona la inyección de dependencias.
from fastapi import Depends, FastAPI
# SQLModel es la clase base para nuestros modelos de datos.
# Session gestiona la "conversación" con la base de datos.
# create_engine crea el motor de conexión a la base de datos.
from sqlmodel import SQLModel, Session, create_engine


# Define el nombre del archivo de la base de datos. Usamos SQLite, una base de datos simple basada en un archivo.
sqlite_file_name = "database.db"
# Esta es la URL de conexión. `sqlite:///` indica que es un archivo local.
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Creamos el "motor" de SQLAlchemy/SQLModel. Este objeto gestiona las conexiones a la base de datos.
# `echo=True` es muy útil para el desarrollo, ya que imprime en la consola todas las sentencias SQL que se ejecutan.
engine = create_engine(sqlite_url, echo=True)

# Esta función se ejecutará una sola vez cuando la aplicación se inicie (gracias al `lifespan` en main.py).
def create_db_and_tables():
    # SQLModel.metadata contiene toda la información de nuestras tablas (definidas con `table=True`).
    # `create_all` le dice al motor que cree todas esas tablas en la base de datos si no existen.
    SQLModel.metadata.create_all(engine)


# Esta es una función generadora que se usará para la inyección de dependencias.
def get_session():
    # `with` garantiza que la sesión se cierre automáticamente al final, incluso si hay errores.
    with Session(engine) as session:
        # `yield` entrega la sesión al endpoint que la solicitó. El código del endpoint se ejecuta aquí.
        yield session
    # Cuando el endpoint termina, el código después de `yield` se ejecuta, y el `with` cierra la sesión.

# Creamos un tipo anotado para la inyección de dependencias.
# Esto le dice a FastAPI: "Cuando un endpoint pida una `SessionDep`, ejecuta la función `get_session` y pásale el resultado".
# Es el análogo a `@Autowired` en Spring.
SessionDep = Annotated[Session, Depends(get_session)]
