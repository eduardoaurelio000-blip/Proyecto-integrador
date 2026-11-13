
def generar_reporte(asistencias, id_sesion, total_estudiantes):

    presentes = 0
    ausentes = 0

    for asistencia in asistencias:
        if asistencia["id_sesion"] == id_sesion:
            if asistencia["estado"] == "Presente":
                presentes += 1
            elif asistencia["estado"] == "Ausente":
                ausentes += 1

    if total_estudiantes <= 0:
        porcentaje_asistencia = 0
    else:
        porcentaje_asistencia = (presentes / total_estudiantes) * 100

    return {
        "id_sesion": id_sesion,
        "total_estudiantes": total_estudiantes,
        "presentes": presentes,
        "ausentes": ausentes,
        "sin_registro": total_estudiantes - presentes - ausentes,
        "porcentaje_asistencia": round(porcentaje_asistencia, 2)
    }

