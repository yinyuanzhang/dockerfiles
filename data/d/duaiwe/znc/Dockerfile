FROM        debian:8
MAINTAINER  Jonathan Borzilleri "jonathan@borzilleri.net"

ENV ZNC_VERSION 1.6.2

# Install ZNC dependencies.
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install \
  python3 python3-dev build-essential libssl-dev libperl-dev pkg-config

# Download, Compile, and install ZNC.
ADD http://znc.in/releases/znc-${ZNC_VERSION}.tar.gz /tmp/
RUN tar xf /tmp/znc-${ZNC_VERSION}.tar.gz && \
  cd "znc-${ZNC_VERSION}" && \
  ./configure --enable-python && make && make install && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -r znc && useradd -r -g znc znc
RUN mkdir /data && chown znc:znc /data
VOLUME ["/data"]
USER znc

EXPOSE 6667
ENTRYPOINT ["znc", "--datadir=/data"]
CMD ["--foreground"]
