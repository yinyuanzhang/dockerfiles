# Minecraft Server image

FROM openjdk:8-jre-alpine

MAINTAINER Jiri Zuna <jiri@zunovi.cz>

ENV MINECRAFT_VERSION=1.15.1
ENV MINECRAFT_JAR="https://launcher.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar"

# Install wget and certificates
RUN     apk update \
    &&  apk add ca-certificates wget bash \
    &&  update-ca-certificates

# Download the server jar file
RUN  	mkdir -p /opt/minecraft \
    &&  cd /opt/minecraft \
    &&  wget -q $MINECRAFT_JAR

WORKDIR /data
VOLUME /data

EXPOSE 25565

ADD ./minecraft.sh /opt
RUN chmod a+x /opt/minecraft.sh

CMD /opt/minecraft.sh