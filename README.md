#Sistema de Control de Asistencia de Estudiantes

#Proyecto Integrador I — UNAN-León


#Descripción

El proyecto consiste en el diseño de un prototipo de un sistema digital de control de asistencia de estudiantes, basado en una base de datos relacional.

Su propósito es demostrar cómo se puede organizar, almacenar y consultar la información académica para sustituir el registro tradicional de asistencia en papel, reducir errores y facilitar el seguimiento de las faltas por estudiante, curso y fecha.

La base de datos contempla siete entidades principales: estudiantes, docentes, cursos, matrículas, sesiones de clase, asistencias y usuarios. Su estructura está diseñada siguiendo principios de normalización hasta la Tercera Forma Normal (3FN), con claves primarias, claves foráneas y restricciones de integridad.

El proyecto se desarrolla como un prototipo académico que permite representar el funcionamiento de una base de datos mediante una arquitectura de tres capas.


#Objetivo

Diseñar y documentar un prototipo de un sistema digital que permita representar cómo se registran, organizan y consultan las asistencias de los estudiantes de manera eficiente y ordenada.


#Entidades principales

1. Estudiante.
2. Docente.
3. Curso.
4. Matrícula.
5. Sesión de clase.
6. Asistencia.
7. Usuario.


#Funcionalidades previstas

- Gestión de estudiantes.
- Gestión de docentes.
- Gestión de cursos y matrículas.
- Registro de sesiones de clase.
- Registro de asistencia mediante los estados "Presente" y "Ausente".
0- Consulta de faltas por estudiante, curso y fecha.
- Prevención de registros duplicados de asistencia en una misma sesión.
- Control de acceso mediante usuarios autorizados.

Estas funcionalidades representan las operaciones previstas para el prototipo y no implican que exista una aplicación completa implementada.


#Tecnologías y herramientas

- Python: utilizado para implementar una simulación funcional de la lógica de negocio, incluyendo validaciones, registro de asistencia y generación de reportes. La simulación utiliza datos en memoria y no se conecta directamente a MariaDB.
- MariaDB: sistema gestor de bases de datos utilizado para crear y administrar la base de datos.
- Figma: herramienta para el diseño de interfaces y prototipos.
- Git y GitHub: control de versiones y alojamiento del repositorio.
- Termux: entorno utilizado para trabajar con el repositorio y administrar MariaDB desde Android.


#Arquitectura del sistema

- El prototipo contempla una arquitectura de software de tres capas:

#Presentation (Presentación)

- Representa la interfaz mediante la cual los usuarios interactuarían con el sistema. Incluye el diseño de pantallas, formularios y consultas.

#Business (Lógica de negocio)

- Representa las reglas y operaciones del sistema, como la validación de matrículas, el registro de asistencias y la prevención de registros duplicados.

#Data (Datos)

- Contiene la estructura de la base de datos, las tablas, las relaciones y las restricciones necesarias para almacenar y organizar la información.


# Estructura del repositorio

```text
proyecto-integrador/
├── docs/
│   ├── diccionario_datos/
│   ├── documentacion/
│   ├── figma/
│   │   └── capturas/
│   └── modelo_entidad_relacion/
├── src/
│   ├── presentation/
│   ├── business/
│   ├── data/
│   └── database.sql
├── tests/
├── .gitignore
└── README.md
```


#Documentación

El repositorio contempla los siguientes documentos:

- Diccionario de datos.
- Modelo entidad-relación.
- Diseño del prototipo en Figma.
- Informe técnico del proyecto.

Los documentos se incorporarán conforme avance el desarrollo del proyecto y estén disponibles los aportes del equipo.


#Estado del proyecto

El proyecto se encuentra en etapa de diseño, organización y construcción del prototipo. Su desarrollo contempla la documentación de la base de datos y la representación de las operaciones mediante una arquitectura de tres capas.
