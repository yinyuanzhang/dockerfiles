FROM golang:1.11

MAINTAINER 935661686@qq.com

ENV GO111MODULE on

EXPOSE 9999

WORKDIR /go/src/go-docker

COPY . .

RUN go mod vendor

RUN go build main.go

CMD [ "bash", "-c", "/go/src/go-docker/main;" ]