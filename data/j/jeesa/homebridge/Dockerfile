ARG S6_ARCH
FROM oznu/s6-node:10.16.0-${S6_ARCH:-amd64}

# build ffmpeg
ARG FFMPEG_VERSION=4.1.2
ARG PREFIX=/opt/ffmpeg
ARG LD_LIBRARY_PATH=/opt/ffmpeg/lib
ARG MAKEFLAGS="-j4"

# add ffmpeg folder
RUN mkdir /opt/ffmpeg

# FFmpeg build dependencies.
RUN apk add --update \
build-base \
coreutils \
freetype-dev \
gcc \
lame-dev \
libogg-dev \
libass \
libass-dev \
libvpx-dev \
libvorbis-dev \
libwebp-dev \
libtheora-dev \
opus-dev \
pkgconf \
pkgconfig \
rtmpdump-dev \
wget \
x264-dev \
x265-dev \
yasm git python make g++ avahi-compat-libdns_sd avahi-dev dbus iputils sudo nano

# Get fdk-aac from testing.
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
apk add --update fdk-aac-dev

# Get ffmpeg source.
RUN cd /tmp/ && \
wget http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz && \
tar zxf ffmpeg-${FFMPEG_VERSION}.tar.gz && rm ffmpeg-${FFMPEG_VERSION}.tar.gz

# Compile ffmpeg.
RUN cd /tmp/ffmpeg-${FFMPEG_VERSION} && \
./configure \
--enable-version3 \
--enable-gpl \
--enable-nonfree \
--enable-small \
--enable-libmp3lame \
--enable-libx264 \
--enable-libx265 \
--enable-libvpx \
--enable-libtheora \
--enable-libvorbis \
--enable-libopus \
--enable-libfdk-aac \
--enable-libass \
--enable-libwebp \
--enable-librtmp \
--enable-postproc \
--enable-avresample \
--enable-libfreetype \
--enable-openssl \
--disable-debug \
--disable-doc \
--disable-ffplay \
--extra-cflags="-I${PREFIX}/include" \
--extra-ldflags="-L${PREFIX}/lib" \
--extra-libs="-lpthread -lm" \
--prefix="${PREFIX}" && \
make -j8 && make install && make distclean

# Cleanup.
RUN rm -rf /var/cache/apk/* /tmp/*

ENV PATH=/opt/ffmpeg/bin:$PATH

# Install Homebridge
RUN chmod 4755 /bin/ping \
&& mkdir /homebridge \
&& npm set global-style=true \
&& npm set package-lock=false

ENV HOMEBRIDGE_VERSION=0.4.50
RUN npm install -g --unsafe-perm homebridge@${HOMEBRIDGE_VERSION}

ENV CONFIG_UI_VERSION=4.5.1
RUN npm install -g --unsafe-perm homebridge-config-ui-x@${CONFIG_UI_VERSION}

WORKDIR /homebridge
VOLUME /homebridge

COPY root /

ARG AVAHI
RUN [ "${AVAHI:-1}" = "1" ] || (echo "Removing Avahi" && \
rm -rf /etc/services.d/avahi \
/etc/services.d/dbus \
/etc/cont-init.d/40-dbus-avahi)
