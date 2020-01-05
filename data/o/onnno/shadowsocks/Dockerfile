FROM ubuntu:16.04

MAINTAINER Dong Li "docker@lidong.me”

RUN apt update \
&& apt upgrade -y \
&& apt install -y python-pip \
&& pip --no-cache-dir install https://github.com/shadowsocks/shadowsocks/archive/master.zip

ENTRYPOINT ["/usr/local/bin/ssserver"]
