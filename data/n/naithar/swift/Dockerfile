FROM ubuntu:16.04
MAINTAINER Sergey Minakov <naithar@icloud.com>

ENV CURL_VERSION=7.47.0
ENV CURL_UBUNTU_VERSION=1ubuntu2.2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
    && apt-get -y install apt-utils \
    && apt-get -y install software-properties-common \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial main restricted \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates main restricted \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial universe \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates universe \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse \
     >> /etc/apt/sources.list \
    && echo deb-src http://archive.canonical.com/ubuntu xenial partner \
     >> /etc/apt/sources.list \
    && apt-get -y update \
    && apt-get -y build-dep curl

RUN apt-get -y install git \
    && git clone https://github.com/tatsuhiro-t/nghttp2.git \
    && cd nghttp2 \
    && autoreconf -i \
    && automake \
    && autoconf \
    && ./configure \
    && make \
    && make install \
    && ldconfig /usr/local/lib

RUN apt-get -y install wget \
    && apt-get build-dep curl \
    && wget http://curl.haxx.se/download/curl-$CURL_VERSION.tar.bz2 \
    && tar -xvjf curl-$CURL_VERSION.tar.bz2 \
    && cd curl-$CURL_VERSION \
    && ./configure --with-nghttp2=/usr/local --with-ssl \
    && make \
    && make install \
    && ldconfig /usr/local/lib

RUN apt-get -y purge \
      build-essential \
      autoconf \
      automake \
      autotools-dev \
      cpp-5 \
      debhelper \
      g++-5 \
      libstdc++-5-dev \
      gcc-5 \
      libgcc-5-dev \
      intltool-debian \
      make \
      m4 \
      patch \
      python2.7 \
      libpython2.7-minimal \
      perl \
      perl-modules-5.22 \
      libp11-kit-dev \
      libtasn1-6-dev \
      nettle-dev \
    && apt-get -y autoremove \
    && rm -rf /tmp/*

RUN curl --version
RUN curl --http2 -I nghttp2.org

# Install related packages and set LLVM 3.6 as the compiler
RUN apt-get -q update && \
    apt-get -q install -y \
    make \
    libc6-dev \
    clang-3.8 \
    libedit-dev \
    python2.7 \
    python2.7-dev \
    libicu-dev \
    libssl-dev \
    libxml2 \
    git \
    pkg-config \
    && update-alternatives --quiet --install /usr/bin/clang clang /usr/bin/clang-3.8 100 \
    && update-alternatives --quiet --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.8 100 \
    && rm -r /var/lib/apt/lists/*

# Everything up to here should cache nicely between Swift versions, assuming dev dependencies change little
ARG SWIFT_PLATFORM=ubuntu16.04
ARG SWIFT_BRANCH=swift-3.1.1-release
ARG SWIFT_VERSION=swift-3.1.1-RELEASE

ENV SWIFT_PLATFORM=$SWIFT_PLATFORM \
    SWIFT_BRANCH=$SWIFT_BRANCH \
    SWIFT_VERSION=$SWIFT_VERSION

# Download GPG keys, signature and Swift package, then unpack and cleanup
RUN SWIFT_URL=https://swift.org/builds/$SWIFT_BRANCH/$(echo "$SWIFT_PLATFORM" | tr -d .)/$SWIFT_VERSION/$SWIFT_VERSION-$SWIFT_PLATFORM.tar.gz \
    && curl -fSsL $SWIFT_URL -o swift.tar.gz \
    && curl -fSsL $SWIFT_URL.sig -o swift.tar.gz.sig \
    && export GNUPGHOME="$(mktemp -d)" \
    && set -e; \
        for key in \
      # pub   4096R/412B37AD 2015-11-19 [expires: 2017-11-18]
      #       Key fingerprint = 7463 A81A 4B2E EA1B 551F  FBCF D441 C977 412B 37AD
      # uid                  Swift Automatic Signing Key #1 <swift-infrastructure@swift.org>
          7463A81A4B2EEA1B551FFBCFD441C977412B37AD \
      # pub   4096R/21A56D5F 2015-11-28 [expires: 2017-11-27]
      #       Key fingerprint = 1BE1 E29A 084C B305 F397  D62A 9F59 7F4D 21A5 6D5F
      # uid                  Swift 2.2 Release Signing Key <swift-infrastructure@swift.org>
          1BE1E29A084CB305F397D62A9F597F4D21A56D5F \
      # pub   4096R/91D306C6 2016-05-31 [expires: 2018-05-31]
      #       Key fingerprint = A3BA FD35 56A5 9079 C068  94BD 63BC 1CFE 91D3 06C6
      # uid                  Swift 3.x Release Signing Key <swift-infrastructure@swift.org>
          A3BAFD3556A59079C06894BD63BC1CFE91D306C6 \
        ; do \
          gpg --quiet --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
        done \
    && gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz \
    && tar -xzf swift.tar.gz --directory / --strip-components=1 \
    && rm -r "$GNUPGHOME" swift.tar.gz.sig swift.tar.gz

# Post cleanup for binaries orthogonal to swift runtime, but was used to download and install.
RUN apt-get -y remove --purge \
    python2.7

# Print Installed Swift Version
RUN swift --version
RUN curl --version
RUN curl --http2 -I nghttp2.org
