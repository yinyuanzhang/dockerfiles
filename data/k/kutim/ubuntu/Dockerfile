FROM ubuntu:18.10
LABEL maintainer="1252900197@qq.com"
RUN apt update && \
    apt install tzdata && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    rm -rf /var/lib/apt/lists/*
