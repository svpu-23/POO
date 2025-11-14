CREATE TABLE usuario (
nombre varchar(45),
rut varchar(10),
correo varchar(30),
);
        
        
CREATE TABLE estudiante (
id_estudiante INTEGER PRIMARY KEY,
nombre varchar(45),
rut varchar(10),
correo varchar(30),
);
        
        
CREATE TABLE docente (
id_docente INTEGER PRIMARY KEY,
nombre varchar(45),
rut varchar(10),
correo varchar(30),
);
        
        
CREATE TABLE investigador (
id_investigador INTEGER PRIMARY KEY,
nombre varchar(45),
rut varchar(10),
correo varchar(30),
);
    
        
CREATE TABLE prestamo (
id_prestamo INTEGER PRIMARY KEY,
fecha_inicio DATE,
fecha_fin DATE,
estado varchar(20)
);
        
        
CREATE TABLE libro (
id_libro INTEGER PRIMARY KEY,
titulo varchar(50),
autor varchar(20),
categoria varchar(35),
disponibilidad BOOLEAN
);