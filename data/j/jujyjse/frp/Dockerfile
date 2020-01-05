FROM golang:1.8.3-alpine3.6

COPY . /go/src/github.com/fatedier/frp

RUN apk --no-cache add make

RUN cd /go/src/github.com/fatedier/frp \
 && make \
 && mv bin/frpc /frpc \
 && mv bin/frps /frps \
 && mv conf/frpc.ini /frpc.ini \
 && mv conf/frps.ini /frps.ini

WORKDIR /

EXPOSE 80 443 6000 7000 7500

ENTRYPOINT ["/frps"]
