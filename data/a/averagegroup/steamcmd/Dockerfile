FROM ubuntu:latest
LABEL maintainer="admin@average.group"

WORKDIR /opt/steamcmd
RUN apt-get update; apt-get install -y curl tar lib32gcc1 lib32stdc++6; \
    curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -; \
    chmod +x steamcmd.sh;

VOLUME "/opt/steamcmd"

ENTRYPOINT [ "/opt/steamcmd/steamcmd.sh" ]