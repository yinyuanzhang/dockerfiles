#
# MiniDLNA Dockerfile
#

# Pull base image.
FROM debian:jessie-slim

MAINTAINER dvare

# Add config files
ADD minidlna.conf /etc/minidlna.conf
ADD minidlna /etc/default/minidlna
ADD init.d_minidlna /etc/init.d/minidlna

# Add starter 
ADD start.sh /root/start.sh

# Install MiniDLNA(ReadyMedia).
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends git \
    autopoint debhelper dh-autoreconf gcc libavutil-dev libavcodec-dev libavformat-dev \
    libjpeg-dev libsqlite3-dev libexif-dev libid3tag0-dev libogg-dev libvorbis-dev libflac-dev && \
  cd /tmp && \
  git config --global http.sslVerify false && \
  git clone https://github.com/dva-re/minidlna.git && \
  cd minidlna && \
  ./autogen.sh && \
  ./configure && \
  make && make install && \
  rm -rf /tmp/midlna && \
  apt-get remove --purge -y autopoint debhelper dh-autoreconf gcc git && \
  apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \
  rm -rf /var/cache/debconf/*-old && rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && \
  chmod +x /etc/init.d/minidlna && chmod +x /root/start.sh && update-rc.d minidlna defaults

# Define mountable directories.
VOLUME /media
VOLUME /config

# Define default command.
CMD ["/bin/bash", "/root/start.sh"]

# Expose ports.
#   - 1900: UPnP
#   - 8200: HTTP
EXPOSE 1900/udp
EXPOSE 8200
