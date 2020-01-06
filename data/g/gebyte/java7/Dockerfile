# ----------------------------------
# Environment: Java  7
# please note that java 7 is no longer supported and no security updates will follow. Please use this image with care or use a Java 8 image!
# ----------------------------------
FROM openjdk:7-jdk-alpine

MAINTAINER Gebyte.com, <lukas.fichtner@gebyte.com>

RUN apk update \
    && apk upgrade \
    && apk add --no-cache --update curl ca-certificates openssl git zip tar bash lftp sqlite fontconfig tzdata iproute2 \
    && adduser -D -h /home/container container

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]