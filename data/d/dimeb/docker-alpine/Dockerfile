FROM alpine:3.8

ARG TIME_ZONE=Europe/Brussels

RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && echo "${TIME_ZONE}" >  /etc/timezone \
    && apk del tzdata \
    && apk add --no-cache ca-certificates && update-ca-certificates \
    && apk add --no-cache openssl
