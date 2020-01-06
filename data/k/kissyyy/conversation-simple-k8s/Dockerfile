FROM ibmcom/ibmnode:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app
RUN npm install

EXPOSE 3000

COPY . /usr/src/app

CMD ["node", "server.js"]
