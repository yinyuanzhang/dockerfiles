FROM foundationkitty/gameservers:mono-complete

RUN \
apt-get update && \
apt-get dist-upgrade -y && \
apt-get install -y curl xdg-utils lib32stdc++ lib32gcc1 wget ca-certificates && \
mkdir /steamcmd && \
mkdir /smod && \
cd /steamcmd && \
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz

CMD \
/steamcmd/steamcmd +login "$STEAM_USERNAME" "$STEAM_PASSWORD" +force_install_dir /vanilla +app_update 996560 validate -beta Linux +quit && /vanilla/LocalAdmin "$SERVER_PORT"

WORKDIR /vanilla
