# Garrys Mod - CSS Content 
#
# VERSION 0.1

FROM bfosberry/steam_base
MAINTAINER bfosberry

# prep data folder
RUN mkdir -p /opt/mods/css-content
WORKDIR /opt/mods/css-content

RUN /opt/steam/steamcmd.sh +force_install_dir "/opt/mods/css-content/" +login anonymous  +app_update 232330 +quit
ENTRYPOINT /bin/bash
VOLUME /opt/mods/css-content
