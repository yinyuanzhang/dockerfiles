FROM golang:1.12

# No module support，go get package from gopath and verdor
ENV GO111MODULE off

RUN mkdir -p /go/src/github.com/eleme/lindb \
    && cd /go/src/github.com/eleme/lindb \
    && echo '[http] \nport = 8900 \n[coordinator] \nnamespace = "/lindb/broker/" \n' \
     'endpoints = ["http://etcd:2379"] \ndialTimeout = 5 \n' \
     '[user] \nusername = "admin" \npassword = "admin123"' > broker.toml \
    && cat broker.toml

WORKDIR /go/src/github.com/eleme/lindb

COPY . /go/src/github.com/eleme/lindb

EXPOSE 8900

#ENTRYPOINT ["go","run"]