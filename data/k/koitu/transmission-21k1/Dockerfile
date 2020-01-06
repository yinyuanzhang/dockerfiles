FROM alpine:3.10

ARG BUILD_DATE
ARG TRANSMISSION_WEB_HOME=/web-control/
ENV TRANSMISSION_WEB_HOME="${TRANSMISSION_WEB_HOME}"
ARG PUID=1000
ARG GUID=1000
ENV PUID=${PUID}
ENV GUID=${GUID}
LABEL build_version="patched for bakabt.me on ${BUILD_DATE}"
LABEL maintainer="someone.zip@gmail.com"

COPY other /other
COPY start.sh /start.sh

RUN \
 echo "+++ install packages +++" && \
 apk add --no-cache \
 alpine-sdk libnotify-dev libevent-dev openssl-dev dbus-glib-dev curl-dev \
 autoconf automake libtool intltool cmake shadow \
 bsd-compat-headers \
 tini \
 moreutils unzip curl tar jq \
 libcurl libevent libintl openssl zlib && \
 echo "+++ build transmission +++" && \
 mkdir -p \
	/tmp/transmission && \
 TRAVERSION=$(curl -s https://api.github.com/repos/transmission/transmission/releases/latest | jq -r -j .tag_name) && \
 curl -o \
	/tmp/transmission.tar.gz -L \
	"https://github.com/transmission/transmission/archive/${TRAVERSION}.tar.gz" && \
 tar xf \
	/tmp/transmission.tar.gz -C \
	/tmp/transmission --strip-components=1 && \
 sed -i "s/int const sndbuf = isScrape ? 4096 : 1024;/int const sndbuf = 8192;/g" /tmp/transmission/libtransmission/web.c && \
 sed -i "s/int const rcvbuf = isScrape ? 4096 : 3072;/int const rcvbuf = 8192;/g" /tmp/transmission/libtransmission/web.c && \
 mv /other/CMakeLists.txt /tmp/transmission/CMakeLists.txt && \
 cmake -S \
	/tmp/transmission -B \
	/tmp/transmission && \
 echo "+++ install transmission +++" && \
 make install -C /tmp/transmission/ && \
 echo "+++ install transmission web control +++" && \
 mkdir -p \
	/tmp/twc && \
 TWCVERSION=$(curl -s https://api.github.com/repos/ronggang/transmission-web-control/releases/latest | jq -r -j .tag_name) && \
 curl -o \
	/tmp/twc.tar.gz -L \
	"https://github.com/ronggang/transmission-web-control/archive/${TWCVERSION}.tar.gz" && \
 tar xf \
	/tmp/twc.tar.gz -C \
	/tmp/twc --strip-components=1 && \
 mv /tmp/twc/src /web-control && \
 echo "+++ install combustion +++" && \
 curl -o \
	/tmp/combustion.zip -L \
	"https://github.com/Secretmapper/combustion/archive/release.zip" && \
 unzip \
	/tmp/combustion.zip -d / && \
 echo "+++ install kettu +++" && \
 mkdir -p /kettu && \
 curl -o \
	/tmp/kettu.tar.gz -L \
	"https://github.com/endor/kettu/archive/master.tar.gz" && \
 tar xf \
	/tmp/kettu.tar.gz -C \
	/kettu --strip-components=1 && \
 echo "+++ cleaning up +++" && \
 apk del --purge \
	alpine-sdk libnotify-dev libevent-dev openssl-dev dbus-glib-dev curl-dev && \
 rm -rf \
	/tmp/* 

ENTRYPOINT ["/sbin/tini", "--", "/start.sh"]

#CMD ["/usr/local/bin/transmission-daemon", "-g", "/config", "-c", "/watch", "-f"]

EXPOSE 9091 51413
VOLUME /config /downloads /watch
