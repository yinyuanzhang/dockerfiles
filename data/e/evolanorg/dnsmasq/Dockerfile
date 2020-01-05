FROM alpine:edge
LABEL maintainer="vegardsaglien@gmail.com"

ENV DNSONLY false
ENV WEBPROC_VERSION 0.1.9
ENV WEBPROC_URL https://github.com/jpillora/webproc/releases/download/$WEBPROC_VERSION/webproc_linux_amd64.gz
ENV BOOTFILE_URL https://boot.netboot.xyz/ipxe/netboot.xyz.kpxe

COPY src/ /src

RUN apk update \
	&& apk add --no-cache dnsmasq \
	&& apk add --no-cache --virtual .build-deps curl wget \
	&& curl -sL $WEBPROC_URL | gzip -d - > /usr/local/bin/webproc \
	&& curl -sL $BOOTFILE_URL > /src/bootfile \
	&& chmod +x /usr/local/bin/webproc /src/start.sh \
	&& chmod 777 /src/* \
	&& apk del .build-deps 

ENTRYPOINT [ "sh","/src/start.sh" ]

