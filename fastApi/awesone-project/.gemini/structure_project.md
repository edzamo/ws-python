yActúa como un Arquitecto de Software experto en Python, FastAPI y SQLModel. Vengo del mundo Java (Spring Boot/JPA), por lo que valoro mucho la modularidad, la arquitectura limpia y los patrones de diseño robustos.

Actualmente estoy diseñando una API y tengo las siguientes entidades de base de datos que se relacionan entre sí: Customer, Transaction, Billing e Invoice. 

En lugar de meter todo en un único archivo gigante o mantener una estructura puramente plana, quiero organizar el proyecto siguiendo las buenas prácticas modernas de Python (Domain-Driven Design o arquitectura por módulos/características).

Por favor, ayúdame con lo siguiente:

1. Estructura de carpetas: Diseña el árbol de directorios ideal para este proyecto en FastAPI, mostrando dónde deben ir los modelos, esquemas, rutas y los archivos '__init__.py'.
2. Solución a los Imports Circulares: Muéstrame el código exacto de SQLModel para configurar las relaciones entre estas entidades (por ejemplo, un Customer tiene múltiples Transactions e Invoices) utilizando 'TYPE_CHECKING' y strings en 'Relationship(back_populates=...)' para evitar de forma profesional los imports circulares en runtime.
3. El rol de '__init__.py': Explícame brevemente cómo debo configurar los archivos '__init__.py' de cada módulo para exponer una "fachada pública" limpia que facilite los imports en el resto de la aplicación.

Por favor, genera código limpio, tipado (Type Hints) y adaptado a las convenciones de Python 3.10+.