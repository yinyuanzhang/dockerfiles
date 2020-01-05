# 基础镜像
FROM jenkins/jenkins:lts

LABEL maintainer = "leafiy <t@leafiy.com>"

# 切换为root用户
USER root

# 升级到debian10以便使用certbot nginx插件
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade
RUN apt-get update
RUN apt-get install --assume-yes --no-install-recommends  \
    apt-transport-https \
    ca-certificates \
    curl \
    nginx \
    gnupg-agent \
    software-properties-common \
    git \
    nano

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get update
RUN apt-get install --assume-yes --no-install-recommends  \
    yarn \
    nodejs


RUN apt-get -y install certbot python-certbot-nginx

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
RUN npm install -g pm2


CMD sh -c jenkins.sh && nginx -g 'daemon off;'