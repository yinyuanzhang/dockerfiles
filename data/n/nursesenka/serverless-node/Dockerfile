FROM node:10.16.0-alpine

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin
ENV YARN_VERSION 1.16.0

RUN set -x && \
  apk add --update --no-cache tzdata --virtual .build-deps-yarn curl && \
  cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
  echo "Asia/Tokyo" > /etc/timezone && \
  apk del tzdata && \
  curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" && \
  tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ && \
  ln -snf /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn && \
  ln -snf /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg && \
  rm yarn-v$YARN_VERSION.tar.gz && \
  apk del .build-deps-yarn && \
  npm install --global npm@6.9.0 && \
  yarn global add serverless@1.45.1

USER node

WORKDIR /home/node
