# # Glassfish 5.0 with JDK 8 Docker image
# Based on: https://github.com/aws/aws-eb-glassfish-dockerfiles/blob/aafcfc5e812dfb9b998105d3ca9da1b7f10664e1/4.0-jdk7/Dockerfile

FROM        openjdk:8-jdk-alpine

MAINTAINER  Almir Dzinovic <almirdzin@gmail.com>

ENV         JAVA_HOME         /usr/lib/jvm/default-jvm
ENV         GLASSFISH_HOME    /usr/glassfish
ENV         PATH              $PATH:$JAVA_HOME/bin:$GLASSFISH_HOME/bin

RUN         apk --update --upgrade add curl unzip zip inotify-tools ca-certificates && \
            rm -rf /var/cache/apk/*

RUN         curl -L -o /tmp/glassfish5.zip http://download.oracle.com/glassfish/5.0/release/glassfish-5.0.zip && \
            unzip /tmp/glassfish5.zip -d /usr && \
            mv -f /usr/glassfish5 /usr/glassfish && \
            rm -f /tmp/glassfish5.zip && \
            find /usr/glassfish/glassfish/ -name "*.bat" -exec rm -f {} \;

EXPOSE      8080 4848 8181

WORKDIR     /usr/glassfish

# verbose causes the process to remain in the foreground so that docker can track it
CMD         asadmin start-domain --verbose
