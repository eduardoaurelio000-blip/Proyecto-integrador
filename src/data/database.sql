
CREATE DATABASE IF NOT EXISTS control_asistencia;

USE control_asistencia;

-- 1. ESTUDIANTE
CREATE TABLE ESTUDIANTE (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    nombres VARCHAR(60) NOT NULL,
    apellidos VARCHAR(60) NOT NULL
);

-- 2. DOCENTE
CREATE TABLE DOCENTE (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(60) NOT NULL,
    apellidos VARCHAR(60) NOT NULL
);

-- 3. CURSO
CREATE TABLE CURSO (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    grupo VARCHAR(30) NOT NULL,
    id_docente INT NOT NULL,
    FOREIGN KEY (id_docente)
        REFERENCES DOCENTE(id_docente)
);

-- 4. MATRICULA
CREATE TABLE MATRICULA (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    FOREIGN KEY (id_estudiante)
        REFERENCES ESTUDIANTE(id_estudiante),
    FOREIGN KEY (id_curso)
        REFERENCES CURSO(id_curso)
);

-- 5. SESION_CLASE
CREATE TABLE SESION_CLASE (
    id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_curso)
        REFERENCES CURSO(id_curso)
);

-- 6. ASISTENCIA
CREATE TABLE ASISTENCIA (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_sesion INT NOT NULL,
    id_estudiante INT NOT NULL,
    estado VARCHAR(10) NOT NULL,
    UNIQUE (id_sesion, id_estudiante),
    CHECK (estado IN ('Presente', 'Ausente')),
    FOREIGN KEY (id_sesion)
        REFERENCES SESION_CLASE(id_sesion),
    FOREIGN KEY (id_estudiante)
        REFERENCES ESTUDIANTE(id_estudiante)
);

-- 7. USUARIO
CREATE TABLE USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(30) NOT NULL
);

