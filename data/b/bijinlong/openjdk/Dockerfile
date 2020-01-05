FROM openjdk:8-alpine
ENV TZ Asia/Shanghai
RUN apk add -U tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo $TZ > /etc/timezone
