FROM node:6.9.4

MAINTAINER Zheeeng <hi@zheeeng.me>

ENV KEYSTONEJS_VERSION 0.3.17

ENV NODE_MODULE_INSTALLATION_PATH /usr/src/modules
ENV NODE_PATH $NODE_MODULE_INSTALLATION_PATH/node_modules

WORKDIR $NODE_MODULE_INSTALLATION_PATH

RUN npm install dotenv@1.2.0 node-sass-middleware keystone@$KEYSTONEJS_VERSION

# FIX "Cannot find module '../build/Release/bson'] code" from http://stackoverflow.com/a/28932441/4494083
RUN cp $NODE_PATH/bson/browser_build/bson.js $NODE_PATH/bson/build/Release/bson.js

WORKDIR /usr/src/app

CMD [ "node", "keystone.js" ]
