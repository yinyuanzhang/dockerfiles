FROM octoblu/node:7-alpine-gyp

EXPOSE 80

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json package-lock.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

CMD [ "node", "--max-executable-size=256", "--max-old-space-size=256", "--max-semi-space-size=2", "keystone.js" ]
