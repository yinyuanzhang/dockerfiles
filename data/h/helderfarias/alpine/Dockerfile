FROM alpine:3.7
RUN apk add -U tzdata curl && cp /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
