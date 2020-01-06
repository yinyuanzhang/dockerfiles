FROM node:latest

MAINTAINER Amir Haghighati <haghighati.ami@gmail.com>

ENV NODE_ENV=production
ENV PORT=3000
ENV HOST=0.0.0.0

WORKDIR /app
EXPOSE 3000
COPY package.json yarn.lock /app/
COPY . /app/

RUN yarn install --frozen-lockfile --non-interactive
RUN yarn build
CMD yarn start
