FROM node:latest

RUN npm install -g yarn && \
    mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN yarn install && \
    yarn clean && \
    yarn build:prod && \
    yarn build:server

ENV PORT=80
EXPOSE 80

ENTRYPOINT [ "/usr/local/bin/yarn", "start" ]
