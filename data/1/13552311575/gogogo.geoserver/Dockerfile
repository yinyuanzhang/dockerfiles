FROM golang:1.13

RUN mkdir -p /go/src/github.com/liuwangchen/gogogo.geoserver

COPY ./ /go/src/github.com/liuwangchen/gogogo.geoserver

WORKDIR /go/src/github.com/liuwangchen/gogogo.geoserver

ENV GO111MODULE off

RUN ./make.sh

FROM registry.cn-beijing.aliyuncs.com/gogogo/base

MAINTAINER liuwangchen

WORKDIR /data/gogogo

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.geoserver/bin/geoserver ./

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.geoserver/config/*.yaml ./config/

EXPOSE 10091 9091

CMD ./geoserver -f ./config/docker.yaml
