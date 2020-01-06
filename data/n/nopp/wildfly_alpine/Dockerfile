FROM alpine:3.7

LABEL maintainer "Carlos Augusto Malucelli <malucellicarlos@gmail.com>"

ENV wildfly_version 10.1.0

RUN apk update \ 
    && apk add openssl curl unzip openjdk8-jre \
    && curl -LO http://download.jboss.org/wildfly/${wildfly_version}.Final/wildfly-${wildfly_version}.Final.zip \
    && unzip -q wildfly-${wildfly_version}.Final.zip \
    && mv wildfly-${wildfly_version}.Final /usr/share/jboss-as \
    && rm -f wildfly-${wildfly_version}.Final.zip \
    && apk del curl unzip \
    && echo "admin=c22052286cd5d72239a90fe193737253" >> /usr/share/jboss-as/standalone/configuration/mgmt-users.properties

WORKDIR /usr/share/jboss-as

EXPOSE 8080 9990

ENTRYPOINT ["./bin/standalone.sh","-b=0.0.0.0","-bmanagement=0.0.0.0"]
