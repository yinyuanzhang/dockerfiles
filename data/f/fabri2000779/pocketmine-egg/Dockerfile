FROM ubuntu:16.04

MAINTAINER fabri2000779, <fabrizio@skynode.pro>

RUN apt update \
    && apt upgrade -y \
    && apt install -y tar curl iproute2 openssl \
    && apt update -y \
    && useradd -d /home/container -m container

USER container
ENV USER=container HOME=/home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
