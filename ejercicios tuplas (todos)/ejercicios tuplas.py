# Crea una tupla con los días de la semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print(f"El tercer día de la semana es: {dias_semana[2]}")

dia1, dia2, dia3, *_ = dias_semana

print(f"El primer día desempaquetado es: {dia1}")
print(f"El segundo día desempaquetado es: {dia2}")
print(f"El tercer día desempaquetado es: {dia3}")