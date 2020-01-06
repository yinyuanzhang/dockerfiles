FROM linuxserver/rutorrent:arm64v8-latest

# set labels
LABEL maintainer="Nightah"

# modifications
RUN \
 echo "**** apply patch for /downloads/ ****" && \
 sed -i '7d;32,36d' /etc/cont-init.d/50-config

# ports and volumes
EXPOSE 80
VOLUME /config /downloads