############################################################
# Dockerfile that builds a GarrysMod Gameserver
############################################################
FROM cm2network/steamcmd
LABEL maintainer="martin@sirscythe.net"


# Install lib32tinfo5
USER root
RUN apt-get update && apt-get -y upgrade && \
apt-get install -y lib32tinfo5 && \
apt-get clean autoclean && \
apt-get autoremove -y && \
rm -rf /var/lib/{apt,dpkg,cache,log}


# Run Steamcmd and install Gmod
USER steam
RUN ./home/steam/steamcmd/steamcmd.sh +login anonymous \
        +force_install_dir /home/steam/gmod-dedicated \
        +app_update 4020 validate \
        +quit

ENV MAP=gm_construct EXTRAARGS=""

VOLUME /home/steam/gmod-dedicated

# Set Entrypoint; Technically 2 steps: 1. Update server, 2. Start server
ENTRYPOINT ./home/steam/steamcmd/steamcmd.sh +login anonymous +force_install_dir /home/steam/gmod-dedicated +app_update 4020 +quit && \
        ./home/steam/gmod-dedicated/srcds_run -game garrysmod +map $MAP $EXTRAARGS

# Expose ports
EXPOSE 27015/udp 27005
