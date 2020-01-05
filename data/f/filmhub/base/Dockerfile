FROM ruby:2.6.5-slim-buster
COPY 99-timeout.apt.conf /etc/apt/apt.conf.d/99-timeout

ARG DEBIAN_FRONTEND=noninteractive
# http://ffmpeg.org/releases
ARG FFMPEG_VERSION=4.2.1
# https://www.nasm.us/
# https://www.nasm.us/pub/nasm/releasebuilds
ARG NASM_VERSION=2.14.02
# http://download.videolan.org/pub/x264/snapshots/
ARG X264_VERSION=20191214-2245-stable
# https://bitbucket.org/multicoreware/x265/downloads
ARG X265_VERSION=3.2.1
# https://github.com/mltframework/mlt/releases
ARG MLT_VERSION=6.18.0
# https://mediaarea.net/en/MediaInfo/Download/Debian
ARG MEDIAINFO_VERSION=19.09
ARG LIBZEN0_VERSION=0.4.37
# https://github.com/nodesource/distributions#deb
ARG NODE_MAJOR=10
# https://yarnpkg.com/en/docs/install#debian-stable
ARG YARN_VERSION=1.21.1
ARG PG_MAJOR=11
ARG MAKEFLAGS="-j 4"

# @see http://redsymbol.net/articles/unofficial-bash-strict-mode/
RUN set -eux && \
  PREFIX=/usr/local \
  PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig" \
  CFLAGS=-w \
  # X265_BUILD_DEPS="libnuma-dev" \
  # X265_RUNTIME_DEPS="libnuma1" \
  NASM_BUILD_DEPS="asciidoc autoconf automake pkg-config libgtk-3-dev xmlto" \
  FFMPEG_BUILD_DEPS="autoconf automake cmake libass-dev python texinfo" \
  FFMPEG_RUNTIME_DEPS="libass9" \
  MELT_BUILD_DEPS="pkg-config libxml2-dev" \
  MELT_RUNTIME_DEPS="libxml2" \
  MEDIAINFO_RUNTIME_DEPS="libmms0 libcurl3-gnutls" \
  BUILD_DEPS="\
    $FFMPEG_BUILD_DEPS \
    $NASM_BUILD_DEPS \
    $MELT_BUILD_DEPS \
    gnupg2 \
    libc-dev \
    libtool \
    pkg-config \
    xz-utils \
    yasm" \
  RUNTIME_DEPS=" \
    $FFMPEG_RUNTIME_DEPS \
    $MEDIAINFO_RUNTIME_DEPS \
    $MELT_RUNTIME_DEPS \
    bash-completion \
    curl \
    fontconfig \
    g++ \
    gcc \
    git \
    imagemagick \
    less \
    libicu-dev \
    libpq-dev \
    libsqlite3-dev \
    make \
    zlib1g-dev" \

# Install dependencies
  && apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends $RUNTIME_DEPS $BUILD_DEPS \

# Add custom repos
# NodeJS
# RUN curl -sL https://deb.nodesource.com/setup_$NODE_MAJOR.x | bash -
  && curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
  && echo 'deb https://deb.nodesource.com/node_10.x buster main' > /etc/apt/sources.list.d/nodesource.list \

# Yarn
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo 'deb https://dl.yarnpkg.com/debian/ stable main' | tee /etc/apt/sources.list.d/yarn.list \

# PostgreSQL client
  && curl -sSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' > /etc/apt/sources.list.d/pgdg.list \

# Install from custom repos
  && apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    nodejs \
    postgresql-client-$PG_MAJOR \
    yarn=$YARN_VERSION-1 \

#
# Build from source
#
  && TMP_DIR=$(mktemp -d) && cd $TMP_DIR \
#
# nasm
#
  && curl --retry 5 -Ls https://www.nasm.us/pub/nasm/releasebuilds/${NASM_VERSION}/nasm-${NASM_VERSION}.tar.gz | tar zxf - -C $TMP_DIR \
  && cd $TMP_DIR/nasm* \
  && ./autogen.sh \
  && ./configure -q --prefix=$PREFIX --bindir=$PREFIX/bin --mandir=$TMP_DIR \
  && make --silent \
  && make --silent install \
#
# x264
#
  && curl --retry 5 -Ls http://download.videolan.org/pub/x264/snapshots/x264-snapshot-${X264_VERSION}.tar.bz2 | tar -jxf - -C $TMP_DIR \
  && cd $TMP_DIR/x264* \
  && ./configure  --extra-cflags=-w --prefix=$PREFIX --bindir=$PREFIX/bin --disable-opencl --enable-shared \
  && make --silent \
  && make --silent install \
#
# libx265: H.265/HEVC
#
  # && curl --retry 5 -Ls https://bitbucket.org/multicoreware/x265/downloads/x265_${X265_VERSION}.tar.gz | tar zxf - -C $TMP_DIR \
  # && cd $TMP_DIR/x265*/build/linux \
  # && cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="$PREFIX" -DENABLE_SHARED:bool=on ../../source \
  # && make --silent \
  # && make --silent install \
#
# ffmpeg
#
  # && curl --retry 5 -Ls http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.bz2 | tar jxf - -C $TMP_DIR  \
  # && cd $TMP_DIR/ffmpeg* \
  && curl --retry 5 -Ls https://github.com/FFmpeg/FFmpeg/archive/c8232e50074f6f9f9b0674d0a5433f49d73a4e50.tar.gz | tar zxf - -C $TMP_DIR  \
  && cd $TMP_DIR/FFmpeg* \
  && ./configure \
    --prefix=$PREFIX \
    --bindir=$PREFIX/bin  \
    --extra-cflags="-I$PREFIX/include -w" \
    --extra-ldflags="-L$PREFIX/lib" \
    --extra-libs="-lpthread -lm" \
    --enable-shared \
    --enable-pthreads \
    --enable-hardcoded-tables \
    --disable-static \
    --disable-debug \
    --disable-doc \
    --disable-ffplay \
    --disable-libxcb \
    --enable-gpl \
    --enable-version3 \
    --enable-nonfree \
    --enable-openssl \
    --enable-postproc \
    --enable-libass \
    --enable-libx264 \
    # --enable-libx265 \
  && make --silent \
  && make --silent install  \
  && hash -r \
  && ldconfig \
#
# Melt
#
  && curl --retry 5 -Ls https://github.com/mltframework/mlt/archive/v${MLT_VERSION}.tar.gz | tar zxf - -C $TMP_DIR \
  && cd $TMP_DIR/mlt* \
  && ./configure \
    -q \
    --prefix=$PREFIX \
    --extra-cflags=-w \
    --docdir=$TMP_DIR \
    --mandir=$TMP_DIR \
    --enable-gpl \
    --disable-frei0r \
    --disable-gtk2 \
    --disable-jackrack \
    --disable-opengl \
    --disable-rtaudio \
    --disable-swfdec  \
    --disable-gtk  \
    --disable-qt \
  && make --silent \
  && make --silent install \
  && ldconfig \
#
# Mediainfo
# https://mediaarea.net/download/binary/libzen0/0.4.37/libzen0v5_0.4.37-1_amd64.Debian_9.0.deb
# python-dev \
  && cd $TMP_DIR \
  && curl --retry 5 \
    -Ls https://mediaarea.net/download/binary/libzen0/${LIBZEN0_VERSION}/libzen0v5_${LIBZEN0_VERSION}-1_amd64.Debian_9.0.deb --output libzen0.deb \
    -Ls https://mediaarea.net/download/binary/libmediainfo0/${MEDIAINFO_VERSION}/libmediainfo0v5_${MEDIAINFO_VERSION}-1_amd64.Debian_9.0.deb --output libmediainfo0.deb \
    -Ls https://mediaarea.net/download/binary/mediainfo/${MEDIAINFO_VERSION}/mediainfo_${MEDIAINFO_VERSION}-1_amd64.Debian_9.0.deb --output mediainfo.deb \
  && dpkg -i libzen0.deb libmediainfo0.deb mediainfo.deb \
#
# clean-up
#
  && cd / \
  && apt-get purge --auto-remove -y $BUILD_DEPS apt-utils \
  && apt-get clean \
  && rm -rf /tmp/* /var/tmp/* \
  && rm -rf /var/lib/apt/lists/* \
  && truncate -s 0 /var/log/*log \
#
# test that builds work
#
  && x264 -V \
  # && x265 -V \
  && ffmpeg -buildconf \
  && melt --version \
  && mediainfo --version || [ $? -eq 255 ] || [ $? -eq 16 ] \
  && node --version

COPY bashrc /root/.bashrc
COPY policy.xml /etc/ImageMagick-6/policy.xml
CMD ["/bin/bash"]
