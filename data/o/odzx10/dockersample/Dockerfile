FROM golang:1.8

WORKDIR /go/src/docker-go
COPY . /go/src/docker-go

RUN go build
RUN go install

CMD ["docker-go"]
