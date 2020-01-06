FROM hoysoft/node:10.8
MAINTAINER Justin Firth <jmfirth@gmail.com>

RUN npm config set registry http://registry.npm.taobao.org
RUN npm install -g webpack webpack-dev-server yarn

VOLUME /app

EXPOSE 3000

WORKDIR /app
