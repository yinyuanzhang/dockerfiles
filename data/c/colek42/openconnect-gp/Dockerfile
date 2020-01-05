FROM debian:9-slim as builder
RUN apt update \
    && apt install -y  \
	build-essential \
	gettext \
	autoconf \
	automake \
	libproxy-dev \
	libxml2-dev \
	libtool \
	vpnc-scripts \
	pkg-config \
	libgnutls28-dev \
	git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN curl -LO https://github.com/openconnect/openconnect/archive/v8.02.tar.gz
RUN tar -xzf v8.02.tar.gz
WORKDIR openconnect-8.02
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /
ADD ./docker-entrypoint.sh /

ENTRYPOINT [ "/docker-entrypoint.sh" ]

