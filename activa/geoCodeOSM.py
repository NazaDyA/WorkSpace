import requests
import urllib.parse

def geoCodeLat(address:str):
    """return latitude of one direction
    Args:
        adress (str): be specific
    """
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    return response[0]["lat"]

def geoCodeLon(address:str):
    """return latitude of one direction
    Args:
        adress (str): be specific
    """
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    
    return response[0]["lon"]

def geoCodeLatLon(address:str):
    """return latitude of one direction
    Args:
        adress (str): be specific
    """

    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response)>0:
        return f'{response[0]["lat"]} * {response[0]["lon"]}'
    else:
        return "0*0"