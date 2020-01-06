FROM golang:latest
MAINTAINER Dmitriy Papkov <re@nsnow.xyz>

COPY . /home

RUN go get github.com/go-chi/chi
RUN go get go.mongodb.org/mongo-driver/mongo

CMD go run /home/main.go

EXPOSE 8080