# Tienes una tupla con nombres y una lista con edades
nombres = ("Ana", "Luis", "Marta")
edades = [25, 30, 28]

persona_dict = dict(zip(nombres, edades))

print(f"Diccionario de personas: {persona_dict}")