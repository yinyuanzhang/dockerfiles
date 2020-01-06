FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y git

RUN pip install --upgrade pip
RUN pip install git+https://github.com/shadowsocks/shadowsocks.git@master
RUN pip install dumb-init

ADD start-shadowsocks /usr/local/bin

ENTRYPOINT ["dumb-init", "--", "start-shadowsocks"]
