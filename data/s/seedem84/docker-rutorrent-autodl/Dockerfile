FROM lsiobase/alpine:3.8

LABEL maintainer="horjulf"

# copy patches
COPY patches/ /defaults/patches/

# install packages
RUN \
echo "**** install packages ****" && \
apk add --no-cache -U \
 	linux-headers \
 	build-base \
	py-psutil \
 	python-dev \
	bash-completion \
	binutils \
	zlib-dev \
	libxml2-dev \
        libressl \
	ca-certificates \
	curl \
	fcgi \
	ffmpeg \
	geoip \
	gzip \
	irssi \
	irssi-perl \
	logrotate \
	mediainfo \
	nginx \
	perl \
	perl-archive-zip \
	perl-digest-sha1 \
	perl-html-parser \
	perl-json \
	perl-net-ssleay \
	perl-xml-libxml \
	python \
	py-pip \
	findutils \
	php7 \
	php7-cgi \
	php7-fpm \
	php7-json \
	php7-mbstring \
	php7-pear \
	php7-sockets \
	rtorrent \
	dtach \
	sox \
	tar \
	unrar \
	unzip \
	wget \
	git \
	zlib \
	zip \
	xz && \
 # Begin Added
 # install build packages
 apk add --no-cache --virtual=build-dependencies \
        make && \
 # End Added
 apk add --no-cache -U --repository http://nl.alpinelinux.org/alpine/edge/testing \
	perl-json-xs && \
 echo "**** setup python pip dependencies ****" && \
 python -m pip install --no-cache-dir -U pip setuptools requests urllib3 && \
 echo "**** install webui ****" && \
 mkdir -p \
	/usr/share/webapps/rutorrent \
	/defaults/rutorrent-conf && \
 curl -o \
	/tmp/rutorrent.tar.gz -L \
	"https://github.com/Novik/ruTorrent/archive/master.tar.gz" && \
 tar xf \
	/tmp/rutorrent.tar.gz -C \
	/usr/share/webapps/rutorrent --strip-components=1 && \
 mv /usr/share/webapps/rutorrent/conf/* \
	/defaults/rutorrent-conf/ && \
 rm -rf \
	/defaults/rutorrent-conf/users && \
 echo "**** patch snoopy.inc for rss fix ****" && \
 cd /usr/share/webapps/rutorrent/php && \
 patch < /defaults/patches/snoopy.patch && \
 echo "**** install additional rutorrent theme ****" && \
 git clone git://github.com/phlooo/ruTorrent-MaterialDesign.git /usr/share/webapps/rutorrent/plugins/theme/themes/MaterialDesign && \
 # Begin Added
 # install webui extras
 # QuickBox Theme
 git clone https://github.com/QuickBox/club-QuickBox /usr/share/webapps/rutorrent/plugins/theme/themes/club-QuickBox && \
 #git clone https://github.com/Phlooo/ruTorrent-MaterialDesign /usr/share/webapps/rutorrent/plugins/theme/themes/MaterialDesign && \
 # ruTorrent plugins
 cd /usr/share/webapps/rutorrent/plugins/ && \
 git clone https://github.com/orobardet/rutorrent-force_save_session force_save_session && \
 git clone https://github.com/AceP1983/ruTorrent-plugins  && \
 mv ruTorrent-plugins/* . && \
 rm -rf ruTorrent-plugins && \
 apk add --no-cache cksfv && \
 git clone https://github.com/nelu/rutorrent-thirdparty-plugins.git && \
 mv rutorrent-thirdparty-plugins/* . && \
 rm -rf rutorrent-thirdparty-plugins && \
 cd /usr/share/webapps/rutorrent/ && \
 chmod 755 plugins/filemanager/scripts/* && \
 rm -rf plugins/fileupload && \
 cd /tmp && \
 git clone https://github.com/mcrapet/plowshare.git && \
 cd plowshare/ && \
 make install && \
 cd .. && \
 rm -rf plowshare* && \
 apk add --no-cache unzip bzip2 && \
 cd /usr/share/webapps/rutorrent/plugins/ && \
 git clone https://github.com/Gyran/rutorrent-pausewebui pausewebui && \
 git clone https://github.com/Gyran/rutorrent-ratiocolor ratiocolor && \
 sed -i 's/changeWhat = "cell-background";/changeWhat = "font";/g' /usr/share/webapps/rutorrent/plugins/ratiocolor/init.js && \
 git clone https://github.com/Gyran/rutorrent-instantsearch instantsearch && \
 git clone https://github.com/xombiemp/rutorrentMobile mobile && \
 git clone https://github.com/dioltas/AddZip && \
 mv AddZip addzip && \
 # End added
 echo "**** fix logrotate ****" && \
 sed -i "s#/var/log/messages {}.*# #g" /etc/logrotate.conf && \
 echo "**** cleanup ****" && \
 rm -rf \
	/etc/nginx/conf.d/default.conf \
	/tmp/*

# add local files
COPY root/ /

ENV \
  S6_KILL_GRACETIME=30000

# ports and volumes
EXPOSE 80
VOLUME /config /mnt
