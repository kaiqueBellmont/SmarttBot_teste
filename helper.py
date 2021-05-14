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
    data = str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    return data


def last_open():
    last = buscar_api()['last']
    return last


def last_close():
    last_open()
    close = buscar_api()['last']
    return close


def low():
    return buscar_api()['low24hr']


def high():
    return buscar_api()['high24hr']


def buscar_api2():
    request = requests.get(_PUBLIC_URL)
    teste = json.loads(request.content)
    teste1 = teste['BTC_XMR']
    return teste1


def buscar_moeda2():
    return 'BTC_XMR'


def buscar_data2():
    return str(datetime.now())


def last_open2():
    return buscar_api2()['last']


def last_close2():
    return buscar_api2()['last']


def low2():
    return buscar_api2()['low24hr']


def high2():
    return buscar_api2()['high24hr']

