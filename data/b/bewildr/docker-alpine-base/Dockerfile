FROM alpine:latest
LABEL maintainer="Aadryn <aadryn@users.noreply.github.com>"
RUN apk add -q --no-cache curl wget bash nano vim tzdata \
    && apk del -q --no-cache --purge \
    && rm -rf /tmp/*

ENV TERM=xterm
ENV TZ=Europe/Paris
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8