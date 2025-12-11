import bcrypt 

# Paso 1. Obtener contraseña en plano
incoming_password = input("Ingresa tu contraseña: ").encode("UTF-8")
# Paso 2. crear un pedazo de sal
salt = bcrypt.gensalt(rounds=12)
# Paso 3. Hashear la contraseña en plano y dar una sal al hasheo
hased_password = bcrypt.hashpw(password=incoming_password, salt=salt)
print("Cpntraseña haseada", hased_password)
# Paso 4. Ingresar demuevo la contraseña
confirm_password = input("Ingrese nuevamente la contraseña: ").encode("UTF-8")
# Paso 5. Comparar/berificar contraseñas
if bcrypt.checkpw(confirm_password, hased_password):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

