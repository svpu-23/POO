import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")            


#for query in tables:
#create_schema(query)



def create_schema():

    tables = [
        (
            "CREATE TABLE usuario ("
            "nombre varchar(45),"
            "rut varchar(10),"
            "correo varchar(30),"
            ")"
        )
        (
           "CREATE TABLE estudiante ("
           "id_estudiante INTEGER PRIMARY KEY,"
           "nombre varchar(45),"
            "rut varchar(10),"
            "correo varchar(30),"
            ")"
        )
        (
            "CREATE TABLE docente ("
            "id_docente INTEGER PRIMARY KEY,"
            "nombre varchar(45),"
            "rut varchar(10),"
            "correo varchar(30),"
            ")" 
        )
        (
            "CREATE TABLE investigador ("
            "id_investigador INTEGER PRIMARY KEY,"
            "nombre varchar(45),"
            "rut varchar(10),"
            "correo varchar(30),"
            ")"
        )
        (
            "CREATE TABLE prestamo ("
            "id_prestamo INTEGER PRIMARY KEY,"
            "fecha_inicio DATE,"
            "fecha_fin DATE," 
            "estado varchar(20)"
            ")"
        )
        (
            "CREATE TABLE libro ("
            "id_libro INTEGER PRIMARY KEY," 
            "titulo varchar(50)," 
            "autor varchar(20)," 
            "categoria varchar(35)," 
            "disponibilidad BOOLEAN"
        )
    ]




def create_usuario (
    nombre,
    rut,
    correo                      
):
    sql =(
        "INSERT INTO USUARIO(nombre,rut,correo)"
        "VALUES (:nombre,:rut,:correo)"
    )

    parametros = {
        "nombre": nombre,
        "rut": rut,
        "correo": correo,
    }

def create_estudiante (
    id_estudiante,
    nombre,
    rut,
    correo                      
):
    pass

def create_docente (
    id_docente,
    nombre,
    rut,
    correo                      
):
    pass

def create_investigador (
    id_investigador,
    nombre,
    rut,
    correo                      
):
    pass

def create_prestamo (
    id_prestamo,
    fecha_inicio,
    fecha_fin,
    estado,
    
):
    pass

def create_libro (
    id_libro,
    titulo,
    autor,
    categoria,
    disponibilidad

):
    pass