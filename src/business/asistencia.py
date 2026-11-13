
from src.business.validaciones import (
    estudiante_existe,
    estudiante_matriculado,
    estado_valido,
    sesion_pertenece_a_curso
)


def registrar_asistencia(estudiantes, matriculas, sesiones, asistencias,
                         codigo, id_curso, id_sesion, estado):

    if not estudiante_existe(estudiantes, codigo):
        return "Error: el estudiante no existe."

    if not estudiante_matriculado(matriculas, codigo, id_curso):
        return "Error: el estudiante no está matriculado en este curso."

    if not sesion_pertenece_a_curso(sesiones, id_sesion, id_curso):
        return "Error: la sesión no pertenece a este curso."

    if not estado_valido(estado):
        return "Error: el estado de asistencia no es válido."

    for asistencia in asistencias:
        if (asistencia["codigo_estudiante"] == codigo
                and asistencia["id_sesion"] == id_sesion):
            return "Error: la asistencia ya fue registrada."

    asistencias.append({
        "codigo_estudiante": codigo,
        "id_curso": id_curso,
        "id_sesion": id_sesion,
        "estado": estado
    })

    return "Asistencia registrada correctamente."

