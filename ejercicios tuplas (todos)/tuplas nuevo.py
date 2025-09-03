import random

# 1
inventario = {
    'computadoras': [('laptop', 10), ('pc de escritorio', 5)],
    'accesorios': [('mouse', 25), ('teclado', 15), ('webcam', 8)],
    'periféricos': [('monitor', 7), ('impresora', 3)]
}

print("--- Inventario de la tienda (al principio) ---")
for categoria, productos in inventario.items():
    print(f"Categoría: {categoria}")
    for producto, cantidad in productos:
        print(f"  - {producto}: {cantidad} unidades")

# 2
print("\n--- ¡Simulando 3 ventas al azar! ---")

for i in range(3):
    print(f"\nVenta #{i+1}:")
    
    categoria_a_vender = random.choice(list(inventario.keys()))

    if not inventario[categoria_a_vender]:
        print(f"  ¡Ups! La categoría '{categoria_a_vender}' está vacía. No vendimos nada aquí.")
        continue
        
    producto_a_vender_info = random.choice(inventario[categoria_a_vender])
    nombre_producto = producto_a_vender_info[0]
    cantidad_producto = producto_a_vender_info[1]
    
    print(f"  Un cliente se lleva 1 '{nombre_producto}' de la categoría '{categoria_a_vender}'.")
    
    if cantidad_producto > 1:
        nueva_cantidad = cantidad_producto - 1
        inventario[categoria_a_vender].remove(producto_a_vender_info)
        inventario[categoria_a_vender].append((nombre_producto, nueva_cantidad))
        print(f"  ¡Genial! Quedan {nueva_cantidad} de ese producto.")
    else:
        inventario[categoria_a_vender].remove(producto_a_vender_info)
        print(f"  ¡Se vendió el último! El producto '{nombre_producto}' se agotó.")
        
print("\n--- ¡Llegaron productos nuevos! ---")

categoria_a_reponer = 'periféricos'
nuevo_producto = ('parlantes', 12)

inventario[categoria_a_reponer].append(nuevo_producto)
print(f"Se añadieron {nuevo_producto[1]} '{nuevo_producto[0]}' a la categoría '{categoria_a_reponer}'.")

# 3
print("\n--- Resumen final del inventario ---")
for categoria, productos in inventario.items():
    print(f"\nCategoría: {categoria}")
    if productos:
        for producto, cantidad in productos:
            print(f"  - {producto}: {cantidad} unidades")
    else:
        print("  ¡Esta categoría está vacía! ¡A reponer!")