FROM php:7-apache

# Install PHP Curl extension
RUN apt-get update \
    && apt-get install -y libcurl4-openssl-dev \
    && docker-php-ext-install curl

RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>/etc/apt/sources.list
RUN echo "deb-src http://www.deb-multimedia.org jessie main non-free" >>/etc/apt/sources.list
RUN apt-get update && apt-get install -y --force-yes deb-multimedia-keyring

RUN apt-get update && apt-get install -y \
        wget \
        build-essential \
        libmp3lame-dev \
        libvorbis-dev \
        libtheora-dev \
        libspeex-dev \
        yasm \
        pkg-config \
        libfaac-dev \
        libopenjpeg-dev \
        libx264-dev \
        libfreetype6 \
        libfreetype6-dev \
        libfribidi-dev \
        libfontconfig1-dev

RUN mkdir /software \
    && cd /software \
    && wget http://ffmpeg.org/releases/ffmpeg-2.7.2.tar.bz2 \
    && mkdir src \
    && cd src \
    && tar xvjf ../ffmpeg-2.7.2.tar.bz2 \
    && cd ffmpeg-2.7.2 \
    && ./configure \
        --enable-gpl \
        --enable-postproc \
        --enable-swscale \
        --enable-avfilter \
        --enable-libmp3lame \
        --enable-libvorbis \
        --enable-libtheora \
        --enable-libx264 \
        --enable-libspeex \
        --enable-shared \
        --enable-pthreads \
        --enable-libopenjpeg \
        --enable-libfaac \
        --enable-nonfree \
        --enable-libfreetype \
        --enable-libfontconfig \
        --enable-libfribidi \
    && make \
    && make install \
    && rm -rf /software/ffmpeg-2.7.2 \
    && ldconfig

RUN apt-get install -y python-pip \
    && pip install youtube-dl


