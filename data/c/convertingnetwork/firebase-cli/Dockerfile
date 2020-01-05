FROM node:alpine
RUN unset NPM_CONFIG_USER && \
    apk add --no-cache git python2 openssh-client curl && \
    npm install -g firebase-tools
