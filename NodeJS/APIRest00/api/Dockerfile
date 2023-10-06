FROM ubuntu:latest

COPY alura-node app/


RUN apt update && apt install curl -y

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

RUN apt install -y nodejs

EXPOSE 3000

WORKDIR app/

#CMD [ "npm run", "dev"]