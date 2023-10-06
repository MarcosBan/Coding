FROM golang:1.21.2-bullseye

COPY ./app /app/

WORKDIR /app

COPY ./app /app/

RUN go mod init bango/app

RUN go get github.com/gin-gonic/gin

EXPOSE 8080:8080

CMD ["go", "run", "."] 