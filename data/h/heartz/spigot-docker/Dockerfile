FROM openjdk:8-jre-alpine

VOLUME ["/data"]

COPY paper.jar /paper.jar
COPY start_server.sh /start_server.sh

RUN  apk update \
    && adduser -D -h /data minecraft \
    && chmod +x start_server.sh

EXPOSE 25565