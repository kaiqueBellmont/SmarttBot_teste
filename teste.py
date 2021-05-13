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
    time.sleep(60)
    x = 1
    while x < 11:

        candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                 open=candle1[1], low=helper.low(),
                                                 high=helper.high(), data=helper.buscar_data(),
                                                 close=helper.last_close())
        if x == 1:
            # modo de fazer acesso
            # print(candle1[1])
            print(f'Candle de 1 {candle_1_fechado} x = {x}')
            x += 1

        if x > 1:
            # isso serve para pegar o valor do open
            candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=helper.last_open(), low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close())
            time.sleep(60)

            candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=candle_1_fechado[1], low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close())

            print(f'Candle de 1 {candle_1_fechado} x = {x}')
            time.sleep(1)
            if x == 5:
                candle_5_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                         open=candle1[1], low=helper.low(),
                                                         high=helper.high(), data=candle_1_fechado[5],
                                                         close=candle_1_fechado[4], periodicidade=5)

                print(f'candle de 5 : {candle_5_fechado} x = {x}')

            if x == 10:
                candle_10_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                          open=candle1[1], low=helper.low(),
                                                          high=helper.high(), data=candle_1_fechado[5],
                                                          close=candle_1_fechado[4], periodicidade=10)
                print(f'candle de 10 : {candle_10_fechado} x = {x}')

            x += 1

    # arrumar o parametro do helper.lastclose linha 73
    # prestar atenção no close
