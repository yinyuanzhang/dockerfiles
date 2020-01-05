FROM node:alpine
# replace this with your application's default port
EXPOSE 33067

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install

CMD [ "node", "index.js"]
