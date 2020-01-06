FROM alpine:3.10.1
MAINTAINER ThomasK <t@kuhlins.org>

RUN apk add --update openjdk11-jre-headless && rm -rf /var/cache/apk/*

ADD https://repo.kuhlins.org/artifactory/public/net/limbomedia/limboesp/0.1/limboesp-0.1.jar /limboesp.jar
RUN mkdir data

VOLUME /data

EXPOSE 8080

ENTRYPOINT java -Ddir=/data -jar /limboesp.jar
