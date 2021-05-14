SET TIME ZONE 'UTC';

CREATE TABLE IF NOT EXISTS candle (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    MOEDA varchar(15) NOT NULL,
    periodicidade INT(3) NOT NULL,
    datetime datetime NOT NULL,
    open decimal(16, 8) NOT NULL,
    low decimal(16, 8) NOT NULL,
    high decimal(16, 8) NOT NULL,
    close decimal(16, 8) NOT NULL
);
