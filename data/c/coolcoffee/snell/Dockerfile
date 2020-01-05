FROM jeanblanchard/alpine-glibc:latest

ARG BUILD_DEPS="wget unzip"

ENV LOCAL_PORT 80
ENV VERSION v1.1.0

# China mirrors
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN set -ex && \
    apk update && \
    apk add --no-cache --virtual $BUILD_DEPS && \
    apk add --update libstdc++ && rm -rf /var/cache/apk/* && \
    apk add openssl && \
    mkdir /snell && \
	cd /snell && \
	wget https://github.com/surge-networks/snell/releases/download/${VERSION}/snell-server-${VERSION}-linux-amd64.zip && \
    unzip snell-server-${VERSION}-linux-amd64.zip && \
    rm /snell/snell-server-${VERSION}-linux-amd64.zip && \
    apk del $BUILD_DEPS

ADD entrypoint.sh /snell
RUN ["chmod", "+x", "/snell/entrypoint.sh"]
ENTRYPOINT ["/snell/entrypoint.sh"]
