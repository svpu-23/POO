import bcrypt
import requests
import oracledb
import os
import datetime
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

# =======================
# DATABASE
# =======================
class Database:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn

    def get_connection(self):
        return oracledb.connect(
            user=self.username,
            password=self.password,
            dsn=self.dsn
        )

    def query(self, sql: str, parameters: Optional[dict] = None):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parameters or {})

                if sql.strip().upper().startswith("SELECT"):
                    rows = cur.fetchall()

                    
                    fixed_rows = []
                    for row in rows:
                        fixed_row = []
                        for col in row:
                            if isinstance(col, oracledb.LOB):
                                fixed_row.append(col.read())
                            else:
                                fixed_row.append(col)
                        fixed_rows.append(tuple(fixed_row))

                    return fixed_rows

            conn.commit()


    def registrar_consulta(self, nombre_indicador, valor, fecha_indicador, usuario, fuente):
        sql = """
        INSERT INTO CONSULTA_INDICADOR
        (nombre_indicador, valor, fecha_indicador, fecha_consulta, usuario, fuente)
        VALUES
        (:nombre_indicador, :valor, :fecha_indicador, :fecha_consulta, :usuario, :fuente)
        """
        self.query(sql, {
            "nombre_indicador": nombre_indicador,
            "valor": valor,
            "fecha_indicador": fecha_indicador,
            "fecha_consulta": datetime.datetime.now(),
            "usuario": usuario,
            "fuente": fuente
        })


# =======================
# AUTH
# =======================
class Auth:
    @staticmethod
    def register(db: Database, id: int, username: str, password: str):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)

        db.query(
            "INSERT INTO USERS (id, username, password) VALUES (:id, :username, :password)",
            {"id": id, "username": username, "password": hashed}
        )
        print("Usuario registrado correctamente")

    @staticmethod
    def login(db: Database, username: str, password: str):
        rows = db.query(
            "SELECT password FROM USERS WHERE username = :username",
            {"username": username}
        )

        if len(rows) == 0:
            print("Usuario no encontrado")
            return False

        stored_hash = rows[0][0].read()   
        password_bytes = password.encode("utf-8")

        if bcrypt.checkpw(password_bytes, stored_hash):
            print("Login exitoso")
            return True
        else:
            print("Contraseña incorrecta")
            return False



# =======================
# FINANCE
# =======================
class Finance:
    def __init__(self):
        self.base_url = "https://mindicador.cl/api"

    def get_indicator(self, indicador: str):
        r = requests.get(f"{self.base_url}/{indicador}")
        data = r.json()
        serie = data["serie"][0]
        valor = serie["valor"]
        fecha = datetime.datetime.strptime(serie["fecha"][:10], "%Y-%m-%d")
        return valor, fecha

    def consultar_y_guardar(self, indicador, db, usuario):
        valor, fecha_indicador = self.get_indicator(indicador)
        print(f"{indicador.upper()} = {valor}")

        guardar = input("¿Desea guardar la consulta? (s/n): ").lower()
        if guardar == "s":
            db.registrar_consulta(
                nombre_indicador=indicador.upper(),
                valor=valor,
                fecha_indicador=fecha_indicador,
                usuario=usuario,
                fuente="https://mindicador.cl"
            )
            print("Consulta guardada en Oracle")


# =======================
# MENU
# =======================
def menu_indicadores(finance, db, usuario):
    while True:
        os.system("cls")
        print("""
=========================================
|     Menu: Indicadores Económicos      |
|---------------------------------------|
| 1. UF                                |
| 2. IVP                               |
| 3. IPC                               |
| 4. UTM                               |
| 5. Dólar                             |
| 6. Euro                              |
| 0. Salir                             |
=========================================
""")
        op = input("Seleccione una opción: ")

        if op == "1":
            finance.consultar_y_guardar("uf", db, usuario)
        elif op == "2":
            finance.consultar_y_guardar("ivp", db, usuario)
        elif op == "3":
            finance.consultar_y_guardar("ipc", db, usuario)
        elif op == "4":
            finance.consultar_y_guardar("utm", db, usuario)
        elif op == "5":
            finance.consultar_y_guardar("dolar", db, usuario)
        elif op == "6":
            finance.consultar_y_guardar("euro", db, usuario)
        elif op == "0":
            break
        else:
            print("Opción inválida")

        input("\nPresione ENTER para continuar...")


# =======================
# MAIN
# =======================
if __name__ == "__main__":
    db = Database(
        os.getenv("ORACLE_USER"),
        os.getenv("ORACLE_PASSWORD"),
        os.getenv("ORACLE_DSN")
    )

    # Auth.register(db, 1, "C##VICENTE_SEPULVEDA", "Inacap#2025")
    #Auth.register(db, 1, "C##VICENTE_SEPULVEDA", "Inacap#2025")

    Auth.login(db, "C##VICENTE_SEPULVEDA", "Inacap#2025")
    finance = Finance()
    menu_indicadores(finance, db, "C##VICENTE_SEPULVEDA")
