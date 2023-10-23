import requests
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = 'https://wdp-smart-home.azurewebsites.net'

def getData():
    res = requests.get(BASE_URL)
    data = res.json()

    return data

def updateTemp(temp):
    res = requests.post(BASE_URL + '/temp', json={
        "temp": temp,
        "API_KEY": API_KEY
    })
        
    data = res.json()

    return data
