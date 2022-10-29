def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)

        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1

        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1

        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1


numeros = [7, 2, 11, 3, 4, 5, 13, 6, 10, 8, 9, 0]
print(numeros)

merge_sort(numeros)
print(numeros)

# Lo primero es dividir el array en dos mitados del inicio a la mitad y de la mitad al final
# Luego realiza una comparación por parejas de mitades esto quiere decir que divide la mitad en otra mitad
# Seguid a esto divide la mitad restante hasta hacer comparaciones por termino uno a uno
# Por ultimo de manera ascendente va multiplicandose por mitades hasta volver  hasta su posición original
