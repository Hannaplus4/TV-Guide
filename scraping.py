import requests
from bs4 import BeautifulSoup
import json

# URL de la página de programación de TV de Disney NL
url = 'https://tv.disney.nl/tv-gids'

# Realiza una solicitud a la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Analiza el HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra los elementos que contienen la información de la programación
    schedule_items = soup.find_all('div', class_='schedule-item')  # Ajusta según la estructura real

    # Extrae y estructura la información
    program_data = []
    for item in schedule_items:
        title = item.find('h3').text.strip()  # Ajusta según la estructura real
        time = item.find('div', class_='schedule-time').text.strip()  # Ajusta según la estructura real
        program_data.append({
            'title': title,
            'time': time
        })
    
    # Guarda la programación en un archivo JSON
    with open('programacion.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(program_data, jsonfile, ensure_ascii=False, indent=4)
else:
    print('No se pudo acceder a la página')
