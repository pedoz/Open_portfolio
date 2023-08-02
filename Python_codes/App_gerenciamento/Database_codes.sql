
CREATE TABLE vendas_table(
id INTEGER PRIMARY KEY AUTOINCREMENT,  
data DATE NOT NULL,
categoria varchar(255) NOT NULL,       
valor float(10,2) NOT NULL);


CREATE TABLE sqlite_sequence(name,seq);


CREATE TABLE inventario_movel(
id INTEGER PRIMARY KEY AUTOINCREMENT,  
nome varchar(255),
valor FLOAT(10,2),
unidades INTEGER,
date DATE);


CREATE TABLE inventario_fixo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar(255),
valor float(10,2),
unidades INTEGER,
date DATE);


CREATE TABLE custos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar(255),
valor float(10,2),
data DATE);


CREATE TABLE despesas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar(255),
valor float(10,2),
data DATE);


CREATE TABLE custos_despesas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar(255),
valor float(10,2),
data DATE,
categoria VARCHAR(255));


CREATE TABLE inventario_perdido (
id INTEGER PRIMARY KEY AUTOINCREMENT,
inventario_id INTEGER,
nome VARCHAR(255),
unidades INTEGER,
data DATE,
FOREIGN KEY (inventario_id) REFERENCES inventario_movel (id))