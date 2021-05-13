from datetime import datetime
import helper
import time


while True:
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
            self.last = helper.last_close()
            self.periodicidade = periodicidade
            self.hora = hora
            super().__init__()

        def bitcoin_candle(self, moeda=helper.buscar_moeda(),
                           data=helper.buscar_data(), open=helper.open_teste(),
                           low=helper.low(), high=helper.high(),
                           close=None, periodicidade=1, last=helper.last_close()):
            self.last = last
            self.moeda = moeda
            self.open = open
            self.low = low
            self.high = high
            self.close = close
            self.data = data
            self.close = helper.last_close()
            self.periodicidade = periodicidade

            return self.moeda, self.open, self.low, self.high, self.close, self.data, self.periodicidade


    candle = Candle()

    candle1 = candle.bitcoin_candle()
    print(f'abertura   : {candle1}')
    # mudar valr até aqui candle.open = 10

    x = 1
    while x < 11:
        candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                 open=candle.open, low=helper.low(),
                                                 high=helper.high(), data=helper.buscar_data(),
                                                 close=helper.last_close())
        # modo de fazer acesso
        # print(candle1[1])
        print(f'Candle de 1 {candle_1_fechado} x = {x}')

        if x == 5:
            candle_5_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=candle1[1], low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close(), periodicidade=5)

            print(f'candle de 5 : {candle_5_fechado} x = {x}')

        if x == 10:
            candle_10_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                      open=candle1[1], low=helper.low(),
                                                      high=helper.high(), data=helper.buscar_data(),
                                                      close=helper.last_close(), periodicidade=10)
            print(f'candle de 10 : {candle_10_fechado} x = {x}')

        x += 1
        time.sleep(5)
