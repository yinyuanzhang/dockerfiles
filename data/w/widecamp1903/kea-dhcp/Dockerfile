FROM ubuntu:bionic
LABEL maintainer "Taichi MIYA <tmiya@protonmail.ch>"

RUN apt-get -y update && \
    apt-get install -y kea-dhcp4-server kea-admin

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 67/udp
ENTRYPOINT ["/entrypoint.sh"]
