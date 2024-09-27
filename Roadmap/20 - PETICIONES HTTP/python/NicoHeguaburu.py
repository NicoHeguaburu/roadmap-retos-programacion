import requests
import json
# response = requests.get("https://www.google.com/apfpaf")

# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Error codigo: {response.status_code}")

 
 
 
#extra
pokemon = input("Introduce el nombre del pokemon a buscar o su id").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print(f"Nombre:{data["name"]}")
    print(f"id:{data["id"]}")
    print(f"peso:{data["weight"]}")
    print(f"altura:{data["height"]}")
    for type in data["types"]:
        print(f"tipo:{type["type"]["name"]}")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Cadena de evolucion:")
            print(data["chain"]["species"]["name"])
        else:
            print(f"ocurrio un error buscando las evoluciones: {response.status_code}")
    else:
        print(f"ocurrio un error buscando evoluciones: {response.status_code}")
else:
    print(f"ocurrio un error buscando al pokemon: {response.status_code}")