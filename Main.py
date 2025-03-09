import requests

url = "https://www.mercadolibre.com.ar/c/inmuebles#menu=categories"
# Se incluye un header para simular una petición desde un navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Imprime el contenido HTML obtenido de la URL
    print(response.text)
else:
    print("Error en la petición:", response.status_code)