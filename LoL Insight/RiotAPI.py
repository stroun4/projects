#Api

import requests

API_KEY = "Tu_clave_de_api"
REGION = "Tu_region" #Por ejemplo "NA1" para Norteamerica

def obtener_id_sumoner (name_sumoner):
    url = f"https://{REGION}.api.riotgames.com/lol/sumoner/v4/sumonner/by-name/{name_sumoner}?api_key={API_KEY}"
    responde = requests.get(url)
    
    if responde.status_code == 200:
        datos_sumoner = responde.json()
        return datos_sumoner["id"]
    
    else:
        print(f"Error al obtener datos del invocador. Codigo de estado: {responde.status_code}")
        return None
    
def obtener_estadisticas_partidas(id_sumoner):
    url = f"https://{REGION}.api.riotgames/lol/match/v4/matchlists/by-account/{id_sumoner}?api_key={API_KEY}"

#Ejemplo de uso 
name_sumoner = "nombre_de_tu_invocador"
id_sumoner = obtener_id_sumoner(name_sumoner)

if id_sumoner:
    estadisticas_partidas = obtener_estadisticas_partidas(id_sumoner)
    if estadisticas_partidas:
        print(f"Estadisticas de partidas para {name_sumoner}: {estadisticas_partidas}")
        
# -----------------------------------------------------------------------------------------------------------------------#

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#---------------------------------------------------------------------------------#

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
