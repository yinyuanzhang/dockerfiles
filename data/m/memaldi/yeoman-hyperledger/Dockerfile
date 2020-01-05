FROM node:8

RUN npm install -g yo@latest

USER node
RUN npm config set prefix '~/.npm-global'
RUN npm install -g generator-hyperledger-composer@0.20

VOLUME /workdir
WORKDIR /workdir

ENTRYPOINT [ "yo" ]