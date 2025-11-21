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


tables = [
        (
            "CREATE TABLE usuario ("
            "nombre VARCHAR(45),"
            "rut VARCHAR(10) PRIMARY KEY,"
            "correo VARCHAR(30)"
            ");"
        )
        (
            "CREATE TABLE estudiante ("
            "id_estudiante INTEGER PRIMARY KEY,"
            "nombre VARCHAR(45),"
            "rut VARCHAR(10),"
            "correo VARCHAR(30),"
            "FOREIGN KEY (rut) REFERENCES usuario(rut)"
            ");"
        )
        (
            "CREATE TABLE docente ("
            "id_docente INTEGER PRIMARY KEY,"
            "nombre VARCHAR(45),"
            "rut VARCHAR(10),"
            "correo VARCHAR(30),"
            "FOREIGN KEY (rut) REFERENCES usuario(rut)"
            ");" 
        )
        (
            "CREATE TABLE investigador ("
            "id_investigador INTEGER PRIMARY KEY,"
            "nombre varchar(45),"
            "rut varchar(10),"
            "correo varchar(30),"
            ");"
        )
        (
            "CREATE TABLE libro ("
            "id_libro INTEGER PRIMARY KEY,"
            "titulo VARCHAR(50),"
            "autor VARCHAR(20),"
            "categoria VARCHAR(35),"
            "disponibilidad BOOLEAN"
            ");"
        )
        (
            "CREATE TABLE prestamo ("
            "id_prestamo INTEGER PRIMARY KEY,"
            "fecha_inicio DATE,"
            "fecha_fin DATE,"
            "estado VARCHAR(20),"
            "rut_usuario VARCHAR(10),"
            "id_libro INTEGER,"
            "FOREIGN KEY (rut_usuario) REFERENCES usuario(rut),"
            "FOREIGN KEY (id_libro) REFERENCES libro(id_libro)"
            ");"
        )
    ]

for query in tables:
    create_schema(query)

def create_usuario(
    nombre,
    rut,
    correo                      
):
    sql = (
        "INSERT INTO USUARIO(nombre,rut,correo)"
        "VALUES (:nombre,:rut,:correo)"
    )

    parametros = {
        "nombre": nombre,
        "rut": rut,
        "correo": correo,
    }

try: 
    with get_connection() as connection: 
        with connection.cursor() as cursor:
            cursor.execute(sql, parametros)
        connection.commit()
        print("Insercion de datos correcta")
except oracledb.DatabaseError as error:
    print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")

def create_estudiante (
    id_estudiante,
    nombre,
    rut,
    correo                      
):
    sql =(
        "INSERT INTO ESTUDIANTE(id_estudiante,nombre,rut,correo)"
        "VALUES (:id_estudiante,:nombre,:rut,:correo)"
    )

    parametros = {
        "id_estudiante":id_estudiante,
        "nombre": nombre,
        "rut": rut,
        "correo": correo,
    }



def create_docente (
    id_docente,
    nombre,
    rut,
    correo                      
):
    sql =(
        "INSERT INTO DOCENTE(id_docente,nombre,rut,correo)"
        "VALUES (:id_docente,:nombre,:rut,:correo)"
    )

    parametros = {
        "id_docente":id_docente,
        "nombre": nombre,
        "rut": rut,
        "correo": correo,
    }



def create_investigador (
    id_investigador,
    nombre,
    rut,
    correo                      
):
    sql =(
        "INSERT INTO INVESTIGADOR(id_investigador,nombre,rut,correo)"
        "VALUES (:id_investigador,:nombre,:rut,:correo)"
    )

    parametros = {
        "id_investigador":id_investigador,
        "nombre": nombre,
        "rut": rut,
        "correo": correo,
    }



def create_libro (
    id_libro,
    titulo,
    autor,
    categoria,
    disponibilidad

):
    sql =(
        "INSERT INTO LIBRO(id_libro,titulo,autor,categoria,disponibilidad)"
        "VALUES(:id_libro,:titulo,:autor,:categoria,:disponibilidad)"
    )

    parametros ={
        "id_libro": id_libro,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponibilidad": disponibilidad,
    }

def create_prestamo (
    id_prestamo,
    fecha_inicio,
    fecha_fin,
    estado,
    rut_usuario,
    id_libro
):
    
    
    sql =(
        "INSERT INTO PRESTAMO(id_prestamo,fecha_inicio,fecha_fin,estado,rut_usuario,id_libro)"
        "VALUES (:id_prestamo,:fecha_inicio,:fecha_fin,:estado,:rut_usuario,:id_libro)"
)

    parametros = {
        "id_prestamo":id_prestamo,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "estado": estado,
        "rut_usuario": rut_usuario,
        "id_libro": id_libro
    }



def read_usuario():
    sql =(
        "SELECT * FROM USUARIO"
    )
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error}\n {sql}")


def read_usuario_by_id(id: int):
    sql =(
        "SELECT * FROM USUARIO"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")


def read_estudiante():
    pass


def read_estudiante_by_id(id: int):
    sql =(
        "SELECT * FROM USUARIO"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")


def read_docente():
    pass


def read_docente_by_id(id: int):
    sql =(
        "SELECT * FROM DOCENTE WHERE id = :id"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")



def read_investigador():
    pass


def read_investigador_by_id(id: int):
    sql =(
        "SELECT * FROM USUARIO"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")


def read_libro():
    pass


def read_libro_by_id(id: int):
    sql =(
        "SELECT * FROM USUARIO"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")


def read_prestamo():
    pass


def read_prestamo_by_id(id: int):
    sql =(
        "SELECT * FROM USUARIO"
    )
    parametros = {"id" : id}
    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")