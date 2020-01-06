FROM openjdk:8-alpine

RUN apk add -U \
    ca-certificates \
    openssl \
    lsof \
    su-exec \
    bash \
    curl iputils wget \
    mysql-client \
    vim \
    rm -rf /var/cache/apk/*

WORKDIR /home/mc/server
COPY server .

ENV MAX_RAM="1G" \
    MC_VERSION="1.8.8" \
    MAX_PLAYERS="100" \
    PORT="25565" \
    VIEW_DISTANCE="10" \
    WHITELIST="false" \
    GAMEMODE="survival"

CMD ["bash", "start.sh"]
