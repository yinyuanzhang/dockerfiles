FROM node:alpine

RUN apk add --update 

RUN apk --no-cache add --virtual builds-deps build-base python \
  gcc libgcc libstdc++ linux-headers autoconf automake nasm git && \
  npm install --quiet --unsafe-perm node-gyp bcryptjs dotenv-safe -g

RUN mkdir -p /newfolder
WORKDIR /newfolder
