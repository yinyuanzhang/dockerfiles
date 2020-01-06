
FROM openjdk:8-jre-alpine

MAINTAINER lulichn <daisuke.develop@gmail.com>

ENV DIGDAG_VERSION 0.9.15

RUN \
        apk --no-cache add --virtual deps curl && \
        curl -L https://dl.bintray.com/digdag/maven/digdag-$DIGDAG_VERSION.jar --create-dirs -o /opt/digdag && \
        apk del deps

COPY server.properties /etc/digdag/server.properties

WORKDIR /root

ENTRYPOINT ["java", "-jar", "/opt/digdag"]
CMD ["--help"]

