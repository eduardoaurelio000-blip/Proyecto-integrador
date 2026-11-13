
from src.business.asistencia import registrar_asistencia

estudiantes = [
    {"codigo": "2026001", "nombre": "Carlos Pérez"},
    {"codigo": "2026002", "nombre": "Ana López"}
]

matriculas = [
    {"codigo_estudiante": "2026001", "id_curso": 1},
    {"codigo_estudiante": "2026002", "id_curso": 2}
]

sesiones = [
    {"id_sesion": 1, "id_curso": 1},
    {"id_sesion": 2, "id_curso": 2}
]

asistencias = []

print("=== PRUEBAS DE REGISTRO DE ASISTENCIA ===")

print("\n1. Registrar asistencia de Carlos:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026001", 1, 1, "Presente"
))

print("\n2. Intentar registrar nuevamente a Carlos:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026001", 1, 1, "Presente"
))

print("\n3. Registrar a Carlos en un curso incorrecto:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026001", 2, 2, "Presente"
))

print("\n4. Registrar con un estado incorrecto:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026002", 2, 2, "Tarde"
))

print("\n5. Intentar registrar un estudiante inexistente:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026003", 1, 1, "Presente"
))

print("\n6. Utilizar una sesión de otro curso:")
print(registrar_asistencia(
    estudiantes, matriculas, sesiones, asistencias,
    "2026001", 1, 2, "Presente"
))

print("\n=== LISTA FINAL DE ASISTENCIAS ===")
print(asistencias)
	
