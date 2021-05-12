import threading
from datetime import datetime
import helper
import time


class Bot(object):

    def __init__(self, moeda=None, data=datetime.utcnow(), open=None,
                 low=None, high=None, close=None):
        self.moeda = moeda
        self.data = data
        self.open = open
        self.low = low
        self.high = high
        self.close = close


class Candle(Bot):
    abertura1 = helper.open_teste()

    def __init__(self, periodicidade=None, hora=None):
        self.periodicidade = periodicidade
        self.hora = hora
        super().__init__()

    def bitcoin_candle(self, moeda=helper.buscar_moeda(),
                       data=helper.buscar_data(), open=helper.open_teste(),
                       low=helper.low(), high=helper.high(), close=None, periodicidade=1):
        t = threading.Timer(10.0, lambda: bitcoin_candle)
        last1 = helper.last_close()
        self.moeda = moeda
        self.open = open
        self.low = low
        self.high = high
        self.close = close
        self.data = data
        self.close = helper.last_close()
        self.periodicidade = periodicidade

        return self.moeda, self.open, self.low, self.high, self.close, self.data, self.periodicidade


candle1 = Candle()
print(candle1.bitcoin_candle())


