FROM lsiobase/nginx:arm32v7-3.9
RUN [ “cross-build-start” ]
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
 apk add --no-cache --upgrade \
	bind-tools \
	ca-certificates \
	curl \
	dtach \
	fcgi \
	ffmpeg \
	geoip \
	git \
	gzip \
	irssi \
	irssi-perl \
	mediainfo \
	perl \
	perl-archive-zip \
	perl-digest-sha1 \
	perl-html-parser \
	perl-json \
	perl-net-ssleay \
	perl-xml-libxml \
	php7 \
	php7-cgi \
	php7-json \
	php7-mbstring \
	php7-pear \
	php7-sockets \
	php7-zip \
	procps \
	python3 \
	rtorrent \
	sox \
	tar \
	unrar \
	unzip \
	wget \
	xz \
	zip && \
 echo "**** install pip packages ****" && \
 pip3 install --no-cache-dir -U \
	cfscrape && \
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
	/root/.cache \
	/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 80
RUN [ “cross-build-end” ]
