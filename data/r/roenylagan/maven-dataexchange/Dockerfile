FROM maven:3.6.0-jdk-8-alpine

COPY settings-docker.xml /usr/share/maven/ref/

RUN apk update && apk add --no-cache git openssh
RUN git config --global user.email "roen@dataexchange.io"
RUN git config --global user.name "Roen Ylagan"