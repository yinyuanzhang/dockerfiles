FROM alpine:3.5

USER root

# /dev/urandom is used as random source, which is prefectly safe
# according to http://www.2uo.de/myths-about-urandom/
RUN apk add --update \
    curl \
    openjdk8=8.121.13-r0 \
 && rm /var/cache/apk/* \
 && echo "securerandom.source=file:/dev/urandom" >> /usr/lib/jvm/default-jvm/jre/lib/security/java.security

