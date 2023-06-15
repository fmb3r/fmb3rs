import requests

url = 'https://swapi.dev/api'
responce = requests.get(url).json()

people_api = responce.get("people")
planets_api = responce.get("planets")
starships_api = responce.get("starships")


def check_peolple(url):
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        print(responce)

def check_planets(url):
    diametrs_list = []
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        diametrs_list.append({responce.get("name") : responce.get("diameter")})
    print(diametrs_list)

def check_starships(url):
    lenght_list = []
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        lenght_list.append({responce.get("name"): responce.get("lenght")})
    print(lenght_list)

check_starships(starships_api)