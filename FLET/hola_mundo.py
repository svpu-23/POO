# 1. paso: Importar flet
import flet as ft 

# 2. paso: Clase principal de al aplicacion 
class App:
    def __init__(self, page: ft.Page):
        self.page = page 
        self.page.title = "Hola mundo"
        #Siempre como ultima linea de __init__
        self.build()
    # Metodo principal para agregar elementos
    # En mi pagina/aplicacion
    def build(self):
        self.page.add(
            ft.Text("Hola mundo")
        )
# 3. Paso: Inicializar app
if __name__ == "__main__":
    ft.app(target=App)  