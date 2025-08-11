# Crea diccionario con datos de una persona
persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera"
}

print(f"Diccionario original: {persona}")

# Cambia la edad
persona["edad"] = 31

# Agrega nuevo campo "ciudad"
persona["ciudad"] = "Madrid"

# Elimina campo "profesión"
del persona["profesion"]

# Muestra el diccionario modificado
print(f"Diccionario modificado: {persona}")