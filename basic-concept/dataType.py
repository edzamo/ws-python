# Ejemplos de todos los tipos de datos que maneja Python

# Tipos numéricos
entero = 42
flotante = 3.1416
complejo = 2 + 3j
print(f"Entero: {entero}, Tipo: {type(entero)}")
print(f"Flotante: {flotante}, Tipo: {type(flotante)}")
print(f"Complejo: {complejo}, Tipo: {type(complejo)}")

# Tipo texto
cadena = "Hola, mundo!"
print(f"Cadena: {cadena}, Tipo: {type(cadena)}")

# Tipo booleano
booleano_verdadero = True
booleano_falso = False
print(f"Booleano True: {booleano_verdadero}, Tipo: {type(booleano_verdadero)}")
print(f"Booleano False: {booleano_falso}, Tipo: {type(booleano_falso)}")

# Tipos de secuencia
lista = [1, 2, 3, "manzana"]
tupla = (1, 2, 3, "manzana")
rango = range(5)
print(f"Lista: {lista}, Tipo: {type(lista)}")
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")
print(f"Rango: {list(rango)}, Tipo: {type(rango)}")

# Tipo mapeo
diccionario = {"nombre": "Ana", "edad": 25}
print(f"Diccionario: {diccionario}, Tipo: {type(diccionario)}")

# Tipos de conjunto
conjunto = {1, 2, 3, 3, 4}
frozenset_ejemplo = frozenset([1, 2, 3, 4])
print(f"Conjunto: {conjunto}, Tipo: {type(conjunto)}")
print(f"Frozenset: {frozenset_ejemplo}, Tipo: {type(frozenset_ejemplo)}")

# Tipos binarios
bytes_ejemplo = b"Hola"
bytearray_ejemplo = bytearray(4)
memoryview_ejemplo = memoryview(bytes_ejemplo)
print(f"Bytes: {bytes_ejemplo}, Tipo: {type(bytes_ejemplo)}")
print(f"Bytearray: {bytearray_ejemplo}, Tipo: {type(bytearray_ejemplo)}")
print(f"Memoryview: {memoryview_ejemplo}, Tipo: {type(memoryview_ejemplo)}")

# Función para imprimir el tamaño de una cadena
def imprimir_tamano_cadena(cadena):
    print(f"El tamaño de la cadena es: {len(cadena)}")

# Ejemplo de uso de la función
ejemplo_cadena = "Python"
imprimir_tamano_cadena(ejemplo_cadena)
