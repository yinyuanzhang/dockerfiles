FROM node:latest

ENV NPM_CONFIG_LOGLEVEL info
RUN yarn global add pm2
RUN pm2 install pm2-logrotate
RUN pm2 set pm2-logrotate:retain 7

WORKDIR /home/node/nemv
