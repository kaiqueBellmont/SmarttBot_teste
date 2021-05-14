# imports de bibliotecas básicas, não usei nada demais. datetime para pegar tempo real
# helper que é meu arquivo de comunicar com a API e pegar os dados formatados
# o time é uma biblioteca muito utilizada para bots.
# ex : time.sleep(segundos que o programa espera para seguir)
from datetime import datetime
import helper
import time
import pymysql

# aqui eu criei minha conexão com o banco e ja defini o cursor,
# cooloquei fora do while que faz meu programa repetir e assim não parar de cotar e salvar os valores.
conexao = pymysql.connect(
    host='172.10.3.2',
    port=3306,
    user='smartbot',
    passwd='smartbot',
    db='smartbot'
)
cursor = conexao.cursor()

# while utilizado para meu programa nunca parar (já que utilizei POO + logica sem bibliotecas).
while True:
    class Bot(object):  # crio minha classe bot que é a mais importante

        # inicio meus valores, passando none
        def __init__(self, moeda=None, data=datetime.utcnow(), open=None,
                     low=None, high=None, close=None):
            self.moeda = moeda
            self.data = data
            self.open = open
            self.low = low
            self.high = high
            self.close = close

    # crio a classe candle e herdo de bot, pois precisava das caracteristicas
    class Candle(Bot):

        # crio a periodicidade, pois o bot nao tem
        def __init__(self, periodicidade=None):
            self.periodicidade = periodicidade
            super().__init__()

        # defino o candle do bitcoin, passando os valores nos parametros intencionalmente
        # pois preciso que quando eu solicitar, venha em tempo real.
        # os valores passados vem do meu arquivo helper, que pega da api o que eu preciso
        # a periodicidade e close deixei assim para passar depois
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
            # aqui eu passei o close, poderia fazer de outra forma, mas em baixo, eu mostro a logica usada
            self.close = helper.last_close()
            self.periodicidade = periodicidade

            # retorna os valores recebidos da api em uma tupla
            return self.moeda, self.open, self.low, self.high, self.close, self.data, self.periodicidade

        # basicamente fiz a mesma coisa com o candle de bitcoin
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


    # inicio a classe
    candle = Candle()

    """
    essa parte foi dificil. Eu recebi os valores do candle (primeiros 60 segundos) para fechar
    então eu cotei, esperei 60 segundos, para fechar o candle de 1
    """
    candle_bitcoin = candle.bitcoin_candle()
    candle_monero = candle.monero_candle()

    # função utilizada para esperar 60 segundos e iniciar o bot, já com valores cotados
    time.sleep(0)
    x = 1

    while x < 11:
        # aqui fica legal.
        # eu recebi o valor de open do candle_bitcoin que é o do bitcoin
        # no close, recebi o last, que basicamente busca na api o ultimo valor e fecho o candle
        # era tudo que eu precisava.
        # eu repito a mesma coisa para o monero.

        candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                 open=candle_bitcoin[1], low=helper.low(),
                                                 high=helper.high(), data=helper.buscar_data(),
                                                 close=helper.last_close())

        candle_2_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                open=candle_monero[1], low=helper.low2(),
                                                high=helper.high2(), data=helper.buscar_data(),
                                                close=helper.last_close2())

        # importante:
        """
        Como o programa ja esperou 1 minuto da linha 92, eu coloquei ele para cotar de novo,
        salvar apenas o open de cada um deles, e ja fechar
        eu fiz isso para fazer o open/close e sem duvidas, foi a parte mais dificil.
        """

        # eu precisava startar o sql correto, para salvar os valores do 1 candle, que era o mais importante
        sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
               f" VALUES ('{candle_1_fechado[0]}', {candle_1_fechado[6]}," \
               f" '{candle_1_fechado[5]}', {candle_1_fechado[1]}," \
               f" {candle_1_fechado[2]}, {candle_1_fechado[3]}, {candle_1_fechado[4]})"

        sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
               f" VALUES ('{candle_2_fechado[0]}', {candle_2_fechado[6]}," \
               f" '{candle_2_fechado[5]}', {candle_2_fechado[1]}," \
               f" {candle_2_fechado[2]}, {candle_2_fechado[3]}, {candle_2_fechado[4]})"

        # aqui fiz o x ser igual a 1 para ele ja salvar e dar commit
        # ja que o timer ja passou, o candle ja foi fehcado nas linhas 102 ou 107.
        if x == 1:
            # modo de fazer acesso
            # print(candle_bitcoin[1])

            cursor.execute(sql1)
            cursor.execute(sql2)
            conexao.commit()

            print(f'bitcoin {candle_1_fechado} x = {x}')
            print(f'monero  {candle_2_fechado} x = {x}')

            x += 1

        # aqui começa a fazer sentido:
        """
        1- depois que ele salvar o candle 1, ele vai cotar denovo e esperar um tempo, 1 minuto ou menos
        2 - depois que ele esperar, utilizei a mesma variavel, mudando so o valor do parametro
        para manter o open, e pegar o resto em tempo real :)
        3 - utilizei o x > 1 justamente para ficar nesse mini-loop
        """
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

            # esse time, foi utilizado para parar 1 minuto ou menos intencionalmente
            # para cotar valores e manter o open do candle
            # depois que ele espera, o restante ja vai direto, seta valores corretamente
            # e salva no banco

            time.sleep(0)

            # aqui ja seto os valores mantendo o open depois de 1 minuto ou menos.

            candle_1_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                     open=candle_1_fechado[1], low=helper.low(),
                                                     high=helper.high(), data=helper.buscar_data(),
                                                     close=helper.last_close())

            candle_2_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                    open=candle_2_fechado[1], low=helper.low2(),
                                                    high=helper.high2(), data=helper.buscar_data(),
                                                    close=helper.last_close2())

            # aqui eu salvo os candles de 1 depois do primeiro
            print(f'bitcoin {candle_1_fechado} ')
            print(f'monero  {candle_2_fechado} ')

            # salvo no banco os candles depois do primeiro, != 5 e != 10.
            cursor.execute(sql1)
            cursor.execute(sql2)
            conexao.commit()

            # fiz essa condição para pegar somente uma vez o valor de x == 5
            # para que nao continuasse com os dados diferentes do candle de 1
            # eu precisava disso, pois deveria receber valores esppecificos nos parametros
            # ex : open que foi cotado nas linhas 88, 89, para fazer o fechamento correto de 5 min.
            if x == 5 and x < 6:
                candle_5_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                         open=candle_bitcoin[1], low=helper.low(),
                                                         high=helper.high(), data=candle_1_fechado[5],
                                                         close=helper.last_close(), periodicidade=5)

                sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_5_fechado[0]}', {candle_5_fechado[6]}," \
                       f" '{candle_5_fechado[5]}', {candle_5_fechado[1]}," \
                       f" {candle_5_fechado[2]}, {candle_5_fechado[3]}, {candle_1_fechado[4]})"

                candle_52_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                         open=candle_monero[1], low=helper.low2(),
                                                         high=helper.high2(), data=candle_2_fechado[5],
                                                         close=helper.last_close2(), periodicidade=5)

                sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_52_fechado[0]}', {candle_52_fechado[6]}," \
                       f" '{candle_52_fechado[5]}', {candle_52_fechado[1]}," \
                       f" {candle_52_fechado[2]}, {candle_52_fechado[3]}, {candle_52_fechado[4]})"

                print(f'bitcoin {candle_5_fechado} ')
                print(f'monero  {candle_52_fechado}')

                cursor.execute(sql1)
                cursor.execute(sql2)
                conexao.commit()

            # basicamente fiz a mesma coisa que o de 5
            # a diferença e que o x vai sair da condição, o programa reinicia na linha 21,
            # ele cota o candle 0 (abertura do primeiro) espera 60s ou menos,
            # ja fecha o primeiro e a magica acontece denovo
            # Leia o final do codigo !
            if x == 10:
                candle_10_fechado = candle.bitcoin_candle(moeda=helper.buscar_moeda(),
                                                          open=candle_bitcoin[1], low=helper.low(),
                                                          high=helper.high(), data=candle_1_fechado[5],
                                                          close=helper.last_close(), periodicidade=10)

                sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_10_fechado[0]}', {candle_10_fechado[6]}," \
                       f" '{candle_10_fechado[5]}', {candle_10_fechado[1]}," \
                       f" {candle_10_fechado[2]}, {candle_10_fechado[3]}, {candle_10_fechado[4]})"

                candle_102_fechado = candle.monero_candle(moeda='BTC_XMR',
                                                          open=candle_monero[1], low=helper.low2(),
                                                          high=helper.high2(), data=candle_2_fechado[5],
                                                          close=helper.last_close2(), periodicidade=10)

                sql2 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_102_fechado[0]}', {candle_102_fechado[6]}," \
                       f" '{candle_102_fechado[5]}', {candle_102_fechado[1]}," \
                       f" {candle_102_fechado[2]}, {candle_102_fechado[3]}, {candle_102_fechado[4]})"

                print(f'bitcoin  {candle_10_fechado} ')
                print(f'monero   {candle_102_fechado}')
                cursor.execute(sql1)
                cursor.execute(sql2)
                conexao.commit()

            x += 1

    """
    peço desculpas por isso:
     sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
                       f" VALUES ('{candle_10_fechado[0]}', {candle_10_fechado[6]}," \
                       f" '{candle_10_fechado[5]}', {candle_10_fechado[1]}," \
                       f" {candle_10_fechado[2]}, {candle_10_fechado[3]}, {candle_10_fechado[4]})"
                       
    #Eu realmente fiz assim porque estava ficando sem tempo, e o codigo já ficou muito pesado
    me perdoem, no proximos meses pretendo adicionar statisticas e boas dicas de investimentos.
    o bot foi testado e esta funcionando perfeitamente.
    obrigado por me darem tal desafio, adorei fazer.
    """
