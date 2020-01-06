#
# Build image
#
FROM debian:stretch-slim as build
LABEL maintainer="Pavel Volkovitskiy <olfway@olfway.net>"

ENV LANG 'C.UTF-8'
ENV DEBIAN_FRONTEND=noninteractive

ARG QEMU_RELEASE=2.12.0
ARG QEMU_RELEASE_SUM=e69301f361ff65bf5dabd8a19196aeaa5613c1b5ae1678f0823bdf50e7d5c6fc

RUN set -x \
    && echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/zz-no-install-recommends

RUN set -x \
    && apt-get update \
    && apt-get dist-upgrade -y

RUN set -x \
    && apt-get install -y \
       bison \
       build-essential \
       ca-certificates \
       curl \
       file \
       flex \
       gnupg \
       libglib2.0-dev \
       libpixman-1-dev \
       pkg-config \
       python \
       rename \
       zlib1g-dev

WORKDIR /usr/src

RUN set -x \
    && curl -s -o "qemu-${QEMU_RELEASE}.tar.xz" "https://download.qemu.org/qemu-${QEMU_RELEASE}.tar.xz" \
    && echo "${QEMU_RELEASE_SUM} qemu-${QEMU_RELEASE}.tar.xz" | sha256sum --check \
    && tar -axf "qemu-${QEMU_RELEASE}.tar.xz"

WORKDIR /usr/src/qemu

RUN set -x \
    && /usr/src/qemu-${QEMU_RELEASE}/configure \
        --prefix=/usr \
        --disable-blobs \
        --disable-system \
        --disable-tools \
        --disable-guest-agent \
        --static \
        --target-list=arm-linux-user,aarch64-linux-user \
    && make \
    && make install DESTDIR=/usr/src/qemu-root/ \
    && rename 's/$/-static/' /usr/src/qemu-root/usr/bin/*

CMD [ "/bin/bash" ]

#
# Production image
#
FROM scratch
LABEL maintainer="Pavel Volkovitskiy <olfway@olfway.net>"

COPY --from=build /usr/src/qemu-root/usr/bin/* /
