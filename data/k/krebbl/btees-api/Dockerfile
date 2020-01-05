FROM node:6.9.1

RUN npm i -g babel-cli nodemon

COPY api/package.json /usr/src/api/

WORKDIR /usr/src/api

RUN npm install

COPY api/. /usr/src/api/

RUN chmod -R +x bootstrap.js

CMD nodemon bootstrap.js --env docker --exec babel-node --presets es2015,stage-2 --watch src --watch config
