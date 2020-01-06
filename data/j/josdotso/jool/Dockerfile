# TL;DR:
#
# $ docker run --rm --privileged --network host \
#     -v /usr/src:/usr/src -v /lib/modules:/lib/modules \
#     --name jool josdotso/jool
#
# Debian 9 amd64 was used in the development
# of this Dockerfile.
#
# Kernel headers must be pre-installed on the
# host machine. Here is how you might do that
# for Debian 9:
#
#   $ apt install linux-headers-$(uname -r)
#
# This container image builds kernel modules, so:
#
# * It is necessary to mount (read/write)
#   `/usr/rc` and `/lib/modules` from the host.
#
# * The container will be slow to start, because
#   it may need to build kernel modules.
#
# * TODO: Detect if kernel modules already exist
#         and skip building if so.
#
FROM debian:9-slim

RUN apt update \
 && apt install -y \
      autoconf \
      build-essential \
      curl \
      dkms \
      git \
      iproute \
      iptables \
      libnl-genl-3-dev \
      libxtables-dev \
      pkg-config \
      tar \
 && git clone https://github.com/NICMx/Jool.git /opt/jool \
 && cd /opt/jool \
 && ./autogen.sh \
 && ./configure \
 && cd src/usr \
 && make \
 && make install \
 && apt clean \
 && echo OK

COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

VOLUME ["/usr/src", "/lib/modules"]
