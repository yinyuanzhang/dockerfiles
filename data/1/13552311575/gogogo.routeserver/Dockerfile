FROM golang:1.13

RUN mkdir -p /go/src/github.com/liuwangchen/gogogo.routeserver

COPY ./ /go/src/github.com/liuwangchen/gogogo.routeserver

WORKDIR /go/src/github.com/liuwangchen/gogogo.routeserver

ENV GO111MODULE off

RUN ./make.sh

FROM registry.cn-beijing.aliyuncs.com/gogogo/base

MAINTAINER liuwangchen

WORKDIR /data/gogogo

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.routeserver/bin/routeserver ./

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.routeserver/config/*.yaml ./config/

EXPOSE 10092 9092

CMD ./routeserver -f ./config/docker.yaml
