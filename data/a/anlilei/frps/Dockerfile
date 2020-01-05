FROM alpine:3.9.4
 
MAINTAINER lilei <lilei.727@gmail.com>

ENV frp_v 0.27.0

RUN wget --no-check-certificate https://github.com/fatedier/frp/releases/download/v${frp_v}/frp_${frp_v}_linux_amd64.tar.gz && \
    tar -zxf frp_${frp_v}_linux_amd64.tar.gz && \
    mkdir /var/frp && \
    mkdir /var/frp/conf && \
    mkdir /var/frp/log && \
    mv frp_${frp_v}_linux_amd64/* /var/frp && \
    rm -rf frp_${frp_v}_linux_amd64.tar.gz 
    
ADD https://raw.githubusercontent.com/anlilei504/frps/master/frps.ini /var/frp/conf

WORKDIR /var/frp


ENTRYPOINT ./frps -c conf/frps.ini
