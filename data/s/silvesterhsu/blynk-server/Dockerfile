FROM ubuntu as build

RUN mkdir /blynk

RUN apt update && \
    apt install curl -y && \
    apt clean

RUN curl -L https://github.com/blynkkk/blynk-server/releases/download/v0.41.6/server-0.41.6-java8.jar > /blynk/server.jar

FROM openjdk:8u212-jre-slim
MAINTAINER SilvesterHsu <459745355@qq.com>

ENV BLYNK_SERVER_VERSION 0.41.6
RUN mkdir /blynk
COPY --from=build /blynk/server.jar /blynk/server.jar

# Create data folder. To persist data, map a volume to /data
RUN mkdir /data

# Create configuration folder. To persist data, map a file to /config/server.properties
RUN mkdir /config && touch /config/server.properties
VOLUME ["/config", "/data"]

# IP port listing:
# 8080: Hardware without ssl/tls support
# 9443: Blynk app, https, web sockets, admin port
EXPOSE 8080 9443

WORKDIR /data
ENTRYPOINT ["java", "-jar", "/blynk/server.jar", "-dataFolder", "/data", "-serverConfig", "/config/server.properties"]
