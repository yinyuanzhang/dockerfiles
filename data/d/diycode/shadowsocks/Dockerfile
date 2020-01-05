FROM alpine:latest
MAINTAINER diycode <i@diycode.me>

RUN apk add --no-cache ca-certificates python py-setuptools
RUN apk add --no-cache --virtual .build-deps \
    wget \
  \
  && wget "https://github.com/shadowsocks/shadowsocks/archive/2.9.0.tar.gz" -O shadowsocks.tar.gz \
  && tar -C /usr/local -xzf shadowsocks.tar.gz \
  && rm shadowsocks.tar.gz \
  && cd /usr/local/shadowsocks-2.9.0 \
  && python setup.py install \
  && apk del .build-deps

ENTRYPOINT ["ssserver"]