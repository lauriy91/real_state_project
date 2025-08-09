# Ejercicio de arrays

def organize_blocks(arr):
    bloques = []
    actual = []

    for num in arr:
        if num == 0:
            bloques.append(actual)
            actual = []
        else:
            actual.append(num)
    bloques.append(actual)

    partes = []
    for bloque in bloques:
        if len(bloque) == 0:
            partes.append("X")
        else:
            bloque.sort()
            str_num = ""
            for num in bloque:
                str_num += str(num)
            partes.append(str_num)

    return " ".join(partes)

# Evidencia
print(organize_blocks([1,3,2,0,7,8,1,3,0,6,7,1]))
print(organize_blocks([2,1,0,0,3,4]))  