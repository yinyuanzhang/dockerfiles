FROM node:10.11.0 as base

WORKDIR /digsup/front

RUN yarn global add lerna --production

COPY package.json .
COPY yarn.lock .
COPY lerna.json .

COPY packages/front ./packages/front
RUN yarn
RUN yarn bootstrap --loglevel notice

RUN yarn build && yarn --production
EXPOSE 3000

CMD ["yarn", "start"]
