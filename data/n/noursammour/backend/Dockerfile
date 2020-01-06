FROM node:10.11.0 as base

WORKDIR /digsup/backend

RUN \
    npm i lerna -g --loglevel notice && \
    npm i yarn -g --loglevel notice && \
    rm -rf /var/lib/apt/lists/*

COPY package.json .
COPY yarn.lock .
COPY lerna.json .
COPY .flowconfig .
COPY packages/backend ./packages/backend

ENV PORT=4000
RUN yarn bootstrap --loglevel notice

EXPOSE 4000
CMD ["yarn", "dev"]
