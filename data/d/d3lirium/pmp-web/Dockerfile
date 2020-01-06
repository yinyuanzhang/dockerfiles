FROM node:latest

MAINTAINER Paolo Chiabrera <paolo.chiabrera@gmail.com>

# currently only works for development

ENV NODE_ENV production

ENV LOG_LEVEL warn

ENV PORT 9030

ENV PM2_HOME /home/app/.pm2

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:

ADD package.json /tmp/package.json

RUN cd /tmp && npm install --save pm2@latest -g && npm install --production

RUN mkdir -p /home/app && cp -a /tmp/node_modules /home/app

# RUN pm2 startup ubuntu

WORKDIR /home/app

ADD . /home/app

# replace this with your application's default port

# EXPOSE 9160

CMD pm2 start /home/app/app.js -x -i 1 --name pmp_web && pm2 save && pm2 logs
