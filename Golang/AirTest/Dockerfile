FROM golang:latest
WORKDIR /app
COPY . .
RUN go install github.com/cosmtrek/air@latest
CMD air
