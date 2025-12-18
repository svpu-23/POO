import bcrypt
import requests
import oracledb
import os
from dotenv import load_dotenv
from typing import Optional
import datetime

load_dotenv()

class Database:
    def __init__(self, username, dsn, password):
        self.username = username
        self.dsn = dsn
        self.password = password
    def get_connection(self):
        return oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
    def create_all_tables(self):
        tables = [
            (
                "CREATE TABLE USERS("
                "id INTEGER PRIMARY KEY,"
                "username VARCHAR(32) UNIQUE,"
                "password VARCHAR(128)"
                ")"
            )
        ]

        for table in tables:
            self.query(table)

    def query(self, sql: str, parameters: Optional[dict] = None):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    ejecucion = cur.execute(sql, parameters)
                    if sql.startswith("SELECT"):
                        resultado = []
                        for fila in ejecucion:
                            resultado.append(fila)
                        return resultado
                conn.commit()
        except oracledb.DatabaseError as error:
            print(error)


    def create_table_consulta_indicador(self):
        sql = """
        CREATE TABLE CONSULTA_INDICADOR (
            id_consulta NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nombre_indicador VARCHAR2(20),
            valor NUMBER(15,4),
            fecha_indicador DATE,
            fecha_consulta DATE,
            usuario VARCHAR2(32),
            fuente VARCHAR2(100)
        )
        """
        self.query(sql)


    def registrar_consulta(
    self,
    nombre_indicador,
    valor,
    fecha_indicador,
    usuario,
    fuente
):
        sql = """
        INSERT INTO CONSULTA_INDICADOR
        (nombre_indicador, valor, fecha_indicador, fecha_consulta, usuario, fuente)
        VALUES
        (:nombre_indicador, :valor, :fecha_indicador, :fecha_consulta, :usuario, :fuente)
        """

        parametros = {
            "nombre_indicador": nombre_indicador,
            "valor": valor,
            "fecha_indicador": fecha_indicador,
            "fecha_consulta": datetime.datetime.now(),
            "usuario": usuario,
            "fuente": fuente
        }

        self.query(sql, parametros)




class Auth:
    @staticmethod
    def login(db: Database, username: str, password: str):
        password = password.encode("UTF-8")

        resultado = db.query(
            "SELECT * FROM USERS WHERE username = :username",
            {"username": username}
        )

        if len(resultado) == 0:
            print("Usuario no encontrado")
            return False

        hashed_password = resultado[0][2].encode("UTF-8")

        if bcrypt.checkpw(password, hashed_password):
            print("Logeado correctamente")
            return True
        else:
            print("Contraseña incorrecta")
            return False


    @staticmethod
    def register(db: Database, id: int, username: str, password: str):
        print("registrando usuario")
        password = password.encode("UTF-8")
        salt = bcrypt.gensalt(12)
        hash_password = bcrypt.hashpw(password,salt)

        usuario = {
            "id": id,
            "username": username,
            "password": hash_password
        }

        db.query(
            sql= "INSERT INTO USERS(id,username,password) VALUES (:id, :username, :password)",
            parameters=usuario
        )
        print("usuario registrado con exito")

class Finance:
    def __init__(self, base_url: str = "https://mindicador.cl/api"):
        self.base_url = base_url
    def get_indicator(self, indicator: str, fecha: str = None) -> float:
        try:
            if not fecha:
                dd = datetime.datetime.now().day
                mm = datetime.datetime.now().month
                yyyy = datetime.datetime.now().year
                fecha = f"{dd}-{mm}-{yyyy}"
            url = f"{self.base_url}/{indicator}/{fecha}"
            respuesta = requests.get(url).json()
            return respuesta["serie"][0]["valor"]
        except:
            print("Hubo un error con la solicitud")
    def get_usd(self, fecha: str = None):
        valor = self.get_indicator("dolar", fecha)
        print(f"El valor del dolar en CLP es: {valor}")
    def get_eur(self, fecha: str = None):
        self.get_indicator("euro", fecha)
    def get_uf(self, fecha: str = None):
        self.get_indicator("uf", fecha)
    def get_ivp(self, fecha: str = None):
        self.get_indicator("ivp", fecha)
    def get_ipc(self, fecha: str = None):
        self.get_indicator("ipc", fecha)
    def get_utm(self, fecha: str = None):
        self.get_indicator("utm", fecha)
    
    def consultar_y_guardar(
    self,
    indicator: str,
    db,
    usuario: str,
    fecha: str = None
):
        try:
            valor = self.get_indicator(indicator, fecha)

            if valor is None:
                return

            print(f"{indicator.upper()} = {valor}")

            guardar = input("¿Desea guardar la consulta? (s/n): ").lower()

            if guardar == "s":
                if not fecha:
                    fecha_indicador = datetime.datetime.now()
                else:
                    fecha_indicador = datetime.datetime.strptime(fecha, "%d-%m-%Y")

                db.registrar_consulta(
                    nombre_indicador=indicator.upper(),
                    valor=valor,
                    fecha_indicador=fecha_indicador,
                    usuario=usuario,
                    fuente="https://mindicador.cl"
                )

                print("Consulta registrada en Oracle")

        except:
            print("Error al consultar o guardar el indicador")

def menu_indicadores(finance, db, usuario):
    while True:
        os.system("cls")  

        print(
            """
            =========================================
            |     Menu: Indicadores Económicos      |
            |---------------------------------------|
            | 1. Consultar Unidad de Fomento (UF)   |
            | 2. Consultar IVP                      |
            | 3. Consultar IPC                      |
            | 4. Consultar UTM                      |
            | 5. Consultar Dólar Observado          |
            | 6. Consultar Euro                     |
            | 0. Salir                              |
            =========================================
            """
        )

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            finance.consultar_y_guardar("uf", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            finance.consultar_y_guardar("ivp", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            finance.consultar_y_guardar("ipc", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            finance.consultar_y_guardar("utm", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            finance.consultar_y_guardar("dolar", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "6":
            finance.consultar_y_guardar("euro", db, usuario)
            input("\nPresione ENTER para continuar...")
        elif opcion == "0":
            print("Saliendo del menú de indicadores...")
            break
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar...")



if __name__ == "__main__":
    db = Database(
        username=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )

    Auth.register(db, 1, "C##VICENTE_SEPULVEDA", "Inacap#2025")


    # db.create_all_tables()
    # db.create_table_consulta_indicador()

    Auth.login(db, "C##VICENTE_SEPULVEDA", "Inacap#2025")
    finance = Finance()
    menu_indicadores(finance, db, "C##VICENTE_SEPULVEDA")


