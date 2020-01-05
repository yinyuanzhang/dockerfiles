FROM node:9

RUN npm install -g webpack

WORKDIR /tmp

COPY package.json /tmp/

RUN yarn install

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN cp -a /tmp/node_modules /usr/src/app/

RUN webpack

CMD ["/usr/local/bin/node", "./server.js"]
EXPOSE ${PORT}