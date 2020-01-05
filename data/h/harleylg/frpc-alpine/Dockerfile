FROM alpine

ENV FRP_VERSION 0.29.0
RUN wget https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && tar -xf frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && cp frp_${FRP_VERSION}_linux_amd64/frpc /usr/local/bin/ \
    && rm -rf frp_${FRP_VERSION}_linux_amd64* 

VOLUME /etc/frpc

ENTRYPOINT ["frpc","-c","/etc/frpc/frpc.ini"]