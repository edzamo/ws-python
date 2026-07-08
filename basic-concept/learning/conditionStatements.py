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

# 6. Asigna una calificación según el puntaje
Score = int(input("Introduce el puntaje (0-100): "))
if 90 <= Score <= 100:
    grade = "A"
elif 80 <= Score <= 89:
    grade = "B"
elif 70 <= Score <= 79:
    grade = "C"
elif 60 <= Score <= 69:
    grade = "D"
else:
    grade = "F"
print(f"La calificación es: {grade}")




