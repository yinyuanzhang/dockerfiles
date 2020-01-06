FROM ubuntu:18.04

RUN apt-get update &&  \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    subversion g++ zlib1g-dev build-essential git python rsync man-db \
    libncurses5-dev gawk gettext unzip file libssl-dev wget zip time

RUN useradd openwrt-maker && mkdir /home/openwrt-maker && \
    chown openwrt-maker /home/openwrt-maker

USER openwrt-maker

WORKDIR /home/openwrt-maker

RUN git clone https://git.openwrt.org/openwrt/openwrt.git || \
    git clone git://git.openwrt.org/openwrt/openwrt.git || \
    git clone https://github.com/openwrt/openwrt.git

WORKDIR /home/openwrt-maker/openwrt

CMD ["bash"]
