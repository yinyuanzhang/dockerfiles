FROM ubuntu:14.04

MAINTAINER buhuipao <chenhua22@outlook.com>

WORKDIR /root

ADD . /root/
ARG DEBIAN_FRONTEND=noninteractive
RUN mv sysctl.conf /etc/sysctl.conf;\
    mv /etc/apt/sources.list sources.list.bak;\
    mv sources.list /etc/apt/sources.list;\
    apt-get update -y;\
    apt-get -y install python-pip;\
    pip install shadowsocks;\
    apt-get install libnet1;\
    apt-get install libc6;\
    apt-get install libpcap0.8;\
    apt-get install libc6-dev;\
    apt-get install libnet1-dev;\
    apt-get install libpcap0.8-dev;\
    apt-get clean;\
    chmod a+x /root/run.sh
    #pip install gevent;\

EXPOSE 8081 8082 8083 8084

CMD ["/root/run.sh"]
