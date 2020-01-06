FROM node:lts-alpine

EXPOSE 8080 4200
USER root
RUN apk update && apk add python g++ make bash
RUN mkdir /home/node/app
RUN mkdir /home/node/.cache
RUN chown -fR node:node /home/node
RUN chmod -fR og+rwx /home/node
RUN chmod -fR og+rwx /home/node/.cache
RUN npm install -g yarn
USER node
WORKDIR /home/node/app
ENV PATH=/home/node/.npm-global/bin:/.npm-global:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
