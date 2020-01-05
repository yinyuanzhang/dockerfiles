FROM alpine:3.7

ARG FRP_VERSION=0.19.0
ENV MODE=frps

RUN apk --no-cache add wget

WORKDIR /tmp
RUN wget https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && tar -zxf frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && rm frp_${FRP_VERSION}_linux_amd64.tar.gz \
    && mv frp_${FRP_VERSION}_linux_amd64 /var/frp

WORKDIR /var/frp
ENTRYPOINT ./$MODE -c ./$MODE.ini
