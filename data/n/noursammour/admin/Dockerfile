FROM node:10.11.0 as base

WORKDIR /digsup/admin

RUN \
    npm i lerna -g --loglevel notice && \
    npm i yarn -g --loglevel notice && \
    rm -rf /var/lib/apt/lists/*

COPY package.json .
COPY yarn.lock .
COPY lerna.json .
COPY packages/admin ./packages/admin

ENV PORT=3001
RUN yarn bootstrap --loglevel notice

EXPOSE 3001
CMD ["yarn", "dev"]
