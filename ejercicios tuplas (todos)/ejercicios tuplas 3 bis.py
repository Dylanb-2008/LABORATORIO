
numeros_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros_impares = {num for num in numeros_set if num % 2 != 0}
numeros_set.difference_update(numeros_impares)

print(f"Conjunto original: {numeros_set.union(numeros_impares)}") # Para mostrar el original completo
print(f"Conjunto resultante sin números impares: {numeros_set}")