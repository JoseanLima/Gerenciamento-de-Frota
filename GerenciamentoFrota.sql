-- DROP DATABASE IF EXISTS GerenciamentoFrota;
-- CREATE DATABASE GerenciamentoFrota;
-- USE GerenciamentoFrota;

CREATE TABLE Motorista_Veiculo (
    ID_funcionario SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL,
    cpf VARCHAR(10) NOT NULL,
    quilometragemRodada SMALLINT UNSIGNED NOT NULL,
    consumo SMALLINT UNSIGNED NOT NULL,
    marca VARCHAR(8) NOT NULL,
    placa VARCHAR(5) UNIQUE NOT NULL
);

CREATE TABLE Destinatario (
    cep VARCHAR(8) NOT NULL,
    complemento VARCHAR(100),
    clienteNome VARCHAR(30) NOT NULL,
    ID_pedido SMALLINT unsigned PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE ObjetoTransporte (
    mercadoria VARCHAR(20) NOT NULL,
    peso SMALLINT unsigned NOT NULL,
    tipoMercadoria VARCHAR(20) NOT NULL,
    ID_entrega SMALLINT unsigned PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Rota (
    ID_Rota SMALLINT unsigned PRIMARY KEY AUTO_INCREMENT,
    Tempo_estimado SMALLINT NOT NULL
);
