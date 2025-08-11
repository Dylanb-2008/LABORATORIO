# Dada una tupla con números enteros
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def obtener_pares(tupla):
    return tuple(num for num in tupla if num % 2 == 0)

numeros_pares = obtener_pares(numeros)
print(f"Tupla original: {numeros}")
print(f"Nueva tupla con números pares: {numeros_pares}")