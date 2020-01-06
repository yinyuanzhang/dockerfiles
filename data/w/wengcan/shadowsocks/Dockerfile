FROM alpine:3.4
MAINTAINER wengcan <wengcanvip@gmail.com>

ENV BUILDDEPENDENCIES  git build-base gcc automake autoconf  c-ares-dev libev-dev libsodium-dev linux-headers mbedtls-dev pcre-dev  libtool openssl-dev  udns-dev asciidoc xmlto
ENV DEPENDENCIES  libcrypto1.0 pcre  libev libsodium mbedtls c-ares
RUN apk add --update --no-cache  --virtual .build-deps $BUILDDEPENDENCIES
RUN git clone https://github.com/shadowsocks/simple-obfs.git \
&& cd simple-obfs \
&& git submodule update --init --recursive \
&& ./autogen.sh \
&& ./configure && make \
&&  make install \
&& cd ../ \
&& rm -rf simple-obfs
RUN  git clone https://github.com/shadowsocks/shadowsocks-libev.git \
 && cd shadowsocks-libev \
 && git submodule update --init --recursive \
 && ./autogen.sh \
 && ./configure --disable-documentation \
 && make \
 && make install \
 && cd ../ \
 && rm -rf  shadowsocks-libev \
 && apk add --no-cache $DEPENDENCIES \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/*
#ENTRYPOINT ["/usr/local/bin/ss-local"]
CMD ["bash"]
