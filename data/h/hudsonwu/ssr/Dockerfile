FROM debian:9

LABEL maintainer="hudson <wuhaishui2013@126.com>"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

ENV SERVER_ADDR=0.0.0.0 \
    SERVER_PORT=46176 \
    PASSWORD=HelloWorld \
    METHOD=chacha20-ietf \
    PROTOCOL=auth_aes128_md5 \
    OBFS=tls1.2_ticket_fastauth \
    START=/shadowsocksr/shadowsocks/server.py

RUN echo "deb http://mirrors.aliyun.com/debian stretch main contrib non-free" > /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian stretch-proposed-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian stretch-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security/ stretch/updates main non-free contrib" >> /etc/apt/sources.list

RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils

# 安装libsodium和一些依赖工具
RUN apt-get install -y python-m2crypto libsodium-dev git

# 获取shadowsocksr源代码
RUN git clone https://github.com/HudsonWu/shadowsocksr.git -b hudson

WORKDIR /shadowsocksr/shadowsocks

ENTRYPOINT ["/bin/sh", "-c", "$START -s ${SERVER_ADDR} -p ${SERVER_PORT} -k ${PASSWORD} -m ${METHOD} -O ${PROTOCOL} -o ${OBFS}"]
