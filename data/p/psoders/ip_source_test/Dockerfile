FROM golang:1.11-stretch

WORKDIR /go/src/app

COPY . .

RUN go build -v

CMD ["./app"]