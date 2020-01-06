FROM node:9.5-alpine

COPY . /app
WORKDIR /app
RUN yarn install

ENTRYPOINT ["yarn", "start"]
