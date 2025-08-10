estudiantes = []

while True:
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio general")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar estudiantes con nota mayor al promedio")
    print("6. Mostrar mejor y peor nota")
    print("7. Eliminar estudiante por nombre")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombre = input("Nombre del estudiante: ")
            try:
                edad = int(input("Edad: "))
                nota = float(input("Nota (0-10): "))
            except ValueError:
                print("Edad o nota inválidas. Intenta de nuevo.")
                continue

            if edad <= 0 or nota < 0 or nota > 10:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_estudiante = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante {nombre} registrado con éxito.")

        case "2":
            if not estudiantes:
                print("No hay estudiantes registrados aún.")
            else:
                print("\nEstudiantes registrados:")
                print("-------------------------")
                for i, estudiante in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {estudiante['nombre']}")
                    print(f"   Edad: {estudiante['edad']}")
                    print(f"   Nota: {estudiante['nota']}")
                    print("-------------------------")

        case "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")
                
        case "4":
            if not estudiantes:
                print("No hay estudiantes registrados para buscar.")
            else:
                nombre_buscar = input("Ingresa el nombre del estudiante a buscar: ")
                encontrado = False
                for estudiante in estudiantes:
                    if estudiante['nombre'].lower() == nombre_buscar.lower():
                        print(f"\nEstudiante encontrado:")
                        print(f"  Nombre: {estudiante['nombre']}")
                        print(f"  Edad: {estudiante['edad']}")
                        print(f"  Nota: {estudiante['nota']}")
                        encontrado = True
                        break
                if not encontrado:
                    print(f"No se encontró un estudiante con el nombre '{nombre_buscar}'.")

        case "5":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                
                estudiantes_superan_promedio = [e for e in estudiantes if e['nota'] > promedio]
                
                if estudiantes_superan_promedio:
                    print(f"\nEstudiantes con nota mayor al promedio ({promedio:.2f}):")
                    for estudiante in estudiantes_superan_promedio:
                        print(f"  - {estudiante['nombre']} (Nota: {estudiante['nota']})")
                else:
                    print("Ningún estudiante tiene una nota mayor que el promedio.")

        case "6":
            if not estudiantes:
                print("No hay estudiantes registrados para comparar notas.")
            else:
                mejor_nota = max(estudiantes, key=lambda e: e['nota'])
                peor_nota = min(estudiantes, key=lambda e: e['nota'])
                
                print("\nMejor y peor nota:")
                print(f"  Mejor nota: {mejor_nota['nota']} de {mejor_nota['nombre']}")
                print(f"  Peor nota: {peor_nota['nota']} de {peor_nota['nombre']}")

        case "7":
            if not estudiantes:
                print("No hay estudiantes registrados para eliminar.")
            else:
                nombre_eliminar = input("Ingresa el nombre del estudiante a eliminar: ")
                estudiante_encontrado = False
                for estudiante in estudiantes:
                    if estudiante['nombre'].lower() == nombre_eliminar.lower():
                        estudiantes.remove(estudiante)
                        print(f"Estudiante '{estudiante['nombre']}' eliminado con éxito.")
                        estudiante_encontrado = True
                        break
                if not estudiante_encontrado:
                    print(f"No se encontró un estudiante con el nombre '{nombre_eliminar}'.")
        
        case "8":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")