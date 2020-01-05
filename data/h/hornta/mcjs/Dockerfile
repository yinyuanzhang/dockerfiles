FROM        openjdk:11-jre-slim

LABEL       author="Michael Parker" maintainer="parker@pterodactyl.io"

RUN apt-get update -y \
  && apt-get install -y curl ca-certificates openssl git tar sqlite fontconfig tzdata iproute2 \
  && useradd -d /home/container -m container && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs

USER        container
ENV         USER=container HOME=/home/container

WORKDIR     /home/container

COPY        ./entrypoint.sh /entrypoint.sh

CMD         ["/bin/bash", "/entrypoint.sh"]
