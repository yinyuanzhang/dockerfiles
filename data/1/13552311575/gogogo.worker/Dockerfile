FROM golang:1.12

RUN mkdir -p /go/src/github.com/liuwangchen/gogogo.worker

COPY ./ /go/src/github.com/liuwangchen/gogogo.worker

WORKDIR /go/src/github.com/liuwangchen/gogogo.worker

RUN ./make.sh

FROM alpine:latest

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

# 更改时区
RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apk del tzdata

MAINTAINER liuwangchen

WORKDIR /data/gogogo

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.worker/bin/worker ./

COPY --from=0 /go/src/github.com/liuwangchen/gogogo.worker/asset/* ./asset/

CMD /data/gogogo/worker -p docker
