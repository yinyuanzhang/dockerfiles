FROM debian:latest
MAINTAINER Julius Loman <lomo@kyberia.net>

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get -y install openconnect curl && apt-get clean

ADD ./docker-entrypoint.sh ./network-routes.sh /

ENTRYPOINT [ "/docker-entrypoint.sh" ]
