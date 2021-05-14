from datetime import datetime
import helper
import time
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='kaique',
    passwd='Python@$123',
    db='teste_banco'
)
cursor = conexao.cursor()

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

        def __init__(self, periodicidade=None, hora=None):
            self.periodicidade = periodicidade
            self.hora = hora
            super().__init__()

        def bitcoin_candle(self, moeda=helper.buscar_moeda(),
                           data=helper.buscar_data(), open=helper.last_open(),
                           low=helper.low(), high=helper.high(),
                           close=None, periodicidade=1):
            self.moeda = moeda
            self.open = open
            self.low = low
            self.high = high
            self.close = close
            self.data = data
            self.close = helper.last_close()
            self.periodicidade = periodicidade

            return self.moeda, self.open, self.low, self.high, self.close, self.data, self.periodicidade

        def monero_candle(self, moeda='BTC_XMR',
                          data=helper.buscar_data(), open=helper.last_open2(),
                          low=helper.low2(), high=helper.high2(),
                          close=None, periodicidade=1):
            self.moeda = moeda
            self.open = open
            self.low = low
            self.high = high
            self.close = close
            self.data = data
            self.close = helper.last_close2()
            self.periodicidade = periodicidade

            return self.moeda, self.open, self.low, self.high, self.close, self.data, self.periodicidade


    candle = Candle()

    candle1 = candle.bitcoin_candle()
    candle2 = candle.monero_candle()

    time.sleep(60)
    x = 1

    while x < 11:

        candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                 open=candle1[1], low=helper.low(),
                                                 high=helper.high(), data=helper.buscar_data(),
                                                 close=helper.last_close())

        candle_2_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                open=candle2[1], low=helper.low2(),
                                                high=helper.high2(), data=helper.buscar_data(),
                                                close=helper.last_close2())

        sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
               f" VALUES ('{candle_1_fechado[0]}', {candle_1_fechado[6]}," \
               f" '{candle_1_fechado[5]}', {candle_1_fechado[1]}," \
               f" {candle_1_fechado[2]}, {candle_1_fechado[3]}, {candle_1_fechado[4]})"

        sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
               f" VALUES ('{candle_2_fechado[0]}', {candle_2_fechado[6]}," \
               f" '{candle_2_fechado[5]}', {candle_2_fechado[1]}," \
               f" {candle_2_fechado[2]}, {candle_2_fechado[3]}, {candle_2_fechado[4]})"

        if x == 1:
            # modo de fazer acesso
            # print(candle_bitcoin[1])

            cursor.execute(sql1)
            cursor.execute(sql2)
            conexao.commit()

            print(f'bitcoinde 1 {candle_1_fechado} x = {x}')
            print(f'monero de 1 {candle_2_fechado} x = {x}')

            x += 1

        if x > 1:
            # isso serve para pegar o valor do open
            candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=helper.last_open(), low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close())
            # monero
            candle_2_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                    open=helper.last_open2(), low=helper.low2(),
                                                    high=helper.high2(), data=helper.buscar_data(),
                                                    close=helper.last_close2())
            time.sleep(60)

            candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=candle_1_fechado[1], low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close())

            candle_2_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                    open=candle_2_fechado[1], low=helper.low2(),
                                                    high=helper.high2(), data=helper.buscar_data(),
                                                    close=helper.last_close2())

            print(f'monero  de 1 {candle_2_fechado} x = {x}')
            print(f'bitcoin de 1 {candle_1_fechado} x = {x}')
            cursor.execute(sql1)
            cursor.execute(sql2)
            conexao.commit()

            if x == 5 and x < 6:
                candle_5_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                         open=candle1[1], low=helper.low(),
                                                         high=helper.high(), data=candle_1_fechado[5],
                                                         close=helper.last_close(), periodicidade=5)

                sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_5_fechado[0]}', {candle_5_fechado[6]}," \
                       f" '{candle_5_fechado[5]}', {candle_5_fechado[1]}," \
                       f" {candle_5_fechado[2]}, {candle_5_fechado[3]}, {candle_1_fechado[4]})"

                candle_52_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                         open=candle2[1], low=helper.low2(),
                                                         high=helper.high2(), data=candle_2_fechado[5],
                                                         close=helper.last_close2(), periodicidade=5)

                sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_52_fechado[0]}', {candle_52_fechado[6]}," \
                       f" '{candle_52_fechado[5]}', {candle_52_fechado[1]}," \
                       f" {candle_52_fechado[2]}, {candle_52_fechado[3]}, {candle_52_fechado[4]})"

                cursor.execute(sql1)
                cursor.execute(sql2)
                conexao.commit()

            if x == 10:
                candle_10_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                          open=candle1[1], low=helper.low(),
                                                          high=helper.high(), data=candle_1_fechado[5],
                                                          close=helper.last_close(), periodicidade=10)

                sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_10_fechado[0]}', {candle_10_fechado[6]}," \
                       f" '{candle_10_fechado[5]}', {candle_10_fechado[1]}," \
                       f" {candle_10_fechado[2]}, {candle_10_fechado[3]}, {candle_10_fechado[4]})"

                candle_102_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                          open=candle2[1], low=helper.low2(),
                                                          high=helper.high2(), data=candle_2_fechado[5],
                                                          close=helper.last_close2(), periodicidade=10)

                sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_102_fechado[0]}', {candle_102_fechado[6]}," \
                       f" '{candle_102_fechado[5]}', {candle_102_fechado[1]}," \
                       f" {candle_102_fechado[2]}, {candle_102_fechado[3]}, {candle_102_fechado[4]})"

                print(f'bitcoin de 10 : {candle_10_fechado} x = {x}')
                print(f'monero de 10  : {candle_102_fechado} x = {x}')
                cursor.execute(sql1)
                cursor.execute(sql2)
                conexao.commit()

            x += 1
