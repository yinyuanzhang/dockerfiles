FROM node:carbon

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

COPY . /usr/src/app/
RUN yarn --network-timeout 100000 && \
    yarn cache clean && \
    npm install -g serve && yarn build

CMD ["yarn", "start:prod"]

EXPOSE 5000