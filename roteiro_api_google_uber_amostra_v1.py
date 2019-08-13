import googlemaps
import sqlite3
import random
import time
import datetime
import exemplo_banco_dados
import os
from datetime import datetime
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

try:
    read_input = raw_input
except NameError:   
    read_input = input

    
# banco de dados
os.remove("base_artigo_rae.db") if os.path.exists("base_artigo_rae.db") else None 
# Criando uma conexão
conn = sqlite3.connect('base_artigo_rae.db')   
# Criando um cursor
c = conn.cursor()

c.execute('create table tb_api_uber_pickup_time '\
           '(id_consulta integer, '\
           'json_retorno_api text, '\
           'dt_hora_consulta text)')
  

c.execute('create table tb_api_uber_estimate_price'\
           '(id_consulta integer, '\
           'json_retorno_api text, '\
           'dt_hora_consulta text)')

c.execute('create table tb_api_google_directions'\
           '(id_consulta integer, '\
           'json_retorno_api text, '\
           'dt_hora_consulta datetime)')
# banco de dados 


# session api uber
session = Session(server_token='N4kkHZ1kZr8g-ikt_6NruXcuZKAVIfHMyez6GxwW')
client = UberRidesClient(session)

#estimete price
def uber_get_price_estimates(p_client, p_start_latitude, p_start_longitude, p_end_latitude, p_end_longitude) :
    response = p_client.get_price_estimates(start_latitude = p_start_latitude,
                                            start_longitude = p_start_longitude,
                                            end_latitude = p_end_latitude,
                                            end_longitude = p_end_longitude,
                                            seat_count=2)
    estimate = response.json.get('prices')
    print("estimete price :", estimate)


self.uber_get_price_estimates(client, -23.5598988,)

response = client.get_pickup_time_estimates( 
    start_latitude=-23.5891262,
    start_longitude=-46.644738499,
   )

estimate_time = response.json.get('times')
print("estimete time price :", estimate_time)


# api google maps 
gmaps = googlemaps.Client(key='AIzaSyCd9P9D2WjCaT8UBaq8H1fU4nvTSgdEWIQ')


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Rua Itapeva, 432 - São Paulo",
                                     "Rua Baronesa de Bela vista, 108 - São Paulo",
                                     #alternatives=True,
                                     mode="driving",
                                     departure_time=now)


#leitura do JSON de retorno
for i, rota in enumerate(directions_result, 1):
 #   print("bounds print - ", rota['bounds'])
 #   print("distance print - ", rota['legs'][0]['distance']['text'])
 #   print("duration print - ", rota['legs'][0]['duration']['text'])
    distancia = rota['legs'][0]['distance']['text']
    tempo = rota['legs'][0]['duration']['text']
    tempo_transito = rota['legs'][0]['duration_in_traffic']['text']
 #Exibe o resultado
    print(u'{0}. A distancia è: {1} - O tempo:{2} - O tempo no transito :{3}'.format(i, distancia, tempo, tempo_transito))

        
print(rota)

response = client.get_pickup_time_estimates( 
    start_latitude=-23.5891262,
    start_longitude=-46.644738499,
   )

estimate_time = response.json.get('times')
print("estimete time price :", estimate_time)
