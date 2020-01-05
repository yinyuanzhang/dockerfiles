FROM debian:9

MAINTAINER Yuwei Ba<i@xiaoba.me>

ENV OBFS_RELEASE 2955a57
ENV LIBCORK_RELEASE 3bcb832
ENV BUILD_DEPS curl ca-certificates build-essential autoconf libtool libssl-dev libpcre3-dev libc-ares-dev libev-dev asciidoc xmlto automake

RUN sh -c 'printf "deb http://deb.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list'
RUN apt-get update && \
    yes | apt-get install shadowsocks-libev --no-install-recommends && \

    yes | apt-get install $BUILD_DEPS --no-install-recommends && \
    mkdir -p /src/libcork && \
    curl -L https://github.com/shadowsocks/simple-obfs/tarball/$OBFS_RELEASE | tar -C /src -zx --strip-components 1 && \
    curl -L https://github.com/shadowsocks/libcork/tarball/$LIBCORK_RELEASE | tar -C /src/libcork -zx --strip-components 1 && \
    cd src && \
    ./autogen.sh && \
    ./configure && make && \
    make install && \
    yes | apt-get remove $BUILD_DEPS && yes | apt-get auto-remove && \
     rm -rf /var/lib/apt/lists/*

RUN apt-get update && yes | apt-get install libc-ares-dev && rm -rf /var/lib/apt/lists/*


CMD ["ss-server", "-s", "0.0.0.0", "-p", "32384", "-k", "password", "-m", "aes-256-cfb", "--plugin", "obfs-server", "--plugin-opts", "obfs=http"]

