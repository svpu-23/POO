# ESTE EJEMPLO ABARCA 
#EL USO DE INPUTS, LABELS Y BOTONES
#PARA FAMILIARIZARSE QUE COSAS BASICAS
#DE FUNCIONALIDAD PODEMOS LOGRAR CON FLET

# 1. paso: Importar flet
import flet as ft 

# 2. paso: Crear la clase de la App 
class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Hola nombre"

        self.input_nombre = ft.TextField( hint_text="Ingresa tu nombre" )
        self.button_saludar = ft.Button( text="Saludar", on_click=self.handle_saludo )
        self.text_saludo = ft.Text( value="" )

        self.build()

    def build(self):
        self.page.add(
            self.input_nombre,
            self.button_saludar,
            self.text_saludo
        )
        self.page.update()

    def handle_saludo(self, e):
        nombre = (self.input_nombre.value or "").strip()
        if nombre:
            self.text_saludo.value = f"Hola, {nombre}"
        else:
            self.text_saludo.value = "Ingrese su nombre"
        self.page.update()

# 3. Paso: Ejecutar       
if __name__ == "__main__":
    ft.app(target=App)
