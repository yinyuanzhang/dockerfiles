FROM alpine:latest

MAINTAINER Anton Zakharov hello@antonzakharov.ru

ENV ASTERISK_SOURCE https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-16.5.1.tar.gz
ENV ASTERISK_MODULES_ENABLE format_mp3 chan_sip pbx_ael cdr_adaptive_odbc res_fax res_fax_spandsp
ENV ASTERISK_MODULES_DISABLE BUILD_NATIVE
ENV ASTERISK_CATEGORY_DISABLE MENUSELECT_CORE_SOUNDS MENUSELECT_MOH MENUSELECT_EXTRA_SOUNDS
ENV DOCKERIZE_VERSION v0.6.1

WORKDIR /usr/src

COPY assets/patches/ patches/
COPY assets/lib/ /usr/lib/
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh

# Install dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Install compile deps and install Asterisk
RUN set -ex; apk update \
    # Add runtime libraries
    && apk add --no-cache --virtual .runtime-deps \
      # ncurses-dev
      ncurses-terminfo-base ncurses-terminfo ncurses-libs \
      # util-linux-dev
      libuuid libblkid libfdisk libmount libsmartcols \
      # jansson-dev
      jansson \
      # libxml2-dev
      libxml2 \
      # sqlite-dev
      sqlite-libs \
      # ODBC
      libressl readline unixodbc psqlodbc \
      # spandsp
      libjpeg-turbo tiff libtiffxx spandsp \
      # libedit
      libedit \
    # Add compile libraries
    && apk add --no-cache --virtual .build-deps \
      # Apply patches
      wget patch \
      # Core compile dependencies
      build-base ncurses-dev util-linux-dev jansson-dev libxml2-dev sqlite-dev bsd-compat-headers \
      # ODBC dependencies
      libressl-dev unixodbc-dev \
      # spandsp
      libjpeg-turbo-dev tiff-dev spandsp-dev \
      # libedit
      libedit-dev \
    && wget -O asterisk.tar.gz $ASTERISK_SOURCE; tar vxfz asterisk.tar.gz; rm asterisk.tar.gz \
    && mv asterisk-* asterisk && cp patches/musl-astmm-fix.patch patches/musl-mutex-init.patch asterisk/; cp patches/asterisk-addon-mp3-r201.patch asterisk/addons/ \
    && cd asterisk && patch -p1 < ./musl-astmm-fix.patch && patch -p1 < ./musl-mutex-init.patch && cd addons; patch -p1 < ./asterisk-addon-mp3-r201.patch && cd .. \
    && if ! grep -q ASTMM_LIBC addons/mp3/interface.c; then sed -i -e '/#include "asterisk.h"/i#define ASTMM_LIBC ASTMM_REDIRECT' addons/mp3/interface.c; fi \
    && ./configure --without-pjproject-bundled --enable-permanent-dlopen && make menuselect.makeopts \
    && menuselect/menuselect \
           # Enable modules
           $(for MODULE in $ASTERISK_MODULES_ENABLE; do echo --enable $MODULE; done;) \
           # Disable modules
           $(for MODULE in $ASTERISK_MODULES_DISABLE; do echo --disable $MODULE; done;) \
           # Disable categories
           $(for CATEGORY in $ASTERISK_CATEGORY_DISABLE; do echo --disable-category $CATEGORY; done;) menuselect.makeopts \
    && make -j "$(nproc)" && make install \
    # Save sample configs to config-sample.tar.gz
    && mv configs/samples /usr/src/configs && cd /usr/src/configs \
    && find . -name '*.sample' -type f | while read NAME ; do mv "${NAME}" "${NAME%.sample}" ; done \
    && tar cfz /usr/src/config-samples.tar.gz ./ \
    # Cleanup build files
    && cd ..; rm -Rf /usr/src/asterisk; rm -Rf /usr/src/patches \
    && apk del .build-deps

COPY assets/etc/ /etc/

WORKDIR /etc/asterisk

EXPOSE 5060/udp 5060/tcp 5038/tcp 10000-10005/udp

ENTRYPOINT ["/docker-entrypoint.sh"]
