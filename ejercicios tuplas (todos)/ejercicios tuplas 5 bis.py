estudiantes_cursos = {
    "Ana": {"Matemáticas", "Física"},
    "Juan": {"Química", "Biología"},
    "Pedro": {"Matemáticas", "Programación"},
    "Sofía": {"Matemáticas", "Física", "Historia"}
}

curso_buscado = "Matemáticas"
estudiantes_en_matematicas = []

for estudiante, cursos in estudiantes_cursos.items():
    if curso_buscado in cursos:
        estudiantes_en_matematicas.append(estudiante)

print(f"Los estudiantes inscritos en el curso de '{curso_buscado}' son: {estudiantes_en_matematicas}")