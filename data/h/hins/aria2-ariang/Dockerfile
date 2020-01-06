FROM debian:buster

LABEL Maintainer="hsin"

ARG ARIANG_VARSION="1.1.4"
ENV ARIA2_PASSWD="123456"

WORKDIR /aria2

# 加速国内网络环境下载
#RUN sed -i -e "/security/s/^/#/" \
#   -e "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list

RUN apt update && apt install -y \
    nginx aria2 wget unzip \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/mayswind/AriaNg/releases/download/${ARIANG_VARSION}/AriaNg-${ARIANG_VARSION}.zip \
    && unzip AriaNg-${ARIANG_VARSION}.zip \
    && rm -f AriaNg-${ARIANG_VARSION}.zip

COPY service.sh conf/* ./
RUN mv nginx-default.conf /etc/nginx/sites-enabled/default 

EXPOSE 80 6800 6881
CMD ["/bin/bash", "service.sh"]

