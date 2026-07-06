## about lists
#append(): en Python añade un nuevo elemento al final de una lista. Es el método correcto para esta pregunta.
#pop(): quita un elemento de la lista y lo devuelve. Si no se da índice, elimina el último elemento.
#index(): busca un valor dentro de la lista y devuelve la posición (índice) de su primera aparición.
#add(): no es un método de list en Python. add() se usa en conjuntos (set), no en listas.
#push(): tampoco es un método de list en Python. En JavaScript o en otras estructuras puede existir, pero no en listas Python.
#forward(): no es un método válido de listas en Python.

total=0
count=0
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        num = float(inp)
    except:
        print("Invalid input")
        continue
    total = total + num
    count = count + 1
average = total / count
print("Average:", average)