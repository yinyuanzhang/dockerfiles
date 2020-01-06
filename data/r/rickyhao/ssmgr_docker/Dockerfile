FROM node:10.15.3-alpine
LABEL maintainer="RickyHao <a959695@live.com>"

RUN set -ex \
	# Build environment setup
	&& apk add --no-cache --virtual .build-deps \
		autoconf \
      	automake \
      	build-base \
      	c-ares-dev \
      	libev-dev \
      	libtool \
      	libsodium-dev \
      	linux-headers \
      	mbedtls-dev \
      	pcre-dev \
        git \
 	# Build & install
    && mkdir -p /tmp/repo \
    && git clone https://github.com/shadowsocks/shadowsocks-libev.git /tmp/repo \
 	&& cd /tmp/repo \
    && git submodule update --init --recursive \
 	&& ./autogen.sh \
 	&& ./configure --prefix=/usr --disable-documentation \
 	&& make install \
 	&& apk del .build-deps \
 	# Runtime dependencies setup
 	&& apk add --no-cache \
      	rng-tools \
      	$(scanelf --needed --nobanner /usr/bin/ss-* \
      	| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      	| sort -u) \
 	&& rm -rf /tmp/repo

RUN apk update &&\
    apk add tzdata &&\
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    echo "Asia/Shanghai" > /etc/timezone &&\
    apk del tzdata &&\
    npm config set unsafe-perm true &&\
    npm i -g shadowsocks-manager


EXPOSE 8888
	
ENTRYPOINT ["/usr/local/bin/ssmgr"]
CMD ["-c", "/root/.ssmgr/webgui.yml"]
