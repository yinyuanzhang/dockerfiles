FROM node:9-alpine
MAINTAINER Devops Nasajon<devops@nasajon.com.br>

ENV SASS_BINARY_NAME linux-x64-57

RUN apk add -U --no-cache python ruby git openssh g++ gcc libgcc libstdc++ linux-headers make && \
    rm /var/cache/apk/*

RUN npm install -g npm && \
    npm -g config set user $USER && \
    npm install -g yarn node-sass cordova ionic@latest @ionic/cli-plugin-proxy && \
    echo y | cordova -v && \
    ionic config set -g daemon.updates false

RUN mkdir /ionic

# Default port
EXPOSE 8100

# Live Reload port
EXPOSE 35729

WORKDIR /ionic

CMD ionic serve -b
