def buble_sort(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j] < numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros

numeros = [24, 10, 5, 11, 4]

print(buble_sort(numeros))