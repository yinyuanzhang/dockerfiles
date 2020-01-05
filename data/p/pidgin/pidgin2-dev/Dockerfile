# vi:ft=dockerfile

FROM debian:stretch-slim

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libpurple-dev finch-dev pidgin-dev \
        automake autoconf libtool intltool \
        make meson ninja-build cmake \
        libsoup2.4-dev libjson-glib-dev \
        libgcrypt20-dev zlib1g-dev libprotobuf-c-dev protobuf-c-compiler \
    && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists

