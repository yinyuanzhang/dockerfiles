FROM debian:stretch

ENV TZ='Asia/Tokyo'

RUN apt-get update \
    && apt-get -y install devscripts debhelper dh-systemd fakeroot \
       binutils-mips-linux-gnu binutils-aarch64-linux-gnu \
       binutils-arm-linux-gnueabihf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["debuild"]
