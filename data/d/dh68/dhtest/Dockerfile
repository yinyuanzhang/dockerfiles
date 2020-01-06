FROM golang:latest

MAINTAINER dh68 "78696255@qq.com"

WORKDIR $GOPATH/src/dhtest

COPY . .

RUN go build .

EXPOSE 8080

ENTRYPOINT ["./dhtest"]

# http://127.0.0.1:8080/world
