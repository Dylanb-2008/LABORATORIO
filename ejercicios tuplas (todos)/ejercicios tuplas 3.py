# Crea dos conjuntos con nombres de estudiantes
curso_a = {"Ana", "Pedro", "Luis", "Sofía"}
curso_b = {"Juan", "Sofía", "Marta", "Pedro"}

print(f"Estudiantes del Curso A: {curso_a}")
print(f"Estudiantes del Curso B: {curso_b}")
print("---")

estudiantes_de_ambos = curso_a.intersection(curso_b)
print(f"Estudiantes en ambos cursos: {estudiantes_de_ambos}")

solo_curso_a = curso_a.difference(curso_b)
print(f"Estudiantes en el primer curso pero no en el segundo: {solo_curso_a}")

estudiantes_en_total = curso_a.union(curso_b)
print(f"Estudiantes en total: {estudiantes_en_total}")