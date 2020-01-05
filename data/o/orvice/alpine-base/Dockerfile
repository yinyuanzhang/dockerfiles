FROM alpine

RUN apk update
RUN apk upgrade
RUN apk add ca-certificates && update-ca-certificates
# Change TimeZone
RUN apk add --update tzdata
ENV TZ=Asia/Shanghai
# Clean APK cache
RUN rm -rf /var/cache/apk/*
