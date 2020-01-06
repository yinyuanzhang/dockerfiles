FROM omisegoimages/elixir:1.6-otp20-stretch
MAINTAINER Kridsada Thanabulpong <sirn@omise.co>

ENV LIBSODIUM_VERSION="1.0.15"

RUN set -xe && \
    apt-get update && \
    apt-get install -y --no-install-recommends imagemagick && \
    apt-get clean

RUN set -xe && \
    LIBSODIUM_DOWNLOAD_URL="https://download.libsodium.org/libsodium/releases/libsodium-${LIBSODIUM_VERSION}.tar.gz" && \
    LIBSODIUM_DOWNLOAD_SHA256="fb6a9e879a2f674592e4328c5d9f79f082405ee4bb05cb6e679b90afe9e178f4" && \
    build_deps="autoconf autogen automake libtool" && \
    apt-get update && \
    apt-get install -y --no-install-recommends $build_deps && \
    curl -fsL -o libsodium-src.tar.gz "${LIBSODIUM_DOWNLOAD_URL}" && \
    echo "$LIBSODIUM_DOWNLOAD_SHA256  libsodium-src.tar.gz" | sha256sum -c - && \
    mkdir -p /usr/local/src/libsodium && \
    tar -xzC /usr/local/src/libsodium --strip-components=1 -f libsodium-src.tar.gz && \
    rm libsodium-src.tar.gz && \
    cd /usr/local/src/libsodium && \
    ./autogen.sh && \
    ./configure && \
    make -j$(nproc) && \
    make check && \
    make install && \
    apt-get purge -y --auto-remove $build_deps && \
    apt-get clean && \
    rm -rf /usr/local/src/libsodium
