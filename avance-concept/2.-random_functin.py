from platform import platform
import random


for value in range(5):
    print(random.random())


# Imprime un número entero aleatorio desde 0 hasta (pero sin incluir) 1.
print(random.randrange(1), end=' ')
# Imprime un número entero aleatorio desde 0 hasta (pero sin incluir) 1.
print(random.randrange(0, 1), end=' ')
# Imprime un número entero aleatorio desde 0 hasta (pero sin incluir) 1, con un paso de 1.
print(random.randrange(0, 1, 1), end=' ')
# Imprime un número entero aleatorio entre 0 y 1 (ambos inclusive).
print(random.randint(0, 1))
# Imprime un número entero aleatorio entre 0 y 1 (ambos inclusive).
print(random.randint(0, 1))




##  print(platform())
print(platform())
print(platform(1))
print(platform(0, 1))
