def estudiante_existe(estudiantes, codigo):
    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            return True
    return False


def estudiante_matriculado(matriculas, codigo, id_curso):
    for matricula in matriculas:
        if (matricula["codigo_estudiante"] == codigo
                and matricula["id_curso"] == id_curso):
            return True
    return False


def estado_valido(estado):
    return estado in ["Presente", "Ausente"]


def sesion_pertenece_a_curso(sesiones, id_sesion, id_curso):
    for sesion in sesiones:
        if (sesion["id_sesion"] == id_sesion
                and sesion["id_curso"] == id_curso):
            return True
    return False
