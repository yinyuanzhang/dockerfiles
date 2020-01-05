FROM aibar/alpine-base:3.4

ENV JAVA_HOME=/usr/lib/jvm/default-jvm

RUN apk update && \
    apk upgrade && \
    apk add openjdk8 && \
    rm -rf /var/cache/apk/*