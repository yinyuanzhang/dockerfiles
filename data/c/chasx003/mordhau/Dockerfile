# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: Source Engine - Mordhau
# Minimum Panel Version: 0.6.0
# ----------------------------------
FROM        ubuntu:18.04

LABEL       author="Chazx" maintainer="chasx003@gmail.com"

ENV         DEBIAN_FRONTEND noninteractive
# Install Dependencies
RUN         dpkg --add-architecture i386 \
            && apt-get update \
            && apt-get upgrade -y \
            && apt-get install -y tar curl gcc g++ lib32gcc1 screen libgcc1 libcurl4-gnutls-dev:i386 libssl1.0.0:i386 libcurl4:i386 lib32tinfo5 libtinfo5:i386 lib32z1 lib32stdc++6 libncurses5:i386 libcurl3-gnutls:i386 iproute2 gdb libsdl1.2debian libfontconfig libfontconfig1 libpangocairo-1.0-0 libnss3 libgconf2-4 libxi6 libxcursor1 libxss1 libxcomposite1 libasound2 libxdamage1 libxtst6 libatk1.0-0 libxrandr2 telnet net-tools netcat \
            && useradd -m -d /home/container container

USER        container
ENV         HOME /home/container
WORKDIR     /home/container

COPY        ./entrypoint.sh /entrypoint.sh
CMD         ["/bin/bash", "/entrypoint.sh"]
