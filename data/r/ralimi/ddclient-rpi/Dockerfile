FROM resin/rpi-raspbian:stretch
MAINTAINER Richard Alimi <rich@velvetsea.net>

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      libio-socket-ssl-perl \
      ddclient \
    && rm -rf /var/lib/apt/lists/*

RUN echo > /etc/ddclient.conf
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "--help" ]
