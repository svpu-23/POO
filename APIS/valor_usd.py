import requests
# [Dónde está la API]----↓
base_url = "https://cl.dolarapi.com"
# [Protocolo]---↑

# Ruta o Endpoint que me dice el precio del dolar según CLP 
endpoint_dolar = "/v1/cotizaciones/usd"

# Juntamos la url y su endpoint para realizar una peticion de tipo GET  
respuesta = requests.get(f"{base_url}{endpoint_dolar}")
#                        ↑=https://cl.dolarapi.com/v1/cotizaciones/usd                         

try:
    # Serializamos la informacion en JSON para trabajarla de forma estructurada 
    data = respuesta.json()
    # Mostramos la data rescatada de la respuesta 
    print(data)
except:
    print(respuesta)


import requests

base_url = "https://mindicador.cl/api"
endpoint_euro = "/eur"

respuesta = requests.get(f"{base_url}{endpoint_euro}")

try:
    data = respuesta.json()
    print(data)
except:
    print(respuesta)


import requests

base_url = "https://mindicador.cl/api"
endpoint_uf = "/uf"

respuesta = requests.get(f"{base_url}{endpoint_uf}")

try:
    data = respuesta.json()
    print(data["serie"][0])
except:
    print(respuesta)


import requests

base_url = "https://mindicador.cl/api"
endpoint_ivp = "/ivp"

respuesta = requests.get(f"{base_url}{endpoint_ivp}")

try:
    data = respuesta.json()
    print(data["serie"][0])
except:
    print(respuesta)


import requests

base_url = "https://mindicador.cl/api"
endpoint_ipc = "/ipc"

respuesta = requests.get(f"{base_url}{endpoint_ipc}")

try:
    data = respuesta.json()
    print(data["serie"][0])
except:
    print(respuesta)



import requests

base_url = "https://mindicador.cl/api"
endpoint_utm = "/utm"

respuesta = requests.get(f"{base_url}{endpoint_utm}")

try:
    data = respuesta.json()
    print(data["serie"][0])
except:
    print(respuesta)
