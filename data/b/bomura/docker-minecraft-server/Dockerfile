FROM openjdk:8-jre-alpine
LABEL maintainer 'bomura'

WORKDIR /minecraft-server

RUN apk add curl

ARG MC_SRV_VER

RUN MC_SRV_LATEST_VER=`curl -Lso- https://mcversions.net | grep -oE 'release latest" id="[0-9.]+' | grep -oE '[0-9.]+'` \
 && MC_SRV_URL=`curl -Lso- https://mcversions.net | grep -A3 -E "\"${MC_SRV_VER:=${MC_SRV_LATEST_VER}}\"" | grep -oE 'https.+server.jar'` \
 && curl -O ${MC_SRV_URL}

COPY entrypoint-minecraft-server.sh /entrypoint-minecraft-server.sh

EXPOSE 25565

ENTRYPOINT ["/entrypoint-minecraft-server.sh"]
CMD ["java", "-jar", "server.jar", "nogui"]
