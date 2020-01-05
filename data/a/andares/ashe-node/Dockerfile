FROM node:lts-alpine
LABEL maintainer="A.M <andares@outlook.com>"

ENV VERSION 1.0
ARG scene=default

# CMD ["sh", "-c", "echo", "container build at $scene"]

# 创建目录
# 安装PM2一套
RUN mkdir -p /worker/apps \
    && mkdir -p /worker/logs \
    && mkdir -p /worker/swap \
    && apk add --no-cache bash git openssh \
    && npm i -g pm2 babel-cli babel-register \
    && pm2 install pm2-logrotate \
    && pm2 install pm2-intercom

COPY worker/bootstrap.bash /worker/bootstrap.bash

RUN apk add --no-cache zsh openrc \
    && chmod +x /usr/local/bin/*

ENTRYPOINT ["bash", "/worker/bootstrap.bash"]