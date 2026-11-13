from src.business.validaciones import (
    estudiante_existe,
    estudiante_matriculado,
    estado_valido
)

estudiantes = [
    {"codigo": "2026001", "nombre": "Carlos Pérez"},
    {"codigo": "2026002", "nombre": "Ana López"}
]

matriculas = [
    {"codigo_estudiante": "2026001", "id_curso": 1},
    {"codigo_estudiante": "2026002", "id_curso": 2}
]

print("=== PRUEBAS DE VALIDACIONES ===")

print("¿Existe Carlos?",
      estudiante_existe(estudiantes, "2026001"))

print("¿Existe Pedro?",
      estudiante_existe(estudiantes, "2026003"))

print("¿Carlos está matriculado en el curso 1?",
      estudiante_matriculado(matriculas, "2026001", 1))

print("¿Carlos está matriculado en el curso 2?",
      estudiante_matriculado(matriculas, "2026001", 2))

print("¿Estado Presente válido?",
      estado_valido("Presente"))

print("¿Estado Tarde válido?",
      estado_valido("Tarde"))
