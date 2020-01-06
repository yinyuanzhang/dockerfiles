FROM node:8-stretch

# Maintainer: docker_user <docker_user at email.com> (@docker_user)
MAINTAINER zengyu 284141050@qq.com

#
VOLUME /app

WORKDIR /app

RUN apt-get update \
    && apt-get install sudo \
    && apt-get clean \
    && apt-get autoclean 

RUN echo 'node  ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Commands to update the image
RUN yarn global add nodemon \
    typescript \
    pm2 \
    mocha \
    bower \
    webpack \
    webpack-cli \
    webpack-dev-server




# Commands when creating a new container
USER node
CMD ["node","-v"]