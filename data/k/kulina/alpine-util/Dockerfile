FROM alpine:3.2
MAINTAINER Didiet Noor <dnoor@kulina.id> (@lynxluna)

ENV TERM dumb
# Patch APK Mirror to YKode
RUN echo "https://alpine.ykode.com/alpine/v3.2/main" > /etc/apk/repositories

RUN apk update && apk add curl && \
  rm -rf /var/cache/apk/*
