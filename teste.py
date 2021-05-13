sql1 = f"INSERT INTO `candle` (`MOEDA`, `periodicidade`, `datetime`, `open`, `low`, `high`, `close`)" \
       f" VALUES ('{candle_1_fechado[0]}', {candle_1_fechado[6]}," \
       f" '{candle_1_fechado[5]}', {candle_1_fechado[1]}," \
       f" {candle_1_fechado[2]}, {candle_1_fechado[3]}, {candle_1_fechado[4]})"
