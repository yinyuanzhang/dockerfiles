FROM debian:jessie-slim

ENV DEBIAN_FRONTEND noninteractive

ENV ASTERISK_VERSION 15.5.0

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        openssl \
        libxml2-dev \
        libncurses5-dev \
        uuid-dev \
        sqlite3 \
        libsqlite3-dev \
        pkg-config \
        libjansson-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        libopus-dev \
        curl \
        msmtp \
        subversion \
        xmlstarlet

# Asterisk expects /usr/sbin/sendmail
RUN ln -s /usr/bin/msmtp /usr/sbin/sendmail

RUN cd /tmp \
    && curl https://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-${ASTERISK_VERSION}.tar.gz | tar xz \
    && cd asterisk-${ASTERISK_VERSION} \
    && ./configure --with-pjproject-bundled --with-crypto --with-ssl \
    && make menuselect.makeopts \
    && menuselect/menuselect --enable codec_opus --enable format_mp3 \
    && contrib/scripts/get_mp3_source.sh \
    && make \
    && make install \
    && make samples \
    && make config \
    && cd / \
    && rm -rf /tmp/asterisk-${ASTERISK_VERSION}

CMD asterisk -fvvv
