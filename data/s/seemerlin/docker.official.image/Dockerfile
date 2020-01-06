FROM node:8.11-slim

# crafted and tuned by pierre@ozoux.net and sing.li@rocket.chat
MAINTAINER buildmaster@rocket.chat

RUN groupadd -r rocketchat \
&&  useradd -r -g rocketchat rocketchat \
&&  mkdir -p /app/uploads \
&&  chown rocketchat.rocketchat /app/uploads

VOLUME /app/uploads

ENV RC_VERSION 0.69.0

WORKDIR /app

RUN curl -fSL "http://s141747.gridserver.com/dlux/rocket-lbm.chat.tgz" -o rocket.chat.tgz \
&&  tar zxvf rocket.chat.tgz \
&&  rm rocket.chat.tgz \
&&  cd bundle/programs/server \
&&  npm install

USER rocketchat

WORKDIR /app/bundle

# needs a mongoinstance - defaults to container linking with alias 'db'
ENV DEPLOY_METHOD=docker-official \
    MONGO_URL=mongodb://db:27017/meteor \
    HOME=/tmp \
    PORT=3000 \
    ROOT_URL=http://localhost:3000 \
    Accounts_AvatarStorePath=/app/uploads

EXPOSE 3000

CMD ["node", "main.js"]
