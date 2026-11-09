# Sistema de Control de Asistencia de Estudiantes

**Proyecto Integrador I — UNAN-León**

## Descripción

El proyecto consiste en el diseño de una base de datos relacional para un sistema digital de control de asistencia de estudiantes, orientado a sustituir el registro tradicional en papel para prevenir errores, evitar la pérdida de información y facilitar la consulta de faltas por estudiante, curso y fecha.

La estructura organiza la información en siete entidades principales: estudiantes, docentes, cursos, matrículas, sesiones de clase, asistencias y usuarios. Estas entidades están diseñadas bajo normas de normalización hasta la Tercera Forma Normal (3FN), respaldadas por un diccionario de datos en MySQL y reglas operativas que garantizan la integridad de los registros y el acceso autorizado.

## Objetivo

Diseñar un sistema digital que permita registrar, organizar y consultar la asistencia de los estudiantes de manera eficiente y segura.

## Entidades principales

1. Estudiantes
2. Docentes
3. Cursos
4. Matrículas
5. Sesiones de clase
6. Asistencias
7. Usuarios

## Funcionalidades del sistema

- Gestión de estudiantes.
- Gestión de docentes.
- Gestión de cursos y matrículas.
- Registro de sesiones de clase.
- Control de asistencia mediante los estados "Presente" y "Ausente".
- Consulta de faltas por estudiante, curso y fecha.
- Restricción de un registro por estudiante por sesión.
- Acceso y modificación de datos únicamente por usuarios autorizados.

## Tecnologías y herramientas

- Python: lenguaje de programación.
- MySQL: sistema de gestión de bases de datos.
- Figma: diseño de interfaces y prototipos.
- Git y GitHub: control de versiones y alojamiento del repositorio.

## Arquitectura del sistema

El proyecto contempla una arquitectura de software de tres capas:

- **Presentation:** Interfaz de usuario y presentación de la información.
- **Business:** Reglas de negocio y procesamiento de las operaciones.
- **Data:** Acceso a datos, consultas y conexión con MySQL.

## Estructura del repositorio

```text
proyecto-integrador/
├── docs/
├── src/
│   ├── presentation/
│   ├── business/
│   └── data/
├── tests/
├── .gitignore
└── README.md
