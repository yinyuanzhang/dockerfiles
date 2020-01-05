FROM ubuntu:18.04

MAINTAINER !Dark!, <dark@biggames.pl>

ENV         DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt upgrade -y \
    && apt install -y lib32gcc1 lib32stdc++6 unzip curl iproute2 \
    && useradd -d /home/container -m container

USER container
ENV HOME=/home/container
WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]
