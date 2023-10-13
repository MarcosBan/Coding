CREATE SCHEMA IF NOT EXISTS testclients;
CREATE TABLE IF NOT EXISTS testclients.clients (
    "IdClient" SERIAL NOT NULL,
    "CPF" VARCHAR(55) NOT NULL,
    "Name" VARCHAR(55) NOT NULL,
    "Email" VARCHAR(55) NOT NULL,
    CONSTRAINT "PK_Clients" PRIMARY KEY ("IdClient")
); 

INSERT INTO testclients.clients( "CPF", "Name", "Email")
VALUES ('142358967', 'dbmussarelo', 'dbmussarelo@emailo.com');

INSERT INTO testclients.clients ( "CPF", "Name", "Email")
VALUES ('142358987', 'dbcalabresso', 'dbcalabresso@emailo.com');

INSERT INTO testclients.clients ( "CPF", "Name", "Email")
VALUES ('185358987', 'dbtroncudo', 'dbtroncudo@emailo.com');

INSERT INTO testclients.clients ( "CPF", "Name", "Email")
VALUES ('185898987', 'dbcasosbahio', 'dbcasosbahio@emailo.com');

INSERT INTO testclients.clients ( "CPF", "Name", "Email")
VALUES ('185898222', 'dbludmilo', 'dbludmilo@emailo.com');

INSERT INTO testclients.clients ( "CPF", "Name", "Email")
VALUES ('185898224', 'dbdelicio', 'dbdelicio@emailo.com');