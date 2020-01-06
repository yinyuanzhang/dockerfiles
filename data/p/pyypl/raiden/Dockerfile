FROM debian:9-slim

ENV RAIDEN_VERSION=v0.12.0

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get -y update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN wget -O- https://github.com/raiden-network/raiden/releases/download/${RAIDEN_VERSION}/raiden-${RAIDEN_VERSION}-linux.tar.gz \
  | tar xz

RUN mv /raiden-${RAIDEN_VERSION}-linux /usr/bin/raiden

EXPOSE 5001 38647/udp

ENTRYPOINT ["raiden"]
