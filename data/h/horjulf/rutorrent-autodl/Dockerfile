FROM lsiobase/nginx:3.8

LABEL maintainer="horjulf"

# copy patches
COPY patches/ /defaults/patches/

# install packages
RUN \
 echo "**** install build packages ****" && \
 apk add --no-cache --virtual=build-dependencies \
	g++ \
	libffi-dev \
	make \
	musl \
	openssl-dev \
	perl-dev \
	python3-dev && \
 echo "**** install packages ****" && \
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
	perl-utils \
	perl-archive-zip \
	perl-digest-sha1 \
	perl-html-parser \
	perl-json \
	perl-net-ssleay \
	perl-xml-libxml \
	php7 \
	php7-cgi \
	php7-curl \
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
	zip \
	zlib && \
 echo "**** install perl dependencies ****" && \
	PERL_MM_USE_DEFAULT=1 cpan JSON::XS && \
 echo "**** setup python pip dependencies ****" && \
 python3 -m pip install --no-cache-dir -U \
	cloudscraper \
	pip \
	requests \
	setuptools \
	urllib3 && \
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
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/etc/nginx/conf.d/default.conf \
	/root/.cache \
	/tmp/*

# add local files
COPY root/ /

ENV \
  # 2 minutes for finish scripts to run
  S6_KILL_FINISH_MAXTIME=120000 \
  S6_SERVICES_GRACETIME=5000 \
  S6_KILL_GRACETIME=5000

# ports and volumes
EXPOSE 80
