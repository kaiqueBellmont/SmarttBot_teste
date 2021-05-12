import json
import requests
from datetime import datetime
import time

_PUBLIC_URL = 'https://poloniex.com/public?command=returnTicker'


def buscar_api():
    request = requests.get(_PUBLIC_URL)
    teste = json.loads(request.content)
    teste1 = teste['BTC_BTS']
    return teste1


def buscar_moeda():
    moeda = 'BTC_BTS'
    return moeda


def buscar_hora():
    a = str(datetime.now())
    a = a.split()
    data = a[0]
    hora = a[1].split('.')[0]
    return hora


def buscar_data():
    data = str(datetime.now())
    return data


def last_open():
    last = buscar_api()['last']
    return last


def open_teste():
    last_open()
    open = buscar_api()['last']
    return open


def last_close():
    last_open()
    close = buscar_api()['last']
    return close


def low():
    low = buscar_api()['low24hr']
    return low


def high():
    high = buscar_api()['high24hr']
    return high