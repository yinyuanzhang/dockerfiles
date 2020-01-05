FROM lsiobase/alpine.python:3.9

# set version label
ARG BUILD_DATE
ARG VERSION
ARG LAZYLIBRARIAN_COMMIT
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="chbmb"

RUN \
 echo "**** install build packages ****" && \
 apk add --no-cache --virtual=build-dependencies \
	g++ \
	gcc \
	make && \
 echo "**** install runtime packages ****" && \
 apk add --no-cache \
        mesa-gl \
	ghostscript && \
 echo "***** build unrarlib ****" && \
 rar_ver=$(apk info unrar | grep unrar- | cut -d "-" -f2 | head -1) && \
 mkdir -p \
	/tmp/unrar && \
 curl -o \
 /tmp/unrar-src.tar.gz -L \
	"http://www.rarlab.com/rar/unrarsrc-${rar_ver}.tar.gz" && \
 tar xf \
 /tmp/unrar-src.tar.gz -C \
	/tmp/unrar --strip-components=1 && \
 cd /tmp/unrar && \
 make lib && \
 make install-lib && \
 echo "**** install app ****" && \
 mkdir -p \
	/app/lazylibrarian && \
 if [ -z ${LAZYLIBRARIAN_COMMIT+x} ]; then \
 	LAZYLIBRARIAN_COMMIT=$(curl -sX GET "https://gitlab.com/api/v4/projects/9317860/repository/commits/master" \
    	| awk '/id/{print $4;exit}' FS='[""]'); \
 fi && \
 echo "Building from commit ${LAZYLIBRARIAN_COMMIT}" && \
 echo "${LAZYLIBRARIAN_COMMIT}" > /defaults/version.txt && \
 curl -o \
 /tmp/lazylibrarian.tar.gz -L \
	"https://gitlab.com/LazyLibrarian/LazyLibrarian/repository/archive.tar.gz?sha={$LAZYLIBRARIAN_COMMIT}" && \
 tar xf \
 /tmp/lazylibrarian.tar.gz -C \
	/app/lazylibrarian --strip-components=1 && \
 echo "**** install GNU libc (aka glibc) ****" && \
 ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" && \
 ALPINE_GLIBC_PACKAGE_VERSION=$(curl -s https://api.github.com/repos/sgerrand/alpine-pkg-glibc/releases/latest | grep 'tag_name' | cut -d\" -f4) && \
 ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
 ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
 ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
 mkdir -p /var/cache/apk && \
 apk add --no-cache --virtual=.build-dependencies && \
 apk add --no-cache parallel && \
    wget "https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub" \
         -O "/etc/apk/keys/sgerrand.rsa.pub" && \
    wget "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
         "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
         "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
    apk add --no-cache \
        "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
    cat /init/LOCALE.md | parallel "echo generate locale {}; /usr/glibc-compat/bin/localedef --force --inputfile {} --charmap UTF-8 {}.UTF-8;" && \
    apk del .build-dependencies && \
    rm "/etc/apk/keys/sgerrand.rsa.pub" && \
    rm "/root/.wget-hsts" && \
    rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
       "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
       "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
	rm -rf /var/cache/apk/* && \
 echo "**** install calibre binary ****" && \
 LD_LIBRARY_PATH="/usr/lib:/opt/calibre/lib" && \
 PATH="$PATH:/opt/calibre" && \
 wget -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | \
      python -c \
      "import sys; \
       main=lambda:sys.stderr.write('Download failed\n'); \
       exec(sys.stdin.read()); \
       main(install_dir='/opt', isolated=True)" && \
    rm -rf /tmp/calibre-installer-cache && \
 echo "**** cleanup ****" && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 5299
VOLUME /config /books /downloads
