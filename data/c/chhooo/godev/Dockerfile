FROM golang:1.13.3-alpine3.10
MAINTAINER Chris <cenne1986@qq.com>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh gcc g++ make
ENV GO111MODULE=on GOPROXY=https://goproxy.io
RUN apk add tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone
