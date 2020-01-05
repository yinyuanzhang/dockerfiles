FROM ubuntu

RUN apt-get update && apt-get install -y \
    curl                \
    dnsutils            \
    telnet              \
    net-tools           \
    netcat              \
    vim                 \
    && apt-get clean

COPY rootfs/ /