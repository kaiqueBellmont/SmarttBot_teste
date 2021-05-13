import json
import requests
from datetime import datetime

_PUBLIC_URL = 'https://poloniex.com/public?command=returnTicker'


def buscar_api():
    request = requests.get(_PUBLIC_URL)
    teste = json.loads(request.content)
    teste1 = teste['BTC_BTS']
    return teste1


def buscar_moeda():
    moeda = 'BTC_BTS'
    return moeda


def buscar_data():
    data = str(datetime.now())
    return data


def last_open():
    last = buscar_api()['last']
    return last


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


def buscar_api2():
    request = requests.get(_PUBLIC_URL)
    teste = json.loads(request.content)
    teste1 = teste['BTC_XMR']
    return teste1


def buscar_moeda2():
    moeda = 'BTC_XMR'
    return moeda


def buscar_data2():
    data = str(datetime.now())
    return data


def last_open2():
    last = buscar_api2()['last']
    return last


def last_close2():
    close = buscar_api2()['last']
    return close


def low2():
    low = buscar_api2()['low24hr']
    return low


def high2():
    high = buscar_api2()['high24hr']
    return high
