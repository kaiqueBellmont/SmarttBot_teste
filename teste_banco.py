import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='kaique',
    passwd='Python@$123',
    db='teste_banco'
)


with conexao.cursor() as cursor:
    # Create a new record
    sql1 = "INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetimee`, `openn`, `low`, `high`, `closee`) VALUES ('BTC_XMR', 5, '2021/05/13 16:05:18', 0.00776482, 0.00776482, 0.00820000, 0.00776482)"
    cursor.execute(sql1)

conexao.commit()

