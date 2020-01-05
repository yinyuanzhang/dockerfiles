FROM node:6-alpine
MAINTAINER Eric Higgins <erichiggins@gmail.com>

RUN apk --no-cache add --virtual native-deps python git make gcc g++ openssl-dev openssl openssh-client libc6-compat \
  && git clone https://github.com/AGWA/git-crypt.git \
  && cd git-crypt \
  && make \
  && make install \
  && cd .. \
  && rm -rf git-crypt \
  && yarn config set spin false \
  && yarn global add bower ember-cli@2.16.2 firebase-tools@3.19.1 phantomjs-prebuilt grpc node-pre-gyp node-gyp \
  && yarn cache clean \
  && apk del make gcc g++ openssl-dev
