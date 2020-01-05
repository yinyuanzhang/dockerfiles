FROM node:alpine
LABEL name="build-essential"
LABEL description="Node Build Essential Docker Image"
LABEL maintainer="Ahmad Nassri <email@ahmadnassri.com>"

RUN apk add --update --no-cache build-base ca-certificates git openssh

USER node

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:$NPM_CONFIG_PREFIX/bin
ENV MANPATH=$MANPATH:$NPM_CONFIG_PREFIX/share/man
ENV NODE_PATH=$NPM_CONFIG_PREFIX/lib/node_modules

RUN npm install -g install-peerdeps
RUN npx install-peerdeps --only-peers --global @ahmadnassri/build-essential
