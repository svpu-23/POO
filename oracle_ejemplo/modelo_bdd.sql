CREATE TABLE usuario (
    nombre VARCHAR(45),
    rut VARCHAR(10) PRIMARY KEY,
    correo VARCHAR(30)
);

CREATE TABLE estudiante (
    id_estudiante INTEGER PRIMARY KEY,
    nombre VARCHAR(45),
    rut VARCHAR(10),
    correo VARCHAR(30),
    FOREIGN KEY (rut) REFERENCES usuario(rut)
);

CREATE TABLE docente (
    id_docente INTEGER PRIMARY KEY,
    nombre VARCHAR(45),
    rut VARCHAR(10),
    correo VARCHAR(30),
    FOREIGN KEY (rut) REFERENCES usuario(rut)
);

CREATE TABLE investigador (
    id_investigador INTEGER PRIMARY KEY,
    nombre VARCHAR(45),
    rut VARCHAR(10),
    correo VARCHAR(30),
    FOREIGN KEY (rut) REFERENCES usuario(rut)
);

CREATE TABLE libro (
    id_libro INTEGER PRIMARY KEY,
    titulo VARCHAR(50),
    autor VARCHAR(20),
    categoria VARCHAR(35),
    disponibilidad NUMBER(1)
);

CREATE TABLE prestamo (
    id_prestamo INTEGER PRIMARY KEY,
    fecha_inicio DATE,
    fecha_fin DATE,
    estado VARCHAR(20),
    rut_usuario VARCHAR(10),
    id_libro INTEGER,
    FOREIGN KEY (rut_usuario) REFERENCES usuario(rut),
    FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
);