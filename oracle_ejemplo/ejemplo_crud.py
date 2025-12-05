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
            "nombre VARCHAR2(45),"
            "rut VARCHAR2(10) PRIMARY KEY,"
            "correo VARCHAR2(30)"
            ")"
        ),
        (
            "CREATE TABLE estudiante ("
            "id_estudiante INTEGER PRIMARY KEY,"
            "nombre VARCHAR2(45),"
            "rut VARCHAR2(10),"
            "correo VARCHAR2(30),"
            "FOREIGN KEY (rut) REFERENCES usuario(rut)"
            ")"
        ),
        (
            "CREATE TABLE docente ("
            "id_docente INTEGER PRIMARY KEY,"
            "nombre VARCHAR2(45),"
            "rut VARCHAR2(10),"
            "correo VARCHAR2(30),"
            "FOREIGN KEY (rut) REFERENCES usuario(rut)"
            ")"
        ),
        (
            "CREATE TABLE investigador ("
            "id_investigador INTEGER PRIMARY KEY,"
            "nombre VARCHAR2(45),"
            "rut VARCHAR2(10),"
            "correo VARCHAR2(30)"
            ")"   
        ),
        (
            "CREATE TABLE libro ("
            "id_libro INTEGER PRIMARY KEY,"
            "titulo VARCHAR2(50),"
            "autor VARCHAR2(20),"
            "categoria VARCHAR2(35),"
            "disponibilidad NUMBER(1)"  
            ")"
        ),
        (
            "CREATE TABLE prestamo ("
            "id_prestamo INTEGER PRIMARY KEY,"
            "fecha_inicio DATE,"
            "fecha_fin DATE,"
            "estado VARCHAR2(20),"
            "rut_usuario VARCHAR2(10),"
            "id_libro INTEGER,"
            "FOREIGN KEY (rut_usuario) REFERENCES usuario(rut),"
            "FOREIGN KEY (id_libro) REFERENCES libro(id_libro)"
            ")"
        ),
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
        "fecha_inicio": datetime.strptime(fecha_inicio, "%d-%m-%Y"),
        "fecha_fin": datetime.strptime(fecha_fin, "%d-%m-%Y"),
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

def read_usuario_by_id(rut: str):
    sql =(
        "SELECT * FROM USUARIO WHERE rut = :rut"
    )
    parametros = {"rut" : rut}
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
        "SELECT * FROM ESTUDIANTE WHERE id_estudiante = :id"
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
        "SELECT * FROM DOCENTE WHERE id_docente = :id"
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
        "SELECT * FROM INVESTIGADOR WHERE id_investigador = :id"
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
        "SELECT * FROM LIBRO WHERE id_libro = :id"
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
        "SELECT * FROM PRESTAMO WHERE id_prestamo = :id"
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

    sql = f"UPDATE USUARIO SET {', '.join(modificaciones)} WHERE rut = :rut"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con RUT={rut} actualizado.")

def update_estudiante(
    id_estudiante: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id_estudiante": id_estudiante}

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

    sql = f"UPDATE ESTUDIANTE SET {', '.join(modificaciones)} WHERE id_estudiante = :id_estudiante"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id_estudiante} actualizado.")

def update_docente(
    id_docente: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id_docente": id_docente}

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

    sql = f"UPDATE DOCENTE SET {', '.join(modificaciones)} WHERE id_docente = :id_docente"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id_docente} actualizado.")

def update_investigador(
    id_investigador: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correo: Optional[str] = None

):
    modificaciones = []
    parametros = {"id_investigador": id_investigador}

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

    sql = f"UPDATE INVESTIGADOR SET {', '.join(modificaciones)} WHERE id_investigador = :id_investigador"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id_investigador} actualizado.")

def update_libro(
    id_libro: int,
    titulo: Optional[str] = None,
    autor: Optional[str] = None,
    categoria: Optional[str] = None,
    disponibilidad: Optional[bool] = None

):
    modificaciones = []
    parametros = {"id_libro": id_libro}

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
    
    

    sql = f"UPDATE LIBRO SET {', '.join(modificaciones)} WHERE id_libro = :id_libro"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id_libro} actualizado.")

def update_prestamo(
    id_prestamo: int,
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    estado: Optional[str] = None,
    rut_usuario: Optional[bool] = None,
    id_libro: Optional[int] = None

):
    modificaciones = []
    parametros = {"id_prestamo": id_prestamo}

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
    


    sql = f"UPDATE PRESTAMO SET {', '.join(modificaciones)} WHERE id_prestamo = :id_prestamo"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id_prestamo} actualizado.")


#eliminacion de datos 

def delete_usuario(rut: str):
    sql = (
        "DELETE FROM USUARIO WHERE rut = :rut"
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

def delete_estudiante(id_estudiante: int):
    sql = (
        "DELETE FROM ESTUDIANTE WHERE id_estudiante = :id_estudiante"
    )
    parametros = {"id_estudiante" : id_estudiante}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_docente(id_docente: int):
    sql = (
        "DELETE FROM DOCENTE WHERE id_docente = :id_docente"
    )
    parametros = {"id_docente" : id_docente}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_investigador(id_investigador: int):
    sql = (
        "DELETE FROM INVESTIGADOR WHERE id_investigador = :id_investigador"
    )
    parametros = {"id_investigador" : id_investigador}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_libro(id_libro: int):
    sql = (
        "DELETE FROM LIBRO WHERE id_libro = :id_libro"
    )
    parametros = {"id_libro" : id_libro}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_prestamo(id_prestamo: int):
    sql = (
        "DELETE FROM PRESTAMO WHERE id_prestamo = :id_prestamo"
    )
    parametros = {"id_prestamo" : id_prestamo}

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

def menu_estudiante():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |       Menu: Estudiantes          |
                |----------------------------------|
                | 1. Insertar Estudiante           |
                | 2. Consultar Estudiantes         |
                | 3. Consultar Estudiante por ID   |
                | 4. Modificar Estudiante          |
                | 5. Eliminar Estudiante           |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-5, 0]: ")

        if opcion == "1":
            os.system("cls")
            print("1. Insertar Estudiante")
            id = input("ID Estudiante: ")
            nombre = input("Nombre: ")
            rut = input("RUT (debe existir primero en Usuario): ")
            correo = input("Correo: ")
            create_estudiante(id, nombre, rut, correo)
            input("ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("2. Consultar Estudiantes")
            read_estudiante()
            input("ENTER...")

        elif opcion == "3":
            os.system("cls")
            id = input("ID Estudiante: ")
            read_estudiante_by_id(id)
            input("ENTER...")

        elif opcion == "4":
            os.system("cls")
            id = input("ID a modificar: ")
            print("[Deje vacío para no modificar]")
            nombre = input("Nuevo nombre: ")
            rut = input("Nuevo rut: ")
            correo = input("Nuevo correo: ")

            if nombre.strip()== "": nombre=None
            if rut.strip()== "": rut=None
            if correo.strip()== "": correo=None

            update_estudiante(id, nombre, rut, correo)
            input("ENTER...")

        elif opcion == "5":
            os.system("cls")
            id = input("ID a eliminar: ")
            delete_estudiante(id)
            input("ENTER...")

        elif opcion == "0":
            break

        else:
            print("Opción incorrecta")
            input("ENTER...")

def menu_docente():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |          Menu: Docentes          |
                |----------------------------------|
                | 1. Insertar Docente              |
                | 2. Consultar Docentes            |
                | 3. Consultar Docente por ID      |
                | 4. Modificar Docente             |
                | 5. Eliminar Docente              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige opción: ")

        if opcion=="1":
            id=input("ID Docente: ")
            nombre=input("Nombre: ")
            rut=input("RUT usuario: ")
            correo=input("Correo: ")
            create_docente(id,nombre,rut,correo)
            input("ENTER...")

        elif opcion=="2": read_docente(); input("ENTER...")
        elif opcion=="3": read_docente_by_id(input("ID: ")); input("ENTER...")

        elif opcion=="4":
            id=input("ID a modificar: ")
            nombre=input("Nuevo nombre: ") or None
            rut=input("Nuevo rut: ") or None
            correo=input("Nuevo correo: ") or None
            update_docente(id,nombre,rut,correo)
            input("ENTER...")

        elif opcion=="5": delete_docente(input("ID: ")); input("ENTER...")
        elif opcion=="0": break
        else: input("Opción incorrecta...")

def menu_investigador():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |       Menu: Investigadores       |
                |----------------------------------|
                | 1. Insertar Investigador         |
                | 2. Consultar Investigadores      |
                | 3. Consultar Investigador por ID |
                | 4. Modificar Investigador        |
                | 5. Eliminar Investigador         |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion=input("Opción: ")

        if opcion=="1":
            id=input("ID: ")
            nombre=input("Nombre: ")
            rut=input("RUT usuario: ")
            correo=input("Correo: ")
            create_investigador(id,nombre,rut,correo)
            input("ENTER...")

        elif opcion=="2": read_investigador(); input("ENTER...")
        elif opcion=="3": read_investigador_by_id(input("ID: ")); input("ENTER...")

        elif opcion=="4":
            id=input("ID modificar: ")
            nombre=input("Nombre: ") or None
            rut=input("RUT: ") or None
            correo=input("Correo: ") or None
            update_investigador(id,nombre,rut,correo)
            input("ENTER...")

        elif opcion=="5": delete_investigador(input("ID: ")); input("ENTER...")
        elif opcion=="0": break

def menu_libro():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |           Menu: Libros           |
                |----------------------------------|
                | 1. Insertar Libro                |
                | 2. Consultar Libros              |
                | 3. Consultar Libro por ID        |
                | 4. Modificar Libro               |
                | 5. Eliminar Libro                |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion=input("Opción: ")

        if opcion=="1":
            id=input("ID libro: ")
            titulo=input("Título: ")
            autor=input("Autor: ")
            categoria=input("Categoría: ")
            disponibilidad=input("Disponible (1/0): ")
            create_libro(id,titulo,autor,categoria,disponibilidad)
            input("ENTER...")

        elif opcion=="2": read_libro(); input("ENTER...")
        elif opcion=="3": read_libro_by_id(input("ID libro: ")); input("ENTER...")

        elif opcion=="4":
            id=input("ID libro: ")
            titulo=input("Nuevo título: ") or None
            autor=input("Nuevo autor: ") or None
            categoria=input("Nueva categoría: ") or None
            disponibilidad=input("Disponible(1/0): ") or None
            update_libro(id,titulo,autor,categoria,disponibilidad)
            input("ENTER...")

        elif opcion=="5": delete_libro(input("ID libro: ")); input("ENTER...")
        elif opcion=="0": break
def menu_prestamo():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |         Menu: Prestamos          |
                |----------------------------------|
                | 1. Registrar Prestamo            |
                | 2. Consultar Prestamos           |
                | 3. Consultar Prestamo por ID     |
                | 4. Modificar Prestamo            |
                | 5. Eliminar Prestamo             |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion=input("Opción: ")

        if opcion=="1":
            id=input("ID prestamo: ")
            fi=input("Fecha inicio: ")
            ff=input("Fecha fin: ")
            estado=input("Estado: ")

            print("\nUsuarios disponibles:")
            read_usuario()
            rut=input("RUT usuario: ")

            print("\nLibros disponibles:")
            read_libro()
            id_l=input("ID libro: ")

            create_prestamo(id,fi,ff,estado,rut,id_l)
            input("ENTER...")

        elif opcion=="2": read_prestamo(); input("ENTER...")
        elif opcion=="3": read_prestamo_by_id(input("ID prestamo: ")); input("ENTER...")

        elif opcion=="4":
            id=input("ID modificar: ")
            fi=input("Fecha inicio: ") or None
            ff=input("Fecha fin: ") or None
            estado=input("Estado: ") or None
            rut=input("Nuevo rut usuario: ") or None
            id_l=input("Nuevo id libro: ") or None

            update_prestamo(id,fi,ff,estado,rut,id_l)
            input("ENTER...")

        elif opcion=="5": delete_prestamo(input("ID: ")); input("ENTER...")
        elif opcion=="0": break

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
            menu_estudiante()
        elif opcion == "4":
            menu_docente()  
        elif opcion == "5":
            menu_investigador()  
        elif opcion == "6":
            menu_libro()  
        elif opcion == "7":
            menu_prestamo()  

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