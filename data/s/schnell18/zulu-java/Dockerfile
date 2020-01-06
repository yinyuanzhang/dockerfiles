FROM alpine:3.10
MAINTAINER Justin Zhang "schnell18@gmail.com"

RUN apk add --no-cache ca-certificates && \
    update-ca-certificates && \
    apk add --no-cache --update curl bash tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

ARG ZULU_JRE="zulu11.31.11-ca-jre11.0.3-linux_musl_x64"
ARG ZULU_DOWNLOAD_URL="https://cdn.azul.com/zulu/bin/${ZULU_JRE}.tar.gz"
RUN curl -L --silent ${ZULU_DOWNLOAD_URL} | tar -xzf - -C / && \
    mv /$ZULU_JRE /jre

ENV PATH $PATH:/jre/bin