FROM alpine:latest
MAINTAINER endpot@gmail.com

ENV FRP_VER 0.20.0
ENV FRP_FULL_VER frp_${FRP_VER}_linux_amd64

RUN cd /root \ 
    && wget https://github.com/fatedier/frp/releases/download/v${FRP_VER}/${FRP_FULL_VER}.tar.gz \
    && tar -vxzf ${FRP_FULL_VER}.tar.gz \
    && rm ${FRP_FULL_VER}.tar.gz \
    && mkdir -p /usr/local/frps \
    && cp ${FRP_FULL_VER}/frps ${FRP_FULL_VER}/frps.ini /usr/local/frps \
    && rm -rf ${FRP_FULL_VER}
    
WORKDIR /usr/local/frps

CMD [ "./frps", "-c", "./frps.ini" ]
