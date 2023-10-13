FROM golang:1.21.2-bullseye
WORKDIR /usr/src/app
COPY . .
RUN go install github.com/cosmtrek/air@latest
CMD air
