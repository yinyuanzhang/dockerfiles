FROM golang:alpine AS builder

MAINTAINER siddontang

EXPOSE 12800/tcp

RUN apk add --no-cache tini mariadb-client

#RUN cd /go/src/github.com/siddontang/go-mysql-elasticsearch/ && \
#    go build -o bin/go-mysql-elasticsearch ./cmd/go-mysql-elasticsearch && \
#    cp -f ./bin/go-mysql-elasticsearch /go/bin/go-mysql-elasticsearch

WORKDIR $GOPATH/src/gozer/go-mysql-elasticsearch

COPY . .

RUN go get -d -v ./cmd/go-mysql-elasticsearch
RUN GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /go/bin/go-mysql-elasticsearch ./cmd/go-mysql-elasticsearch

FROM alpine

RUN apk add --no-cache tini mariadb-client

# Copy our static executable.
COPY --from=builder /go/bin/go-mysql-elasticsearch /go/bin/go-mysql-elasticsearch

ENTRYPOINT [ "/go/bin/go-mysql-elasticsearch", "-config", "/config/river.toml" ]
