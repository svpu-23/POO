from datetime import datetime
import oracledb
import os
from dotenv import load_dotenv
from typing import Optional
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

def create_all_tables():
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

    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
             cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")

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

    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")

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

    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")

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

    try: 
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")

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
        "fecha_inicio": datetime.striptime(fecha_inicio, "%d-%m-%Y"),
        "fecha_fin": datetime.striptime(fecha_fin, "%d-%m-%Y"),
        "estado": estado,
        "rut_usuario": rut_usuario,
        "id_libro": id_libro
    }

    try:    
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error}\n {sql} \n {parametros}")


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
        "SELECT * FROM USUARIO WHERE id = :id"
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

def read_estudiante():
    sql =(
        "SELECT * FROM ESTUDIANTE"
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

def read_estudiante_by_id(id: int):
    sql =(
        "SELECT * FROM ESTUDIANTE WHERE id = :id"
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

def read_docente():
    sql =(
        "SELECT * FROM DOCENTE"
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
    sql =(
        "SELECT * FROM INVESTIGADOR"
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

def read_investigador_by_id(id: int):
    sql =(
        "SELECT * FROM INVESTIGADOR WHERE id = :id"
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

def read_libro():
    sql =(
        "SELECT * FROM LIBRO"
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

def read_libro_by_id(id: int):
    sql =(
        "SELECT * FROM LIBRO WHERE id = :id"
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

def read_prestamo():
    sql =(
        "SELECT * FROM PRESTAMO"
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

def read_prestamo_by_id(id: int):
    sql =(
        "SELECT * FROM PRESTAMO WHERE id = :id"
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


#actualizacion de datos 

def update_usuario(
    rut: str,
    nombre: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"rut": rut}
 
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    
    if correo is not None:
        modificaciones.append("correo =: correo")
        parametros["correo"] = correo
    if not modificaciones:
        return print("no has enviado datos por modificar")

    sql = f"UPDATE ESTUDIANTE SET { ", ".join(modificaciones) } WHERE rut =: rut"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con RUT={rut} actualizado.")

def update_estudiante(
    id: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id": id}

    if rut is not None:
        modificaciones.append("rut =: rut")
        parametros["rut"] = rut
    
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    
    if correo is not None:
        modificaciones.append("correo =: correo")
        parametros["correo"] = correo
    if not modificaciones:
        return print("no has enviado datos por modificar")

    sql = f"UPDATE ESTUDIANTE SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")

def update_docente(
    id: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id": id}

    if rut is not None:
        modificaciones.append("rut =: rut")
        parametros["rut"] = rut
    
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    
    if correo is not None:
        modificaciones.append("correo =: correo")
        parametros["correo"] = correo
    if not modificaciones:
        return print("no has enviado datos por modificar")

    sql = f"UPDATE DOCENTE SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")

def update_investigador(
    id: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id": id}

    if rut is not None:
        modificaciones.append("rut =: rut")
        parametros["rut"] = rut
    
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    
    if correo is not None:
        modificaciones.append("correo =: correo")
        parametros["correo"] = correo
    if not modificaciones:
        return print("no has enviado datos por modificar")

    sql = f"UPDATE INVESTIGADOR SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")

def update_libro(
    id: int,
    titulo: Optional[str] = None,
    autor: Optional[str] = None,
    categoria: Optional[str] = None,
    disponibilidad: Optional[bool] = None

):
    modificaciones = []
    parametros = {"id": id}

    if titulo is not None:
        modificaciones.append("titulo =: titulo")
        parametros["titulo"] = titulo
    
    if autor is not None:
        modificaciones.append("autor =: autor")
        parametros["autor"] = autor
    
    if categoria is not None:
        modificaciones.append("categoria =: categoria")
        parametros["categoria"] = categoria

    if disponibilidad is not None:
        modificaciones.append("disponibilidad =: disponibilidad")
        parametros["disponibilidad"] = disponibilidad

    if not modificaciones:
        return print("no has enviado datos por modificar")
    
    

    sql = f"UPDATE libro SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")

def update_prestamo(
    id: int,
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    estado: Optional[str] = None,
    rut_usuario: Optional[bool] = None,
    id_libro: Optional[int] = None

):
    modificaciones = []
    parametros = {"id": id}

    if fecha_inicio is not None:
        modificaciones.append("fecha_inicio =: fecha_inicio")
        parametros["fecha_inicio"] = datetime.striptime(fecha_inicio, "Y%-m%-d%")

    if fecha_fin is not None:
        modificaciones.append("fecha_fin =: fecha_fin")
        parametros["fecha_fin"] = datetime.striptime(fecha_fin, "Y%-m%-d%")    
    
    if estado is not None:
        modificaciones.append("estado =: estado")
        parametros["estado"] = estado
    
    if rut_usuario is not None:
        modificaciones.append("rut_usuario =: rut_usuario")
        parametros["rut_usuario"] = rut_usuario

    if id_libro is not None:
        modificaciones.append("id_libro =: id_libro")
        parametros["id_libro"] = id_libro

    if not modificaciones:
        return print("no has enviado datos por modificar")
    
    

    sql = f"UPDATE PRESTAMO SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


#eliminacion de datos 

def delete_usuario(rut: str):
    sql = (
        "DELETE FROM USUARIO WHERE rut: rut"
    )
    parametros = {"rut" : rut}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_estudiante(id: int):
    sql = (
        "DELETE FROM ESTUDIANTE WHERE id: id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_docente(id: int):
    sql = (
        "DELETE FROM DOCENTE WHERE id: id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_investigador(id: int):
    sql = (
        "DELETE FROM INVESTIGADOR WHERE id: id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_libro(id: int):
    sql = (
        "DELETE FROM LIBRO WHERE id: id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_prestamo(id: int):
    sql = (
        "DELETE FROM PRESTAMO WHERE id: id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def menu_usuario():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |          Menu: Usuario           |
                |----------------------------------|
                | 1. Insertar Usuario              |
                | 2. Consultar Usuarios            |
                | 3. Consultar por RUT             |
                | 4. Modificar Usuario             |
                | 5. Eliminar Usuario              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-5, 0]: ")

        if opcion == "1":
            os.system("cls")
            print("1. Insertar Usuario")
            nombre = input("Ingrese nombre del usuario: ")
            rut = input("Ingrese RUT del usuario: ")
            correo = input("Ingrese correo del usuario: ")
            create_usuario(nombre, rut, correo)
            input("Ingrese ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los usuarios")
            read_usuario()
            input("Ingrese ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print("3. Consultar Usuario por RUT")
            rut = input("Ingrese RUT del usuario: ")
            read_usuario_by_id(rut)
            input("Ingrese ENTER para continuar...")

        elif opcion == "4":
            os.system("cls")
            print("4. Modificar Usuario")
            rut = input("Ingrese RUT del usuario a modificar: ")
            print("[Deje vacío lo que no desee modificar]")
            nombre = input("Nuevo nombre (opcional): ")
            correo = input("Nuevo correo (opcional): ")

            if len(nombre.strip()) == 0: nombre = None
            if len(correo.strip()) == 0: correo = None

            update_usuario(rut, nombre, correo)
            input("Ingrese ENTER para continuar...")

        elif opcion == "5":
            os.system("cls")
            print("5. Eliminar Usuario")
            rut = input("Ingrese RUT del usuario: ")
            delete_usuario(rut)
            input("Ingrese ENTER para continuar...")

        elif opcion == "0":
            os.system("cls")
            print("Volviendo...")
            break

        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def main():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |     CRUD Biblioteca (Oracle)     |
                |----------------------------------|
                | 1. Crear todas las tablas        |
                | 2. Gestionar Usuario             |
                | 3. Gestionar Estudiante          |
                | 4. Gestionar Docente             |
                | 5. Gestionar Investigador        |
                | 6. Gestionar Libro               |
                | 7. Gestionar Prestamo            |
                | 0. Salir del sistema             |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-7, 0]: ")

        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Ingrese ENTER para continuar...")

        elif opcion == "2":
            menu_usuario()
        elif opcion == "3":
            pass  
        elif opcion == "4":
            pass  
        elif opcion == "5":
            pass  
        elif opcion == "6":
            pass  
        elif opcion == "7":
            pass  

        elif opcion == "0":
            os.system("cls")
            print("Saliendo del sistema...")
            break

        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")


if __name__ == "__main__":
    main()


