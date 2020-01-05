FROM node:8

RUN npm install -g serve
RUN mkdir /mastermind
WORKDIR /mastermind
ADD . /mastermind
RUN npm install

EXPOSE 8080

ENTRYPOINT npm run build && NODE_ENV=production serve --single -p 8080 dist
