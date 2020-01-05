FROM openjdk:8u181-jdk-alpine

ENV TZ=Asia/Shanghai

RUN apk add --no-cache tzdata \
    && echo "${TZ}" > /etc/timezone \ 
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime