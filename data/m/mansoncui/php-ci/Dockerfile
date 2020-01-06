
FROM alpine

MAINTAINER Mancon Cui <mansoncui@163.com>

RUN apk add --no-cache rsync docker bash openssh-server python python-dev openssh-client tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    rm -rf /var/cache/apk/*

COPY ./assets/* /opt/resource/
