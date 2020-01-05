FROM openjdk:8-jre-alpine

LABEL maintainer "itzg"

RUN apk add --no-cache \
          openssl \
          imagemagick \
          lsof \
          su-exec \
          bash \
          curl iputils wget \
          git \
          jq \
          python python-dev py2-pip

RUN pip install mcstatus

HEALTHCHECK CMD mcstatus localhost ping

RUN addgroup -g 1000 minecraft \
  && adduser -Ss /bin/false -u 1000 -G minecraft -h /home/minecraft minecraft \
  && mkdir /data \
  && chown minecraft:minecraft /data /home/minecraft

EXPOSE 25565 25575

ADD https://github.com/itzg/rcon-cli/releases/download/1.3/rcon-cli_linux_amd64 /usr/local/bin/rcon-cli
COPY start* /usr/local/bin/
RUN chmod +x /usr/local/bin/*

VOLUME ["/data"]
COPY server.properties /tmp/server.properties
WORKDIR /data

ENTRYPOINT [ "start" ]

ENV UID=1000 GID=1000 \
    MOTD="A Minecraft Server Powered by Docker" \
    JVM_XX_OPTS="-XX:+UseG1GC" MEMORY="1G" \
    TYPE=VANILLA VERSION=LATEST FORGEVERSION=LATEST SPONGEBRANCH=STABLE SPONGEVERSION= LEVEL=world \
    PVP=true DIFFICULTY=normal ENABLE_RCON=true RCON_PORT=25575 RCON_PASSWORD=minecraft \
    LEVEL_TYPE=DEFAULT GENERATOR_SETTINGS= WORLD= MODPACK= ONLINE_MODE=true CONSOLE=true
