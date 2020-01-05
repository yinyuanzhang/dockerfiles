FROM lsiobase/alpine:3.8

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="awyun.top version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="FaintGhost"
ENV TZ=Europe/Berlin
ENV WEBUI_VERSION=1.6.0-beta2
ENV GUID=0
ENV PUID=0

RUN \
 echo "**** install packages ****" && \
 apk add --no-cache \
	curl \
	findutils \
	jq \
	openssl \
	p7zip \
	python \
	rsync \
	tar \
	transmission-cli \
	transmission-daemon \
	unrar \
	unzip && \
	curl -fSL https://github.com/ronggang/transmission-web-control/archive/v${WEBUI_VERSION}.zip -o twc.zip && \
	unzip twc.zip -d /tmp && \
	cp -rf /usr/share/transmission/web/index.html /usr/share/transmission/web/index.original.html && \
	cp -rf /tmp/transmission-web-control-${WEBUI_VERSION}/src/* /usr/share/transmission/web/ && \
	rm -rf /tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 9091 45555
VOLUME /config /downloads /watch