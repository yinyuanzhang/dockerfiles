FROM node:12.11-slim

ENV NODE_ENV production

WORKDIR /linter

RUN npm i -g npm-check-updates

COPY package.json .
COPY .eslintrc.yml .

RUN npm install

COPY linter .

# VOLUME /tmp

CMD ./linter
