FROM lolhens/baseimage-oraclejdk:latest
MAINTAINER LolHens <pierrekisters@gmail.com>


ENV UNTISICALSERVER_VERSION 2.0.5
ENV UNTISICALSERVER_NAME untisicalserver-$UNTISICALSERVER_VERSION
ENV UNTISICALSERVER_FILE $UNTISICALSERVER_NAME.zip
ENV UNTISICALSERVER_URL https://github.com/LolHens/UntisIcalServer/releases/download/$UNTISICALSERVER_VERSION/$UNTISICALSERVER_FILE


RUN cd "/tmp" \
 && curl -LO $UNTISICALSERVER_URL \
 && unzip $UNTISICALSERVER_FILE \
 && mv $UNTISICALSERVER_NAME "/usr/local/untisicalserver/" \
 && cleanimage


WORKDIR /usr/local/untisicalserver/bin
CMD ./untisicalserver


EXPOSE 8080
