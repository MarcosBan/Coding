CREATE DATABASE dbclients;

\c dbclients;

CREATE TABLE "clients" (
    "IdClient" SERIAL NOT NULL,
    "CPF" VARCHAR(55) NOT NULL,
    "Name" VARCHAR(55) NOT NULL,
    "Email" VARCHAR(55) NOT NULL,
    CONSTRAINT "PK_Clients" PRIMARY KEY ("IdClient")
); 