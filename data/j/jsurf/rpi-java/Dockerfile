FROM jsurf/rpi-raspbian:latest

RUN [ "cross-build-start" ]

ENV LANG C.UTF-8
ENV TZ Europe/Berlin
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get update \
    && apt-get install -y oracle-java8-jdk ca-certificates-java \
    && ln -s jdk-8-oracle-arm32-vfp-hflt $JAVA_HOME \
    && ln -sf /etc/ssl/certs/java/cacerts $JAVA_HOME/jre/lib/security/cacerts \
    && rm -rf /var/lib/apt/lists/* 

RUN [ "cross-build-end" ]
