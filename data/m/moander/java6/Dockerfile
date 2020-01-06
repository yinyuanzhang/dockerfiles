FROM buildpack-deps:jessie-curl

RUN apt-get update && apt-get install -y --no-install-recommends nano \
 && rm -rf /var/lib/apt/lists/*

MAINTAINER Morten Andersen <moander@outlook.com>

RUN mkdir -p /usr/java \
 && curl -sS https://storage.googleapis.com/mpub/java/jdk-6u45-linux-x64.bin -o java.bin \
 && chmod +x java.bin \
 && ./java.bin \
 && rm -f java.bin \
 && mv jdk1.6.0_45 /usr/java

ENV JAVA_HOME=/usr/java/jdk1.6.0_45

ENV PATH=${JAVA_HOME}/bin:${PATH}

