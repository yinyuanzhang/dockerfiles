
FROM ubuntu:16.04
MAINTAINER Conor Heine <conor.heine@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_TYPE en_US.UTF-8

# Core dependencies
RUN apt-get update
RUN apt-get --yes install \
        build-essential \
        git \
        locales \
        pkg-config libssl-dev bzip2 wget \
        xmltv \
        libavahi-client-dev \
        zlib1g-dev \
        libavcodec-dev \
        libavutil-dev \
        libavformat-dev \
        libswscale-dev \
        libavresample-dev \
        dvb-apps \
        gettext \
        cmake \
        python \
        python-dev

# Generate locales
RUN grep "$LANG" /usr/share/i18n/SUPPORTED >> /etc/locale.gen && locale-gen && update-locale LANG=$LANG

# Install w_scan for debugging dvb devices
RUN cd /tmp && wget http://wirbel.htpc-forum.de/w_scan/w_scan-20170107.tar.bz2 && \
    tar jxvf w_scan-20170107.tar.bz2 && rm w_scan-20170107.tar.bz2 && cd w_scan* && \
    ./configure && make && make install && cd && rm -rf /tmp/*

# Install tvheadend and build from source
RUN git clone https://github.com/tvheadend/tvheadend.git /tvheadend && \
    cd /tvheadend && ./configure && make
RUN groupadd -g 9981 hts && useradd -m -d /tvheadend -u 9981 -g 9981 hts && chown -R hts:hts /tvheadend

WORKDIR /tvheadend
VOLUME /config
VOLUME /recordings
EXPOSE 9981 9982
CMD /tvheadend/build.linux/tvheadend -C -d -u hts -g hts --config /config

