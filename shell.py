def shell(lista):
    mitad = len(lista) // 2

    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista, p, mitad)

        mitad = mitad // 2


def reducir_busqueda(lista, inicio, salto):
    for i in range(inicio + salto, len(lista)):
        valor = lista[i]
        posicion = i

        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto

        lista[posicion] = valor


numeros = [7, 2, 11, 3, 4, 5, 13, 6, 10, 8, 9, 0]
print(numeros)

shell(numeros)
print(numeros)

# Lo primero que hace es reducir el tamaño de la comparación para encontrar el intervalo
# Una vez encontrado el intervelo osea el salto declaramos la posicion entonces el inicio sera el valor menor de la lista
# los saltos seran las veces que el inicio debe moverse hacia a la izquierda realizando la comparación y así llegar al valor menor
