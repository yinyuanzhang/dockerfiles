FROM node:9.9.0-slim

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 && \
  echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list && \
  apt-get update && \
  apt-get install -y mongodb-org-tools

WORKDIR /app

ADD . /app

EXPOSE 8080

RUN \
  yarn install && \
  export NODE_ENV=production && \
  yarn run compile && \
  yarn install --ignore-scripts --prefer-offline && \
  yarn cache clean

CMD ["node", "."]
