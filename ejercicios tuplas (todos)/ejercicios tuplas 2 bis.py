# Crea un diccionario que contenga nombres de productos y sus precios
productos = {
    "laptop": 1200,
    "ratón": 25,
    "teclado": 150,
    "monitor": 350,
    "tablet": 500,
    "impresora": 95
}

print("Productos con precio mayor a 100:")
for nombre, precio in productos.items():
    if precio > 100:
        print(f"- {nombre}: ${precio}")