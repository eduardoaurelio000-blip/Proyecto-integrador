
from src.business.reportes import generar_reporte

asistencias = [
    {"codigo_estudiante": "2026001", "id_sesion": 1, "estado": "Presente"},
    {"codigo_estudiante": "2026002", "id_sesion": 1, "estado": "Presente"},
    {"codigo_estudiante": "2026003", "id_sesion": 1, "estado": "Ausente"},
    {"codigo_estudiante": "2026004", "id_sesion": 1, "estado": "Presente"},
    {"codigo_estudiante": "2026005", "id_sesion": 1, "estado": "Ausente"}
]

print("=== PRUEBA DE REPORTES DE ASISTENCIA ===")

reporte = generar_reporte(asistencias, 1, 10)

print("\nReporte de la sesión 1:")

print("Total de estudiantes:", reporte["total_estudiantes"])
print("Presentes:", reporte["presentes"])
print("Ausentes:", reporte["ausentes"])
print("Sin registro:", reporte["sin_registro"])
print("Porcentaje de asistencia:", reporte["porcentaje_asistencia"], "%")

print("\n=== PRUEBA DE SESIÓN SIN ESTUDIANTES ===")

reporte_vacio = generar_reporte(asistencias, 2, 0)

print("Porcentaje de asistencia:",
      reporte_vacio["porcentaje_asistencia"], "%")

