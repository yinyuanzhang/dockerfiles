FROM alpine:3.10.1
MAINTAINER ThomasKuh <t@kuhlins.org>

RUN apk add --update openjdk11-jre-headless && rm -rf /var/cache/apk/*

ADD https://repo.kuhlins.org/artifactory/public/net/limbomedia/limbodns/5.1/limbodns-5.1-jar-with-dependencies.jar /limbodns.jar
RUN mkdir data

VOLUME /data

EXPOSE 7777
EXPOSE 53/tcp
EXPOSE 53/udp

ENTRYPOINT java -Ddir=/data -jar /limbodns.jar
