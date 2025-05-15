# Ejercicios de condicionales en Python

# 1. Determina si un número es positivo, negativo o cero
numero = int(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 2. Verifica si una persona es mayor de edad (18 años o más)
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. Comprueba si un número es par o impar
n = int(input("Introduce un número para saber si es par o impar: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 4. Encuentra el mayor de dos números
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
if a > b:
    print("El mayor es:", a)
elif b > a:
    print("El mayor es:", b)
else:
    print("Ambos números son iguales")

# 5. Verifica si una letra es vocal o consonante
letra = input("Introduce una letra: ").lower()
if letra in "aeiou":
    print("Es una vocal")
elif letra.isalpha():
    print("Es una consonante")
else:
    print("No es una letra válida")