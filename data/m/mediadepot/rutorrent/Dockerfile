FROM lsiobase/alpine.nginx:3.8

# set version label
ARG BUILD_DATE
ARG VERSION
ARG RUTORRENT_COMMIT
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="alex-phillips"

# copy patches
COPY patches/ /defaults/patches/

RUN \
 echo "**** install runtime packages ****" && \
 apk add --no-cache \
	bind-tools \
	curl \
	fcgi \
	ffmpeg \
	geoip \
	gzip \
	mediainfo \
	php7 \
	php7-cgi \
	php7-pear \
	rtorrent \
	screen \
	sox \
	unrar \
	zip && \
 echo "**** install rutorrent ****" && \
 if [ -z ${RUTORRENT_VERSION+x} ]; then \
	RUTORRENT_VERSION=$(curl -sX GET https://api.github.com/repos/Novik/rutorrent/commits/master \
	| awk '/sha/{print $4;exit}' FS='[""]'); \
 fi && \
 curl -o \
 /tmp/rutorrent.tar.gz -L \
	"https://github.com/Novik/rutorrent/archive/${RUTORRENT_VERSION}.tar.gz" && \
 mkdir -p \
	/app/rutorrent \
	/defaults/rutorrent-conf && \
 tar xf \
 /tmp/rutorrent.tar.gz -C \
	/app/rutorrent --strip-components=1 && \
 mv /app/rutorrent/conf/* \
	/defaults/rutorrent-conf/ && \
 rm -rf \
	/defaults/rutorrent-conf/users && \
 echo "**** patch snoopy.inc for rss fix ****" && \
 cd /app/rutorrent/php && \
 patch < /defaults/patches/snoopy.patch && \
 echo "**** cleanup ****" && \
 rm -rf \
	/etc/nginx/conf.d/default.conf \
	/tmp/* && \
 curl -o /tmp/themes.tar.gz -L https://github.com/artyuum/ruTorrent-Themes/archive/master.tar.gz && \
 tar xf /tmp/themes.tar.gz -C /app/rutorrent/plugins/theme/themes --strip-components=1 && \
 rm -rf /tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 80

