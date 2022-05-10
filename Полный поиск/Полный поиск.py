import sys
from io import BytesIO
import requests
from PIL import Image
from map import get_coordinates

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    print('error')
    exit()

json_response = response.json()
ll, spn = get_coordinates(json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"])

map_params = {
    "ll": f"{ll[0]},{ll[1]}",
    "spn": f"{spn[0]},{spn[1]}",
    "l": "map",
    "pt": f"{ll[0]},{ll[1]},pm2dgl"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
